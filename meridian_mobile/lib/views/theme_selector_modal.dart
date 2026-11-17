import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import '../core/theme_engine.dart';

class ThemeSelectorModal extends ConsumerWidget {
  const ThemeSelectorModal({super.key});

  static const List<Color> accentPillOptions = [
    Color(0xFF38BDF8), // Cyan
    Color(0xFFA855F7), // Purple
    Color(0xFF10B981), // Emerald
    Color(0xFFF59E0B), // Amber
    Color(0xFFEF4444), // Rose
    Color(0xFFEC4899), // Pink
  ];

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final themeState = ref.watch(themeProvider);
    final colors = themeState.colors;

    return Container(
      padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 24),
      decoration: BoxDecoration(
        color: colors.surface,
        borderRadius: const BorderRadius.vertical(top: Radius.circular(24)),
        border: Border(top: BorderSide(color: colors.borderSubtle)),
      ),
      child: Column(
        mainAxisSize: MainAxisSize.min,
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              Row(
                children: [
                  Icon(Icons.palette_outlined, color: colors.primaryAccent, size: 20),
                  const SizedBox(width: 8),
                  Text(
                    'DESIGN SYSTEM & THEME',
                    style: TextStyle(
                      color: colors.textPrimary,
                      fontWeight: FontWeight.w700,
                      fontSize: 14,
                      letterSpacing: 0.8,
                    ),
                  ),
                ],
              ),
              IconButton(
                icon: Icon(Icons.close, color: colors.textSecondary, size: 18),
                onPressed: () => Navigator.pop(context),
              ),
            ],
          ),
          const SizedBox(height: 12),
          Text(
            'Select handcrafted palette and custom glow accent.',
            style: TextStyle(color: colors.textSecondary, fontSize: 13),
          ),
          const SizedBox(height: 18),

          // Palette Cards
          Row(
            children: [
              Expanded(
                child: _ThemePaletteCard(
                  name: 'OLED Abyss',
                  palette: AppThemePalette.oledAbyss,
                  isSelected: themeState.palette == AppThemePalette.oledAbyss,
                  colors: ThemePalettes.oledAbyss,
                  activeAccent: colors.primaryAccent,
                  onTap: () => ref.read(themeProvider.notifier).setPalette(AppThemePalette.oledAbyss),
                ),
              ),
              const SizedBox(width: 8),
              Expanded(
                child: _ThemePaletteCard(
                  name: 'Tokyo Cyber',
                  palette: AppThemePalette.tokyoCyber,
                  isSelected: themeState.palette == AppThemePalette.tokyoCyber,
                  colors: ThemePalettes.tokyoCyber,
                  activeAccent: colors.primaryAccent,
                  onTap: () => ref.read(themeProvider.notifier).setPalette(AppThemePalette.tokyoCyber),
                ),
              ),
            ],
          ),
          const SizedBox(height: 8),
          Row(
            children: [
              Expanded(
                child: _ThemePaletteCard(
                  name: 'Nord Frost',
                  palette: AppThemePalette.nordFrost,
                  isSelected: themeState.palette == AppThemePalette.nordFrost,
                  colors: ThemePalettes.nordFrost,
                  activeAccent: colors.primaryAccent,
                  onTap: () => ref.read(themeProvider.notifier).setPalette(AppThemePalette.nordFrost),
                ),
              ),
              const SizedBox(width: 8),
              Expanded(
                child: _ThemePaletteCard(
                  name: 'Minimalist Studio',
                  palette: AppThemePalette.minimalistStudio,
                  isSelected: themeState.palette == AppThemePalette.minimalistStudio,
                  colors: ThemePalettes.minimalistStudio,
                  activeAccent: colors.primaryAccent,
                  onTap: () => ref.read(themeProvider.notifier).setPalette(AppThemePalette.minimalistStudio),
                ),
              ),
            ],
          ),
          const SizedBox(height: 20),

          // Custom Accent Color Override
          Text(
            'CUSTOM ACCENT GLOW',
            style: TextStyle(
              color: colors.textSecondary,
              fontWeight: FontWeight.w700,
              fontSize: 11,
              letterSpacing: 0.8,
            ),
          ),
          const SizedBox(height: 10),
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              // Default reset pill
              GestureDetector(
                onTap: () => ref.read(themeProvider.notifier).setCustomAccent(null),
                child: Container(
                  padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 6),
                  decoration: BoxDecoration(
                    color: themeState.customAccent == null ? colors.primaryAccent.withValues(alpha: 0.2) : colors.surfaceLight,
                    borderRadius: BorderRadius.circular(10),
                    border: Border.all(
                      color: themeState.customAccent == null ? colors.primaryAccent : colors.borderSubtle,
                    ),
                  ),
                  child: Text(
                    'Default',
                    style: TextStyle(
                      color: themeState.customAccent == null ? colors.primaryAccent : colors.textSecondary,
                      fontSize: 11,
                      fontWeight: FontWeight.w600,
                    ),
                  ),
                ),
              ),
              ...accentPillOptions.map((c) {
                final isSelected = themeState.customAccent?.toARGB32() == c.toARGB32();
                return GestureDetector(
                  onTap: () => ref.read(themeProvider.notifier).setCustomAccent(c),
                  child: Container(
                    width: 28,
                    height: 28,
                    decoration: BoxDecoration(
                      color: c,
                      shape: BoxShape.circle,
                      border: Border.all(
                        color: isSelected ? Colors.white : Colors.transparent,
                        width: 2,
                      ),
                      boxShadow: isSelected
                          ? [BoxShadow(color: c.withValues(alpha: 0.6), blurRadius: 8)]
                          : null,
                    ),
                  ),
                );
              }),
            ],
          ),
        ],
      ),
    );
  }
}

class _ThemePaletteCard extends StatelessWidget {
  final String name;
  final AppThemePalette palette;
  final bool isSelected;
  final PaletteColors colors;
  final Color activeAccent;
  final VoidCallback onTap;

  const _ThemePaletteCard({
    required this.name,
    required this.palette,
    required this.isSelected,
    required this.colors,
    required this.activeAccent,
    required this.onTap,
  });

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onTap: onTap,
      child: Container(
        padding: const EdgeInsets.all(12),
        decoration: BoxDecoration(
          color: colors.background,
          borderRadius: BorderRadius.circular(14),
          border: Border.all(
            color: isSelected ? activeAccent : colors.borderSubtle,
            width: isSelected ? 1.5 : 1.0,
          ),
        ),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                Text(
                  name,
                  style: TextStyle(
                    color: colors.textPrimary,
                    fontSize: 12,
                    fontWeight: FontWeight.w700,
                  ),
                ),
                if (isSelected)
                  Icon(Icons.check_circle, color: activeAccent, size: 14),
              ],
            ),
            const SizedBox(height: 8),
            Row(
              children: [
                _ColorDot(color: colors.background),
                const SizedBox(width: 4),
                _ColorDot(color: colors.surface),
                const SizedBox(width: 4),
                _ColorDot(color: colors.primaryAccent),
                const SizedBox(width: 4),
                _ColorDot(color: colors.secondaryAccent),
              ],
            ),
          ],
        ),
      ),
    );
  }
}

class _ColorDot extends StatelessWidget {
  final Color color;

  const _ColorDot({required this.color});

  @override
  Widget build(BuildContext context) {
    return Container(
      width: 12,
      height: 12,
      decoration: BoxDecoration(
        color: color,
        shape: BoxShape.circle,
        border: Border.all(color: Colors.white24, width: 0.5),
      ),
    );
  }
}
