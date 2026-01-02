# TODO: Refactoring Plan untuk Analisis Data Pasien

## Phase 1: Infrastructure Setup

- [ ] Create `config.py` - Centralized constants
- [ ] Create `data_loader.py` - Data loading with caching and error handling

## Phase 2: Business Logic

- [ ] Create `health_analyzer.py` - Data processing and analysis logic
- [ ] Create `visualizer.py` - All graphing functions

## Phase 3: Refactor Main Application

- [ ] Refactor `menu_utama.py` - Use modular imports
- [ ] Remove `risiko_tertinggi.py` - Consolidate functionality

## Phase 4: Testing & Validation

- [ ] Test menu navigation
- [ ] Verify all graphs render correctly
- [ ] Validate data loading and error handling

## Key Improvements Delivered:

- Modular architecture with separation of concerns
- Type hints and docstrings throughout
- Proper error handling
- Centralized configuration (no hardcoded values)
- Pure functions without side effects
- Reusable and testable code
