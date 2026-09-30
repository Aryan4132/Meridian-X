# Meridian-X Flutter Mobile App Specification

This document defines the technical architecture, Dart package ecosystem, and implementation plan for building the **Meridian-X Mobile APK & iOS App** using **Flutter & Dart**.

---

## 1. Why Flutter for Meridian-X?

* **Cross-Platform Single Codebase**: Build both **Android APK** and **iOS IPA** simultaneously.
* **High Performance Custom Canvas**: Smooth 60/120 FPS rendering for **Voice Orb HUD** using `CustomPainter`.
* **Fast WebSocket Streaming**: Native Dart `web_socket_channel` for low-latency agent thoughts & audio PCM streams.

---

## 2. Tech Stack & Recommended Packages (`pubspec.yaml`)

```yaml
name: meridian_mobile
description: "Meridian-X Mobile Agent Control Hub"
publish_to: 'none'
version: 1.0.0+1

environment:
  sdk: '>=3.2.0 <4.0.0'

dependencies:
  flutter:
    sdk: flutter

  # State Management & Concurrency
  flutter_riverpod: ^2.5.1

  # Networking & WebSockets
  web_socket_channel: ^2.4.4
  http: ^1.2.0

  # Real-Time Audio Recording (Voice Orb PCM VAD Stream)
  record: ^5.1.0
  audioplayers: ^6.0.0

  # Camera Vision Analysis
  camera: ^0.10.5+9

  # Desktop Remote Pairing (QR Scanner)
  mobile_scanner: ^5.0.0

  # Secure Encrypted Storage
  flutter_secure_storage: ^9.0.0

  # Micro-Animations & UI Enhancements
  flutter_animate: ^4.5.0
  google_fonts: ^6.1.0
  lucide_icons: ^0.257.0

dev_dependencies:
  flutter_test:
    sdk: flutter
  flutter_lints: ^3.0.0
```

---

## 3. Core Flutter Module Implementation

### 3.1 Voice Orb HUD (`voice_orb_painter.dart`)

* Renders animated glowing orb and reactive frequency spectrum using Flutter `CustomPainter` + `AnimationController`.
* Uses `record` package to capture PCM audio byte streams and emit live audio levels to visualizer.

### 3.2 Thought Process Stream Carousel (`thought_carousel_widget.dart`)

* `ListView.builder` / `SizedBox` horizontal scroll rendering agent thought steps with `flutter_animate` shimmer & pulse effects.

### 3.3 Camera Vision Viewport (`vision_scanner_view.dart`)

* Embeds `CameraPreview(controller)` for scanning physical code, whiteboards, or server screens.
* Converts frame images to Uint8List Base64 strings for payload transmission to Meridian Desktop Python engine.

### 3.4 Hardware Telemetry & Pairing Modal (`pairing_dialog.dart`)

* Uses `mobile_scanner` to read desktop engine QR codes (`ws://<IP>:<PORT>?token=<SECRET>`).
* Emits real-time ping (ms), CPU %, and Anti-Hallucination active status in app header.

---

## 4. Android Configuration (`android/app/src/main/AndroidManifest.xml`)

```xml
<manifest xmlns:android="http://schemas.android.com/apk/res/android">
    <uses-permission android:name="android.permission.INTERNET" />
    <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
    <uses-permission android:name="android.permission.RECORD_AUDIO" />
    <uses-permission android:name="android.permission.CAMERA" />

    <application
        android:label="Meridian-X"
        android:name="${applicationName}"
        android:icon="@mipmap/ic_launcher">
        <activity
            android:name=".MainActivity"
            android:exported="true"
            android:launchMode="singleTop"
            android:theme="@style/LaunchTheme"
            android:configChanges="orientation|keyboardHidden|keyboard|screenSize|smallestScreenSize|locale|layoutDirection|fontScale|screenLayout|density|uiMode"
            android:hardwareAccelerated="true"
            android:windowSoftInputMode="adjustResize">
            <intent-filter>
                <action android:name="android.intent.action.MAIN"/>
                <category android:name="android.intent.category.LAUNCHER"/>
            </intent-filter>
        </activity>
    </application>
</manifest>
```

---

## 5. Directory Structure (`lib/`)

```text
lib/
├── main.dart
├── core/
│   ├── theme.dart (Dark Mode #080C14, Cyan #06B6D4, Purple #A855F7)
│   ├── websocket_client.dart
│   └── secure_storage.dart
├── models/
│   ├── thought_step.dart
│   └── telemetry.dart
├── providers/
│   ├── voice_orb_provider.dart
│   └── agent_chat_provider.dart
└── views/
    ├── voice_orb_hud.dart
    ├── thought_carousel.dart
    ├── camera_vision_view.dart
    └── remote_pairing_modal.dart
```
