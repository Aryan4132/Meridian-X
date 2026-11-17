import 'dart:ui';
import 'package:flutter/material.dart';
import '../core/theme_engine.dart';

class BottomNavDock extends StatelessWidget {
  final int currentIndex;
  final ValueChanged<int> onSelectTab;
  final PaletteColors colors;

  const BottomNavDock({
    super.key,
    required this.currentIndex,
    required this.onSelectTab,
    required this.colors,
  });

  @override
  Widget build(BuildContext context) {
    const items = [
      _NavItem(icon: Icons.chat_bubble_outline_rounded, activeIcon: Icons.chat_bubble_rounded, label: 'Chat'),
      _NavItem(icon: Icons.graphic_eq_rounded, activeIcon: Icons.mic_rounded, label: 'Voice'),
      _NavItem(icon: Icons.tune_rounded, activeIcon: Icons.memory_rounded, label: 'Models'),
      _NavItem(icon: Icons.settings_outlined, activeIcon: Icons.settings_rounded, label: 'Settings'),
    ];

    return SafeArea(
      top: false,
      child: Container(
        margin: const EdgeInsets.fromLTRB(20, 0, 20, 10),
        height: 64,
        decoration: BoxDecoration(
          color: colors.surface.withValues(alpha: 0.85),
          borderRadius: BorderRadius.circular(32),
          border: Border.all(color: colors.borderSubtle.withValues(alpha: 0.8)),
          boxShadow: [
            BoxShadow(
              color: Colors.black.withValues(alpha: 0.4),
              blurRadius: 20,
              offset: const Offset(0, 8),
            ),
            BoxShadow(
              color: colors.borderGlow,
              blurRadius: 10,
              spreadRadius: -2,
            ),
          ],
        ),
        child: ClipRRect(
          borderRadius: BorderRadius.circular(32),
          child: BackdropFilter(
            filter: ImageFilter.blur(sigmaX: 16, sigmaY: 16),
            child: Row(
              mainAxisAlignment: MainAxisAlignment.spaceAround,
              children: List.generate(items.length, (index) {
                final item = items[index];
                final isSelected = currentIndex == index;

                return InkWell(
                  onTap: () => onSelectTab(index),
                  borderRadius: BorderRadius.circular(24),
                  child: AnimatedContainer(
                    duration: const Duration(milliseconds: 250),
                    curve: Curves.easeOutQuart,
                    padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 6),
                    decoration: BoxDecoration(
                      color: isSelected
                          ? colors.primaryAccent.withValues(alpha: 0.15)
                          : Colors.transparent,
                      borderRadius: BorderRadius.circular(20),
                    ),
                    child: Column(
                      mainAxisSize: MainAxisSize.min,
                      mainAxisAlignment: MainAxisAlignment.center,
                      children: [
                        Icon(
                          isSelected ? item.activeIcon : item.icon,
                          size: 20,
                          color: isSelected ? colors.primaryAccent : colors.textSecondary,
                        ),
                        const SizedBox(height: 2),
                        Text(
                          item.label,
                          style: TextStyle(
                            color: isSelected ? colors.primaryAccent : colors.textSecondary,
                            fontSize: 10.5,
                            fontWeight: isSelected ? FontWeight.w700 : FontWeight.w500,
                          ),
                        ),
                      ],
                    ),
                  ),
                );
              }),
            ),
          ),
        ),
      ),
    );
  }
}

class _NavItem {
  final IconData icon;
  final IconData activeIcon;
  final String label;

  const _NavItem({
    required this.icon,
    required this.activeIcon,
    required this.label,
  });
}
