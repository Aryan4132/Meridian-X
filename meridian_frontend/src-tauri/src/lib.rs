use tauri::{Emitter, Manager};
use tauri_plugin_global_shortcut::{Code, GlobalShortcutExt, Modifiers, Shortcut, ShortcutState};
use tauri::{
    menu::{MenuBuilder, MenuItem},
    tray::TrayIconBuilder,
};

#[tauri::command]
fn set_island_mode(window: tauri::WebviewWindow, enable: bool) {
    if enable {
        let width = 360.0;
        let height = 280.0;

        let _ = window.set_size(tauri::Size::Logical(tauri::LogicalSize {
            width,
            height,
        }));
        
        if let Ok(Some(monitor)) = window.current_monitor() {
            let scale_factor = monitor.scale_factor();
            let monitor_size = monitor.size().to_logical::<f64>(scale_factor);
            let monitor_pos = monitor.position().to_logical::<f64>(scale_factor);
            
            let margin_right = 16.0;
            let margin_bottom = 60.0;
            
            let x = monitor_pos.x + monitor_size.width - width - margin_right;
            let y = monitor_pos.y + monitor_size.height - height - margin_bottom;

            let _ = window.set_position(tauri::Position::Logical(tauri::LogicalPosition {
                x,
                y,
            }));
        } else {
            let _ = window.center();
        }
        
        let _ = window.set_always_on_top(true);
    } else {
        let _ = window.set_size(tauri::Size::Logical(tauri::LogicalSize {
            width: 1000.0,
            height: 750.0,
        }));
        let _ = window.center();
        let _ = window.set_always_on_top(false);
    }
}

#[tauri::command]
fn set_mascot_visible(app: tauri::AppHandle, visible: bool) {
    if let Some(mascot_window) = app.get_webview_window("mascot") {
        if visible {
            let _ = mascot_window.show();
            let _ = mascot_window.set_focus();
            if let Some(main_window) = app.get_webview_window("main") {
                let _ = main_window.hide();
            }
            let _ = app.emit("show-mascot", ());
        } else {
            let _ = mascot_window.hide();
            if let Some(main_window) = app.get_webview_window("main") {
                let _ = main_window.show();
                let _ = main_window.set_focus();
            }
            let _ = app.emit("hide-mascot", ());
        }
    }
}

#[tauri::command]
fn close_application(app: tauri::AppHandle) {
    set_mascot_visible(app, true);
}

#[tauri::command]
fn toggle_game_mode(app: tauri::AppHandle, enabled: bool) -> Result<bool, String> {
    use tauri_plugin_global_shortcut::GlobalShortcutExt;
    let alt_m = Shortcut::new(Some(Modifiers::ALT), Code::KeyM);
    let alt_shift_m = Shortcut::new(Some(Modifiers::ALT | Modifiers::SHIFT), Code::KeyM);
    let alt_v = Shortcut::new(Some(Modifiers::ALT), Code::KeyV);
    let shortcut_manager = app.global_shortcut();

    if enabled {
        let _ = shortcut_manager.unregister(alt_m);
        let _ = shortcut_manager.unregister(alt_shift_m);
        let _ = shortcut_manager.unregister(alt_v);
        log::info!("Game Mode enabled: unregistered global shortcuts Alt+M, Alt+Shift+M, Alt+V");
        
        if let Some(mascot_window) = app.get_webview_window("mascot") {
            let _ = mascot_window.hide();
        }
        let _ = app.emit("hide-mascot", ());
    } else {
        if !shortcut_manager.is_registered(alt_m) {
            if let Err(e) = shortcut_manager.register(alt_m) {
                log::error!("Failed to re-register Alt+M: {:?}", e);
            }
        }
        if !shortcut_manager.is_registered(alt_shift_m) {
            if let Err(e) = shortcut_manager.register(alt_shift_m) {
                log::error!("Failed to re-register Alt+Shift+M: {:?}", e);
            }
        }
        if !shortcut_manager.is_registered(alt_v) {
            if let Err(e) = shortcut_manager.register(alt_v) {
                log::error!("Failed to re-register Alt+V: {:?}", e);
            }
        }
        log::info!("Game Mode disabled: re-registered global shortcuts");
    }

    Ok(enabled)
}

fn kill_backend_process() {
    #[cfg(target_os = "windows")]
    {
        use std::process::Command;
        let _ = Command::new("powershell")
            .args(&[
                "-Command",
                "Get-CimInstance Win32_Process -Filter \"Name = 'python.exe' or Name = 'pythonw.exe' or Name = 'api.exe'\" | Where-Object {$_.CommandLine -like '*api.py*' or $_.Name -eq 'api.exe'} | ForEach-Object { Stop-Process -Id $_.ProcessId -Force }"
            ])
            .status();
    }
}

#[tauri::command]
fn trigger_backend_restart() -> Result<String, String> {
    use std::process::Command;
    use std::path::PathBuf;

    let mut current_dir = std::env::current_dir().unwrap_or_else(|_| PathBuf::from("."));
    let mut script_path = None;

    // Check CWD and walk up to 5 parent directories to find restart_backend.bat
    for _ in 0..6 {
        let test_path = current_dir.join("restart_backend.bat");
        if test_path.exists() {
            script_path = Some(test_path);
            break;
        }
        if let Some(parent) = current_dir.parent() {
            current_dir = parent.to_path_buf();
        } else {
            break;
        }
    }

    // Fallback to checking executable directory and walking up from there
    if script_path.is_none() {
        if let Ok(exe_path) = std::env::current_exe() {
            let mut exe_dir = exe_path.parent().map(|p| p.to_path_buf()).unwrap_or_else(|| PathBuf::from("."));
            for _ in 0..6 {
                let test_path = exe_dir.join("restart_backend.bat");
                if test_path.exists() {
                    script_path = Some(test_path);
                    break;
                }
                if let Some(parent) = exe_dir.parent() {
                    exe_dir = parent.to_path_buf();
                } else {
                    break;
                }
            }
        }
    }

    let resolved_path = match script_path {
        Some(path) => path,
        None => return Err("Could not find restart_backend.bat script".into()),
    };

    Command::new("cmd")
        .args(&["/C", resolved_path.to_str().unwrap()])
        .spawn()
        .map_err(|e| format!("Failed to spawn restart script: {}", e))?;

    Ok("Restart initiated".into())
}

#[tauri::command]
fn open_url(url: String) -> Result<(), String> {
    #[cfg(target_os = "windows")]
    {
        use std::process::Command;
        Command::new("cmd")
            .args(&["/C", "start", "", &url])
            .spawn()
            .map_err(|e| e.to_string())?;
    }
    #[cfg(target_os = "macos")]
    {
        use std::process::Command;
        Command::new("open")
            .arg(&url)
            .spawn()
            .map_err(|e| e.to_string())?;
    }
    #[cfg(target_os = "linux")]
    {
        use std::process::Command;
        Command::new("xdg-open")
            .arg(&url)
            .spawn()
            .map_err(|e| e.to_string())?;
    }
    Ok(())
}

#[cfg_attr(mobile, tauri::mobile_entry_point)]
pub fn run() {
    tauri::Builder::default()
        .invoke_handler(tauri::generate_handler![set_island_mode, trigger_backend_restart, set_mascot_visible, close_application, toggle_game_mode, open_url])
        .plugin(
            tauri_plugin_global_shortcut::Builder::new()
                .with_handler(|app, shortcut, event| {
                    log::info!("Global shortcut event received: key={:?}, mods={:?}, state={:?}", shortcut.key, shortcut.mods, event.state());
                    if event.state() == ShortcutState::Pressed {
                        // Alt + M: Toggle visibility of the main window
                        if shortcut.matches(Modifiers::ALT, Code::KeyM) {
                            log::info!("Alt+M shortcut matched");
                            if let Some(main_window) = app.get_webview_window("main") {
                                if let Ok(visible) = main_window.is_visible() {
                                    if visible {
                                        let _ = main_window.hide();
                                        if let Some(mascot_window) = app.get_webview_window("mascot") {
                                            let _ = mascot_window.show();
                                            let _ = mascot_window.set_focus();
                                        }
                                        let _ = app.emit("show-mascot", ());
                                    } else {
                                        let _ = main_window.show();
                                        let _ = main_window.set_focus();
                                        if let Some(mascot_window) = app.get_webview_window("mascot") {
                                            let _ = mascot_window.hide();
                                        }
                                        let _ = app.emit("hide-mascot", ());
                                    }
                                }
                            }
                        }

                        // Alt + Shift + M: Toggle mascot (Dynamic Island) visibility
                        if shortcut.matches(Modifiers::ALT | Modifiers::SHIFT, Code::KeyM) {
                            log::info!("Alt+Shift+M shortcut matched");
                            if let Some(mascot_window) = app.get_webview_window("mascot") {
                                if let Ok(visible) = mascot_window.is_visible() {
                                    if visible {
                                        let _ = mascot_window.hide();
                                        if let Some(main_window) = app.get_webview_window("main") {
                                            let _ = main_window.show();
                                            let _ = main_window.set_focus();
                                        }
                                        let _ = app.emit("hide-mascot", ());
                                    } else {
                                        let _ = mascot_window.show();
                                        let _ = mascot_window.set_focus();
                                        if let Some(main_window) = app.get_webview_window("main") {
                                            let _ = main_window.hide();
                                        }
                                        let _ = app.emit("show-mascot", ());
                                    }
                                }
                            }
                        }

                        // Alt + V: Trigger Global Push-to-Talk
                        if shortcut.matches(Modifiers::ALT, Code::KeyV) {
                            log::info!("Alt+V shortcut matched - triggering global-push-to-talk");
                            let mut focus_target_emitted = false;
                            
                            if let Some(mascot_window) = app.get_webview_window("mascot") {
                                if let Ok(visible) = mascot_window.is_visible() {
                                    if visible {
                                        let _ = mascot_window.set_focus();
                                        let _ = app.emit("global-push-to-talk", ());
                                        focus_target_emitted = true;
                                    }
                                }
                            }
                            
                            if !focus_target_emitted {
                                if let Some(main_window) = app.get_webview_window("main") {
                                    if let Ok(visible) = main_window.is_visible() {
                                        if visible {
                                            let _ = main_window.set_focus();
                                            let _ = app.emit("global-push-to-talk", ());
                                            focus_target_emitted = true;
                                        }
                                    }
                                }
                            }
                            
                            if !focus_target_emitted {
                                if let Some(mascot_window) = app.get_webview_window("mascot") {
                                    let _ = mascot_window.show();
                                    let _ = mascot_window.set_focus();
                                    let _ = app.emit("show-mascot", ());
                                    let _ = app.emit("global-push-to-talk", ());
                                }
                            }
                        }
                    }
                })
                .build(),
        )
        .setup(|app| {
            if cfg!(debug_assertions) {
                app.handle().plugin(
                    tauri_plugin_log::Builder::default()
                        .level(log::LevelFilter::Info)
                        .build(),
                )?;
            }

            // Spawn the python backend in production mode if packaged as a resource
            #[cfg(not(debug_assertions))]
            {
                let app_handle = app.handle();
                let mut api_exe_path = None;

                // Try resolving via standard Resource directory first
                if let Ok(res_path) = app_handle.path().resolve("api/api.exe", tauri::path::BaseDirectory::Resource) {
                    if res_path.exists() {
                        api_exe_path = Some(res_path);
                    }
                }

                // Fallback: check sibling api directory relative to current executable (useful when running from target/release directly)
                if api_exe_path.is_none() {
                    if let Ok(mut exe_path) = std::env::current_exe() {
                        exe_path.pop(); // Remove executable name
                        let local_api = exe_path.join("api/api.exe");
                        if local_api.exists() {
                            api_exe_path = Some(local_api);
                        }
                    }
                }

                if let Some(api_exe_path) = api_exe_path {
                    // Get OS app local data directory: %LOCALAPPDATA%/meridian-x
                    if let Ok(app_local_data_dir) = app_handle.path().app_local_data_dir() {
                            let data_dir = app_local_data_dir.join("Meridian");
                            let _ = std::fs::create_dir_all(&data_dir);
                            
                            log::info!("Spawning backend sidecar: {:?}", api_exe_path);
                            let mut cmd = std::process::Command::new(&api_exe_path);
                            
                            // Set CWD to resources/api directory
                            if let Some(parent) = api_exe_path.parent() {
                                cmd.current_dir(parent);
                            }
                            
                            // Configure MERIDIAN_DATA_DIR env variable
                            if let Some(data_dir_str) = data_dir.to_str() {
                                cmd.env("MERIDIAN_DATA_DIR", data_dir_str);
                            }
                            
                            #[cfg(target_os = "windows")]
                            {
                                // On Windows, run the process in the background without opening a command window
                                use std::os::windows::process::CommandExt;
                                const CREATE_NO_WINDOW: u32 = 0x08000000;
                                cmd.creation_flags(CREATE_NO_WINDOW);
                            }
                            
                            match cmd.spawn() {
                                Ok(_) => {
                                    log::info!("Successfully spawned backend daemon!");
                                    // Wait for the backend to bind to port 4132 before showing the main window
                                    let mut retry = 0;
                                    while retry < 50 {
                                        if std::net::TcpStream::connect("127.0.0.1:4132").is_ok() {
                                            log::info!("Backend daemon is online and responsive.");
                                            break;
                                        }
                                        std::thread::sleep(std::time::Duration::from_millis(100));
                                        retry += 1;
                                    }
                                }
                                Err(e) => log::error!("Failed to spawn backend daemon: {:?}", e),
                            }
                        }
                    }
                }

            let window = app.get_webview_window("main").unwrap();
            let _ = window.maximize();
            let _ = window.show();
            let _ = window.set_focus();
            let app_handle = app.handle().clone();
            window.on_window_event(move |event| {
                if let tauri::WindowEvent::CloseRequested { api, .. } = event {
                    api.prevent_close();
                    set_mascot_visible(app_handle.clone(), true);
                }
            });

            // System Tray Menu setup
                        let show_dashboard = MenuItem::with_id(app, "show_dashboard", "Show Dashboard", true, None::<&str>)?;
            let open_mascot = MenuItem::with_id(app, "open_mascot", "Open Mascot Companion", true, None::<&str>)?;
            let toggle_game_mode = MenuItem::with_id(app, "toggle_game_mode", "Toggle Game Mode 🎮", true, None::<&str>)?;
            let quit_app = MenuItem::with_id(app, "quit", "Quit", true, None::<&str>)?;
            
            let tray_menu = MenuBuilder::new(app)
                .item(&show_dashboard)
                .item(&open_mascot)
                .item(&toggle_game_mode)
                .separator()
                .item(&quit_app)
                .build()?;

            let tray_icon = app.default_window_icon().cloned().unwrap_or_else(|| {
                tauri::image::Image::from_bytes(include_bytes!("../icons/32x32.png")).unwrap()
            });

            let _tray = TrayIconBuilder::new()
                .menu(&tray_menu)
                .icon(tray_icon)
                .on_menu_event(|app, event| {
                    match event.id().as_ref() {
                        "show_dashboard" => {
                            if let Some(main_window) = app.get_webview_window("main") {
                                let _ = main_window.show();
                                let _ = main_window.set_focus();
                            }
                            if let Some(mascot_window) = app.get_webview_window("mascot") {
                                let _ = mascot_window.hide();
                            }
                        }
                        "open_mascot" => {
                            if let Some(mascot_window) = app.get_webview_window("mascot") {
                                let _ = mascot_window.show();
                                let _ = mascot_window.set_focus();
                            }
                            if let Some(main_window) = app.get_webview_window("main") {
                                let _ = main_window.hide();
                            }
                        }
                        "toggle_game_mode" => {
                            let _ = app.emit("tray-toggle-game-mode", ());
                        }
                        "quit" => {
                            kill_backend_process();
                            app.exit(0);
                        }
                        _ => {}
                    }
                })
                .build(app)?;



            // Register global shortcuts
            let alt_m = Shortcut::new(Some(Modifiers::ALT), Code::KeyM);
            let alt_shift_m = Shortcut::new(Some(Modifiers::ALT | Modifiers::SHIFT), Code::KeyM);
            let alt_v = Shortcut::new(Some(Modifiers::ALT), Code::KeyV);

            let shortcut_manager = app.global_shortcut();
            if let Err(e) = shortcut_manager.register(alt_m) {
                log::error!("Failed to register Alt+M global hotkey: {:?}", e);
            } else {
                log::info!("Successfully registered Alt+M global hotkey");
            }

            if let Err(e) = shortcut_manager.register(alt_shift_m) {
                log::error!("Failed to register Alt+Shift+M global hotkey: {:?}", e);
            } else {
                log::info!("Successfully registered Alt+Shift+M global hotkey");
            }

            if let Err(e) = shortcut_manager.register(alt_v) {
                log::error!("Failed to register Alt+V global hotkey: {:?}", e);
            } else {
                log::info!("Successfully registered Alt+V global hotkey");
            }

            Ok(())
        })
        .build(tauri::generate_context!())
        .expect("error while building tauri application")
        .run(|_app_handle, event| {
            if let tauri::RunEvent::Exit = event {
                kill_backend_process();
            }
        });
}
