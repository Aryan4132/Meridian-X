use tauri::Manager;

#[cfg_attr(mobile, tauri::mobile_entry_point)]
pub fn run() {
    tauri::Builder::default()
        .plugin(tauri_plugin_log::Builder::new().build())
        .plugin(tauri_plugin_websocket::init())
        .setup(|_app| {
            Ok(())
        })

        .run(tauri::generate_context!())
        .expect("error while running Meridian-X Mobile");
}
