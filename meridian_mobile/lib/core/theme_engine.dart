import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:google_fonts/google_fonts.dart';
import 'secure_storage.dart';

enum AppThemePalette {
  oledAbyss,
  tokyoCyber,
  nordFrost,
  minimalistStudio;

  String get displayName {
    switch (this) {
      case AppThemePalette.oledAbyss:
        return 'OLED Abyss';
      case AppThemePalette.tokyoCyber:
        return 'Tokyo Cyber';
      case AppThemePalette.nordFrost:
        return 'Nord Frost';
      case AppThemePalette.minimalistStudio:
        return 'Minimalist Studio';
    }
  }

  PaletteColors get colors => ThemePalettes.getColors(this);
}

class PaletteColors {
  final Color background;
  final Color surface;
  final Color surfaceLight;
  final Color primaryAccent;
  final Color secondaryAccent;
  final Color textPrimary;
  final Color textSecondary;
  final Color borderSubtle;
  final Color borderGlow;

  const PaletteColors({
    required this.background,
    required this.surface,
    required this.surfaceLight,
    required this.primaryAccent,
    required this.secondaryAccent,
    required this.textPrimary,
    required this.textSecondary,
    required this.borderSubtle,
    required this.borderGlow,
  });
}

class ThemePalettes {
  static const PaletteColors oledAbyss = PaletteColors(
    background: Color(0xFF030712),
    surface: Color(0xFF0B0F19),
    surfaceLight: Color(0xFF131B2E),
    primaryAccent: Color(0xFF38BDF8),
    secondaryAccent: Color(0xFF818CF8),
    textPrimary: Color(0xFFF9FAFB),
    textSecondary: Color(0xFF9CA3AF),
    borderSubtle: Color(0x1AFFFFFF),
    borderGlow: Color(0x3338BDF8),
  );

  static const PaletteColors tokyoCyber = PaletteColors(
    background: Color(0xFF080C16),
    surface: Color(0xFF0F172A),
    surfaceLight: Color(0xFF1E293B),
    primaryAccent: Color(0xFFA855F7),
    secondaryAccent: Color(0xFF06B6D4),
    textPrimary: Color(0xFFF8FAFC),
    textSecondary: Color(0xFF94A3B8),
    borderSubtle: Color(0x1FFFFFFF),
    borderGlow: Color(0x33A855F7),
  );

  static const PaletteColors nordFrost = PaletteColors(
    background: Color(0xFF242933),
    surface: Color(0xFF2E3440),
    surfaceLight: Color(0xFF3B4252),
    primaryAccent: Color(0xFF88C0D0),
    secondaryAccent: Color(0xFF81A1C1),
    textPrimary: Color(0xFFECEFF4),
    textSecondary: Color(0xFFD8DEE9),
    borderSubtle: Color(0x24D8DEE9),
    borderGlow: Color(0x4088C0D0),
  );

  static const PaletteColors minimalistStudio = PaletteColors(
    background: Color(0xFF121214),
    surface: Color(0xFF1C1C1F),
    surfaceLight: Color(0xFF27272A),
    primaryAccent: Color(0xFFF59E0B),
    secondaryAccent: Color(0xFF10B981),
    textPrimary: Color(0xFFFAFAFA),
    textSecondary: Color(0xFFA1A1AA),
    borderSubtle: Color(0x1CFAFAFA),
    borderGlow: Color(0x33F59E0B),
  );

  static PaletteColors getColors(AppThemePalette palette) {
    switch (palette) {
      case AppThemePalette.oledAbyss:
        return oledAbyss;
      case AppThemePalette.tokyoCyber:
        return tokyoCyber;
      case AppThemePalette.nordFrost:
        return nordFrost;
      case AppThemePalette.minimalistStudio:
        return minimalistStudio;
    }
  }
}

class ThemeState {
  final AppThemePalette palette;
  final Color? customAccent;

  const ThemeState({
    this.palette = AppThemePalette.tokyoCyber,
    this.customAccent,
  });

  PaletteColors get colors {
    final base = ThemePalettes.getColors(palette);
    if (customAccent == null) return base;
    return PaletteColors(
      background: base.background,
      surface: base.surface,
      surfaceLight: base.surfaceLight,
      primaryAccent: customAccent!,
      secondaryAccent: base.secondaryAccent,
      textPrimary: base.textPrimary,
      textSecondary: base.textSecondary,
      borderSubtle: base.borderSubtle,
      borderGlow: customAccent!.withValues(alpha: 0.25),
    );
  }

  ThemeData get themeData {
    final c = colors;
    return ThemeData.dark().copyWith(
      scaffoldBackgroundColor: c.background,
      primaryColor: c.primaryAccent,
      cardColor: c.surface,
      colorScheme: ColorScheme.dark(
        primary: c.primaryAccent,
        secondary: c.secondaryAccent,
        surface: c.surface,
        error: const Color(0xFFEF4444),
      ),
      textTheme: GoogleFonts.plusJakartaSansTextTheme(ThemeData.dark().textTheme).copyWith(
        displayLarge: GoogleFonts.plusJakartaSans(color: c.textPrimary, fontWeight: FontWeight.w700),
        titleLarge: GoogleFonts.plusJakartaSans(color: c.textPrimary, fontWeight: FontWeight.w600, letterSpacing: -0.2),
        bodyLarge: GoogleFonts.plusJakartaSans(color: c.textPrimary, fontSize: 15),
        bodyMedium: GoogleFonts.plusJakartaSans(color: c.textSecondary, fontSize: 13),
      ),
      appBarTheme: AppBarTheme(
        backgroundColor: c.background,
        elevation: 0,
        centerTitle: true,
      ),
      dialogTheme: DialogThemeData(
        backgroundColor: c.surface,
        shape: RoundedRectangleBorder(
          borderRadius: BorderRadius.circular(20),
          side: BorderSide(color: c.borderSubtle),
        ),
      ),
    );
  }

  ThemeState copyWith({
    AppThemePalette? palette,
    Color? customAccent,
    bool clearCustomAccent = false,
  }) {
    return ThemeState(
      palette: palette ?? this.palette,
      customAccent: clearCustomAccent ? null : (customAccent ?? this.customAccent),
    );
  }
}

class ThemeController extends StateNotifier<ThemeState> {
  ThemeController() : super(const ThemeState()) {
    _loadPreferences();
  }

  static const _themePrefKey = 'meridian_app_theme';
  static const _accentPrefKey = 'meridian_custom_accent';

  Future<void> _loadPreferences() async {
    try {
      final savedThemeName = await MeridianSecureStorage.read(_themePrefKey);
      final savedAccentHex = await MeridianSecureStorage.read(_accentPrefKey);

      AppThemePalette palette = AppThemePalette.tokyoCyber;
      if (savedThemeName != null) {
        for (final p in AppThemePalette.values) {
          if (p.name == savedThemeName) {
            palette = p;
            break;
          }
        }
      }

      Color? accent;
      if (savedAccentHex != null) {
        final val = int.tryParse(savedAccentHex);
        if (val != null) {
          accent = Color(val);
        }
      }

      state = ThemeState(palette: palette, customAccent: accent);
    } catch (_) {
      // Default fallback
    }
  }

  Future<void> setPalette(AppThemePalette palette) async {
    state = state.copyWith(palette: palette);
    await MeridianSecureStorage.write(_themePrefKey, palette.name);
  }

  Future<void> setCustomAccent(Color? accent) async {
    if (accent == null) {
      state = state.copyWith(clearCustomAccent: true);
      await MeridianSecureStorage.delete(_accentPrefKey);
    } else {
      state = state.copyWith(customAccent: accent);
      await MeridianSecureStorage.write(_accentPrefKey, accent.toARGB32().toString());
    }
  }

  Future<void> resetCustomAccent() => setCustomAccent(null);
}

final themeProvider = StateNotifierProvider<ThemeController, ThemeState>((ref) {
  return ThemeController();
});
