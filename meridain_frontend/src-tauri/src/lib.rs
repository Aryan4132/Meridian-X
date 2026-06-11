use tauri::{Emitter, Manager};
use tauri_plugin_global_shortcut::{Code, GlobalShortcutExt, Modifiers, Shortcut, ShortcutState};

#[tauri::command]
fn set_island_mode(window: tauri::WebviewWindow, enable: bool) {
    if enable {
        let width = 360.0;
        let height = 280.0;

        let _ = window.set_size(tauri::Size::Logical(tauri::LogicalSize {
            width,
            height,
        }));
        
        if let Ok(Some(_monitor)) = window.current_monitor() {
            // Position 10px from the top and left edges of the active monitor
            let x = 10.0;
            let y = 10.0;

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
    kill_backend_process();
    app.exit(0);
}

fn kill_backend_process() {
    #[cfg(target_os = "windows")]
    {
        use std::process::Command;
        let _ = Command::new("powershell")
            .args(&[
                "-Command",
                "Get-CimInstance Win32_Process -Filter \"Name = 'python.exe'\" | Where-Object {$_.CommandLine -like '*api.py*'} | ForEach-Object { Stop-Process -Id $_.ProcessId -Force }"
            ])
            .status();
    }
}

#[tauri::command]
fn trigger_backend_restart() -> Result<String, String> {
    use std::process::Command;
    use std::path::Path;

    let path_parent = Path::new("../restart_backend.bat");
    let path_cwd = Path::new("restart_backend.bat");

    let script_path = if path_parent.exists() {
        path_parent
    } else if path_cwd.exists() {
        path_cwd
    } else {
        return Err("Could not find restart_backend.bat script".into());
    };

    Command::new("cmd")
        .args(&["/C", script_path.to_str().unwrap()])
        .spawn()
        .map_err(|e| format!("Failed to spawn restart script: {}", e))?;

    Ok("Restart initiated".into())
}

#[cfg_attr(mobile, tauri::mobile_entry_point)]
pub fn run() {
    tauri::Builder::default()
        .invoke_handler(tauri::generate_handler![set_island_mode, trigger_backend_restart, set_mascot_visible, close_application])
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

            let window = app.get_webview_window("main").unwrap();
            let _ = window.show();
            let _ = window.set_focus();
            let app_handle = app.handle().clone();
            window.on_window_event(move |event| {
                if let tauri::WindowEvent::CloseRequested { .. } = event {
                    kill_backend_process();
                    app_handle.exit(0);
                }
            });

            // Register global shortcuts
            let alt_m = Shortcut::new(Some(Modifiers::ALT), Code::KeyM);
            let alt_shift_m = Shortcut::new(Some(Modifiers::ALT | Modifiers::SHIFT), Code::KeyM);

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
