# Workspace Architecture & Component Map
Generated automatically by Meridian-X.

## Component Dependency Graph
```mermaid
graph TD
    N1["build_mobile.py []"]
    N2["build_standalone.py []"]
    N3["bump_version.py []"]
    N4["doctor.py []"]
    N5["main.py []"]
    N6["setup_db.py []"]
    N7["setup_startup.py []"]
    N8["verify_system.py []"]
    N9["analyze_music_cues.py [.agents/skills/brag/scripts]"]
    N10["config.py [generated_repos/attention_is_all_you_need__transformer_]"]
    N11["dataset.py [generated_repos/attention_is_all_you_need__transformer_]"]
    N12["model.py [generated_repos/attention_is_all_you_need__transformer_]"]
    N13["trainer.py [generated_repos/attention_is_all_you_need__transformer_]"]
    N14["api.py [meridian_backend]"]
    N15["database.py [meridian_backend]"]
    N16["mobile_bridge_service.py [meridian_backend]"]
    N17["tests_run.py [meridian_backend]"]
    N18["ProfileHeader.tsx [meridian_backend/meridian_frontend/src/components]"]
    N19["__init__.py [meridian_backend/src]"]
    N20["automation.py [meridian_backend/src/api]"]
    N21["browser_extension.py [meridian_backend/src/api]"]
    N22["chat.py [meridian_backend/src/api]"]
    N23["deps.py [meridian_backend/src/api]"]
    N24["mcp.py [meridian_backend/src/api]"]
    N25["models_mgmt.py [meridian_backend/src/api]"]
    N26["perception.py [meridian_backend/src/api]"]
    N27["profile.py [meridian_backend/src/api]"]
    N28["rag.py [meridian_backend/src/api]"]
    N29["scheduler.py [meridian_backend/src/api]"]
    N30["swarm.py [meridian_backend/src/api]"]
    N31["system.py [meridian_backend/src/api]"]
    N32["vault.py [meridian_backend/src/api]"]
    N33["voice.py [meridian_backend/src/api]"]
    N34["websockets.py [meridian_backend/src/api]"]
    N35["workspace.py [meridian_backend/src/api]"]
    N36["__init__.py [meridian_backend/src/api]"]
    N37["action_journal.py [meridian_backend/src/core]"]
    N38["agent_status_stream.py [meridian_backend/src/core]"]
    N39["android_automation.py [meridian_backend/src/core]"]
    N40["ar_bridge.py [meridian_backend/src/core]"]
    N41["atomic_storage.py [meridian_backend/src/core]"]
    N42["audit_logger.py [meridian_backend/src/core]"]
    N43["auth.py [meridian_backend/src/core]"]
    N44["behavior_monitor.py [meridian_backend/src/core]"]
    N45["boilerplate_genie.py [meridian_backend/src/core]"]
    N46["breach_sentinel.py [meridian_backend/src/core]"]
    N47["browser_extension_hub.py [meridian_backend/src/core]"]
    N48["bus.py [meridian_backend/src/core]"]
    N49["butler_etiquette.py [meridian_backend/src/core]"]
    N50["butler_ritual.py [meridian_backend/src/core]"]
    N51["camera_sentinel.py [meridian_backend/src/core]"]
    N52["checkpoints.py [meridian_backend/src/core]"]
    N53["clipboard.py [meridian_backend/src/core]"]
    N54["code_graph.py [meridian_backend/src/core]"]
    N55["cognitive_graph.py [meridian_backend/src/core]"]
    N56["commit_whisperer.py [meridian_backend/src/core]"]
    N57["concierge_agent.py [meridian_backend/src/core]"]
    N58["config.py [meridian_backend/src/core]"]
    N59["confirmations.py [meridian_backend/src/core]"]
    N60["consensus_engine.py [meridian_backend/src/core]"]
    N61["deep_project_context.py [meridian_backend/src/core]"]
    N62["device_handoff.py [meridian_backend/src/core]"]
    N63["device_sentinel.py [meridian_backend/src/core]"]
    N64["dev_automation.py [meridian_backend/src/core]"]
    N65["discord_bridge.py [meridian_backend/src/core]"]
    N66["discord_utils.py [meridian_backend/src/core]"]
    N67["doc_generator.py [meridian_backend/src/core]"]
    N68["doc_indexer.py [meridian_backend/src/core]"]
    N69["elevated_runner.py [meridian_backend/src/core]"]
    N70["emergency_lockdown.py [meridian_backend/src/core]"]
    N71["error_diagnostics.py [meridian_backend/src/core]"]
    N72["experiment_runner.py [meridian_backend/src/core]"]
    N73["explain_code_engine.py [meridian_backend/src/core]"]
    N74["exporter.py [meridian_backend/src/core]"]
    N75["fim_sentinel.py [meridian_backend/src/core]"]
    N76["gaze_tracker.py [meridian_backend/src/core]"]
    N77["governor.py [meridian_backend/src/core]"]
    N78["graph_rag.py [meridian_backend/src/core]"]
    N79["graph_sync.py [meridian_backend/src/core]"]
    N80["hardware_detector.py [meridian_backend/src/core]"]
    N81["history_manager.py [meridian_backend/src/core]"]
    N82["lifespan.py [meridian_backend/src/core]"]
    N83["llm_auth.py [meridian_backend/src/core]"]
    N84["llm_client.py [meridian_backend/src/core]"]
    N85["llm_clients.py [meridian_backend/src/core]"]
    N86["llm_provider.py [meridian_backend/src/core]"]
    N87["local_model_manager.py [meridian_backend/src/core]"]
    N88["logger.py [meridian_backend/src/core]"]
    N89["logging_config.py [meridian_backend/src/core]"]
    N90["loop.py [meridian_backend/src/core]"]
    N91["loop_dispatcher.py [meridian_backend/src/core]"]
    N92["loop_executor.py [meridian_backend/src/core]"]
    N93["loop_parser.py [meridian_backend/src/core]"]
    N94["loop_planning.py [meridian_backend/src/core]"]
    N95["loop_stream.py [meridian_backend/src/core]"]
    N96["lsp_client.py [meridian_backend/src/core]"]
    N97["malware_scanner.py [meridian_backend/src/core]"]
    N98["mcp_client.py [meridian_backend/src/core]"]
    N99["mcp_executor.py [meridian_backend/src/core]"]
    N100["memory_backup.py [meridian_backend/src/core]"]
    N101["memory_consolidation.py [meridian_backend/src/core]"]
    N102["memory_editor.py [meridian_backend/src/core]"]
    N103["mobile_bridge.py [meridian_backend/src/core]"]
    N104["mode.py [meridian_backend/src/core]"]
    N105["neural_rag.py [meridian_backend/src/core]"]
    N106["oauth_manager.py [meridian_backend/src/core]"]
    N107["ollama_manager.py [meridian_backend/src/core]"]
    N108["p2p.py [meridian_backend/src/core]"]
    N109["p2p_crypto.py [meridian_backend/src/core]"]
    N110["p2p_discovery.py [meridian_backend/src/core]"]
    N111["p2p_pairing.py [meridian_backend/src/core]"]
    N112["perception.py [meridian_backend/src/core]"]
    N113["persistence_sentinel.py [meridian_backend/src/core]"]
    N114["personal_crm.py [meridian_backend/src/core]"]
    N115["plugins.py [meridian_backend/src/core]"]
    N116["polyglot.py [meridian_backend/src/core]"]
    N117["predictive_engine.py [meridian_backend/src/core]"]
    N118["presence_briefing.py [meridian_backend/src/core]"]
    N119["proactive_system_guard.py [meridian_backend/src/core]"]
    N120["prompt_injection.py [meridian_backend/src/core]"]
    N121["prompt_templates.py [meridian_backend/src/core]"]
    N122["rag_optimizer.py [meridian_backend/src/core]"]
    N123["reflection_engine.py [meridian_backend/src/core]"]
    N124["response_models.py [meridian_backend/src/core]"]
    N125["routine_executor.py [meridian_backend/src/core]"]
    N126["sandbox_runner.py [meridian_backend/src/core]"]
    N127["scheduler.py [meridian_backend/src/core]"]
    N128["screen_sense.py [meridian_backend/src/core]"]
    N129["security_middleware.py [meridian_backend/src/core]"]
    N130["self_evolving_tooling.py [meridian_backend/src/core]"]
    N131["silent_workflow_guardian.py [meridian_backend/src/core]"]
    N132["skills_loader.py [meridian_backend/src/core]"]
    N133["sos_protocol.py [meridian_backend/src/core]"]
    N134["speculative.py [meridian_backend/src/core]"]
    N135["swarm.py [meridian_backend/src/core]"]
    N136["system_defense.py [meridian_backend/src/core]"]
    N137["telegram_bridge.py [meridian_backend/src/core]"]
    N138["temporal_memory.py [meridian_backend/src/core]"]
    N139["tool_indexer.py [meridian_backend/src/core]"]
    N140["tool_regression_sentinel.py [meridian_backend/src/core]"]
    N141["triggers.py [meridian_backend/src/core]"]
    N142["updater.py [meridian_backend/src/core]"]
    N143["vault.py [meridian_backend/src/core]"]
    N144["vision.py [meridian_backend/src/core]"]
    N145["vision_face.py [meridian_backend/src/core]"]
    N146["vision_gesture.py [meridian_backend/src/core]"]
    N147["watcher.py [meridian_backend/src/core]"]
    N148["what_broke_detective.py [meridian_backend/src/core]"]
    N149["workflow_engine.py [meridian_backend/src/core]"]
    N150["workspace_orchestrator.py [meridian_backend/src/core]"]
    N151["commits.py [meridian_backend/src/core/proactive]"]
    N152["dispatcher.py [meridian_backend/src/core/proactive]"]
    N153["ergonomics.py [meridian_backend/src/core/proactive]"]
    N154["guard.py [meridian_backend/src/core/proactive]"]
    N155["__init__.py [meridian_backend/src/core/proactive]"]
    N156["cache.py [meridian_backend/src/db]"]
    N157["connection.py [meridian_backend/src/db]"]
    N158["contacts.py [meridian_backend/src/db]"]
    N159["conversations.py [meridian_backend/src/db]"]
    N160["embeddings.py [meridian_backend/src/db]"]
    N161["logs.py [meridian_backend/src/db]"]
    N162["memory.py [meridian_backend/src/db]"]
    N163["parsers.py [meridian_backend/src/db]"]
    N164["profile.py [meridian_backend/src/db]"]
    N165["rag.py [meridian_backend/src/db]"]
    N166["vectors.py [meridian_backend/src/db]"]
    N167["__init__.py [meridian_backend/src/db]"]
    N168["auto_reviewer.py [meridian_backend/src/tools]"]
    N169["bill_radar.py [meridian_backend/src/tools]"]
    N170["bookmark_manager.py [meridian_backend/src/tools]"]
    N171["browser_agent.py [meridian_backend/src/tools]"]
    N172["browser_extension_tools.py [meridian_backend/src/tools]"]
    N173["browser_use_agent.py [meridian_backend/src/tools]"]
    N174["cam_guard.py [meridian_backend/src/tools]"]
    N175["car_logbook.py [meridian_backend/src/tools]"]
    N176["chrome_manager.py [meridian_backend/src/tools]"]
    N177["clipboard.py [meridian_backend/src/tools]"]
    N178["communication.py [meridian_backend/src/tools]"]
    N179["day_planner.py [meridian_backend/src/tools]"]
    N180["db_query.py [meridian_backend/src/tools]"]
    N181["desktop.py [meridian_backend/src/tools]"]
    N182["detonation_sandbox.py [meridian_backend/src/tools]"]
    N183["developer.py [meridian_backend/src/tools]"]
    N184["dns_shield.py [meridian_backend/src/tools]"]
    N185["documents.py [meridian_backend/src/tools]"]
    N186["documents_office.py [meridian_backend/src/tools]"]
    N187["documents_slides.py [meridian_backend/src/tools]"]
    N188["dynamic_manager.py [meridian_backend/src/tools]"]
    N189["expense_pool.py [meridian_backend/src/tools]"]
    N190["expiry_sentinel.py [meridian_backend/src/tools]"]
    N191["exporter.py [meridian_backend/src/tools]"]
    N192["external_connectors.py [meridian_backend/src/tools]"]
    N193["family_board.py [meridian_backend/src/tools]"]
    N194["filesystem.py [meridian_backend/src/tools]"]
    N195["file_janitor.py [meridian_backend/src/tools]"]
    N196["finance_sentinel.py [meridian_backend/src/tools]"]
    N197["geo_location.py [meridian_backend/src/tools]"]
    N198["habit_tracker.py [meridian_backend/src/tools]"]
    N199["health_ingest.py [meridian_backend/src/tools]"]
    N200["home_assistant.py [meridian_backend/src/tools]"]
    N201["household.py [meridian_backend/src/tools]"]
    N202["knowledge.py [meridian_backend/src/tools]"]
    N203["learning_queue.py [meridian_backend/src/tools]"]
    N204["mcp_marketplace.py [meridian_backend/src/tools]"]
    N205["network_guardian.py [meridian_backend/src/tools]"]
    N206["networth_tracker.py [meridian_backend/src/tools]"]
    N207["ollama_manager.py [meridian_backend/src/tools]"]
    N208["os_automation.py [meridian_backend/src/tools]"]
    N209["papercoder.py [meridian_backend/src/tools]"]
    N210["parental_controls.py [meridian_backend/src/tools]"]
    N211["password_auditor.py [meridian_backend/src/tools]"]
    N212["phishing_guard.py [meridian_backend/src/tools]"]
    N213["phone_agent.py [meridian_backend/src/tools]"]
    N214["photo_organizer.py [meridian_backend/src/tools]"]
    N215["price_watcher.py [meridian_backend/src/tools]"]
    N216["recording.py [meridian_backend/src/tools]"]
    N217["registry.py [meridian_backend/src/tools]"]
    N218["review.py [meridian_backend/src/tools]"]
    N219["routine_composer.py [meridian_backend/src/tools]"]
    N220["scheduler.py [meridian_backend/src/tools]"]
    N221["screenshot_memory.py [meridian_backend/src/tools]"]
    N222["search_hub.py [meridian_backend/src/tools]"]
    N223["secure_shredder.py [meridian_backend/src/tools]"]
    N224["security_auditor.py [meridian_backend/src/tools]"]
    N225["shell.py [meridian_backend/src/tools]"]
    N226["system.py [meridian_backend/src/tools]"]
    N227["system_windows.py [meridian_backend/src/tools]"]
    N228["task_scheduler.py [meridian_backend/src/tools]"]
    N229["totp_generator.py [meridian_backend/src/tools]"]
    N230["travel_butler.py [meridian_backend/src/tools]"]
    N231["usb_watchdog.py [meridian_backend/src/tools]"]
    N232["vault.py [meridian_backend/src/tools]"]
    N233["video_editor.py [meridian_backend/src/tools]"]
    N234["voice.py [meridian_backend/src/tools]"]
    N235["watcher.py [meridian_backend/src/tools]"]
    N236["web.py [meridian_backend/src/tools]"]
    N237["web_browser.py [meridian_backend/src/tools]"]
    N238["web_scraper.py [meridian_backend/src/tools]"]
    N239["wellness.py [meridian_backend/src/tools]"]
    N240["whatsapp_manager.py [meridian_backend/src/tools]"]
    N241["wifi_assessor.py [meridian_backend/src/tools]"]
    N242["workspace_layout.py [meridian_backend/src/tools]"]
    N243["ambient_listener.py [meridian_backend/src/voice]"]
    N244["duplex.py [meridian_backend/src/voice]"]
    N245["polyglot.py [meridian_backend/src/voice]"]
    N246["stt.py [meridian_backend/src/voice]"]
    N247["tts.py [meridian_backend/src/voice]"]
    N248["vad.py [meridian_backend/src/voice]"]
    N249["voice_biometrics.py [meridian_backend/src/voice]"]
    N250["wakeword.py [meridian_backend/src/voice]"]
    N251["conftest.py [meridian_backend/tests]"]
    N252["run_tests.py [meridian_backend/tests]"]
    N253["test_advanced_proactive.py [meridian_backend/tests]"]
    N254["test_atomic_storage.py [meridian_backend/tests]"]
    N255["test_audit_bugfixes.py [meridian_backend/tests]"]
    N256["test_audit_remediation.py [meridian_backend/tests]"]
    N257["test_auto_bug_fixer.py [meridian_backend/tests]"]
    N258["test_backend_improvements.py [meridian_backend/tests]"]
    N259["test_backlog_features.py [meridian_backend/tests]"]
    N260["test_backlog_sprint.py [meridian_backend/tests]"]
    N261["test_bridges.py [meridian_backend/tests]"]
    N262["test_browser_agent.py [meridian_backend/tests]"]
    N263["test_browser_extension.py [meridian_backend/tests]"]
    N264["test_browser_fallback.py [meridian_backend/tests]"]
    N265["test_browser_frame.py [meridian_backend/tests]"]
    N266["test_browser_use.py [meridian_backend/tests]"]
    N267["test_butler_media.py [meridian_backend/tests]"]
    N268["test_chat_abort.py [meridian_backend/tests]"]
    N269["test_cognitive_graph.py [meridian_backend/tests]"]
    N270["test_config.py [meridian_backend/tests]"]
    N271["test_consensus_gate.py [meridian_backend/tests]"]
    N272["test_context_budget.py [meridian_backend/tests]"]
    N273["test_custom_password_auth.py [meridian_backend/tests]"]
    N274["test_database.py [meridian_backend/tests]"]
    N275["test_day10_features.py [meridian_backend/tests]"]
    N276["test_day11_features.py [meridian_backend/tests]"]
    N277["test_day12_features.py [meridian_backend/tests]"]
    N278["test_day13_features.py [meridian_backend/tests]"]
    N279["test_day14_day15_features.py [meridian_backend/tests]"]
    N280["test_day16_17_18_features.py [meridian_backend/tests]"]
    N281["test_day3_features.py [meridian_backend/tests]"]
    N282["test_day4_features.py [meridian_backend/tests]"]
    N283["test_day5_features.py [meridian_backend/tests]"]
    N284["test_day6_features.py [meridian_backend/tests]"]
    N285["test_day7_features.py [meridian_backend/tests]"]
    N286["test_day8_features.py [meridian_backend/tests]"]
    N287["test_day9_features.py [meridian_backend/tests]"]
    N288["test_dev_intelligence_suite.py [meridian_backend/tests]"]
    N289["test_document_tools.py [meridian_backend/tests]"]
    N290["test_error_diagnostics.py [meridian_backend/tests]"]
    N291["test_exhaustive_fallback.py [meridian_backend/tests]"]
    N292["test_full_proactive_suite.py [meridian_backend/tests]"]
    N293["test_geo_location.py [meridian_backend/tests]"]
    N294["test_hybrid_rag.py [meridian_backend/tests]"]
    N295["test_jarvis_perception.py [meridian_backend/tests]"]
    N296["test_known_errors_remediation.py [meridian_backend/tests]"]
    N297["test_llm_provider.py [meridian_backend/tests]"]
    N298["test_logging.py [meridian_backend/tests]"]
    N299["test_loop_parser.py [meridian_backend/tests]"]
    N300["test_loop_submodules.py [meridian_backend/tests]"]
    N301["test_mobile_websocket.py [meridian_backend/tests]"]
    N302["test_model_source.py [meridian_backend/tests]"]
    N303["test_multimode_routing.py [meridian_backend/tests]"]
    N304["test_multi_os.py [meridian_backend/tests]"]
    N305["test_new_features.py [meridian_backend/tests]"]
    N306["test_oauth.py [meridian_backend/tests]"]
    N307["test_p2p.py [meridian_backend/tests]"]
    N308["test_perception_bridge.py [meridian_backend/tests]"]
    N309["test_proactive.py [meridian_backend/tests]"]
    N310["test_proactive_mode.py [meridian_backend/tests]"]
    N311["test_proactive_notifications.py [meridian_backend/tests]"]
    N312["test_reflection_engine.py [meridian_backend/tests]"]
    N313["test_research_optimization.py [meridian_backend/tests]"]
    N314["test_response_resilience.py [meridian_backend/tests]"]
    N315["test_security_features.py [meridian_backend/tests]"]
    N316["test_silero_vad.py [meridian_backend/tests]"]
    N317["test_skill_packs.py [meridian_backend/tests]"]
    N318["test_small_model_support.py [meridian_backend/tests]"]
    N319["test_sprint24_hardening.py [meridian_backend/tests]"]
    N320["test_sprint25_hardening.py [meridian_backend/tests]"]
    N321["test_sprint27_hardening.py [meridian_backend/tests]"]
    N322["test_sprint28_hardening.py [meridian_backend/tests]"]
    N323["test_sprint2_features.py [meridian_backend/tests]"]
    N324["test_sprint40.py [meridian_backend/tests]"]
    N325["test_sprint45.py [meridian_backend/tests]"]
    N326["test_standalone_bridge.py [meridian_backend/tests]"]
    N327["test_stream_resiliency.py [meridian_backend/tests]"]
    N328["test_swarm.py [meridian_backend/tests]"]
    N329["test_swarm_routing.py [meridian_backend/tests]"]
    N330["test_system_hardening.py [meridian_backend/tests]"]
    N331["test_timeline_completion.py [meridian_backend/tests]"]
    N332["test_tools.py [meridian_backend/tests]"]
    N333["test_tool_intelligence.py [meridian_backend/tests]"]
    N334["test_tool_modernization.py [meridian_backend/tests]"]
    N335["test_tool_regression.py [meridian_backend/tests]"]
    N336["test_user_delight_tools.py [meridian_backend/tests]"]
    N337["test_vault.py [meridian_backend/tests]"]
    N338["test_video_editor.py [meridian_backend/tests]"]
    N339["test_voice_hardening.py [meridian_backend/tests]"]
    N340["test_voice_speed.py [meridian_backend/tests]"]
    N341["test_wakeword_continuous.py [meridian_backend/tests]"]
    N342["test_wakeword_onnx.py [meridian_backend/tests]"]
    N343["test_web_guards.py [meridian_backend/tests]"]
    N344["test_workflow.py [meridian_backend/tests]"]
    N345["vite.config.ts [meridian_frontend]"]
    N346["AppContext.tsx [meridian_frontend/src]"]
    N347["main.tsx [meridian_frontend/src]"]
    N348["Mascot.tsx [meridian_frontend/src]"]
    N349["Mascot3DCharacter.tsx [meridian_frontend/src]"]
    N350["MobileApp.tsx [meridian_frontend/src]"]
    N351["AgentStatusStream.tsx [meridian_frontend/src/components]"]
    N352["CommandPalette.tsx [meridian_frontend/src/components]"]
    N353["DevAutomationPanel.tsx [meridian_frontend/src/components]"]
    N354["DeveloperSuitePanel.tsx [meridian_frontend/src/components]"]
    N355["LocalModelManager.tsx [meridian_frontend/src/components]"]
    N356["MemoryConsolidationView.tsx [meridian_frontend/src/components]"]
    N357["NavRail.tsx [meridian_frontend/src/components]"]
    N358["PerceptionHUD.tsx [meridian_frontend/src/components]"]
    N359["ProactiveGuardBanner.tsx [meridian_frontend/src/components]"]
    N360["ProfileHeader.tsx [meridian_frontend/src/components]"]
    N361["RightDrawer.tsx [meridian_frontend/src/components]"]
    N362["ServerConnectionModal.tsx [meridian_frontend/src/components]"]
    N363["Shell.tsx [meridian_frontend/src/components]"]
    N364["StatusBar.tsx [meridian_frontend/src/components]"]
    N365["DropdownNav.tsx [meridian_frontend/src/components/mobile]"]
    N366["LiveThoughtCarousel.tsx [meridian_frontend/src/components/mobile]"]
    N367["MobilePairingModal.tsx [meridian_frontend/src/components/mobile]"]
    N368["VoiceOrbHUD.tsx [meridian_frontend/src/components/mobile]"]
    N369["AmbientParticles.tsx [meridian_frontend/src/components/ui]"]
    N370["CodeDiffViewer.tsx [meridian_frontend/src/components/ui]"]
    N371["ConnectionBanner.tsx [meridian_frontend/src/components/ui]"]
    N372["DataBadge.tsx [meridian_frontend/src/components/ui]"]
    N373["GlowCard.tsx [meridian_frontend/src/components/ui]"]
    N374["HoloButton.tsx [meridian_frontend/src/components/ui]"]
    N375["ProgressArc.tsx [meridian_frontend/src/components/ui]"]
    N376["TerminalLine.tsx [meridian_frontend/src/components/ui]"]
    N377["ToastContext.tsx [meridian_frontend/src/components/ui]"]
    N378["useMemoryOptimizer.ts [meridian_frontend/src/hooks]"]
    N379["oauthService.ts [meridian_frontend/src/services]"]
    N380["streamingAudioPlayer.ts [meridian_frontend/src/services]"]
    N381["BackendSetup.tsx [meridian_frontend/src/startup]"]
    N382["BootSequence.tsx [meridian_frontend/src/startup]"]
    N383["OnboardingWizard.tsx [meridian_frontend/src/startup]"]
    N384["SetupWizard.tsx [meridian_frontend/src/startup]"]
    N385["Clipboard.tsx [meridian_frontend/src/views]"]
    N386["Jobs.tsx [meridian_frontend/src/views]"]
    N387["MemoryEditor.tsx [meridian_frontend/src/views]"]
    N388["Productivity.tsx [meridian_frontend/src/views]"]
    N389["Settings.tsx [meridian_frontend/src/views]"]
    N390["SwarmDebate.tsx [meridian_frontend/src/views]"]
    N391["Timeline.tsx [meridian_frontend/src/views]"]
    N392["WorkflowBuilder.tsx [meridian_frontend/src/views]"]
    N393["AiModelsTab.tsx [meridian_frontend/src/views/settings]"]
    N394["IntegrationsTab.tsx [meridian_frontend/src/views/settings]"]
    N395["MascotTab.tsx [meridian_frontend/src/views/settings]"]
    N396["MultiModeTab.tsx [meridian_frontend/src/views/settings]"]
    N397["PasswordInput.tsx [meridian_frontend/src/views/settings]"]
    N398["SpendAirGapTab.tsx [meridian_frontend/src/views/settings]"]
    N399["SystemGuardTab.tsx [meridian_frontend/src/views/settings]"]
    N400["VoiceTab.tsx [meridian_frontend/src/views/settings]"]
    N401["config.py [meridian_frontend/src-tauri/api/_internal/cv2]"]
    N402["load_config_py3.py [meridian_frontend/src-tauri/api/_internal/cv2]"]
    N403["__init__.py [meridian_frontend/src-tauri/api/_internal/cv2]"]
    N404["__init__.py [meridian_frontend/src-tauri/api/_internal/cv2/data]"]
    N405["__init__.py [meridian_frontend/src-tauri/api/_internal/cv2/mat_wrapper]"]
    N406["version.py [meridian_frontend/src-tauri/api/_internal/cv2/misc]"]
    N407["__init__.py [meridian_frontend/src-tauri/api/_internal/cv2/typing]"]
    N408["__init__.py [meridian_frontend/src-tauri/api/_internal/cv2/utils]"]
    N409["applications.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N410["background.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N411["cli.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N412["concurrency.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N413["datastructures.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N414["encoders.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N415["exceptions.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N416["exception_handlers.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N417["logger.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N418["params.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N419["param_functions.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N420["requests.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N421["responses.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N422["routing.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N423["sse.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N424["staticfiles.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N425["templating.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N426["testclient.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N427["types.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N428["utils.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N429["websockets.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N430["__init__.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N431["__main__.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N432["models.py [meridian_frontend/src-tauri/api/_internal/fastapi/dependencies]"]
    N433["utils.py [meridian_frontend/src-tauri/api/_internal/fastapi/dependencies]"]
    N434["asyncexitstack.py [meridian_frontend/src-tauri/api/_internal/fastapi/middleware]"]
    N435["cors.py [meridian_frontend/src-tauri/api/_internal/fastapi/middleware]"]
    N436["gzip.py [meridian_frontend/src-tauri/api/_internal/fastapi/middleware]"]
    N437["httpsredirect.py [meridian_frontend/src-tauri/api/_internal/fastapi/middleware]"]
    N438["trustedhost.py [meridian_frontend/src-tauri/api/_internal/fastapi/middleware]"]
    N439["wsgi.py [meridian_frontend/src-tauri/api/_internal/fastapi/middleware]"]
    N440["__init__.py [meridian_frontend/src-tauri/api/_internal/fastapi/middleware]"]
    N441["docs.py [meridian_frontend/src-tauri/api/_internal/fastapi/openapi]"]
    N442["models.py [meridian_frontend/src-tauri/api/_internal/fastapi/openapi]"]
    N443["utils.py [meridian_frontend/src-tauri/api/_internal/fastapi/openapi]"]
    N444["api_key.py [meridian_frontend/src-tauri/api/_internal/fastapi/security]"]
    N445["base.py [meridian_frontend/src-tauri/api/_internal/fastapi/security]"]
    N446["http.py [meridian_frontend/src-tauri/api/_internal/fastapi/security]"]
    N447["oauth2.py [meridian_frontend/src-tauri/api/_internal/fastapi/security]"]
    N448["open_id_connect_url.py [meridian_frontend/src-tauri/api/_internal/fastapi/security]"]
    N449["shared.py [meridian_frontend/src-tauri/api/_internal/fastapi/_compat]"]
    N450["v2.py [meridian_frontend/src-tauri/api/_internal/fastapi/_compat]"]
    N451["coreBundle.js [meridian_frontend/src-tauri/api/_internal/playwright/driver/package/lib]"]
    N452["utilsBundle.js [meridian_frontend/src-tauri/api/_internal/playwright/driver/package/lib]"]
    N453["structs.d.ts [meridian_frontend/src-tauri/api/_internal/playwright/driver/package/types]"]
    N454["types.d.ts [meridian_frontend/src-tauri/api/_internal/playwright/driver/package/types]"]
    N455["aliases.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N456["alias_generators.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N457["annotated_handlers.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N458["color.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N459["config.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N460["dataclasses.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N461["errors.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N462["fields.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N463["functional_serializers.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N464["functional_validators.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N465["json_schema.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N466["main.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N467["mypy.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N468["networks.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N469["root_model.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N470["types.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N471["type_adapter.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N472["validate_call_decorator.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N473["version.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N474["warnings.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N475["_migration.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N476["__init__.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N477["class_validators.py [meridian_frontend/src-tauri/api/_internal/pydantic/deprecated]"]
    N478["config.py [meridian_frontend/src-tauri/api/_internal/pydantic/deprecated]"]
    N479["copy_internals.py [meridian_frontend/src-tauri/api/_internal/pydantic/deprecated]"]
    N480["decorator.py [meridian_frontend/src-tauri/api/_internal/pydantic/deprecated]"]
    N481["json.py [meridian_frontend/src-tauri/api/_internal/pydantic/deprecated]"]
    N482["parse.py [meridian_frontend/src-tauri/api/_internal/pydantic/deprecated]"]
    N483["tools.py [meridian_frontend/src-tauri/api/_internal/pydantic/deprecated]"]
    N484["arguments_schema.py [meridian_frontend/src-tauri/api/_internal/pydantic/experimental]"]
    N485["missing_sentinel.py [meridian_frontend/src-tauri/api/_internal/pydantic/experimental]"]
    N486["pipeline.py [meridian_frontend/src-tauri/api/_internal/pydantic/experimental]"]
    N487["_loader.py [meridian_frontend/src-tauri/api/_internal/pydantic/plugin]"]
    N488["_schema_validator.py [meridian_frontend/src-tauri/api/_internal/pydantic/plugin]"]
    N489["__init__.py [meridian_frontend/src-tauri/api/_internal/pydantic/plugin]"]
    N490["annotated_types.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N491["class_validators.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N492["color.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N493["config.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N494["dataclasses.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N495["datetime_parse.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N496["decorator.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N497["env_settings.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N498["errors.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N499["error_wrappers.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N500["fields.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N501["generics.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N502["json.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N503["main.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N504["mypy.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N505["networks.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N506["parse.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N507["schema.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N508["tools.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N509["types.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N510["typing.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N511["utils.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N512["validators.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N513["version.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N514["_hypothesis_plugin.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N515["__init__.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N516["_config.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N517["_core_metadata.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N518["_core_utils.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N519["_dataclasses.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N520["_decorators.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N521["_decorators_v1.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N522["_discriminated_union.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N523["_docs_extraction.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N524["_fields.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N525["_forward_ref.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N526["_generate_schema.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N527["_generics.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N528["_git.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N529["_import_utils.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N530["_internal_dataclass.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N531["_known_annotated_metadata.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N532["_mock_val_ser.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N533["_model_construction.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N534["_namespace_utils.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N535["_repr.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N536["_schema_gather.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N537["_schema_generation_shared.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N538["_serializers.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N539["_signature.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N540["_typing_extra.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N541["_utils.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N542["_validate_call.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N543["_validators.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N544["applications.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N545["authentication.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N546["background.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N547["concurrency.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N548["config.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N549["convertors.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N550["datastructures.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N551["endpoints.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N552["exceptions.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N553["formparsers.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N554["requests.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N555["responses.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N556["routing.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N557["schemas.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N558["staticfiles.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N559["status.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N560["templating.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N561["testclient.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N562["types.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N563["websockets.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N564["_exception_handler.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N565["_utils.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N566["authentication.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N567["base.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N568["cors.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N569["errors.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N570["exceptions.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N571["gzip.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N572["httpsredirect.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N573["sessions.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N574["trustedhost.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N575["wsgi.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N576["__init__.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N577["config.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N578["importer.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N579["logging.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N580["main.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N581["server.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N582["workers.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N583["_compat.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N584["_subprocess.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N585["_types.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N586["__init__.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N587["__main__.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N588["off.py [meridian_frontend/src-tauri/api/_internal/uvicorn/lifespan]"]
    N589["on.py [meridian_frontend/src-tauri/api/_internal/uvicorn/lifespan]"]
    N590["asyncio.py [meridian_frontend/src-tauri/api/_internal/uvicorn/loops]"]
    N591["auto.py [meridian_frontend/src-tauri/api/_internal/uvicorn/loops]"]
    N592["uvloop.py [meridian_frontend/src-tauri/api/_internal/uvicorn/loops]"]
    N593["asgi2.py [meridian_frontend/src-tauri/api/_internal/uvicorn/middleware]"]
    N594["message_logger.py [meridian_frontend/src-tauri/api/_internal/uvicorn/middleware]"]
    N595["proxy_headers.py [meridian_frontend/src-tauri/api/_internal/uvicorn/middleware]"]
    N596["wsgi.py [meridian_frontend/src-tauri/api/_internal/uvicorn/middleware]"]
    N597["utils.py [meridian_frontend/src-tauri/api/_internal/uvicorn/protocols]"]
    N598["auto.py [meridian_frontend/src-tauri/api/_internal/uvicorn/protocols/http]"]
    N599["flow_control.py [meridian_frontend/src-tauri/api/_internal/uvicorn/protocols/http]"]
    N600["h11_impl.py [meridian_frontend/src-tauri/api/_internal/uvicorn/protocols/http]"]
    N601["httptools_impl.py [meridian_frontend/src-tauri/api/_internal/uvicorn/protocols/http]"]
    N602["auto.py [meridian_frontend/src-tauri/api/_internal/uvicorn/protocols/websockets]"]
    N603["websockets_impl.py [meridian_frontend/src-tauri/api/_internal/uvicorn/protocols/websockets]"]
    N604["websockets_sansio_impl.py [meridian_frontend/src-tauri/api/_internal/uvicorn/protocols/websockets]"]
    N605["wsproto_impl.py [meridian_frontend/src-tauri/api/_internal/uvicorn/protocols/websockets]"]
    N606["basereload.py [meridian_frontend/src-tauri/api/_internal/uvicorn/supervisors]"]
    N607["multiprocess.py [meridian_frontend/src-tauri/api/_internal/uvicorn/supervisors]"]
    N608["statreload.py [meridian_frontend/src-tauri/api/_internal/uvicorn/supervisors]"]
    N609["watchfilesreload.py [meridian_frontend/src-tauri/api/_internal/uvicorn/supervisors]"]
    N610["__init__.py [meridian_frontend/src-tauri/api/_internal/uvicorn/supervisors]"]
    N611["auth.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N612["cli.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N613["client.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N614["connection.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N615["datastructures.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N616["exceptions.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N617["frames.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N618["headers.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N619["http11.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N620["imports.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N621["protocol.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N622["proxy.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N623["server.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N624["streams.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N625["typing.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N626["uri.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N627["utils.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N628["version.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N629["__init__.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N630["client.py [meridian_frontend/src-tauri/api/_internal/websockets/asyncio]"]
    N631["connection.py [meridian_frontend/src-tauri/api/_internal/websockets/asyncio]"]
    N632["messages.py [meridian_frontend/src-tauri/api/_internal/websockets/asyncio]"]
    N633["router.py [meridian_frontend/src-tauri/api/_internal/websockets/asyncio]"]
    N634["server.py [meridian_frontend/src-tauri/api/_internal/websockets/asyncio]"]
    N635["base.py [meridian_frontend/src-tauri/api/_internal/websockets/extensions]"]
    N636["permessage_deflate.py [meridian_frontend/src-tauri/api/_internal/websockets/extensions]"]
    N637["auth.py [meridian_frontend/src-tauri/api/_internal/websockets/legacy]"]
    N638["client.py [meridian_frontend/src-tauri/api/_internal/websockets/legacy]"]
    N639["exceptions.py [meridian_frontend/src-tauri/api/_internal/websockets/legacy]"]
    N640["framing.py [meridian_frontend/src-tauri/api/_internal/websockets/legacy]"]
    N641["handshake.py [meridian_frontend/src-tauri/api/_internal/websockets/legacy]"]
    N642["http.py [meridian_frontend/src-tauri/api/_internal/websockets/legacy]"]
    N643["protocol.py [meridian_frontend/src-tauri/api/_internal/websockets/legacy]"]
    N644["server.py [meridian_frontend/src-tauri/api/_internal/websockets/legacy]"]
    N645["__init__.py [meridian_frontend/src-tauri/api/_internal/websockets/legacy]"]
    N646["client.py [meridian_frontend/src-tauri/api/_internal/websockets/sync]"]
    N647["connection.py [meridian_frontend/src-tauri/api/_internal/websockets/sync]"]
    N648["messages.py [meridian_frontend/src-tauri/api/_internal/websockets/sync]"]
    N649["router.py [meridian_frontend/src-tauri/api/_internal/websockets/sync]"]
    N650["server.py [meridian_frontend/src-tauri/api/_internal/websockets/sync]"]
    N651["utils.py [meridian_frontend/src-tauri/api/_internal/websockets/sync]"]
    N652["client.py [meridian_frontend/src-tauri/api/_internal/websockets/trio]"]
    N653["connection.py [meridian_frontend/src-tauri/api/_internal/websockets/trio]"]
    N654["messages.py [meridian_frontend/src-tauri/api/_internal/websockets/trio]"]
    N655["router.py [meridian_frontend/src-tauri/api/_internal/websockets/trio]"]
    N656["server.py [meridian_frontend/src-tauri/api/_internal/websockets/trio]"]
    N657["utils.py [meridian_frontend/src-tauri/api/_internal/websockets/trio]"]
    N658["build_apk.py [meridian_mobile]"]
    N659["flutter_lldb_helper.py [meridian_mobile/ios/Flutter/ephemeral]"]
    N660["get_system_platform_info.py [plugins]"]

    N1 --> N481
    N1 --> N502
    N1 --> N510
    N1 --> N625
    N2 --> N481
    N2 --> N502
    N2 --> N510
    N2 --> N625
    N3 --> N481
    N3 --> N502
    N4 --> N481
    N4 --> N502
    N4 --> N510
    N4 --> N625
    N5 --> N590
    N5 --> N481
    N5 --> N502
    N5 --> N15
    N5 --> N14
    N9 --> N481
    N9 --> N502
    N9 --> N510
    N9 --> N625
    N10 --> N460
    N10 --> N494
    N13 --> N10
    N13 --> N58
    N13 --> N401
    N13 --> N459
    N13 --> N478
    N13 --> N493
    N13 --> N548
    N13 --> N577
    N13 --> N12
    N13 --> N11
    N14 --> N481
    N14 --> N502
    N14 --> N579
    N14 --> N590
    N14 --> N510
    N14 --> N625
    N14 --> N15
    N16 --> N481
    N16 --> N502
    N16 --> N590
    N16 --> N579
    N16 --> N510
    N16 --> N625
    N20 --> N481
    N20 --> N502
    N20 --> N510
    N20 --> N625
    N20 --> N15
    N21 --> N481
    N21 --> N502
    N21 --> N579
    N21 --> N510
    N21 --> N625
    N22 --> N481
    N22 --> N502
    N22 --> N590
    N22 --> N510
    N22 --> N625
    N22 --> N15
    N23 --> N481
    N23 --> N502
    N23 --> N579
    N23 --> N510
    N23 --> N625
    N23 --> N15
    N24 --> N481
    N24 --> N502
    N24 --> N510
    N24 --> N625
    N25 --> N481
    N25 --> N502
    N25 --> N510
    N25 --> N625
    N25 --> N15
    N26 --> N510
    N26 --> N625
    N27 --> N510
    N27 --> N625
    N27 --> N15
    N28 --> N510
    N28 --> N625
    N28 --> N15
    N29 --> N481
    N29 --> N502
    N29 --> N510
    N29 --> N625
    N29 --> N15
    N30 --> N481
    N30 --> N502
    N30 --> N579
    N30 --> N590
    N30 --> N510
    N30 --> N625
    N30 --> N15
    N31 --> N481
    N31 --> N502
    N31 --> N510
    N31 --> N625
    N31 --> N15
    N31 --> N590
    N32 --> N510
    N32 --> N625
    N33 --> N579
    N33 --> N510
    N33 --> N625
    N34 --> N481
    N34 --> N502
    N34 --> N590
    N34 --> N510
    N34 --> N625
    N35 --> N481
    N35 --> N502
    N35 --> N510
    N35 --> N625
    N35 --> N15
    N37 --> N481
    N37 --> N502
    N37 --> N579
    N37 --> N510
    N37 --> N625
    N37 --> N15
    N38 --> N590
    N38 --> N579
    N38 --> N510
    N38 --> N625
    N39 --> N579
    N39 --> N510
    N39 --> N625
    N40 --> N579
    N40 --> N510
    N40 --> N625
    N41 --> N481
    N41 --> N502
    N41 --> N579
    N41 --> N510
    N41 --> N625
    N42 --> N481
    N42 --> N502
    N42 --> N579
    N43 --> N510
    N43 --> N625
    N43 --> N481
    N43 --> N502
    N44 --> N579
    N44 --> N510
    N44 --> N625
    N45 --> N579
    N45 --> N510
    N45 --> N625
    N46 --> N579
    N46 --> N510
    N46 --> N625
    N46 --> N481
    N46 --> N502
    N47 --> N590
    N47 --> N481
    N47 --> N502
    N47 --> N579
    N47 --> N510
    N47 --> N625
    N48 --> N590
    N48 --> N510
    N48 --> N625
    N49 --> N579
    N49 --> N510
    N49 --> N625
    N50 --> N579
    N50 --> N510
    N50 --> N625
    N50 --> N460
    N50 --> N494
    N51 --> N579
    N51 --> N510
    N51 --> N625
    N52 --> N590
    N52 --> N510
    N52 --> N625
    N53 --> N510
    N53 --> N625
    N53 --> N15
    N54 --> N510
    N54 --> N625
    N55 --> N481
    N55 --> N502
    N55 --> N579
    N55 --> N510
    N55 --> N625
    N56 --> N579
    N56 --> N510
    N56 --> N625
    N57 --> N579
    N57 --> N510
    N57 --> N625
    N57 --> N460
    N57 --> N494
    N59 --> N590
    N59 --> N510
    N59 --> N625
    N59 --> N15
    N60 --> N481
    N60 --> N502
    N60 --> N579
    N60 --> N510
    N60 --> N625
    N60 --> N590
    N60 --> N15
    N61 --> N579
    N61 --> N510
    N61 --> N625
    N62 --> N579
    N62 --> N510
    N62 --> N625
    N62 --> N460
    N62 --> N494
    N63 --> N579
    N63 --> N510
    N63 --> N625
    N63 --> N460
    N63 --> N494
    N64 --> N590
    N64 --> N579
    N64 --> N510
    N64 --> N625
    N65 --> N590
    N65 --> N510
    N65 --> N625
    N65 --> N15
    N66 --> N510
    N66 --> N625
    N68 --> N481
    N68 --> N502
    N68 --> N579
    N68 --> N510
    N68 --> N625
    N68 --> N15
    N69 --> N579
    N69 --> N510
    N69 --> N625
    N70 --> N579
    N70 --> N510
    N70 --> N625
    N71 --> N510
    N71 --> N625
    N72 --> N579
    N72 --> N510
    N72 --> N625
    N73 --> N579
    N73 --> N510
    N73 --> N625
    N74 --> N510
    N74 --> N625
    N74 --> N15
    N75 --> N579
    N75 --> N510
    N75 --> N625
    N76 --> N579
    N76 --> N510
    N76 --> N625
    N77 --> N510
    N77 --> N625
    N78 --> N481
    N78 --> N502
    N78 --> N510
    N78 --> N625
    N79 --> N481
    N79 --> N502
    N79 --> N510
    N79 --> N625
    N80 --> N579
    N80 --> N510
    N80 --> N625
    N80 --> N474
    N80 --> N481
    N80 --> N502
    N82 --> N590
    N82 --> N579
    N82 --> N15
    N83 --> N579
    N83 --> N510
    N83 --> N625
    N83 --> N15
    N84 --> N590
    N84 --> N579
    N84 --> N510
    N84 --> N625
    N84 --> N15
    N85 --> N510
    N85 --> N625
    N85 --> N15
    N86 --> N481
    N86 --> N502
    N86 --> N579
    N86 --> N590
    N86 --> N510
    N86 --> N625
    N86 --> N15
    N87 --> N579
    N87 --> N590
    N87 --> N510
    N87 --> N625
    N87 --> N15
    N87 --> N481
    N87 --> N502
    N88 --> N481
    N88 --> N502
    N88 --> N579
    N88 --> N510
    N88 --> N625
    N89 --> N579
    N89 --> N481
    N89 --> N502
    N90 --> N481
    N90 --> N502
    N90 --> N590
    N90 --> N510
    N90 --> N625
    N90 --> N15
    N91 --> N481
    N91 --> N502
    N91 --> N590
    N91 --> N510
    N91 --> N625
    N91 --> N15
    N92 --> N481
    N92 --> N502
    N92 --> N510
    N92 --> N625
    N92 --> N15
    N93 --> N481
    N93 --> N502
    N93 --> N590
    N93 --> N510
    N93 --> N625
    N93 --> N15
    N94 --> N481
    N94 --> N502
    N94 --> N590
    N94 --> N510
    N94 --> N625
    N94 --> N15
    N95 --> N481
    N95 --> N502
    N95 --> N590
    N95 --> N510
    N95 --> N625
    N95 --> N15
    N96 --> N481
    N96 --> N502
    N96 --> N590
    N96 --> N510
    N96 --> N625
    N97 --> N579
    N97 --> N510
    N97 --> N625
    N98 --> N481
    N98 --> N502
    N98 --> N590
    N98 --> N579
    N98 --> N510
    N98 --> N625
    N99 --> N590
    N99 --> N481
    N99 --> N502
    N99 --> N579
    N99 --> N510
    N99 --> N625
    N100 --> N481
    N100 --> N502
    N100 --> N510
    N100 --> N625
    N101 --> N579
    N101 --> N590
    N101 --> N481
    N101 --> N502
    N101 --> N510
    N101 --> N625
    N101 --> N15
    N102 --> N481
    N102 --> N502
    N102 --> N510
    N102 --> N625
    N102 --> N15
    N103 --> N481
    N103 --> N502
    N103 --> N579
    N103 --> N510
    N103 --> N625
    N103 --> N15
    N103 --> N590
    N104 --> N510
    N104 --> N625
    N104 --> N15
    N104 --> N481
    N104 --> N502
    N105 --> N510
    N105 --> N625
    N106 --> N481
    N106 --> N502
    N106 --> N510
    N106 --> N625
    N107 --> N579
    N107 --> N590
    N107 --> N510
    N107 --> N625
    N107 --> N481
    N107 --> N502
    N108 --> N481
    N108 --> N502
    N108 --> N510
    N108 --> N625
    N108 --> N15
    N110 --> N510
    N110 --> N625
    N111 --> N510
    N111 --> N625
    N112 --> N579
    N112 --> N510
    N112 --> N625
    N113 --> N579
    N113 --> N510
    N113 --> N625
    N114 --> N579
    N114 --> N510
    N114 --> N625
    N114 --> N15
    N115 --> N510
    N115 --> N625
    N116 --> N579
    N116 --> N510
    N116 --> N625
    N117 --> N579
    N117 --> N510
    N117 --> N625
    N118 --> N579
    N118 --> N510
    N118 --> N625
    N119 --> N579
    N119 --> N510
    N119 --> N625
    N120 --> N579
    N120 --> N510
    N120 --> N625
    N121 --> N481
    N121 --> N502
    N121 --> N510
    N121 --> N625
    N122 --> N510
    N122 --> N625
    N123 --> N481
    N123 --> N502
    N123 --> N579
    N123 --> N510
    N123 --> N625
    N124 --> N510
    N124 --> N625
    N125 --> N579
    N125 --> N510
    N125 --> N625
    N126 --> N579
    N126 --> N510
    N126 --> N625
    N127 --> N590
    N127 --> N474
    N127 --> N15
    N127 --> N481
    N127 --> N502
    N128 --> N590
    N128 --> N579
    N128 --> N510
    N128 --> N625
    N129 --> N579
    N129 --> N510
    N129 --> N625
    N130 --> N579
    N130 --> N510
    N130 --> N625
    N131 --> N579
    N131 --> N510
    N131 --> N625
    N132 --> N579
    N132 --> N510
    N132 --> N625
    N133 --> N579
    N133 --> N510
    N133 --> N625
    N133 --> N15
    N134 --> N481
    N134 --> N502
    N134 --> N590
    N134 --> N510
    N134 --> N625
    N134 --> N15
    N135 --> N590
    N135 --> N481
    N135 --> N502
    N135 --> N510
    N135 --> N625
    N135 --> N15
    N136 --> N579
    N136 --> N510
    N136 --> N625
    N137 --> N510
    N137 --> N625
    N137 --> N590
    N137 --> N15
    N138 --> N510
    N138 --> N625
    N139 --> N510
    N139 --> N625
    N140 --> N579
    N140 --> N510
    N140 --> N625
    N141 --> N510
    N141 --> N625
    N142 --> N579
    N142 --> N510
    N142 --> N625
    N143 --> N481
    N143 --> N502
    N143 --> N510
    N143 --> N625
    N144 --> N579
    N144 --> N510
    N144 --> N625
    N144 --> N15
    N145 --> N579
    N145 --> N510
    N145 --> N625
    N146 --> N579
    N146 --> N510
    N146 --> N625
    N147 --> N579
    N147 --> N510
    N147 --> N625
    N148 --> N579
    N148 --> N510
    N148 --> N625
    N149 --> N481
    N149 --> N502
    N149 --> N510
    N149 --> N625
    N150 --> N579
    N150 --> N510
    N150 --> N625
    N151 --> N510
    N151 --> N625
    N151 --> N15
    N151 --> N14
    N152 --> N590
    N152 --> N510
    N152 --> N625
    N153 --> N510
    N153 --> N625
    N154 --> N579
    N154 --> N510
    N154 --> N625
    N154 --> N15
    N156 --> N510
    N156 --> N625
    N157 --> N510
    N157 --> N625
    N158 --> N510
    N158 --> N625
    N159 --> N510
    N159 --> N625
    N160 --> N510
    N160 --> N625
    N161 --> N510
    N161 --> N625
    N162 --> N481
    N162 --> N502
    N164 --> N481
    N164 --> N502
    N164 --> N510
    N164 --> N625
    N165 --> N481
    N165 --> N502
    N165 --> N510
    N165 --> N625
    N166 --> N510
    N166 --> N625
    N168 --> N510
    N168 --> N625
    N169 --> N481
    N169 --> N502
    N169 --> N510
    N169 --> N625
    N170 --> N579
    N170 --> N510
    N170 --> N625
    N171 --> N481
    N171 --> N502
    N171 --> N579
    N171 --> N510
    N171 --> N625
    N172 --> N590
    N172 --> N510
    N172 --> N625
    N173 --> N481
    N173 --> N502
    N173 --> N510
    N173 --> N625
    N173 --> N590
    N173 --> N15
    N174 --> N510
    N174 --> N625
    N175 --> N579
    N175 --> N510
    N175 --> N625
    N175 --> N460
    N175 --> N494
    N176 --> N481
    N176 --> N502
    N176 --> N510
    N176 --> N625
    N176 --> N15
    N177 --> N510
    N177 --> N625
    N177 --> N15
    N177 --> N481
    N177 --> N502
    N178 --> N579
    N178 --> N510
    N178 --> N625
    N178 --> N15
    N179 --> N579
    N179 --> N510
    N179 --> N625
    N180 --> N510
    N180 --> N625
    N180 --> N15
    N181 --> N510
    N181 --> N625
    N181 --> N15
    N182 --> N510
    N182 --> N625
    N183 --> N590
    N183 --> N510
    N183 --> N625
    N184 --> N510
    N184 --> N625
    N185 --> N510
    N185 --> N625
    N186 --> N510
    N186 --> N625
    N187 --> N510
    N187 --> N625
    N188 --> N579
    N188 --> N510
    N188 --> N625
    N189 --> N579
    N189 --> N510
    N189 --> N625
    N190 --> N481
    N190 --> N502
    N190 --> N510
    N190 --> N625
    N191 --> N481
    N191 --> N502
    N191 --> N510
    N191 --> N625
    N191 --> N15
    N192 --> N481
    N192 --> N502
    N192 --> N420
    N192 --> N554
    N192 --> N510
    N192 --> N625
    N193 --> N579
    N193 --> N510
    N193 --> N625
    N194 --> N510
    N194 --> N625
    N195 --> N510
    N195 --> N625
    N196 --> N481
    N196 --> N502
    N196 --> N510
    N196 --> N625
    N197 --> N510
    N197 --> N625
    N198 --> N579
    N198 --> N510
    N198 --> N625
    N199 --> N510
    N199 --> N625
    N200 --> N579
    N200 --> N510
    N200 --> N625
    N201 --> N481
    N201 --> N502
    N201 --> N510
    N201 --> N625
    N202 --> N510
    N202 --> N625
    N202 --> N15
    N203 --> N579
    N203 --> N510
    N203 --> N625
    N204 --> N481
    N204 --> N502
    N204 --> N510
    N204 --> N625
    N205 --> N510
    N205 --> N625
    N206 --> N579
    N206 --> N510
    N206 --> N625
    N207 --> N15
    N208 --> N579
    N208 --> N510
    N208 --> N625
    N209 --> N481
    N209 --> N502
    N209 --> N510
    N209 --> N625
    N209 --> N460
    N209 --> N494
    N209 --> N10
    N209 --> N58
    N209 --> N401
    N209 --> N459
    N209 --> N478
    N209 --> N493
    N209 --> N548
    N209 --> N577
    N209 --> N12
    N209 --> N11
    N210 --> N579
    N210 --> N510
    N210 --> N625
    N211 --> N510
    N211 --> N625
    N212 --> N510
    N212 --> N625
    N213 --> N481
    N213 --> N502
    N213 --> N590
    N213 --> N579
    N213 --> N510
    N213 --> N625
    N213 --> N15
    N214 --> N579
    N214 --> N510
    N214 --> N625
    N215 --> N579
    N215 --> N510
    N215 --> N625
    N216 --> N481
    N216 --> N502
    N216 --> N15
    N217 --> N590
    N217 --> N510
    N217 --> N625
    N217 --> N15
    N217 --> N481
    N217 --> N502
    N218 --> N510
    N218 --> N625
    N218 --> N15
    N219 --> N579
    N219 --> N510
    N219 --> N625
    N221 --> N481
    N221 --> N502
    N221 --> N510
    N221 --> N625
    N222 --> N510
    N222 --> N625
    N222 --> N15
    N223 --> N579
    N223 --> N510
    N223 --> N625
    N224 --> N510
    N224 --> N625
    N225 --> N510
    N225 --> N625
    N225 --> N15
    N226 --> N15
    N229 --> N510
    N229 --> N625
    N230 --> N481
    N230 --> N502
    N230 --> N510
    N230 --> N625
    N231 --> N510
    N231 --> N625
    N232 --> N510
    N232 --> N625
    N232 --> N481
    N232 --> N502
    N233 --> N579
    N233 --> N510
    N233 --> N625
    N235 --> N510
    N235 --> N625
    N236 --> N510
    N236 --> N625
    N236 --> N15
    N237 --> N481
    N237 --> N502
    N237 --> N510
    N237 --> N625
    N237 --> N15
    N238 --> N510
    N238 --> N625
    N238 --> N15
    N239 --> N510
    N239 --> N625
    N240 --> N481
    N240 --> N502
    N240 --> N579
    N240 --> N510
    N240 --> N625
    N240 --> N15
    N241 --> N579
    N241 --> N510
    N241 --> N625
    N242 --> N579
    N242 --> N510
    N242 --> N625
    N243 --> N590
    N243 --> N579
    N243 --> N510
    N243 --> N625
    N244 --> N510
    N244 --> N625
    N245 --> N579
    N245 --> N510
    N245 --> N625
    N246 --> N579
    N246 --> N15
    N247 --> N579
    N247 --> N510
    N247 --> N625
    N247 --> N15
    N248 --> N510
    N248 --> N625
    N249 --> N510
    N249 --> N625
    N250 --> N579
    N250 --> N510
    N250 --> N625
    N250 --> N15
    N254 --> N481
    N254 --> N502
    N255 --> N590
    N255 --> N481
    N255 --> N502
    N257 --> N590
    N257 --> N14
    N259 --> N15
    N260 --> N14
    N263 --> N590
    N267 --> N15
    N268 --> N14
    N272 --> N15
    N274 --> N15
    N275 --> N590
    N281 --> N15
    N282 --> N15
    N283 --> N14
    N285 --> N481
    N285 --> N502
    N285 --> N15
    N287 --> N481
    N287 --> N502
    N287 --> N15
    N287 --> N590
    N288 --> N590
    N288 --> N14
    N291 --> N481
    N291 --> N502
    N294 --> N15
    N297 --> N590
    N298 --> N579
    N298 --> N481
    N298 --> N502
    N299 --> N481
    N299 --> N502
    N300 --> N590
    N301 --> N481
    N301 --> N502
    N301 --> N14
    N301 --> N590
    N302 --> N15
    N303 --> N481
    N303 --> N502
    N303 --> N15
    N303 --> N14
    N305 --> N590
    N305 --> N14
    N307 --> N15
    N308 --> N14
    N309 --> N590
    N310 --> N481
    N310 --> N502
    N311 --> N590
    N311 --> N14
    N313 --> N481
    N313 --> N502
    N314 --> N481
    N314 --> N502
    N315 --> N14
    N315 --> N510
    N315 --> N625
    N315 --> N590
    N318 --> N481
    N318 --> N502
    N319 --> N14
    N320 --> N481
    N320 --> N502
    N321 --> N579
    N322 --> N15
    N323 --> N14
    N324 --> N590
    N325 --> N481
    N325 --> N502
    N325 --> N4
    N326 --> N481
    N326 --> N502
    N326 --> N16
    N327 --> N590
    N328 --> N590
    N330 --> N481
    N330 --> N502
    N331 --> N510
    N331 --> N625
    N332 --> N481
    N332 --> N502
    N333 --> N481
    N333 --> N502
    N334 --> N590
    N340 --> N14
    N341 --> N14
    N342 --> N14
    N346 --> N427
    N346 --> N454
    N346 --> N470
    N346 --> N509
    N346 --> N562
    N346 --> N10
    N346 --> N58
    N346 --> N401
    N346 --> N459
    N346 --> N478
    N346 --> N493
    N346 --> N548
    N346 --> N577
    N347 --> N613
    N347 --> N630
    N347 --> N638
    N347 --> N646
    N347 --> N652
    N347 --> N382
    N347 --> N384
    N347 --> N363
    N347 --> N346
    N347 --> N10
    N347 --> N58
    N347 --> N401
    N347 --> N459
    N347 --> N478
    N347 --> N493
    N347 --> N548
    N347 --> N577
    N347 --> N383
    N347 --> N381
    N348 --> N10
    N348 --> N58
    N348 --> N401
    N348 --> N459
    N348 --> N478
    N348 --> N493
    N348 --> N548
    N348 --> N577
    N348 --> N346
    N348 --> N380
    N350 --> N365
    N350 --> N368
    N350 --> N366
    N351 --> N10
    N351 --> N58
    N351 --> N401
    N351 --> N459
    N351 --> N478
    N351 --> N493
    N351 --> N548
    N351 --> N577
    N353 --> N10
    N353 --> N58
    N353 --> N401
    N353 --> N459
    N353 --> N478
    N353 --> N493
    N353 --> N548
    N353 --> N577
    N354 --> N10
    N354 --> N58
    N354 --> N401
    N354 --> N459
    N354 --> N478
    N354 --> N493
    N354 --> N548
    N354 --> N577
    N355 --> N377
    N355 --> N10
    N355 --> N58
    N355 --> N401
    N355 --> N459
    N355 --> N478
    N355 --> N493
    N355 --> N548
    N355 --> N577
    N356 --> N10
    N356 --> N58
    N356 --> N401
    N356 --> N459
    N356 --> N478
    N356 --> N493
    N356 --> N548
    N356 --> N577
    N357 --> N346
    N357 --> N348
    N359 --> N10
    N359 --> N58
    N359 --> N401
    N359 --> N459
    N359 --> N478
    N359 --> N493
    N359 --> N548
    N359 --> N577
    N361 --> N346
    N361 --> N375
    N361 --> N372
    N362 --> N10
    N362 --> N58
    N362 --> N401
    N362 --> N459
    N362 --> N478
    N362 --> N493
    N362 --> N548
    N362 --> N577
    N363 --> N346
    N363 --> N357
    N363 --> N364
    N363 --> N361
    N363 --> N352
    N363 --> N377
    N363 --> N391
    N363 --> N386
    N363 --> N385
    N363 --> N388
    N363 --> N369
    N363 --> N359
    N363 --> N371
    N364 --> N367
    N364 --> N346
    N364 --> N10
    N364 --> N58
    N364 --> N401
    N364 --> N459
    N364 --> N478
    N364 --> N493
    N364 --> N548
    N364 --> N577
    N367 --> N10
    N367 --> N58
    N367 --> N401
    N367 --> N459
    N367 --> N478
    N367 --> N493
    N367 --> N548
    N367 --> N577
    N369 --> N378
    N371 --> N346
    N371 --> N10
    N371 --> N58
    N371 --> N401
    N371 --> N459
    N371 --> N478
    N371 --> N493
    N371 --> N548
    N371 --> N577
    N379 --> N10
    N379 --> N58
    N379 --> N401
    N379 --> N459
    N379 --> N478
    N379 --> N493
    N379 --> N548
    N379 --> N577
    N380 --> N10
    N380 --> N58
    N380 --> N401
    N380 --> N459
    N380 --> N478
    N380 --> N493
    N380 --> N548
    N380 --> N577
    N381 --> N10
    N381 --> N58
    N381 --> N401
    N381 --> N459
    N381 --> N478
    N381 --> N493
    N381 --> N548
    N381 --> N577
    N382 --> N10
    N382 --> N58
    N382 --> N401
    N382 --> N459
    N382 --> N478
    N382 --> N493
    N382 --> N548
    N382 --> N577
    N382 --> N348
    N383 --> N10
    N383 --> N58
    N383 --> N401
    N383 --> N459
    N383 --> N478
    N383 --> N493
    N383 --> N548
    N383 --> N577
    N384 --> N374
    N384 --> N10
    N384 --> N58
    N384 --> N401
    N384 --> N459
    N384 --> N478
    N384 --> N493
    N384 --> N548
    N384 --> N577
    N385 --> N427
    N385 --> N454
    N385 --> N470
    N385 --> N509
    N385 --> N562
    N385 --> N346
    N385 --> N374
    N385 --> N10
    N385 --> N58
    N385 --> N401
    N385 --> N459
    N385 --> N478
    N385 --> N493
    N385 --> N548
    N385 --> N577
    N386 --> N427
    N386 --> N454
    N386 --> N470
    N386 --> N509
    N386 --> N562
    N386 --> N374
    N386 --> N373
    N386 --> N10
    N386 --> N58
    N386 --> N401
    N386 --> N459
    N386 --> N478
    N386 --> N493
    N386 --> N548
    N386 --> N577
    N387 --> N10
    N387 --> N58
    N387 --> N401
    N387 --> N459
    N387 --> N478
    N387 --> N493
    N387 --> N548
    N387 --> N577
    N388 --> N427
    N388 --> N454
    N388 --> N470
    N388 --> N509
    N388 --> N562
    N388 --> N375
    N388 --> N374
    N388 --> N373
    N388 --> N10
    N388 --> N58
    N388 --> N401
    N388 --> N459
    N388 --> N478
    N388 --> N493
    N388 --> N548
    N388 --> N577
    N388 --> N355
    N388 --> N356
    N388 --> N353
    N388 --> N351
    N388 --> N354
    N389 --> N10
    N389 --> N58
    N389 --> N401
    N389 --> N459
    N389 --> N478
    N389 --> N493
    N389 --> N548
    N389 --> N577
    N389 --> N427
    N389 --> N454
    N389 --> N470
    N389 --> N509
    N389 --> N562
    N389 --> N346
    N389 --> N378
    N389 --> N375
    N389 --> N374
    N389 --> N373
    N389 --> N395
    N389 --> N400
    N389 --> N394
    N389 --> N393
    N389 --> N396
    N389 --> N399
    N389 --> N398
    N389 --> N397
    N390 --> N376
    N390 --> N374
    N390 --> N10
    N390 --> N58
    N390 --> N401
    N390 --> N459
    N390 --> N478
    N390 --> N493
    N390 --> N548
    N390 --> N577
    N391 --> N427
    N391 --> N454
    N391 --> N470
    N391 --> N509
    N391 --> N562
    N391 --> N374
    N391 --> N373
    N391 --> N10
    N391 --> N58
    N391 --> N401
    N391 --> N459
    N391 --> N478
    N391 --> N493
    N391 --> N548
    N391 --> N577
    N391 --> N380
    N391 --> N370
    N392 --> N10
    N392 --> N58
    N392 --> N401
    N392 --> N459
    N392 --> N478
    N392 --> N493
    N392 --> N548
    N392 --> N577
    N393 --> N373
    N393 --> N374
    N393 --> N397
    N394 --> N373
    N394 --> N374
    N394 --> N397
    N394 --> N10
    N394 --> N58
    N394 --> N401
    N394 --> N459
    N394 --> N478
    N394 --> N493
    N394 --> N548
    N394 --> N577
    N395 --> N373
    N396 --> N373
    N396 --> N374
    N396 --> N10
    N396 --> N58
    N396 --> N401
    N396 --> N459
    N396 --> N478
    N396 --> N493
    N396 --> N548
    N396 --> N577
    N398 --> N373
    N398 --> N374
    N399 --> N373
    N399 --> N374
    N400 --> N373
    N400 --> N374
    N405 --> N510
    N405 --> N625
    N407 --> N510
    N407 --> N625
    N409 --> N510
    N409 --> N625
    N410 --> N510
    N410 --> N625
    N412 --> N510
    N412 --> N625
    N413 --> N510
    N413 --> N625
    N414 --> N460
    N414 --> N494
    N414 --> N427
    N414 --> N454
    N414 --> N470
    N414 --> N509
    N414 --> N562
    N414 --> N510
    N414 --> N625
    N415 --> N510
    N415 --> N625
    N417 --> N579
    N418 --> N474
    N418 --> N460
    N418 --> N494
    N418 --> N510
    N418 --> N625
    N419 --> N510
    N419 --> N625
    N421 --> N510
    N421 --> N625
    N422 --> N481
    N422 --> N502
    N422 --> N427
    N422 --> N454
    N422 --> N470
    N422 --> N509
    N422 --> N562
    N422 --> N460
    N422 --> N494
    N422 --> N510
    N422 --> N625
    N423 --> N510
    N423 --> N625
    N427 --> N454
    N427 --> N470
    N427 --> N509
    N427 --> N562
    N427 --> N510
    N427 --> N625
    N428 --> N474
    N428 --> N510
    N428 --> N625
    N432 --> N460
    N432 --> N494
    N432 --> N510
    N432 --> N625
    N432 --> N590
    N433 --> N460
    N433 --> N494
    N433 --> N510
    N433 --> N625
    N441 --> N481
    N441 --> N502
    N441 --> N510
    N441 --> N625
    N442 --> N510
    N442 --> N625
    N443 --> N446
    N443 --> N642
    N443 --> N474
    N443 --> N510
    N443 --> N625
    N444 --> N510
    N444 --> N625
    N446 --> N510
    N446 --> N625
    N447 --> N510
    N447 --> N625
    N448 --> N510
    N448 --> N625
    N449 --> N427
    N449 --> N454
    N449 --> N470
    N449 --> N509
    N449 --> N562
    N449 --> N510
    N449 --> N625
    N449 --> N474
    N449 --> N460
    N449 --> N494
    N450 --> N474
    N450 --> N460
    N450 --> N494
    N450 --> N510
    N450 --> N625
    N453 --> N427
    N453 --> N454
    N453 --> N470
    N453 --> N509
    N453 --> N562
    N454 --> N621
    N454 --> N643
    N454 --> N453
    N455 --> N460
    N455 --> N494
    N455 --> N510
    N455 --> N625
    N457 --> N510
    N457 --> N625
    N458 --> N510
    N458 --> N625
    N459 --> N474
    N459 --> N510
    N459 --> N625
    N460 --> N494
    N460 --> N427
    N460 --> N454
    N460 --> N470
    N460 --> N509
    N460 --> N562
    N460 --> N510
    N460 --> N625
    N460 --> N474
    N461 --> N510
    N461 --> N625
    N462 --> N460
    N462 --> N494
    N462 --> N510
    N462 --> N625
    N462 --> N474
    N462 --> N490
    N463 --> N460
    N463 --> N494
    N463 --> N510
    N463 --> N625
    N464 --> N460
    N464 --> N494
    N464 --> N474
    N464 --> N510
    N464 --> N625
    N465 --> N460
    N465 --> N494
    N465 --> N474
    N465 --> N510
    N465 --> N625
    N466 --> N427
    N466 --> N454
    N466 --> N470
    N466 --> N509
    N466 --> N562
    N466 --> N474
    N466 --> N510
    N466 --> N625
    N466 --> N481
    N466 --> N502
    N467 --> N510
    N467 --> N625
    N467 --> N504
    N467 --> N474
    N468 --> N460
    N468 --> N494
    N468 --> N510
    N468 --> N625
    N469 --> N510
    N469 --> N625
    N470 --> N460
    N470 --> N494
    N470 --> N427
    N470 --> N454
    N470 --> N509
    N470 --> N562
    N470 --> N510
    N470 --> N625
    N470 --> N490
    N470 --> N481
    N470 --> N502
    N471 --> N427
    N471 --> N454
    N471 --> N470
    N471 --> N509
    N471 --> N562
    N471 --> N460
    N471 --> N494
    N471 --> N510
    N471 --> N625
    N472 --> N427
    N472 --> N454
    N472 --> N470
    N472 --> N509
    N472 --> N562
    N472 --> N510
    N472 --> N625
    N475 --> N510
    N475 --> N625
    N475 --> N474
    N476 --> N510
    N476 --> N625
    N476 --> N474
    N477 --> N427
    N477 --> N454
    N477 --> N470
    N477 --> N509
    N477 --> N562
    N477 --> N510
    N477 --> N625
    N477 --> N474
    N478 --> N474
    N478 --> N510
    N478 --> N625
    N479 --> N510
    N479 --> N625
    N480 --> N474
    N480 --> N510
    N480 --> N625
    N481 --> N474
    N481 --> N427
    N481 --> N454
    N481 --> N470
    N481 --> N509
    N481 --> N562
    N481 --> N510
    N481 --> N625
    N481 --> N460
    N481 --> N494
    N482 --> N481
    N482 --> N502
    N482 --> N474
    N482 --> N510
    N482 --> N625
    N483 --> N481
    N483 --> N502
    N483 --> N474
    N483 --> N510
    N483 --> N625
    N484 --> N510
    N484 --> N625
    N486 --> N460
    N486 --> N494
    N486 --> N510
    N486 --> N625
    N486 --> N490
    N486 --> N427
    N486 --> N454
    N486 --> N470
    N486 --> N509
    N486 --> N562
    N487 --> N474
    N487 --> N510
    N487 --> N625
    N488 --> N510
    N488 --> N625
    N489 --> N510
    N489 --> N625
    N490 --> N510
    N490 --> N625
    N491 --> N474
    N491 --> N427
    N491 --> N454
    N491 --> N470
    N491 --> N509
    N491 --> N562
    N491 --> N510
    N491 --> N625
    N492 --> N510
    N492 --> N625
    N493 --> N481
    N493 --> N502
    N493 --> N510
    N493 --> N625
    N494 --> N460
    N494 --> N510
    N494 --> N625
    N495 --> N510
    N495 --> N625
    N496 --> N510
    N496 --> N625
    N497 --> N474
    N497 --> N510
    N497 --> N625
    N498 --> N510
    N498 --> N625
    N499 --> N481
    N499 --> N502
    N499 --> N510
    N499 --> N625
    N500 --> N510
    N500 --> N625
    N501 --> N427
    N501 --> N454
    N501 --> N470
    N501 --> N509
    N501 --> N562
    N501 --> N510
    N501 --> N625
    N502 --> N427
    N502 --> N454
    N502 --> N470
    N502 --> N509
    N502 --> N562
    N502 --> N510
    N502 --> N625
    N502 --> N460
    N502 --> N494
    N503 --> N474
    N503 --> N427
    N503 --> N454
    N503 --> N470
    N503 --> N509
    N503 --> N562
    N503 --> N510
    N503 --> N625
    N504 --> N510
    N504 --> N625
    N504 --> N467
    N504 --> N474
    N505 --> N510
    N505 --> N625
    N506 --> N481
    N506 --> N502
    N506 --> N510
    N506 --> N625
    N507 --> N474
    N507 --> N460
    N507 --> N494
    N507 --> N510
    N507 --> N625
    N508 --> N481
    N508 --> N502
    N508 --> N510
    N508 --> N625
    N509 --> N474
    N509 --> N427
    N509 --> N454
    N509 --> N470
    N509 --> N562
    N509 --> N510
    N509 --> N625
    N510 --> N625
    N510 --> N427
    N510 --> N454
    N510 --> N470
    N510 --> N509
    N510 --> N562
    N511 --> N474
    N511 --> N427
    N511 --> N454
    N511 --> N470
    N511 --> N509
    N511 --> N562
    N511 --> N510
    N511 --> N625
    N512 --> N510
    N512 --> N625
    N512 --> N474
    N514 --> N481
    N514 --> N502
    N514 --> N510
    N514 --> N625
    N516 --> N474
    N516 --> N510
    N516 --> N625
    N517 --> N510
    N517 --> N625
    N517 --> N474
    N518 --> N510
    N518 --> N625
    N519 --> N460
    N519 --> N494
    N519 --> N474
    N519 --> N510
    N519 --> N625
    N520 --> N427
    N520 --> N454
    N520 --> N470
    N520 --> N509
    N520 --> N562
    N520 --> N460
    N520 --> N494
    N520 --> N510
    N520 --> N625
    N521 --> N510
    N521 --> N625
    N522 --> N510
    N522 --> N625
    N523 --> N510
    N523 --> N625
    N524 --> N460
    N524 --> N494
    N524 --> N474
    N524 --> N510
    N524 --> N625
    N524 --> N490
    N525 --> N460
    N525 --> N494
    N525 --> N510
    N525 --> N625
    N526 --> N460
    N526 --> N494
    N526 --> N510
    N526 --> N625
    N526 --> N474
    N526 --> N427
    N526 --> N454
    N526 --> N470
    N526 --> N509
    N526 --> N562
    N527 --> N427
    N527 --> N454
    N527 --> N470
    N527 --> N509
    N527 --> N562
    N527 --> N510
    N527 --> N625
    N529 --> N510
    N529 --> N625
    N531 --> N510
    N531 --> N625
    N531 --> N490
    N532 --> N510
    N532 --> N625
    N533 --> N510
    N533 --> N625
    N533 --> N474
    N533 --> N427
    N533 --> N454
    N533 --> N470
    N533 --> N509
    N533 --> N562
    N534 --> N510
    N534 --> N625
    N535 --> N427
    N535 --> N454
    N535 --> N470
    N535 --> N509
    N535 --> N562
    N535 --> N510
    N535 --> N625
    N536 --> N460
    N536 --> N494
    N536 --> N510
    N536 --> N625
    N537 --> N510
    N537 --> N625
    N538 --> N510
    N538 --> N625
    N539 --> N460
    N539 --> N494
    N539 --> N510
    N539 --> N625
    N540 --> N427
    N540 --> N454
    N540 --> N470
    N540 --> N509
    N540 --> N562
    N540 --> N510
    N540 --> N625
    N541 --> N460
    N541 --> N494
    N541 --> N474
    N541 --> N427
    N541 --> N454
    N541 --> N470
    N541 --> N509
    N541 --> N562
    N541 --> N510
    N541 --> N625
    N542 --> N510
    N542 --> N625
    N543 --> N510
    N543 --> N625
    N544 --> N510
    N544 --> N625
    N545 --> N510
    N545 --> N625
    N546 --> N510
    N546 --> N625
    N547 --> N474
    N547 --> N510
    N547 --> N625
    N548 --> N474
    N548 --> N510
    N548 --> N625
    N549 --> N510
    N549 --> N625
    N550 --> N510
    N550 --> N625
    N551 --> N481
    N551 --> N502
    N551 --> N510
    N551 --> N625
    N552 --> N446
    N552 --> N642
    N553 --> N460
    N553 --> N494
    N553 --> N510
    N553 --> N625
    N554 --> N481
    N554 --> N502
    N554 --> N446
    N554 --> N642
    N554 --> N510
    N554 --> N625
    N555 --> N446
    N555 --> N642
    N555 --> N481
    N555 --> N502
    N555 --> N510
    N555 --> N625
    N556 --> N427
    N556 --> N454
    N556 --> N470
    N556 --> N509
    N556 --> N562
    N556 --> N474
    N556 --> N510
    N556 --> N625
    N557 --> N510
    N557 --> N625
    N558 --> N510
    N558 --> N625
    N559 --> N474
    N560 --> N510
    N560 --> N625
    N561 --> N481
    N561 --> N502
    N561 --> N474
    N561 --> N427
    N561 --> N454
    N561 --> N470
    N561 --> N509
    N561 --> N562
    N561 --> N510
    N561 --> N625
    N562 --> N510
    N562 --> N625
    N563 --> N481
    N563 --> N502
    N563 --> N510
    N563 --> N625
    N564 --> N510
    N564 --> N625
    N565 --> N510
    N565 --> N625
    N565 --> N590
    N567 --> N510
    N567 --> N625
    N570 --> N510
    N570 --> N625
    N571 --> N436
    N571 --> N510
    N571 --> N625
    N573 --> N481
    N573 --> N502
    N573 --> N510
    N573 --> N625
    N575 --> N474
    N575 --> N510
    N575 --> N625
    N576 --> N510
    N576 --> N625
    N577 --> N590
    N577 --> N481
    N577 --> N502
    N577 --> N579
    N577 --> N510
    N577 --> N625
    N578 --> N510
    N578 --> N625
    N579 --> N446
    N579 --> N642
    N579 --> N510
    N579 --> N625
    N580 --> N590
    N580 --> N579
    N580 --> N474
    N580 --> N510
    N580 --> N625
    N581 --> N590
    N581 --> N579
    N581 --> N427
    N581 --> N454
    N581 --> N470
    N581 --> N509
    N581 --> N562
    N581 --> N510
    N581 --> N625
    N582 --> N590
    N582 --> N579
    N582 --> N474
    N582 --> N510
    N582 --> N625
    N583 --> N590
    N583 --> N510
    N583 --> N625
    N585 --> N427
    N585 --> N454
    N585 --> N470
    N585 --> N509
    N585 --> N562
    N585 --> N510
    N585 --> N625
    N588 --> N510
    N588 --> N625
    N589 --> N590
    N589 --> N579
    N589 --> N510
    N589 --> N625
    N591 --> N590
    N591 --> N592
    N592 --> N590
    N594 --> N579
    N594 --> N510
    N594 --> N625
    N596 --> N590
    N596 --> N474
    N597 --> N590
    N598 --> N590
    N599 --> N590
    N600 --> N590
    N600 --> N446
    N600 --> N642
    N600 --> N579
    N600 --> N510
    N600 --> N625
    N601 --> N590
    N601 --> N446
    N601 --> N642
    N601 --> N579
    N601 --> N510
    N601 --> N625
    N602 --> N590
    N602 --> N34
    N602 --> N429
    N602 --> N563
    N603 --> N590
    N603 --> N446
    N603 --> N642
    N603 --> N579
    N603 --> N510
    N603 --> N625
    N603 --> N34
    N603 --> N429
    N603 --> N563
    N604 --> N590
    N604 --> N579
    N604 --> N446
    N604 --> N642
    N604 --> N510
    N604 --> N625
    N604 --> N34
    N604 --> N429
    N604 --> N563
    N605 --> N590
    N605 --> N579
    N605 --> N510
    N605 --> N625
    N606 --> N579
    N606 --> N427
    N606 --> N454
    N606 --> N470
    N606 --> N509
    N606 --> N562
    N607 --> N579
    N607 --> N510
    N607 --> N625
    N608 --> N579
    N610 --> N510
    N610 --> N625
    N611 --> N474
    N612 --> N590
    N612 --> N510
    N612 --> N625
    N613 --> N474
    N613 --> N510
    N613 --> N625
    N614 --> N474
    N615 --> N510
    N615 --> N625
    N616 --> N474
    N617 --> N460
    N617 --> N494
    N617 --> N510
    N617 --> N625
    N618 --> N510
    N618 --> N625
    N619 --> N460
    N619 --> N494
    N619 --> N474
    N619 --> N510
    N619 --> N625
    N620 --> N474
    N620 --> N510
    N620 --> N625
    N621 --> N579
    N622 --> N460
    N622 --> N494
    N623 --> N446
    N623 --> N642
    N623 --> N474
    N623 --> N510
    N623 --> N625
    N625 --> N446
    N625 --> N642
    N625 --> N579
    N625 --> N510
    N626 --> N460
    N626 --> N494
    N629 --> N510
    N629 --> N625
    N630 --> N590
    N630 --> N579
    N630 --> N427
    N630 --> N454
    N630 --> N470
    N630 --> N509
    N630 --> N562
    N630 --> N510
    N630 --> N625
    N630 --> N34
    N630 --> N429
    N630 --> N563
    N631 --> N590
    N631 --> N579
    N631 --> N427
    N631 --> N454
    N631 --> N470
    N631 --> N509
    N631 --> N562
    N631 --> N510
    N631 --> N625
    N632 --> N590
    N632 --> N510
    N632 --> N625
    N633 --> N446
    N633 --> N642
    N633 --> N510
    N633 --> N625
    N633 --> N34
    N633 --> N429
    N633 --> N563
    N634 --> N590
    N634 --> N446
    N634 --> N642
    N634 --> N579
    N634 --> N427
    N634 --> N454
    N634 --> N470
    N634 --> N509
    N634 --> N562
    N634 --> N510
    N634 --> N625
    N634 --> N34
    N634 --> N429
    N634 --> N563
    N636 --> N510
    N636 --> N625
    N637 --> N446
    N637 --> N642
    N637 --> N510
    N637 --> N625
    N638 --> N590
    N638 --> N579
    N638 --> N474
    N638 --> N427
    N638 --> N454
    N638 --> N470
    N638 --> N509
    N638 --> N562
    N638 --> N510
    N638 --> N625
    N639 --> N446
    N639 --> N642
    N640 --> N510
    N640 --> N625
    N642 --> N590
    N643 --> N590
    N643 --> N579
    N643 --> N474
    N643 --> N510
    N643 --> N625
    N644 --> N590
    N644 --> N446
    N644 --> N642
    N644 --> N579
    N644 --> N474
    N644 --> N427
    N644 --> N454
    N644 --> N470
    N644 --> N509
    N644 --> N562
    N644 --> N510
    N644 --> N625
    N645 --> N474
    N646 --> N579
    N646 --> N474
    N646 --> N427
    N646 --> N454
    N646 --> N470
    N646 --> N509
    N646 --> N562
    N646 --> N510
    N646 --> N625
    N646 --> N34
    N646 --> N429
    N646 --> N563
    N647 --> N579
    N647 --> N427
    N647 --> N454
    N647 --> N470
    N647 --> N509
    N647 --> N562
    N647 --> N510
    N647 --> N625
    N648 --> N510
    N648 --> N625
    N649 --> N446
    N649 --> N642
    N649 --> N510
    N649 --> N625
    N649 --> N34
    N649 --> N429
    N649 --> N563
    N650 --> N446
    N650 --> N642
    N650 --> N579
    N650 --> N474
    N650 --> N427
    N650 --> N454
    N650 --> N470
    N650 --> N509
    N650 --> N562
    N650 --> N510
    N650 --> N625
    N650 --> N34
    N650 --> N429
    N650 --> N563
    N652 --> N579
    N652 --> N427
    N652 --> N454
    N652 --> N470
    N652 --> N509
    N652 --> N562
    N652 --> N510
    N652 --> N625
    N652 --> N34
    N652 --> N429
    N652 --> N563
    N653 --> N579
    N653 --> N427
    N653 --> N454
    N653 --> N470
    N653 --> N509
    N653 --> N562
    N653 --> N510
    N653 --> N625
    N654 --> N510
    N654 --> N625
    N655 --> N446
    N655 --> N642
    N655 --> N510
    N655 --> N625
    N655 --> N34
    N655 --> N429
    N655 --> N563
    N656 --> N446
    N656 --> N642
    N656 --> N579
    N656 --> N427
    N656 --> N454
    N656 --> N470
    N656 --> N509
    N656 --> N562
    N656 --> N510
    N656 --> N625
    N656 --> N34
    N656 --> N429
    N656 --> N563
```

## Detailed File Index
- **.agents/skills/brag/scripts/analyze_music_cues.py**
  - Imports: `__future__`
  - Imports: `argparse`
  - Imports: `json`
  - Imports: `librosa`
  - Imports: `math`
  - Imports: `numpy`
  - Imports: `pathlib`
  - Imports: `typing`
- **build_mobile.py**
  - Imports: `argparse`
  - Imports: `glob`
  - Imports: `hashlib`
  - Imports: `json`
  - Imports: `os`
  - Imports: `shutil`
  - Imports: `subprocess`
  - Imports: `sys`
  - Imports: `typing`
- **build_standalone.py**
  - Imports: `glob`
  - Imports: `json`
  - Imports: `os`
  - Imports: `platform`
  - Imports: `re`
  - Imports: `shutil`
  - Imports: `subprocess`
  - Imports: `sys`
  - Imports: `typing`
- **bump_version.py**
  - Imports: `json`
  - Imports: `os`
  - Imports: `re`
  - Imports: `sys`
- **doctor.py**
  - Imports: `argparse`
  - Imports: `json`
  - Imports: `os`
  - Imports: `platform`
  - Imports: `psutil`
  - Imports: `socket`
  - Imports: `sqlite3`
  - Imports: `subprocess`
  - Imports: `sys`
  - Imports: `typing`
  - Imports: `urllib`
- **generated_repos/attention_is_all_you_need__transformer_/config.py**
  - Imports: `dataclasses`
- **generated_repos/attention_is_all_you_need__transformer_/dataset.py**
  - Imports: `random`
- **generated_repos/attention_is_all_you_need__transformer_/model.py**
  - Imports: `math`
- **generated_repos/attention_is_all_you_need__transformer_/trainer.py**
  - Imports: `config`
  - Imports: `dataset`
  - Imports: `model`
- **main.py**
  - Imports: `api`
  - Imports: `argparse`
  - Imports: `asyncio`
  - Imports: `database`
  - Imports: `httpx`
  - Imports: `json`
  - Imports: `os`
  - Imports: `src`
  - Imports: `subprocess`
  - Imports: `sys`
  - Imports: `time`
  - Imports: `uvicorn`
- **meridian_backend/api.py**
  - Imports: `asyncio`
  - Imports: `contextlib`
  - Imports: `contextvars`
  - Imports: `database`
  - Imports: `dotenv`
  - Imports: `fastapi`
  - Imports: `json`
  - Imports: `logging`
  - Imports: `os`
  - Imports: `platform`
  - Imports: `prometheus_client`
  - Imports: `psutil`
  - Imports: `random`
  - Imports: `slowapi`
  - Imports: `src`
  - Imports: `time`
  - Imports: `typing`
  - Imports: `uuid`
  - Imports: `uvicorn`
- **meridian_backend/database.py**
  - Imports: `src`
- **meridian_backend/meridian_frontend/src/components/ProfileHeader.tsx**
  - Imports: `react`
- **meridian_backend/mobile_bridge_service.py**
  - Imports: `asyncio`
  - Imports: `contextlib`
  - Imports: `fastapi`
  - Imports: `httpx`
  - Imports: `json`
  - Imports: `logging`
  - Imports: `os`
  - Imports: `src`
  - Imports: `sys`
  - Imports: `time`
  - Imports: `typing`
  - Imports: `uvicorn`
- **meridian_backend/src/__init__.py**
  - Imports: `os`
  - Imports: `sys`
- **meridian_backend/src/api/__init__.py**
  - Imports: `src`
- **meridian_backend/src/api/automation.py**
  - Imports: `ast`
  - Imports: `database`
  - Imports: `fastapi`
  - Imports: `json`
  - Imports: `ollama`
  - Imports: `os`
  - Imports: `pydantic`
  - Imports: `src`
  - Imports: `subprocess`
  - Imports: `typing`
- **meridian_backend/src/api/browser_extension.py**
  - Imports: `fastapi`
  - Imports: `json`
  - Imports: `logging`
  - Imports: `src`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/api/chat.py**
  - Imports: `asyncio`
  - Imports: `database`
  - Imports: `fastapi`
  - Imports: `json`
  - Imports: `os`
  - Imports: `pydantic`
  - Imports: `src`
  - Imports: `typing`
- **meridian_backend/src/api/deps.py**
  - Imports: `database`
  - Imports: `hashlib`
  - Imports: `hmac`
  - Imports: `json`
  - Imports: `logging`
  - Imports: `os`
  - Imports: `platform`
  - Imports: `pydantic`
  - Imports: `slowapi`
  - Imports: `socket`
  - Imports: `src`
  - Imports: `subprocess`
  - Imports: `time`
  - Imports: `trustme`
  - Imports: `typing`
- **meridian_backend/src/api/mcp.py**
  - Imports: `fastapi`
  - Imports: `json`
  - Imports: `os`
  - Imports: `pydantic`
  - Imports: `shutil`
  - Imports: `src`
  - Imports: `subprocess`
  - Imports: `tempfile`
  - Imports: `typing`
- **meridian_backend/src/api/models_mgmt.py**
  - Imports: `database`
  - Imports: `fastapi`
  - Imports: `httpx`
  - Imports: `json`
  - Imports: `ollama`
  - Imports: `os`
  - Imports: `pydantic`
  - Imports: `src`
  - Imports: `typing`
  - Imports: `urllib`
- **meridian_backend/src/api/perception.py**
  - Imports: `base64`
  - Imports: `fastapi`
  - Imports: `os`
  - Imports: `pydantic`
  - Imports: `src`
  - Imports: `subprocess`
  - Imports: `tempfile`
  - Imports: `typing`
  - Imports: `webbrowser`
- **meridian_backend/src/api/profile.py**
  - Imports: `database`
  - Imports: `fastapi`
  - Imports: `os`
  - Imports: `pydantic`
  - Imports: `src`
  - Imports: `typing`
- **meridian_backend/src/api/rag.py**
  - Imports: `database`
  - Imports: `fastapi`
  - Imports: `os`
  - Imports: `pydantic`
  - Imports: `shutil`
  - Imports: `src`
  - Imports: `tempfile`
  - Imports: `typing`
- **meridian_backend/src/api/scheduler.py**
  - Imports: `database`
  - Imports: `fastapi`
  - Imports: `hashlib`
  - Imports: `hmac`
  - Imports: `json`
  - Imports: `ollama`
  - Imports: `os`
  - Imports: `pydantic`
  - Imports: `src`
  - Imports: `typing`
  - Imports: `uuid`
- **meridian_backend/src/api/swarm.py**
  - Imports: `asyncio`
  - Imports: `database`
  - Imports: `fastapi`
  - Imports: `json`
  - Imports: `logging`
  - Imports: `os`
  - Imports: `pydantic`
  - Imports: `re`
  - Imports: `socket`
  - Imports: `src`
  - Imports: `typing`
- **meridian_backend/src/api/system.py**
  - Imports: `asyncio`
  - Imports: `database`
  - Imports: `fastapi`
  - Imports: `httpx`
  - Imports: `io`
  - Imports: `json`
  - Imports: `os`
  - Imports: `platform`
  - Imports: `psutil`
  - Imports: `pydantic`
  - Imports: `qrcode`
  - Imports: `random`
  - Imports: `shutil`
  - Imports: `signal`
  - Imports: `socket`
  - Imports: `src`
  - Imports: `subprocess`
  - Imports: `sys`
  - Imports: `typing`
- **meridian_backend/src/api/vault.py**
  - Imports: `fastapi`
  - Imports: `os`
  - Imports: `pydantic`
  - Imports: `secrets`
  - Imports: `src`
  - Imports: `typing`
- **meridian_backend/src/api/voice.py**
  - Imports: `base64`
  - Imports: `fastapi`
  - Imports: `io`
  - Imports: `logging`
  - Imports: `numpy`
  - Imports: `os`
  - Imports: `pydantic`
  - Imports: `random`
  - Imports: `soundfile`
  - Imports: `src`
  - Imports: `sys`
  - Imports: `tempfile`
  - Imports: `typing`
- **meridian_backend/src/api/websockets.py**
  - Imports: `asyncio`
  - Imports: `fastapi`
  - Imports: `json`
  - Imports: `os`
  - Imports: `src`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/api/workspace.py**
  - Imports: `database`
  - Imports: `fastapi`
  - Imports: `json`
  - Imports: `os`
  - Imports: `pydantic`
  - Imports: `src`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/core/action_journal.py**
  - Imports: `database`
  - Imports: `json`
  - Imports: `logging`
  - Imports: `src`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/core/agent_status_stream.py**
  - Imports: `asyncio`
  - Imports: `fastapi`
  - Imports: `logging`
  - Imports: `pydantic`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/core/android_automation.py**
  - Imports: `logging`
  - Imports: `shutil`
  - Imports: `subprocess`
  - Imports: `typing`
- **meridian_backend/src/core/ar_bridge.py**
  - Imports: `logging`
  - Imports: `src`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/core/atomic_storage.py**
  - Imports: `json`
  - Imports: `logging`
  - Imports: `os`
  - Imports: `tempfile`
  - Imports: `typing`
- **meridian_backend/src/core/audit_logger.py**
  - Imports: `getpass`
  - Imports: `hashlib`
  - Imports: `hmac`
  - Imports: `json`
  - Imports: `logging`
  - Imports: `os`
  - Imports: `platform`
  - Imports: `psutil`
  - Imports: `src`
  - Imports: `threading`
  - Imports: `time`
- **meridian_backend/src/core/auth.py**
  - Imports: `fastapi`
  - Imports: `hashlib`
  - Imports: `hmac`
  - Imports: `json`
  - Imports: `os`
  - Imports: `secrets`
  - Imports: `src`
  - Imports: `starlette`
  - Imports: `typing`
- **meridian_backend/src/core/behavior_monitor.py**
  - Imports: `logging`
  - Imports: `os`
  - Imports: `psutil`
  - Imports: `typing`
- **meridian_backend/src/core/boilerplate_genie.py**
  - Imports: `logging`
  - Imports: `os`
  - Imports: `typing`
  - Imports: `{component_name}`
- **meridian_backend/src/core/breach_sentinel.py**
  - Imports: `hashlib`
  - Imports: `json`
  - Imports: `logging`
  - Imports: `os`
  - Imports: `typing`
  - Imports: `urllib`
- **meridian_backend/src/core/browser_extension_hub.py**
  - Imports: `asyncio`
  - Imports: `json`
  - Imports: `logging`
  - Imports: `time`
  - Imports: `typing`
  - Imports: `uuid`
- **meridian_backend/src/core/bus.py**
  - Imports: `asyncio`
  - Imports: `typing`
- **meridian_backend/src/core/butler_etiquette.py**
  - Imports: `logging`
  - Imports: `typing`
- **meridian_backend/src/core/butler_ritual.py**
  - Imports: `dataclasses`
  - Imports: `logging`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/core/camera_sentinel.py**
  - Imports: `cv2`
  - Imports: `logging`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/core/checkpoints.py**
  - Imports: `asyncio`
  - Imports: `src`
  - Imports: `typing`
- **meridian_backend/src/core/clipboard.py**
  - Imports: `database`
  - Imports: `pyperclip`
  - Imports: `src`
  - Imports: `threading`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/core/code_graph.py**
  - Imports: `ast`
  - Imports: `os`
  - Imports: `re`
  - Imports: `src`
  - Imports: `typing`
- **meridian_backend/src/core/cognitive_graph.py**
  - Imports: `json`
  - Imports: `logging`
  - Imports: `math`
  - Imports: `os`
  - Imports: `sqlite3`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/core/commit_whisperer.py**
  - Imports: `logging`
  - Imports: `os`
  - Imports: `subprocess`
  - Imports: `typing`
- **meridian_backend/src/core/concierge_agent.py**
  - Imports: `dataclasses`
  - Imports: `logging`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/core/config.py**
  - Imports: `os`
- **meridian_backend/src/core/confirmations.py**
  - Imports: `asyncio`
  - Imports: `database`
  - Imports: `os`
  - Imports: `typing`
- **meridian_backend/src/core/consensus_engine.py**
  - Imports: `asyncio`
  - Imports: `database`
  - Imports: `datetime`
  - Imports: `json`
  - Imports: `logging`
  - Imports: `re`
  - Imports: `src`
  - Imports: `time`
  - Imports: `typing`
  - Imports: `uuid`
- **meridian_backend/src/core/deep_project_context.py**
  - Imports: `ast`
  - Imports: `logging`
  - Imports: `os`
  - Imports: `typing`
- **meridian_backend/src/core/dev_automation.py**
  - Imports: `asyncio`
  - Imports: `logging`
  - Imports: `os`
  - Imports: `pydantic`
  - Imports: `shutil`
  - Imports: `subprocess`
  - Imports: `sys`
  - Imports: `typing`
- **meridian_backend/src/core/device_handoff.py**
  - Imports: `dataclasses`
  - Imports: `logging`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/core/device_sentinel.py**
  - Imports: `dataclasses`
  - Imports: `logging`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/core/discord_bridge.py**
  - Imports: `asyncio`
  - Imports: `database`
  - Imports: `discord`
  - Imports: `httpx`
  - Imports: `os`
  - Imports: `src`
  - Imports: `tempfile`
  - Imports: `threading`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/core/discord_utils.py**
  - Imports: `httpx`
  - Imports: `os`
  - Imports: `src`
  - Imports: `threading`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/core/doc_generator.py**
  - Imports: `os`
  - Imports: `re`
  - Imports: `src`
- **meridian_backend/src/core/doc_indexer.py**
  - Imports: `ast`
  - Imports: `database`
  - Imports: `hashlib`
  - Imports: `json`
  - Imports: `logging`
  - Imports: `math`
  - Imports: `numpy`
  - Imports: `os`
  - Imports: `re`
  - Imports: `sqlite3`
  - Imports: `time`
  - Imports: `turbovec`
  - Imports: `typing`
- **meridian_backend/src/core/elevated_runner.py**
  - Imports: `ctypes`
  - Imports: `logging`
  - Imports: `os`
  - Imports: `subprocess`
  - Imports: `sys`
  - Imports: `typing`
- **meridian_backend/src/core/emergency_lockdown.py**
  - Imports: `ctypes`
  - Imports: `hashlib`
  - Imports: `logging`
  - Imports: `os`
  - Imports: `src`
  - Imports: `sys`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/core/error_diagnostics.py**
  - Imports: `re`
  - Imports: `typing`
- **meridian_backend/src/core/experiment_runner.py**
  - Imports: `httpx`
  - Imports: `logging`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/core/explain_code_engine.py**
  - Imports: `logging`
  - Imports: `os`
  - Imports: `subprocess`
  - Imports: `typing`
- **meridian_backend/src/core/exporter.py**
  - Imports: `database`
  - Imports: `os`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/core/fim_sentinel.py**
  - Imports: `hashlib`
  - Imports: `logging`
  - Imports: `os`
  - Imports: `src`
  - Imports: `typing`
- **meridian_backend/src/core/gaze_tracker.py**
  - Imports: `logging`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/core/governor.py**
  - Imports: `ollama`
  - Imports: `os`
  - Imports: `psutil`
  - Imports: `src`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/core/graph_rag.py**
  - Imports: `ast`
  - Imports: `json`
  - Imports: `os`
  - Imports: `src`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/core/graph_sync.py**
  - Imports: `json`
  - Imports: `os`
  - Imports: `src`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/core/hardware_detector.py**
  - Imports: `json`
  - Imports: `logging`
  - Imports: `nvidia_ml_py`
  - Imports: `os`
  - Imports: `platform`
  - Imports: `psutil`
  - Imports: `pynvml`
  - Imports: `subprocess`
  - Imports: `sys`
  - Imports: `typing`
  - Imports: `warnings`
- **meridian_backend/src/core/history_manager.py**
  - Imports: `os`
  - Imports: `subprocess`
- **meridian_backend/src/core/lifespan.py**
  - Imports: `asyncio`
  - Imports: `contextlib`
  - Imports: `database`
  - Imports: `fastapi`
  - Imports: `logging`
  - Imports: `os`
  - Imports: `platform`
  - Imports: `src`
  - Imports: `threading`
- **meridian_backend/src/core/llm_auth.py**
  - Imports: `database`
  - Imports: `logging`
  - Imports: `os`
  - Imports: `re`
  - Imports: `src`
  - Imports: `typing`
- **meridian_backend/src/core/llm_client.py**
  - Imports: `asyncio`
  - Imports: `concurrent`
  - Imports: `database`
  - Imports: `logging`
  - Imports: `os`
  - Imports: `src`
  - Imports: `typing`
- **meridian_backend/src/core/llm_clients.py**
  - Imports: `anthropic`
  - Imports: `database`
  - Imports: `ollama`
  - Imports: `openai`
  - Imports: `os`
  - Imports: `psutil`
  - Imports: `subprocess`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/core/llm_provider.py**
  - Imports: `asyncio`
  - Imports: `database`
  - Imports: `httpx`
  - Imports: `json`
  - Imports: `logging`
  - Imports: `math`
  - Imports: `os`
  - Imports: `re`
  - Imports: `src`
  - Imports: `typing`
- **meridian_backend/src/core/local_model_manager.py**
  - Imports: `asyncio`
  - Imports: `database`
  - Imports: `httpx`
  - Imports: `json`
  - Imports: `logging`
  - Imports: `os`
  - Imports: `pydantic`
  - Imports: `sys`
  - Imports: `typing`
- **meridian_backend/src/core/logger.py**
  - Imports: `json`
  - Imports: `logging`
  - Imports: `os`
  - Imports: `sys`
  - Imports: `typing`
- **meridian_backend/src/core/logging_config.py**
  - Imports: `contextvars`
  - Imports: `json`
  - Imports: `logging`
  - Imports: `os`
  - Imports: `src`
  - Imports: `sys`
  - Imports: `uuid`
- **meridian_backend/src/core/loop.py**
  - Imports: `asyncio`
  - Imports: `database`
  - Imports: `json`
  - Imports: `os`
  - Imports: `psutil`
  - Imports: `src`
  - Imports: `threading`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/core/loop_dispatcher.py**
  - Imports: `asyncio`
  - Imports: `database`
  - Imports: `json`
  - Imports: `os`
  - Imports: `random`
  - Imports: `re`
  - Imports: `src`
  - Imports: `threading`
  - Imports: `time`
  - Imports: `typing`
  - Imports: `uuid`
- **meridian_backend/src/core/loop_executor.py**
  - Imports: `ast`
  - Imports: `database`
  - Imports: `inspect`
  - Imports: `json`
  - Imports: `ollama`
  - Imports: `re`
  - Imports: `src`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/core/loop_parser.py**
  - Imports: `asyncio`
  - Imports: `database`
  - Imports: `json`
  - Imports: `ollama`
  - Imports: `re`
  - Imports: `src`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/core/loop_planning.py**
  - Imports: `asyncio`
  - Imports: `database`
  - Imports: `json`
  - Imports: `os`
  - Imports: `re`
  - Imports: `src`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/core/loop_stream.py**
  - Imports: `asyncio`
  - Imports: `database`
  - Imports: `inspect`
  - Imports: `json`
  - Imports: `re`
  - Imports: `src`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/core/lsp_client.py**
  - Imports: `asyncio`
  - Imports: `json`
  - Imports: `os`
  - Imports: `sys`
  - Imports: `typing`
- **meridian_backend/src/core/malware_scanner.py**
  - Imports: `base64`
  - Imports: `logging`
  - Imports: `math`
  - Imports: `os`
  - Imports: `typing`
- **meridian_backend/src/core/mcp_client.py**
  - Imports: `asyncio`
  - Imports: `json`
  - Imports: `logging`
  - Imports: `os`
  - Imports: `shutil`
  - Imports: `typing`
- **meridian_backend/src/core/mcp_executor.py**
  - Imports: `asyncio`
  - Imports: `core`
  - Imports: `json`
  - Imports: `logging`
  - Imports: `meridian_backend`
  - Imports: `src`
  - Imports: `typing`
- **meridian_backend/src/core/memory_backup.py**
  - Imports: `base64`
  - Imports: `cryptography`
  - Imports: `hashlib`
  - Imports: `json`
  - Imports: `os`
  - Imports: `shutil`
  - Imports: `src`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/core/memory_consolidation.py**
  - Imports: `asyncio`
  - Imports: `database`
  - Imports: `json`
  - Imports: `logging`
  - Imports: `os`
  - Imports: `pydantic`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/core/memory_editor.py**
  - Imports: `database`
  - Imports: `json`
  - Imports: `src`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/core/mobile_bridge.py**
  - Imports: `asyncio`
  - Imports: `database`
  - Imports: `datetime`
  - Imports: `fastapi`
  - Imports: `inspect`
  - Imports: `json`
  - Imports: `logging`
  - Imports: `os`
  - Imports: `psutil`
  - Imports: `socket`
  - Imports: `src`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/core/mode.py**
  - Imports: `database`
  - Imports: `datetime`
  - Imports: `hashlib`
  - Imports: `hmac`
  - Imports: `json`
  - Imports: `ollama`
  - Imports: `os`
  - Imports: `platform`
  - Imports: `re`
  - Imports: `src`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/core/neural_rag.py**
  - Imports: `math`
  - Imports: `os`
  - Imports: `src`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/core/oauth_manager.py**
  - Imports: `base64`
  - Imports: `datetime`
  - Imports: `hashlib`
  - Imports: `hmac`
  - Imports: `json`
  - Imports: `jwt`
  - Imports: `os`
  - Imports: `secrets`
  - Imports: `src`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/core/ollama_manager.py**
  - Imports: `asyncio`
  - Imports: `httpx`
  - Imports: `json`
  - Imports: `logging`
  - Imports: `os`
  - Imports: `sys`
  - Imports: `typing`
- **meridian_backend/src/core/p2p.py**
  - Imports: `database`
  - Imports: `hashlib`
  - Imports: `json`
  - Imports: `os`
  - Imports: `socket`
  - Imports: `src`
  - Imports: `threading`
  - Imports: `time`
  - Imports: `typing`
  - Imports: `zeroconf`
- **meridian_backend/src/core/p2p_crypto.py**
  - Imports: `base64`
  - Imports: `cryptography`
  - Imports: `hashlib`
  - Imports: `hmac`
  - Imports: `os`
  - Imports: `secrets`
  - Imports: `socket`
  - Imports: `src`
- **meridian_backend/src/core/p2p_discovery.py**
  - Imports: `socket`
  - Imports: `src`
  - Imports: `typing`
- **meridian_backend/src/core/p2p_pairing.py**
  - Imports: `hmac`
  - Imports: `os`
  - Imports: `socket`
  - Imports: `src`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/core/perception.py**
  - Imports: `cv2`
  - Imports: `datetime`
  - Imports: `logging`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/core/persistence_sentinel.py**
  - Imports: `logging`
  - Imports: `os`
  - Imports: `sys`
  - Imports: `typing`
  - Imports: `winreg`
- **meridian_backend/src/core/personal_crm.py**
  - Imports: `database`
  - Imports: `logging`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/core/plugins.py**
  - Imports: `importlib`
  - Imports: `inspect`
  - Imports: `os`
  - Imports: `src`
  - Imports: `sys`
  - Imports: `threading`
  - Imports: `time`
  - Imports: `typing`
  - Imports: `watchdog`
- **meridian_backend/src/core/polyglot.py**
  - Imports: `logging`
  - Imports: `typing`
- **meridian_backend/src/core/predictive_engine.py**
  - Imports: `logging`
  - Imports: `src`
  - Imports: `subprocess`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/core/presence_briefing.py**
  - Imports: `logging`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/core/proactive/__init__.py**
  - Imports: `sys`
- **meridian_backend/src/core/proactive/commits.py**
  - Imports: `api`
  - Imports: `database`
  - Imports: `datetime`
  - Imports: `ollama`
  - Imports: `os`
  - Imports: `random`
  - Imports: `re`
  - Imports: `src`
  - Imports: `subprocess`
  - Imports: `threading`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/core/proactive/dispatcher.py**
  - Imports: `asyncio`
  - Imports: `datetime`
  - Imports: `os`
  - Imports: `src`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/core/proactive/ergonomics.py**
  - Imports: `datetime`
  - Imports: `psutil`
  - Imports: `src`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/core/proactive/guard.py**
  - Imports: `ctypes`
  - Imports: `database`
  - Imports: `logging`
  - Imports: `os`
  - Imports: `platform`
  - Imports: `psutil`
  - Imports: `socket`
  - Imports: `src`
  - Imports: `subprocess`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/core/proactive_system_guard.py**
  - Imports: `logging`
  - Imports: `os`
  - Imports: `psutil`
  - Imports: `threading`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/core/prompt_injection.py**
  - Imports: `logging`
  - Imports: `re`
  - Imports: `src`
  - Imports: `typing`
- **meridian_backend/src/core/prompt_templates.py**
  - Imports: `json`
  - Imports: `typing`
- **meridian_backend/src/core/rag_optimizer.py**
  - Imports: `math`
  - Imports: `re`
  - Imports: `typing`
- **meridian_backend/src/core/reflection_engine.py**
  - Imports: `json`
  - Imports: `logging`
  - Imports: `re`
  - Imports: `src`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/core/response_models.py**
  - Imports: `pydantic`
  - Imports: `typing`
- **meridian_backend/src/core/routine_executor.py**
  - Imports: `logging`
  - Imports: `os`
  - Imports: `shutil`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/core/sandbox_runner.py**
  - Imports: `logging`
  - Imports: `os`
  - Imports: `subprocess`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/core/scheduler.py**
  - Imports: `apscheduler`
  - Imports: `asyncio`
  - Imports: `database`
  - Imports: `datetime`
  - Imports: `json`
  - Imports: `nvidia_ml_py`
  - Imports: `os`
  - Imports: `psutil`
  - Imports: `pynvml`
  - Imports: `src`
  - Imports: `time`
  - Imports: `warnings`
- **meridian_backend/src/core/screen_sense.py**
  - Imports: `asyncio`
  - Imports: `ctypes`
  - Imports: `logging`
  - Imports: `os`
  - Imports: `psutil`
  - Imports: `src`
  - Imports: `subprocess`
  - Imports: `sys`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/core/security_middleware.py**
  - Imports: `fastapi`
  - Imports: `logging`
  - Imports: `src`
  - Imports: `starlette`
  - Imports: `typing`
- **meridian_backend/src/core/self_evolving_tooling.py**
  - Imports: `ast`
  - Imports: `collections`
  - Imports: `logging`
  - Imports: `os`
  - Imports: `subprocess`
  - Imports: `sys`
  - Imports: `tempfile`
  - Imports: `typing`
- **meridian_backend/src/core/silent_workflow_guardian.py**
  - Imports: `logging`
  - Imports: `os`
  - Imports: `re`
  - Imports: `typing`
- **meridian_backend/src/core/skills_loader.py**
  - Imports: `logging`
  - Imports: `os`
  - Imports: `re`
  - Imports: `src`
  - Imports: `typing`
  - Imports: `yaml`
- **meridian_backend/src/core/sos_protocol.py**
  - Imports: `database`
  - Imports: `logging`
  - Imports: `src`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/core/speculative.py**
  - Imports: `asyncio`
  - Imports: `database`
  - Imports: `importlib`
  - Imports: `json`
  - Imports: `os`
  - Imports: `re`
  - Imports: `socket`
  - Imports: `typing`
  - Imports: `urllib`
- **meridian_backend/src/core/swarm.py**
  - Imports: `asyncio`
  - Imports: `database`
  - Imports: `datetime`
  - Imports: `json`
  - Imports: `os`
  - Imports: `re`
  - Imports: `src`
  - Imports: `sys`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/core/system_defense.py**
  - Imports: `gc`
  - Imports: `logging`
  - Imports: `os`
  - Imports: `psutil`
  - Imports: `src`
  - Imports: `typing`
- **meridian_backend/src/core/telegram_bridge.py**
  - Imports: `asyncio`
  - Imports: `database`
  - Imports: `httpx`
  - Imports: `os`
  - Imports: `src`
  - Imports: `tempfile`
  - Imports: `threading`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/core/temporal_memory.py**
  - Imports: `math`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/core/tool_indexer.py**
  - Imports: `math`
  - Imports: `re`
  - Imports: `src`
  - Imports: `typing`
- **meridian_backend/src/core/tool_regression_sentinel.py**
  - Imports: `logging`
  - Imports: `os`
  - Imports: `src`
  - Imports: `typing`
  - Imports: `yaml`
- **meridian_backend/src/core/triggers.py**
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/core/updater.py**
  - Imports: `hashlib`
  - Imports: `httpx`
  - Imports: `logging`
  - Imports: `os`
  - Imports: `packaging`
  - Imports: `shutil`
  - Imports: `sys`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/core/vault.py**
  - Imports: `base64`
  - Imports: `cryptography`
  - Imports: `getpass`
  - Imports: `hashlib`
  - Imports: `hmac`
  - Imports: `importlib`
  - Imports: `json`
  - Imports: `os`
  - Imports: `platform`
  - Imports: `src`
  - Imports: `threading`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/core/vision.py**
  - Imports: `PIL`
  - Imports: `base64`
  - Imports: `database`
  - Imports: `httpx`
  - Imports: `logging`
  - Imports: `mss`
  - Imports: `os`
  - Imports: `pyautogui`
  - Imports: `src`
  - Imports: `sys`
  - Imports: `tempfile`
  - Imports: `typing`
- **meridian_backend/src/core/vision_face.py**
  - Imports: `base64`
  - Imports: `cv2`
  - Imports: `hashlib`
  - Imports: `logging`
  - Imports: `numpy`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/core/vision_gesture.py**
  - Imports: `logging`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/core/watcher.py**
  - Imports: `ast`
  - Imports: `logging`
  - Imports: `os`
  - Imports: `re`
  - Imports: `src`
  - Imports: `time`
  - Imports: `typing`
  - Imports: `watchdog`
- **meridian_backend/src/core/what_broke_detective.py**
  - Imports: `logging`
  - Imports: `os`
  - Imports: `subprocess`
  - Imports: `typing`
- **meridian_backend/src/core/workflow_engine.py**
  - Imports: `json`
  - Imports: `os`
  - Imports: `re`
  - Imports: `src`
  - Imports: `time`
  - Imports: `typing`
  - Imports: `uuid`
- **meridian_backend/src/core/workspace_orchestrator.py**
  - Imports: `logging`
  - Imports: `os`
  - Imports: `platform`
  - Imports: `shutil`
  - Imports: `subprocess`
  - Imports: `typing`
  - Imports: `webbrowser`
- **meridian_backend/src/db/__init__.py**
  - Imports: `src`
- **meridian_backend/src/db/cache.py**
  - Imports: `collections`
  - Imports: `numpy`
  - Imports: `src`
  - Imports: `threading`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/db/connection.py**
  - Imports: `contextlib`
  - Imports: `os`
  - Imports: `pymongo`
  - Imports: `sqlite3`
  - Imports: `src`
  - Imports: `sys`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/db/contacts.py**
  - Imports: `re`
  - Imports: `src`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/db/conversations.py**
  - Imports: `numpy`
  - Imports: `os`
  - Imports: `re`
  - Imports: `src`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/db/embeddings.py**
  - Imports: `fastembed`
  - Imports: `hashlib`
  - Imports: `httpx`
  - Imports: `numpy`
  - Imports: `ollama`
  - Imports: `os`
  - Imports: `re`
  - Imports: `src`
  - Imports: `typing`
- **meridian_backend/src/db/logs.py**
  - Imports: `pymongo`
  - Imports: `random`
  - Imports: `src`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/db/memory.py**
  - Imports: `datetime`
  - Imports: `json`
  - Imports: `numpy`
  - Imports: `src`
  - Imports: `time`
- **meridian_backend/src/db/parsers.py**
  - Imports: `docx`
  - Imports: `os`
  - Imports: `pypdf`
- **meridian_backend/src/db/profile.py**
  - Imports: `base64`
  - Imports: `cryptography`
  - Imports: `hashlib`
  - Imports: `json`
  - Imports: `os`
  - Imports: `src`
  - Imports: `sys`
  - Imports: `threading`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/db/rag.py**
  - Imports: `json`
  - Imports: `math`
  - Imports: `numpy`
  - Imports: `re`
  - Imports: `src`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/db/vectors.py**
  - Imports: `os`
  - Imports: `src`
  - Imports: `threading`
  - Imports: `time`
  - Imports: `turbovec`
  - Imports: `typing`
- **meridian_backend/src/tools/auto_reviewer.py**
  - Imports: `os`
  - Imports: `src`
  - Imports: `subprocess`
  - Imports: `typing`
- **meridian_backend/src/tools/bill_radar.py**
  - Imports: `datetime`
  - Imports: `json`
  - Imports: `os`
  - Imports: `src`
  - Imports: `typing`
- **meridian_backend/src/tools/bookmark_manager.py**
  - Imports: `logging`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/tools/browser_agent.py**
  - Imports: `json`
  - Imports: `logging`
  - Imports: `os`
  - Imports: `playwright`
  - Imports: `src`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/tools/browser_extension_tools.py**
  - Imports: `asyncio`
  - Imports: `concurrent`
  - Imports: `src`
  - Imports: `typing`
  - Imports: `urllib`
  - Imports: `webbrowser`
- **meridian_backend/src/tools/browser_use_agent.py**
  - Imports: `asyncio`
  - Imports: `concurrent`
  - Imports: `database`
  - Imports: `json`
  - Imports: `ollama`
  - Imports: `os`
  - Imports: `re`
  - Imports: `src`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/tools/cam_guard.py**
  - Imports: `psutil`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/tools/car_logbook.py**
  - Imports: `dataclasses`
  - Imports: `logging`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/tools/chrome_manager.py**
  - Imports: `database`
  - Imports: `json`
  - Imports: `os`
  - Imports: `shutil`
  - Imports: `subprocess`
  - Imports: `sys`
  - Imports: `time`
  - Imports: `typing`
  - Imports: `urllib`
- **meridian_backend/src/tools/clipboard.py**
  - Imports: `bson`
  - Imports: `database`
  - Imports: `json`
  - Imports: `platform`
  - Imports: `pyperclip`
  - Imports: `shutil`
  - Imports: `time`
  - Imports: `typing`
  - Imports: `urllib`
- **meridian_backend/src/tools/communication.py**
  - Imports: `database`
  - Imports: `logging`
  - Imports: `os`
  - Imports: `platform`
  - Imports: `pyautogui`
  - Imports: `src`
  - Imports: `subprocess`
  - Imports: `time`
  - Imports: `typing`
  - Imports: `urllib`
  - Imports: `webbrowser`
- **meridian_backend/src/tools/day_planner.py**
  - Imports: `logging`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/tools/db_query.py**
  - Imports: `database`
  - Imports: `ollama`
  - Imports: `os`
  - Imports: `psycopg2`
  - Imports: `pymysql`
  - Imports: `re`
  - Imports: `sqlite3`
  - Imports: `src`
  - Imports: `threading`
  - Imports: `typing`
- **meridian_backend/src/tools/desktop.py**
  - Imports: `PIL`
  - Imports: `database`
  - Imports: `mss`
  - Imports: `os`
  - Imports: `pyautogui`
  - Imports: `src`
  - Imports: `tempfile`
  - Imports: `typing`
- **meridian_backend/src/tools/detonation_sandbox.py**
  - Imports: `os`
  - Imports: `typing`
- **meridian_backend/src/tools/developer.py**
  - Imports: `asyncio`
  - Imports: `os`
  - Imports: `platform`
  - Imports: `shutil`
  - Imports: `src`
  - Imports: `subprocess`
  - Imports: `tempfile`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/tools/dns_shield.py**
  - Imports: `os`
  - Imports: `re`
  - Imports: `socket`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/tools/documents.py**
  - Imports: `os`
  - Imports: `pypdf`
  - Imports: `re`
  - Imports: `reportlab`
  - Imports: `src`
  - Imports: `typing`
- **meridian_backend/src/tools/documents_office.py**
  - Imports: `docx`
  - Imports: `importlib`
  - Imports: `openpyxl`
  - Imports: `os`
  - Imports: `pptx`
  - Imports: `re`
  - Imports: `src`
  - Imports: `typing`
- **meridian_backend/src/tools/documents_slides.py**
  - Imports: `os`
  - Imports: `pptx`
  - Imports: `src`
  - Imports: `typing`
- **meridian_backend/src/tools/dynamic_manager.py**
  - Imports: `ast`
  - Imports: `builtins`
  - Imports: `logging`
  - Imports: `os`
  - Imports: `src`
  - Imports: `sys`
  - Imports: `typing`
- **meridian_backend/src/tools/expense_pool.py**
  - Imports: `collections`
  - Imports: `logging`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/tools/expiry_sentinel.py**
  - Imports: `datetime`
  - Imports: `json`
  - Imports: `os`
  - Imports: `src`
  - Imports: `typing`
- **meridian_backend/src/tools/exporter.py**
  - Imports: `database`
  - Imports: `json`
  - Imports: `os`
  - Imports: `shutil`
  - Imports: `src`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/tools/external_connectors.py**
  - Imports: `base64`
  - Imports: `email`
  - Imports: `json`
  - Imports: `os`
  - Imports: `requests`
  - Imports: `src`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/tools/family_board.py**
  - Imports: `logging`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/tools/file_janitor.py**
  - Imports: `hashlib`
  - Imports: `os`
  - Imports: `typing`
- **meridian_backend/src/tools/filesystem.py**
  - Imports: `ctypes`
  - Imports: `glob`
  - Imports: `os`
  - Imports: `pathlib`
  - Imports: `shutil`
  - Imports: `src`
  - Imports: `subprocess`
  - Imports: `sys`
  - Imports: `tempfile`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/tools/finance_sentinel.py**
  - Imports: `json`
  - Imports: `os`
  - Imports: `typing`
- **meridian_backend/src/tools/geo_location.py**
  - Imports: `httpx`
  - Imports: `os`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/tools/habit_tracker.py**
  - Imports: `logging`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/tools/health_ingest.py**
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/tools/home_assistant.py**
  - Imports: `logging`
  - Imports: `os`
  - Imports: `typing`
- **meridian_backend/src/tools/household.py**
  - Imports: `datetime`
  - Imports: `json`
  - Imports: `os`
  - Imports: `src`
  - Imports: `typing`
- **meridian_backend/src/tools/knowledge.py**
  - Imports: `database`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/tools/learning_queue.py**
  - Imports: `logging`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/tools/mcp_marketplace.py**
  - Imports: `json`
  - Imports: `os`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/tools/network_guardian.py**
  - Imports: `socket`
  - Imports: `typing`
- **meridian_backend/src/tools/networth_tracker.py**
  - Imports: `logging`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/tools/ollama_manager.py**
  - Imports: `database`
  - Imports: `threading`
- **meridian_backend/src/tools/os_automation.py**
  - Imports: `logging`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/tools/papercoder.py**
  - Imports: `config`
  - Imports: `dataclasses`
  - Imports: `dataset`
  - Imports: `json`
  - Imports: `math`
  - Imports: `model`
  - Imports: `os`
  - Imports: `random`
  - Imports: `re`
  - Imports: `src`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/tools/parental_controls.py**
  - Imports: `logging`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/tools/password_auditor.py**
  - Imports: `math`
  - Imports: `typing`
- **meridian_backend/src/tools/phishing_guard.py**
  - Imports: `typing`
  - Imports: `urllib`
- **meridian_backend/src/tools/phone_agent.py**
  - Imports: `asyncio`
  - Imports: `database`
  - Imports: `json`
  - Imports: `logging`
  - Imports: `os`
  - Imports: `time`
  - Imports: `twilio`
  - Imports: `typing`
- **meridian_backend/src/tools/photo_organizer.py**
  - Imports: `hashlib`
  - Imports: `logging`
  - Imports: `os`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/tools/price_watcher.py**
  - Imports: `logging`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/tools/recording.py**
  - Imports: `cv2`
  - Imports: `database`
  - Imports: `glob`
  - Imports: `json`
  - Imports: `mss`
  - Imports: `ollama`
  - Imports: `os`
  - Imports: `platform`
  - Imports: `pyautogui`
  - Imports: `pyperclip`
  - Imports: `threading`
  - Imports: `time`
- **meridian_backend/src/tools/registry.py**
  - Imports: `asyncio`
  - Imports: `concurrent`
  - Imports: `database`
  - Imports: `inspect`
  - Imports: `json`
  - Imports: `os`
  - Imports: `src`
  - Imports: `typing`
- **meridian_backend/src/tools/review.py**
  - Imports: `database`
  - Imports: `glob`
  - Imports: `os`
  - Imports: `src`
  - Imports: `subprocess`
  - Imports: `typing`
- **meridian_backend/src/tools/routine_composer.py**
  - Imports: `logging`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/tools/scheduler.py**
  - Imports: `apscheduler`
  - Imports: `datetime`
  - Imports: `src`
- **meridian_backend/src/tools/screenshot_memory.py**
  - Imports: `datetime`
  - Imports: `json`
  - Imports: `os`
  - Imports: `typing`
- **meridian_backend/src/tools/search_hub.py**
  - Imports: `database`
  - Imports: `os`
  - Imports: `re`
  - Imports: `typing`
- **meridian_backend/src/tools/secure_shredder.py**
  - Imports: `hashlib`
  - Imports: `logging`
  - Imports: `os`
  - Imports: `secrets`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/tools/security_auditor.py**
  - Imports: `os`
  - Imports: `re`
  - Imports: `socket`
  - Imports: `src`
  - Imports: `subprocess`
  - Imports: `typing`
- **meridian_backend/src/tools/shell.py**
  - Imports: `database`
  - Imports: `ollama`
  - Imports: `os`
  - Imports: `platform`
  - Imports: `src`
  - Imports: `subprocess`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/tools/system.py**
  - Imports: `database`
  - Imports: `os`
  - Imports: `platform`
  - Imports: `psutil`
  - Imports: `pyperclip`
  - Imports: `src`
  - Imports: `subprocess`
  - Imports: `sys`
  - Imports: `time`
  - Imports: `winreg`
- **meridian_backend/src/tools/system_windows.py**
  - Imports: `Quartz`
  - Imports: `ewmh`
  - Imports: `os`
  - Imports: `platform`
  - Imports: `psutil`
  - Imports: `pyautogui`
  - Imports: `pygetwindow`
  - Imports: `src`
  - Imports: `subprocess`
  - Imports: `sys`
  - Imports: `time`
  - Imports: `urllib`
  - Imports: `webbrowser`
- **meridian_backend/src/tools/task_scheduler.py**
  - Imports: `csv`
  - Imports: `os`
  - Imports: `platform`
  - Imports: `src`
  - Imports: `subprocess`
  - Imports: `sys`
- **meridian_backend/src/tools/totp_generator.py**
  - Imports: `base64`
  - Imports: `hashlib`
  - Imports: `hmac`
  - Imports: `struct`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/tools/travel_butler.py**
  - Imports: `datetime`
  - Imports: `json`
  - Imports: `os`
  - Imports: `src`
  - Imports: `typing`
- **meridian_backend/src/tools/usb_watchdog.py**
  - Imports: `typing`
- **meridian_backend/src/tools/vault.py**
  - Imports: `base64`
  - Imports: `cryptography`
  - Imports: `json`
  - Imports: `os`
  - Imports: `src`
  - Imports: `typing`
- **meridian_backend/src/tools/video_editor.py**
  - Imports: `PIL`
  - Imports: `cv2`
  - Imports: `glob`
  - Imports: `logging`
  - Imports: `os`
  - Imports: `src`
  - Imports: `subprocess`
  - Imports: `sys`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/tools/voice.py**
  - Imports: `src`
- **meridian_backend/src/tools/watcher.py**
  - Imports: `os`
  - Imports: `re`
  - Imports: `src`
  - Imports: `typing`
- **meridian_backend/src/tools/web.py**
  - Imports: `concurrent`
  - Imports: `database`
  - Imports: `ddgs`
  - Imports: `duckduckgo_search`
  - Imports: `httpx`
  - Imports: `os`
  - Imports: `re`
  - Imports: `selectolax`
  - Imports: `sqlite3,`
  - Imports: `src`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/tools/web_browser.py**
  - Imports: `base64`
  - Imports: `database`
  - Imports: `httpx`
  - Imports: `json`
  - Imports: `ollama`
  - Imports: `os`
  - Imports: `playwright`
  - Imports: `re`
  - Imports: `selectolax`
  - Imports: `src`
  - Imports: `tempfile`
  - Imports: `time`
  - Imports: `typing`
  - Imports: `urllib`
- **meridian_backend/src/tools/web_scraper.py**
  - Imports: `database`
  - Imports: `httpx`
  - Imports: `ipaddress`
  - Imports: `ollama`
  - Imports: `re`
  - Imports: `selectolax`
  - Imports: `src`
  - Imports: `time`
  - Imports: `typing`
  - Imports: `urllib`
  - Imports: `xml`
- **meridian_backend/src/tools/wellness.py**
  - Imports: `src`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/tools/whatsapp_manager.py**
  - Imports: `database`
  - Imports: `json`
  - Imports: `logging`
  - Imports: `os`
  - Imports: `playwright`
  - Imports: `src`
  - Imports: `time`
  - Imports: `typing`
  - Imports: `webbrowser`
- **meridian_backend/src/tools/wifi_assessor.py**
  - Imports: `logging`
  - Imports: `sys`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/tools/workspace_layout.py**
  - Imports: `logging`
  - Imports: `subprocess`
  - Imports: `sys`
  - Imports: `typing`
- **meridian_backend/src/voice/ambient_listener.py**
  - Imports: `asyncio`
  - Imports: `collections`
  - Imports: `logging`
  - Imports: `src`
  - Imports: `struct`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/voice/duplex.py**
  - Imports: `collections`
  - Imports: `src`
  - Imports: `typing`
- **meridian_backend/src/voice/polyglot.py**
  - Imports: `logging`
  - Imports: `typing`
- **meridian_backend/src/voice/stt.py**
  - Imports: `database`
  - Imports: `faster_whisper`
  - Imports: `logging`
  - Imports: `numpy`
  - Imports: `os`
  - Imports: `sounddevice`
  - Imports: `src`
  - Imports: `tempfile`
  - Imports: `threading`
  - Imports: `time`
  - Imports: `torch`
- **meridian_backend/src/voice/tts.py**
  - Imports: `database`
  - Imports: `datetime`
  - Imports: `logging`
  - Imports: `numpy`
  - Imports: `os`
  - Imports: `queue`
  - Imports: `random`
  - Imports: `re`
  - Imports: `sounddevice`
  - Imports: `soundfile`
  - Imports: `src`
  - Imports: `supertonic`
  - Imports: `tempfile`
  - Imports: `threading`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/voice/vad.py**
  - Imports: `faster_whisper`
  - Imports: `numpy`
  - Imports: `src`
  - Imports: `threading`
  - Imports: `typing`
- **meridian_backend/src/voice/voice_biometrics.py**
  - Imports: `hashlib`
  - Imports: `math`
  - Imports: `src`
  - Imports: `typing`
- **meridian_backend/src/voice/wakeword.py**
  - Imports: `database`
  - Imports: `logging`
  - Imports: `numpy`
  - Imports: `openwakeword`
  - Imports: `os`
  - Imports: `sounddevice`
  - Imports: `src`
  - Imports: `sys`
  - Imports: `threading`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/tests/conftest.py**
  - Imports: `os`
  - Imports: `pyautogui`
  - Imports: `pytest`
  - Imports: `sounddevice`
  - Imports: `src`
  - Imports: `sys`
  - Imports: `tempfile`
  - Imports: `unittest`
- **meridian_backend/tests/run_tests.py**
  - Imports: `os`
  - Imports: `sys`
  - Imports: `unittest`
- **meridian_backend/tests/test_advanced_proactive.py**
  - Imports: `os`
  - Imports: `src`
  - Imports: `sys`
  - Imports: `time`
  - Imports: `unittest`
- **meridian_backend/tests/test_atomic_storage.py**
  - Imports: `json`
  - Imports: `os`
  - Imports: `pytest`
  - Imports: `src`
- **meridian_backend/tests/test_audit_bugfixes.py**
  - Imports: `asyncio`
  - Imports: `json`
  - Imports: `os`
  - Imports: `pytest`
  - Imports: `src`
  - Imports: `sys`
  - Imports: `unittest`
- **meridian_backend/tests/test_audit_remediation.py**
  - Imports: `os`
  - Imports: `src`
  - Imports: `unittest`
- **meridian_backend/tests/test_auto_bug_fixer.py**
  - Imports: `api`
  - Imports: `asyncio`
  - Imports: `fastapi`
  - Imports: `os`
  - Imports: `pytest`
  - Imports: `src`
  - Imports: `sys`
- **meridian_backend/tests/test_backend_improvements.py**
  - Imports: `os`
  - Imports: `pytest`
  - Imports: `src`
  - Imports: `unittest`
- **meridian_backend/tests/test_backlog_features.py**
  - Imports: `database`
  - Imports: `pytest`
  - Imports: `src`
- **meridian_backend/tests/test_backlog_sprint.py**
  - Imports: `api`
  - Imports: `hashlib`
  - Imports: `hmac`
  - Imports: `os`
  - Imports: `pytest`
  - Imports: `socket`
  - Imports: `src`
  - Imports: `threading`
- **meridian_backend/tests/test_bridges.py**
  - Imports: `os`
  - Imports: `src`
  - Imports: `sys`
  - Imports: `unittest`
- **meridian_backend/tests/test_browser_agent.py**
  - Imports: `os`
  - Imports: `src`
  - Imports: `sys`
  - Imports: `unittest`
- **meridian_backend/tests/test_browser_extension.py**
  - Imports: `asyncio`
  - Imports: `src`
  - Imports: `unittest`
- **meridian_backend/tests/test_browser_fallback.py**
  - Imports: `os`
  - Imports: `src`
  - Imports: `sys`
  - Imports: `unittest`
- **meridian_backend/tests/test_browser_frame.py**
  - Imports: `pytest`
  - Imports: `src`
- **meridian_backend/tests/test_browser_use.py**
  - Imports: `os`
  - Imports: `src`
  - Imports: `sys`
  - Imports: `unittest`
- **meridian_backend/tests/test_butler_media.py**
  - Imports: `database`
  - Imports: `os`
  - Imports: `src`
  - Imports: `sys`
  - Imports: `unittest`
- **meridian_backend/tests/test_chat_abort.py**
  - Imports: `api`
  - Imports: `fastapi`
  - Imports: `os`
  - Imports: `src`
  - Imports: `sys`
  - Imports: `unittest`
- **meridian_backend/tests/test_cognitive_graph.py**
  - Imports: `os`
  - Imports: `pytest`
  - Imports: `src`
  - Imports: `time`
- **meridian_backend/tests/test_config.py**
  - Imports: `os`
  - Imports: `src`
  - Imports: `sys`
  - Imports: `unittest`
- **meridian_backend/tests/test_consensus_gate.py**
  - Imports: `pytest`
  - Imports: `src`
- **meridian_backend/tests/test_context_budget.py**
  - Imports: `database`
  - Imports: `os`
  - Imports: `pytest`
  - Imports: `sys`
- **meridian_backend/tests/test_custom_password_auth.py**
  - Imports: `os`
  - Imports: `pytest`
  - Imports: `src`
- **meridian_backend/tests/test_database.py**
  - Imports: `database`
  - Imports: `os`
  - Imports: `shutil`
  - Imports: `sys`
  - Imports: `threading`
  - Imports: `unittest`
- **meridian_backend/tests/test_day10_features.py**
  - Imports: `PIL`
  - Imports: `asyncio`
  - Imports: `os`
  - Imports: `pytest`
  - Imports: `src`
  - Imports: `sys`
  - Imports: `tempfile`
  - Imports: `unittest`
- **meridian_backend/tests/test_day11_features.py**
  - Imports: `os`
  - Imports: `pytest`
  - Imports: `src`
  - Imports: `sys`
- **meridian_backend/tests/test_day12_features.py**
  - Imports: `pytest`
  - Imports: `src`
- **meridian_backend/tests/test_day13_features.py**
  - Imports: `pytest`
  - Imports: `src`
- **meridian_backend/tests/test_day14_day15_features.py**
  - Imports: `os`
  - Imports: `pytest`
  - Imports: `src`
  - Imports: `time`
- **meridian_backend/tests/test_day16_17_18_features.py**
  - Imports: `os`
  - Imports: `pytest`
  - Imports: `src`
  - Imports: `sys`
- **meridian_backend/tests/test_day3_features.py**
  - Imports: `database`
  - Imports: `pytest`
  - Imports: `src`
  - Imports: `unittest`
- **meridian_backend/tests/test_day4_features.py**
  - Imports: `database`
  - Imports: `os`
  - Imports: `pytest`
  - Imports: `src`
  - Imports: `subprocess`
  - Imports: `sys`
  - Imports: `tempfile`
  - Imports: `unittest`
- **meridian_backend/tests/test_day5_features.py**
  - Imports: `api`
  - Imports: `base64`
  - Imports: `fastapi`
  - Imports: `os`
  - Imports: `pytest`
  - Imports: `src`
  - Imports: `sys`
- **meridian_backend/tests/test_day6_features.py**
  - Imports: `os`
  - Imports: `pytest`
  - Imports: `src`
- **meridian_backend/tests/test_day7_features.py**
  - Imports: `database`
  - Imports: `json`
  - Imports: `numpy`
  - Imports: `os`
  - Imports: `pytest`
  - Imports: `src`
  - Imports: `sys`
- **meridian_backend/tests/test_day8_features.py**
  - Imports: `os`
  - Imports: `pytest`
  - Imports: `src`
  - Imports: `sys`
- **meridian_backend/tests/test_day9_features.py**
  - Imports: `asyncio`
  - Imports: `database`
  - Imports: `hashlib`
  - Imports: `json`
  - Imports: `os`
  - Imports: `pytest`
  - Imports: `src`
- **meridian_backend/tests/test_dev_intelligence_suite.py**
  - Imports: `api`
  - Imports: `asyncio`
  - Imports: `fastapi`
  - Imports: `os`
  - Imports: `pytest`
  - Imports: `src`
- **meridian_backend/tests/test_document_tools.py**
  - Imports: `os`
  - Imports: `pytest`
  - Imports: `src`
- **meridian_backend/tests/test_error_diagnostics.py**
  - Imports: `pytest`
  - Imports: `src`
- **meridian_backend/tests/test_exhaustive_fallback.py**
  - Imports: `json`
  - Imports: `os`
  - Imports: `pytest`
  - Imports: `src`
  - Imports: `sys`
  - Imports: `unittest`
- **meridian_backend/tests/test_full_proactive_suite.py**
  - Imports: `os`
  - Imports: `src`
  - Imports: `sys`
  - Imports: `time`
  - Imports: `unittest`
- **meridian_backend/tests/test_geo_location.py**
  - Imports: `pytest`
  - Imports: `src`
  - Imports: `unittest`
- **meridian_backend/tests/test_hybrid_rag.py**
  - Imports: `database`
  - Imports: `pytest`
  - Imports: `sqlite3`
  - Imports: `src`
- **meridian_backend/tests/test_jarvis_perception.py**
  - Imports: `os`
  - Imports: `pytest`
  - Imports: `src`
  - Imports: `sys`
- **meridian_backend/tests/test_known_errors_remediation.py**
  - Imports: `os`
  - Imports: `pytest`
  - Imports: `src`
  - Imports: `sys`
- **meridian_backend/tests/test_llm_provider.py**
  - Imports: `asyncio`
  - Imports: `os`
  - Imports: `shutil`
  - Imports: `src`
  - Imports: `sys`
  - Imports: `unittest`
- **meridian_backend/tests/test_logging.py**
  - Imports: `json`
  - Imports: `logging`
  - Imports: `os`
  - Imports: `shutil`
  - Imports: `src`
  - Imports: `sys`
  - Imports: `unittest`
- **meridian_backend/tests/test_loop_parser.py**
  - Imports: `json`
  - Imports: `pytest`
  - Imports: `src`
  - Imports: `unittest`
- **meridian_backend/tests/test_loop_submodules.py**
  - Imports: `asyncio`
  - Imports: `pytest`
  - Imports: `src`
- **meridian_backend/tests/test_mobile_websocket.py**
  - Imports: `api`
  - Imports: `asyncio`
  - Imports: `concurrent`
  - Imports: `fastapi`
  - Imports: `json`
  - Imports: `os`
  - Imports: `pytest`
  - Imports: `src`
  - Imports: `sys`
- **meridian_backend/tests/test_model_source.py**
  - Imports: `database`
  - Imports: `os`
  - Imports: `pytest`
  - Imports: `src`
- **meridian_backend/tests/test_multi_os.py**
  - Imports: `os`
  - Imports: `platform`
  - Imports: `pytest`
  - Imports: `src`
  - Imports: `sys`
- **meridian_backend/tests/test_multimode_routing.py**
  - Imports: `api`
  - Imports: `database`
  - Imports: `fastapi`
  - Imports: `json`
  - Imports: `os`
  - Imports: `pytest`
  - Imports: `src`
  - Imports: `sys`
  - Imports: `unittest`
- **meridian_backend/tests/test_new_features.py**
  - Imports: `api`
  - Imports: `asyncio`
  - Imports: `fastapi`
  - Imports: `pytest`
  - Imports: `src`
- **meridian_backend/tests/test_oauth.py**
  - Imports: `os`
  - Imports: `pytest`
  - Imports: `src`
  - Imports: `sys`
  - Imports: `time`
- **meridian_backend/tests/test_p2p.py**
  - Imports: `database`
  - Imports: `os`
  - Imports: `pytest`
  - Imports: `sqlite3`
  - Imports: `src`
- **meridian_backend/tests/test_perception_bridge.py**
  - Imports: `api`
  - Imports: `fastapi`
  - Imports: `pytest`
- **meridian_backend/tests/test_proactive.py**
  - Imports: `asyncio`
  - Imports: `pytest`
  - Imports: `src`
- **meridian_backend/tests/test_proactive_mode.py**
  - Imports: `json`
  - Imports: `os`
  - Imports: `src`
  - Imports: `sys`
  - Imports: `unittest`
- **meridian_backend/tests/test_proactive_notifications.py**
  - Imports: `api`
  - Imports: `asyncio`
  - Imports: `fastapi`
  - Imports: `pytest`
  - Imports: `src`
- **meridian_backend/tests/test_reflection_engine.py**
  - Imports: `os`
  - Imports: `pytest`
  - Imports: `src`
  - Imports: `tempfile`
  - Imports: `unittest`
- **meridian_backend/tests/test_research_optimization.py**
  - Imports: `json`
  - Imports: `pytest`
  - Imports: `src`
  - Imports: `threading`
  - Imports: `unittest`
- **meridian_backend/tests/test_response_resilience.py**
  - Imports: `json`
  - Imports: `src`
  - Imports: `unittest`
- **meridian_backend/tests/test_security_features.py**
  - Imports: `api`
  - Imports: `asyncio`
  - Imports: `fastapi`
  - Imports: `httpx`
  - Imports: `os`
  - Imports: `pytest`
  - Imports: `src`
  - Imports: `typing`
- **meridian_backend/tests/test_silero_vad.py**
  - Imports: `numpy`
  - Imports: `os`
  - Imports: `src`
  - Imports: `sys`
  - Imports: `unittest`
- **meridian_backend/tests/test_skill_packs.py**
  - Imports: `os`
  - Imports: `pytest`
  - Imports: `src`
- **meridian_backend/tests/test_small_model_support.py**
  - Imports: `json`
  - Imports: `pytest`
  - Imports: `src`
- **meridian_backend/tests/test_sprint24_hardening.py**
  - Imports: `api`
  - Imports: `fastapi`
  - Imports: `os`
  - Imports: `pytest`
  - Imports: `src`
  - Imports: `tempfile`
- **meridian_backend/tests/test_sprint25_hardening.py**
  - Imports: `json`
  - Imports: `pytest`
  - Imports: `src`
  - Imports: `time`
- **meridian_backend/tests/test_sprint27_hardening.py**
  - Imports: `logging`
  - Imports: `os`
  - Imports: `pytest`
  - Imports: `src`
  - Imports: `sys`
- **meridian_backend/tests/test_sprint28_hardening.py**
  - Imports: `database`
  - Imports: `inspect`
  - Imports: `os`
  - Imports: `pytest`
  - Imports: `src`
- **meridian_backend/tests/test_sprint2_features.py**
  - Imports: `api`
  - Imports: `fastapi`
  - Imports: `os`
  - Imports: `pytest`
  - Imports: `src`
  - Imports: `unittest`
- **meridian_backend/tests/test_sprint40.py**
  - Imports: `asyncio`
  - Imports: `fastapi`
  - Imports: `pytest`
  - Imports: `src`
  - Imports: `unittest`
- **meridian_backend/tests/test_sprint45.py**
  - Imports: `doctor`
  - Imports: `json`
  - Imports: `os`
  - Imports: `pytest`
  - Imports: `src`
  - Imports: `sys`
  - Imports: `yaml`
- **meridian_backend/tests/test_standalone_bridge.py**
  - Imports: `fastapi`
  - Imports: `json`
  - Imports: `mobile_bridge_service`
  - Imports: `os`
  - Imports: `pytest`
  - Imports: `src`
  - Imports: `sys`
- **meridian_backend/tests/test_stream_resiliency.py**
  - Imports: `asyncio`
  - Imports: `os`
  - Imports: `pytest`
  - Imports: `src`
  - Imports: `sys`
- **meridian_backend/tests/test_swarm.py**
  - Imports: `asyncio`
  - Imports: `os`
  - Imports: `pytest`
  - Imports: `src`
  - Imports: `sys`
  - Imports: `unittest`
- **meridian_backend/tests/test_swarm_routing.py**
  - Imports: `pytest`
  - Imports: `src`
- **meridian_backend/tests/test_system_hardening.py**
  - Imports: `json`
  - Imports: `os`
  - Imports: `pytest`
  - Imports: `src`
  - Imports: `sys`
  - Imports: `unittest`
- **meridian_backend/tests/test_timeline_completion.py**
  - Imports: `pytest`
  - Imports: `src`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/tests/test_tool_intelligence.py**
  - Imports: `inspect`
  - Imports: `json`
  - Imports: `pytest`
  - Imports: `src`
- **meridian_backend/tests/test_tool_modernization.py**
  - Imports: `asyncio`
  - Imports: `pytest`
  - Imports: `src`
  - Imports: `unittest`
- **meridian_backend/tests/test_tool_regression.py**
  - Imports: `os`
  - Imports: `pytest`
  - Imports: `src`
- **meridian_backend/tests/test_tools.py**
  - Imports: `json`
  - Imports: `os`
  - Imports: `shutil`
  - Imports: `src`
  - Imports: `sys`
  - Imports: `unittest`
- **meridian_backend/tests/test_user_delight_tools.py**
  - Imports: `missing_module`
  - Imports: `pytest`
  - Imports: `src`
  - Imports: `unittest`
- **meridian_backend/tests/test_vault.py**
  - Imports: `os`
  - Imports: `pytest`
  - Imports: `src`
  - Imports: `time`
- **meridian_backend/tests/test_video_editor.py**
  - Imports: `cv2`
  - Imports: `numpy`
  - Imports: `os`
  - Imports: `pytest`
  - Imports: `src`
  - Imports: `sys`
  - Imports: `tempfile`
- **meridian_backend/tests/test_voice_hardening.py**
  - Imports: `numpy`
  - Imports: `os`
  - Imports: `pytest`
  - Imports: `src`
  - Imports: `sys`
  - Imports: `time`
  - Imports: `unittest`
- **meridian_backend/tests/test_voice_speed.py**
  - Imports: `api`
  - Imports: `fastapi`
  - Imports: `io`
  - Imports: `numpy`
  - Imports: `pytest`
  - Imports: `soundfile`
  - Imports: `src`
  - Imports: `unittest`
- **meridian_backend/tests/test_wakeword_continuous.py**
  - Imports: `api`
  - Imports: `fastapi`
  - Imports: `os`
  - Imports: `pytest`
  - Imports: `src`
  - Imports: `sys`
  - Imports: `time`
- **meridian_backend/tests/test_wakeword_onnx.py**
  - Imports: `api`
  - Imports: `fastapi`
  - Imports: `os`
  - Imports: `pytest`
  - Imports: `src`
  - Imports: `sys`
- **meridian_backend/tests/test_web_guards.py**
  - Imports: `src`
  - Imports: `unittest`
- **meridian_backend/tests/test_workflow.py**
  - Imports: `os`
  - Imports: `pytest`
  - Imports: `src`
  - Imports: `sys`
- **meridian_backend/tests_run.py**
  - Imports: `pytest`
  - Imports: `sys`
- **meridian_frontend/src-tauri/api/_internal/cv2/__init__.py**
  - Imports: `copy`
  - Imports: `importlib`
  - Imports: `numpy`
  - Imports: `os`
  - Imports: `platform`
  - Imports: `sys`
- **meridian_frontend/src-tauri/api/_internal/cv2/config.py**
  - Imports: `os`
- **meridian_frontend/src-tauri/api/_internal/cv2/data/__init__.py**
  - Imports: `os`
- **meridian_frontend/src-tauri/api/_internal/cv2/load_config_py3.py**
  - Imports: `os`
  - Imports: `sys`
- **meridian_frontend/src-tauri/api/_internal/cv2/mat_wrapper/__init__.py**
  - Imports: `cv2`
  - Imports: `numpy`
  - Imports: `typing`
- **meridian_frontend/src-tauri/api/_internal/cv2/misc/version.py**
  - Imports: `cv2`
- **meridian_frontend/src-tauri/api/_internal/cv2/typing/__init__.py**
  - Imports: `cv2`
  - Imports: `numpy`
  - Imports: `typing`
- **meridian_frontend/src-tauri/api/_internal/cv2/utils/__init__.py**
  - Imports: `collections`
  - Imports: `cv2`
- **meridian_frontend/src-tauri/api/_internal/fastapi/__init__.py**
  - Imports: `starlette`
- **meridian_frontend/src-tauri/api/_internal/fastapi/__main__.py**
  - Imports: `fastapi`
- **meridian_frontend/src-tauri/api/_internal/fastapi/_compat/shared.py**
  - Imports: `collections`
  - Imports: `dataclasses`
  - Imports: `fastapi`
  - Imports: `pydantic`
  - Imports: `starlette`
  - Imports: `types`
  - Imports: `typing`
  - Imports: `warnings`
- **meridian_frontend/src-tauri/api/_internal/fastapi/_compat/v2.py**
  - Imports: `collections`
  - Imports: `copy`
  - Imports: `dataclasses`
  - Imports: `enum`
  - Imports: `fastapi`
  - Imports: `functools`
  - Imports: `pydantic`
  - Imports: `pydantic_core`
  - Imports: `re`
  - Imports: `typing`
  - Imports: `warnings`
- **meridian_frontend/src-tauri/api/_internal/fastapi/applications.py**
  - Imports: `Starlette`
  - Imports: `annotated_doc`
  - Imports: `collections`
  - Imports: `enum`
  - Imports: `fastapi`
  - Imports: `os`
  - Imports: `pydantic`
  - Imports: `starlette`
  - Imports: `time`
  - Imports: `typing`
  - Imports: `typing_extensions`
- **meridian_frontend/src-tauri/api/_internal/fastapi/background.py**
  - Imports: `annotated_doc`
  - Imports: `collections`
  - Imports: `fastapi`
  - Imports: `starlette`
  - Imports: `typing`
  - Imports: `typing_extensions`
- **meridian_frontend/src-tauri/api/_internal/fastapi/cli.py**
  - Imports: `fastapi_cli`
- **meridian_frontend/src-tauri/api/_internal/fastapi/concurrency.py**
  - Imports: `anyio`
  - Imports: `collections`
  - Imports: `contextlib`
  - Imports: `starlette`
  - Imports: `typing`
- **meridian_frontend/src-tauri/api/_internal/fastapi/datastructures.py**
  - Imports: `annotated_doc`
  - Imports: `collections`
  - Imports: `fastapi`
  - Imports: `pydantic`
  - Imports: `starlette`
  - Imports: `typing`
- **meridian_frontend/src-tauri/api/_internal/fastapi/dependencies/models.py**
  - Imports: `asyncio`
  - Imports: `collections`
  - Imports: `dataclasses`
  - Imports: `fastapi`
  - Imports: `functools`
  - Imports: `inspect`
  - Imports: `sys`
  - Imports: `typing`
- **meridian_frontend/src-tauri/api/_internal/fastapi/dependencies/utils.py**
  - Imports: `annotationlib`
  - Imports: `collections`
  - Imports: `contextlib`
  - Imports: `copy`
  - Imports: `dataclasses`
  - Imports: `fastapi`
  - Imports: `inspect`
  - Imports: `multipart`
  - Imports: `pydantic`
  - Imports: `python_multipart`
  - Imports: `starlette`
  - Imports: `sys`
  - Imports: `typing`
  - Imports: `typing_inspection`
- **meridian_frontend/src-tauri/api/_internal/fastapi/encoders.py**
  - Imports: `annotated_doc`
  - Imports: `collections`
  - Imports: `dataclasses`
  - Imports: `datetime`
  - Imports: `decimal`
  - Imports: `enum`
  - Imports: `fastapi`
  - Imports: `ipaddress`
  - Imports: `pathlib`
  - Imports: `pydantic`
  - Imports: `pydantic_core`
  - Imports: `pydantic_extra_types`
  - Imports: `re`
  - Imports: `types`
  - Imports: `typing`
  - Imports: `uuid`
- **meridian_frontend/src-tauri/api/_internal/fastapi/exception_handlers.py**
  - Imports: `fastapi`
  - Imports: `starlette`
- **meridian_frontend/src-tauri/api/_internal/fastapi/exceptions.py**
  - Imports: `annotated_doc`
  - Imports: `collections`
  - Imports: `fastapi`
  - Imports: `pydantic`
  - Imports: `starlette`
  - Imports: `typing`
- **meridian_frontend/src-tauri/api/_internal/fastapi/logger.py**
  - Imports: `logging`
- **meridian_frontend/src-tauri/api/_internal/fastapi/middleware/__init__.py**
  - Imports: `starlette`
- **meridian_frontend/src-tauri/api/_internal/fastapi/middleware/asyncexitstack.py**
  - Imports: `contextlib`
  - Imports: `starlette`
- **meridian_frontend/src-tauri/api/_internal/fastapi/middleware/cors.py**
  - Imports: `starlette`
- **meridian_frontend/src-tauri/api/_internal/fastapi/middleware/gzip.py**
  - Imports: `starlette`
- **meridian_frontend/src-tauri/api/_internal/fastapi/middleware/httpsredirect.py**
  - Imports: `starlette`
- **meridian_frontend/src-tauri/api/_internal/fastapi/middleware/trustedhost.py**
  - Imports: `starlette`
- **meridian_frontend/src-tauri/api/_internal/fastapi/middleware/wsgi.py**
  - Imports: `starlette`
- **meridian_frontend/src-tauri/api/_internal/fastapi/openapi/docs.py**
  - Imports: `annotated_doc`
  - Imports: `fastapi`
  - Imports: `json`
  - Imports: `starlette`
  - Imports: `typing`
- **meridian_frontend/src-tauri/api/_internal/fastapi/openapi/models.py**
  - Imports: `collections`
  - Imports: `email_validator`
  - Imports: `enum`
  - Imports: `fastapi`
  - Imports: `pydantic`
  - Imports: `typing`
  - Imports: `typing_extensions`
- **meridian_frontend/src-tauri/api/_internal/fastapi/openapi/utils.py**
  - Imports: `collections`
  - Imports: `copy`
  - Imports: `fastapi`
  - Imports: `http`
  - Imports: `inspect`
  - Imports: `pydantic`
  - Imports: `starlette`
  - Imports: `typing`
  - Imports: `warnings`
- **meridian_frontend/src-tauri/api/_internal/fastapi/param_functions.py**
  - Imports: `annotated_doc`
  - Imports: `collections`
  - Imports: `fastapi`
  - Imports: `pydantic`
  - Imports: `typing`
  - Imports: `typing_extensions`
- **meridian_frontend/src-tauri/api/_internal/fastapi/params.py**
  - Imports: `collections`
  - Imports: `dataclasses`
  - Imports: `enum`
  - Imports: `fastapi`
  - Imports: `pydantic`
  - Imports: `typing`
  - Imports: `typing_extensions`
  - Imports: `warnings`
- **meridian_frontend/src-tauri/api/_internal/fastapi/requests.py**
  - Imports: `starlette`
- **meridian_frontend/src-tauri/api/_internal/fastapi/responses.py**
  - Imports: `fastapi`
  - Imports: `importlib`
  - Imports: `starlette`
  - Imports: `typing`
  - Imports: `typing_extensions`
- **meridian_frontend/src-tauri/api/_internal/fastapi/routing.py**
  - Imports: `Starlette`
  - Imports: `annotated_doc`
  - Imports: `anyio`
  - Imports: `collections`
  - Imports: `contextlib`
  - Imports: `contextvars`
  - Imports: `copy`
  - Imports: `dataclasses`
  - Imports: `email`
  - Imports: `enum`
  - Imports: `errno`
  - Imports: `fastapi`
  - Imports: `functools`
  - Imports: `inspect`
  - Imports: `json`
  - Imports: `os`
  - Imports: `pydantic`
  - Imports: `starlette`
  - Imports: `stat`
  - Imports: `types`
  - Imports: `typing`
  - Imports: `typing_extensions`
- **meridian_frontend/src-tauri/api/_internal/fastapi/security/api_key.py**
  - Imports: `annotated_doc`
  - Imports: `fastapi`
  - Imports: `starlette`
  - Imports: `typing`
- **meridian_frontend/src-tauri/api/_internal/fastapi/security/base.py**
  - Imports: `fastapi`
- **meridian_frontend/src-tauri/api/_internal/fastapi/security/http.py**
  - Imports: `annotated_doc`
  - Imports: `base64`
  - Imports: `binascii`
  - Imports: `fastapi`
  - Imports: `pydantic`
  - Imports: `starlette`
  - Imports: `typing`
- **meridian_frontend/src-tauri/api/_internal/fastapi/security/oauth2.py**
  - Imports: `annotated_doc`
  - Imports: `fastapi`
  - Imports: `starlette`
  - Imports: `typing`
- **meridian_frontend/src-tauri/api/_internal/fastapi/security/open_id_connect_url.py**
  - Imports: `annotated_doc`
  - Imports: `fastapi`
  - Imports: `starlette`
  - Imports: `typing`
- **meridian_frontend/src-tauri/api/_internal/fastapi/sse.py**
  - Imports: `annotated_doc`
  - Imports: `pydantic`
  - Imports: `starlette`
  - Imports: `typing`
- **meridian_frontend/src-tauri/api/_internal/fastapi/staticfiles.py**
  - Imports: `starlette`
- **meridian_frontend/src-tauri/api/_internal/fastapi/templating.py**
  - Imports: `starlette`
- **meridian_frontend/src-tauri/api/_internal/fastapi/testclient.py**
  - Imports: `starlette`
- **meridian_frontend/src-tauri/api/_internal/fastapi/types.py**
  - Imports: `collections`
  - Imports: `enum`
  - Imports: `pydantic`
  - Imports: `types`
  - Imports: `typing`
- **meridian_frontend/src-tauri/api/_internal/fastapi/utils.py**
  - Imports: `fastapi`
  - Imports: `pydantic`
  - Imports: `re`
  - Imports: `typing`
  - Imports: `warnings`
- **meridian_frontend/src-tauri/api/_internal/fastapi/websockets.py**
  - Imports: `starlette`
- **meridian_frontend/src-tauri/api/_internal/playwright/driver/package/lib/coreBundle.js**
  - Imports: `test`
- **meridian_frontend/src-tauri/api/_internal/playwright/driver/package/lib/utilsBundle.js**
  - Imports: `ajv`
  - Imports: `ajv-formats`
- **meridian_frontend/src-tauri/api/_internal/playwright/driver/package/types/structs.d.ts**
  - Imports: `types`
- **meridian_frontend/src-tauri/api/_internal/playwright/driver/package/types/types.d.ts**
  - Imports: `child_process`
  - Imports: `fs`
  - Imports: `protocol`
  - Imports: `stream`
  - Imports: `structs`
  - Imports: `test`
  - Imports: `v3`
  - Imports: `zod`
- **meridian_frontend/src-tauri/api/_internal/pydantic/__init__.py**
  - Imports: `importlib`
  - Imports: `pydantic`
  - Imports: `pydantic_core`
  - Imports: `typing`
  - Imports: `warnings`
- **meridian_frontend/src-tauri/api/_internal/pydantic/_internal/_config.py**
  - Imports: `__future__`
  - Imports: `contextlib`
  - Imports: `pydantic_core`
  - Imports: `re`
  - Imports: `typing`
  - Imports: `typing_extensions`
  - Imports: `warnings`
- **meridian_frontend/src-tauri/api/_internal/pydantic/_internal/_core_metadata.py**
  - Imports: `__future__`
  - Imports: `typing`
  - Imports: `warnings`
- **meridian_frontend/src-tauri/api/_internal/pydantic/_internal/_core_utils.py**
  - Imports: `__future__`
  - Imports: `collections`
  - Imports: `inspect`
  - Imports: `pydantic`
  - Imports: `pydantic_core`
  - Imports: `rich`
  - Imports: `typing`
  - Imports: `typing_extensions`
  - Imports: `typing_inspection`
- **meridian_frontend/src-tauri/api/_internal/pydantic/_internal/_dataclasses.py**
  - Imports: `__future__`
  - Imports: `_typeshed`
  - Imports: `collections`
  - Imports: `contextlib`
  - Imports: `copy`
  - Imports: `dataclasses`
  - Imports: `functools`
  - Imports: `pydantic`
  - Imports: `pydantic_core`
  - Imports: `sys`
  - Imports: `typing`
  - Imports: `typing_extensions`
  - Imports: `warnings`
- **meridian_frontend/src-tauri/api/_internal/pydantic/_internal/_decorators.py**
  - Imports: `__future__`
  - Imports: `collections`
  - Imports: `copy`
  - Imports: `dataclasses`
  - Imports: `functools`
  - Imports: `inspect`
  - Imports: `itertools`
  - Imports: `its`
  - Imports: `pydantic_core`
  - Imports: `the`
  - Imports: `types`
  - Imports: `typing`
  - Imports: `typing_extensions`
- **meridian_frontend/src-tauri/api/_internal/pydantic/_internal/_decorators_v1.py**
  - Imports: `__future__`
  - Imports: `inspect`
  - Imports: `pydantic_core`
  - Imports: `typing`
  - Imports: `typing_extensions`
- **meridian_frontend/src-tauri/api/_internal/pydantic/_internal/_discriminated_union.py**
  - Imports: `__future__`
  - Imports: `collections`
  - Imports: `pydantic_core`
  - Imports: `typing`
- **meridian_frontend/src-tauri/api/_internal/pydantic/_internal/_docs_extraction.py**
  - Imports: `__future__`
  - Imports: `ast`
  - Imports: `inspect`
  - Imports: `sys`
  - Imports: `textwrap`
  - Imports: `typing`
- **meridian_frontend/src-tauri/api/_internal/pydantic/_internal/_fields.py**
  - Imports: `__future__`
  - Imports: `annotated_types`
  - Imports: `collections`
  - Imports: `dataclasses`
  - Imports: `functools`
  - Imports: `inspect`
  - Imports: `pydantic`
  - Imports: `pydantic_core`
  - Imports: `re`
  - Imports: `typing`
  - Imports: `typing_extensions`
  - Imports: `typing_inspection`
  - Imports: `warnings`
- **meridian_frontend/src-tauri/api/_internal/pydantic/_internal/_forward_ref.py**
  - Imports: `__future__`
  - Imports: `dataclasses`
  - Imports: `typing`
- **meridian_frontend/src-tauri/api/_internal/pydantic/_internal/_generate_schema.py**
  - Imports: `__future__`
  - Imports: `collections`
  - Imports: `contextlib`
  - Imports: `copy`
  - Imports: `dataclasses`
  - Imports: `datetime`
  - Imports: `decimal`
  - Imports: `enum`
  - Imports: `fractions`
  - Imports: `functools`
  - Imports: `inspect`
  - Imports: `ipaddress`
  - Imports: `itertools`
  - Imports: `operator`
  - Imports: `os`
  - Imports: `pathlib`
  - Imports: `pydantic`
  - Imports: `pydantic_core`
  - Imports: `re`
  - Imports: `sys`
  - Imports: `types`
  - Imports: `typing`
  - Imports: `typing_extensions`
  - Imports: `typing_inspection`
  - Imports: `uuid`
  - Imports: `warnings`
  - Imports: `zoneinfo`
- **meridian_frontend/src-tauri/api/_internal/pydantic/_internal/_generics.py**
  - Imports: `__future__`
  - Imports: `collections`
  - Imports: `contextlib`
  - Imports: `contextvars`
  - Imports: `functools`
  - Imports: `itertools`
  - Imports: `operator`
  - Imports: `pydantic`
  - Imports: `sys`
  - Imports: `types`
  - Imports: `typing`
  - Imports: `typing_extensions`
  - Imports: `typing_inspection`
  - Imports: `weakref`
- **meridian_frontend/src-tauri/api/_internal/pydantic/_internal/_git.py**
  - Imports: `__future__`
  - Imports: `pathlib`
  - Imports: `subprocess`
- **meridian_frontend/src-tauri/api/_internal/pydantic/_internal/_import_utils.py**
  - Imports: `functools`
  - Imports: `pydantic`
  - Imports: `typing`
- **meridian_frontend/src-tauri/api/_internal/pydantic/_internal/_internal_dataclass.py**
  - Imports: `sys`
- **meridian_frontend/src-tauri/api/_internal/pydantic/_internal/_known_annotated_metadata.py**
  - Imports: `__future__`
  - Imports: `annotated_types`
  - Imports: `collections`
  - Imports: `copy`
  - Imports: `functools`
  - Imports: `pydantic`
  - Imports: `pydantic_core`
  - Imports: `typing`
- **meridian_frontend/src-tauri/api/_internal/pydantic/_internal/_mock_val_ser.py**
  - Imports: `__future__`
  - Imports: `collections`
  - Imports: `pydantic_core`
  - Imports: `typing`
- **meridian_frontend/src-tauri/api/_internal/pydantic/_internal/_model_construction.py**
  - Imports: `__future__`
  - Imports: `abc`
  - Imports: `annotationlib`
  - Imports: `functools`
  - Imports: `operator`
  - Imports: `pydantic_core`
  - Imports: `sys`
  - Imports: `types`
  - Imports: `typing`
  - Imports: `typing_extensions`
  - Imports: `typing_inspection`
  - Imports: `warnings`
  - Imports: `weakref`
- **meridian_frontend/src-tauri/api/_internal/pydantic/_internal/_namespace_utils.py**
  - Imports: `__future__`
  - Imports: `collections`
  - Imports: `contextlib`
  - Imports: `functools`
  - Imports: `pydantic`
  - Imports: `sys`
  - Imports: `typing`
  - Imports: `typing_extensions`
- **meridian_frontend/src-tauri/api/_internal/pydantic/_internal/_repr.py**
  - Imports: `__future__`
  - Imports: `collections`
  - Imports: `types`
  - Imports: `typing`
  - Imports: `typing_extensions`
  - Imports: `typing_inspection`
- **meridian_frontend/src-tauri/api/_internal/pydantic/_internal/_schema_gather.py**
  - Imports: `__future__`
  - Imports: `dataclasses`
  - Imports: `pydantic_core`
  - Imports: `typing`
  - Imports: `typing_extensions`
- **meridian_frontend/src-tauri/api/_internal/pydantic/_internal/_schema_generation_shared.py**
  - Imports: `__future__`
  - Imports: `pydantic_core`
  - Imports: `typing`
- **meridian_frontend/src-tauri/api/_internal/pydantic/_internal/_serializers.py**
  - Imports: `__future__`
  - Imports: `collections`
  - Imports: `pydantic_core`
  - Imports: `typing`
- **meridian_frontend/src-tauri/api/_internal/pydantic/_internal/_signature.py**
  - Imports: `__future__`
  - Imports: `dataclasses`
  - Imports: `inspect`
  - Imports: `itertools`
  - Imports: `pydantic_core`
  - Imports: `typing`
- **meridian_frontend/src-tauri/api/_internal/pydantic/_internal/_typing_extra.py**
  - Imports: `__future__`
  - Imports: `annotationlib`
  - Imports: `collections`
  - Imports: `eval_type_backport`
  - Imports: `functools`
  - Imports: `inspect`
  - Imports: `pydantic`
  - Imports: `re`
  - Imports: `sys`
  - Imports: `types`
  - Imports: `typing`
  - Imports: `typing_extensions`
  - Imports: `typing_inspection`
- **meridian_frontend/src-tauri/api/_internal/pydantic/_internal/_utils.py**
  - Imports: `__future__`
  - Imports: `collections`
  - Imports: `copy`
  - Imports: `dataclasses`
  - Imports: `functools`
  - Imports: `inspect`
  - Imports: `itertools`
  - Imports: `keyword`
  - Imports: `pydantic`
  - Imports: `pydantic_core`
  - Imports: `sys`
  - Imports: `types`
  - Imports: `typing`
  - Imports: `typing_extensions`
  - Imports: `warnings`
  - Imports: `weakref`
- **meridian_frontend/src-tauri/api/_internal/pydantic/_internal/_validate_call.py**
  - Imports: `__future__`
  - Imports: `collections`
  - Imports: `functools`
  - Imports: `inspect`
  - Imports: `pydantic_core`
  - Imports: `typing`
- **meridian_frontend/src-tauri/api/_internal/pydantic/_internal/_validators.py**
  - Imports: `__future__`
  - Imports: `collections`
  - Imports: `decimal`
  - Imports: `fractions`
  - Imports: `importlib`
  - Imports: `ipaddress`
  - Imports: `math`
  - Imports: `pydantic`
  - Imports: `pydantic_core`
  - Imports: `re`
  - Imports: `typing`
  - Imports: `typing_extensions`
  - Imports: `typing_inspection`
  - Imports: `zoneinfo`
- **meridian_frontend/src-tauri/api/_internal/pydantic/_migration.py**
  - Imports: `pydantic`
  - Imports: `sys`
  - Imports: `typing`
  - Imports: `warnings`
- **meridian_frontend/src-tauri/api/_internal/pydantic/alias_generators.py**
  - Imports: `re`
- **meridian_frontend/src-tauri/api/_internal/pydantic/aliases.py**
  - Imports: `__future__`
  - Imports: `dataclasses`
  - Imports: `pydantic_core`
  - Imports: `typing`
- **meridian_frontend/src-tauri/api/_internal/pydantic/annotated_handlers.py**
  - Imports: `__future__`
  - Imports: `pydantic_core`
  - Imports: `typing`
- **meridian_frontend/src-tauri/api/_internal/pydantic/color.py**
  - Imports: `colorsys`
  - Imports: `math`
  - Imports: `pydantic_core`
  - Imports: `re`
  - Imports: `typing`
  - Imports: `typing_extensions`
- **meridian_frontend/src-tauri/api/_internal/pydantic/config.py**
  - Imports: `__future__`
  - Imports: `being`
  - Imports: `decimal`
  - Imports: `enum`
  - Imports: `pydantic`
  - Imports: `re`
  - Imports: `typing`
  - Imports: `typing_extensions`
  - Imports: `warnings`
- **meridian_frontend/src-tauri/api/_internal/pydantic/dataclasses.py**
  - Imports: `__future__`
  - Imports: `dataclasses`
  - Imports: `functools`
  - Imports: `sys`
  - Imports: `types`
  - Imports: `typing`
  - Imports: `typing_extensions`
  - Imports: `warnings`
- **meridian_frontend/src-tauri/api/_internal/pydantic/deprecated/class_validators.py**
  - Imports: `__future__`
  - Imports: ``fields``
  - Imports: `functools`
  - Imports: `types`
  - Imports: `typing`
  - Imports: `typing_extensions`
  - Imports: `warnings`
- **meridian_frontend/src-tauri/api/_internal/pydantic/deprecated/config.py**
  - Imports: `__future__`
  - Imports: `typing`
  - Imports: `typing_extensions`
  - Imports: `warnings`
- **meridian_frontend/src-tauri/api/_internal/pydantic/deprecated/copy_internals.py**
  - Imports: `__future__`
  - Imports: `copy`
  - Imports: `enum`
  - Imports: `typing`
  - Imports: `typing_extensions`
- **meridian_frontend/src-tauri/api/_internal/pydantic/deprecated/decorator.py**
  - Imports: `collections`
  - Imports: `functools`
  - Imports: `inspect`
  - Imports: `typing`
  - Imports: `typing_extensions`
  - Imports: `warnings`
- **meridian_frontend/src-tauri/api/_internal/pydantic/deprecated/json.py**
  - Imports: `collections`
  - Imports: `dataclasses`
  - Imports: `datetime`
  - Imports: `decimal`
  - Imports: `enum`
  - Imports: `ipaddress`
  - Imports: `pathlib`
  - Imports: `re`
  - Imports: `types`
  - Imports: `typing`
  - Imports: `typing_extensions`
  - Imports: `uuid`
  - Imports: `warnings`
- **meridian_frontend/src-tauri/api/_internal/pydantic/deprecated/parse.py**
  - Imports: `__future__`
  - Imports: `enum`
  - Imports: `json`
  - Imports: `pathlib`
  - Imports: `pickle`
  - Imports: `typing`
  - Imports: `typing_extensions`
  - Imports: `warnings`
- **meridian_frontend/src-tauri/api/_internal/pydantic/deprecated/tools.py**
  - Imports: `__future__`
  - Imports: `json`
  - Imports: `typing`
  - Imports: `typing_extensions`
  - Imports: `warnings`
- **meridian_frontend/src-tauri/api/_internal/pydantic/errors.py**
  - Imports: `__future__`
  - Imports: `pydantic`
  - Imports: `re`
  - Imports: `typing`
  - Imports: `typing_extensions`
  - Imports: `typing_inspection`
- **meridian_frontend/src-tauri/api/_internal/pydantic/experimental/arguments_schema.py**
  - Imports: `__future__`
  - Imports: `collections`
  - Imports: `pydantic`
  - Imports: `pydantic_core`
  - Imports: `the`
  - Imports: `typing`
- **meridian_frontend/src-tauri/api/_internal/pydantic/experimental/missing_sentinel.py**
  - Imports: `pydantic_core`
- **meridian_frontend/src-tauri/api/_internal/pydantic/experimental/pipeline.py**
  - Imports: `__future__`
  - Imports: `annotated_types`
  - Imports: `collections`
  - Imports: `dataclasses`
  - Imports: `datetime`
  - Imports: `decimal`
  - Imports: `functools`
  - Imports: `operator`
  - Imports: `pydantic`
  - Imports: `pydantic_core`
  - Imports: `re`
  - Imports: `sys`
  - Imports: `types`
  - Imports: `typing`
- **meridian_frontend/src-tauri/api/_internal/pydantic/fields.py**
  - Imports: `__future__`
  - Imports: `annotated_types`
  - Imports: `collections`
  - Imports: `copy`
  - Imports: `dataclasses`
  - Imports: `functools`
  - Imports: `inspect`
  - Imports: `pydantic`
  - Imports: `pydantic_core`
  - Imports: `random`
  - Imports: `re`
  - Imports: `sys`
  - Imports: `typing`
  - Imports: `typing_extensions`
  - Imports: `typing_inspection`
  - Imports: `warnings`
- **meridian_frontend/src-tauri/api/_internal/pydantic/functional_serializers.py**
  - Imports: `__future__`
  - Imports: `dataclasses`
  - Imports: `datetime`
  - Imports: `functools`
  - Imports: `pydantic`
  - Imports: `pydantic_core`
  - Imports: `typing`
  - Imports: `typing_extensions`
- **meridian_frontend/src-tauri/api/_internal/pydantic/functional_validators.py**
  - Imports: `__future__`
  - Imports: `dataclasses`
  - Imports: `datetime`
  - Imports: `functools`
  - Imports: `pydantic`
  - Imports: `pydantic_core`
  - Imports: `sys`
  - Imports: `typing`
  - Imports: `typing_extensions`
  - Imports: `warnings`
- **meridian_frontend/src-tauri/api/_internal/pydantic/json_schema.py**
  - Imports: `__future__`
  - Imports: `collections`
  - Imports: `copy`
  - Imports: `dataclasses`
  - Imports: `enum`
  - Imports: `inspect`
  - Imports: `math`
  - Imports: `os`
  - Imports: `pprint`
  - Imports: `pydantic`
  - Imports: `pydantic_core`
  - Imports: `re`
  - Imports: `the`
  - Imports: `typing`
  - Imports: `typing_extensions`
  - Imports: `typing_inspection`
  - Imports: `warnings`
- **meridian_frontend/src-tauri/api/_internal/pydantic/main.py**
  - Imports: `__future__`
  - Imports: `collections`
  - Imports: `copy`
  - Imports: `functools`
  - Imports: `inspect`
  - Imports: `json`
  - Imports: `operator`
  - Imports: `pathlib`
  - Imports: `pydantic`
  - Imports: `pydantic_core`
  - Imports: `sys`
  - Imports: `types`
  - Imports: `typing`
  - Imports: `typing_extensions`
  - Imports: `warnings`
- **meridian_frontend/src-tauri/api/_internal/pydantic/mypy.py**
  - Imports: `__future__`
  - Imports: `a`
  - Imports: `collections`
  - Imports: `configparser`
  - Imports: `mypy`
  - Imports: `pydantic`
  - Imports: `sys`
  - Imports: `tomli`
  - Imports: `tomllib`
  - Imports: `typing`
  - Imports: `warnings`
- **meridian_frontend/src-tauri/api/_internal/pydantic/networks.py**
  - Imports: `__future__`
  - Imports: `dataclasses`
  - Imports: `email_validator`
  - Imports: `functools`
  - Imports: `importlib`
  - Imports: `ipaddress`
  - Imports: `pydantic`
  - Imports: `pydantic_core`
  - Imports: `re`
  - Imports: `typing`
  - Imports: `typing_extensions`
- **meridian_frontend/src-tauri/api/_internal/pydantic/plugin/__init__.py**
  - Imports: `__future__`
  - Imports: `pydantic`
  - Imports: `pydantic_core`
  - Imports: `typing`
  - Imports: `typing_extensions`
- **meridian_frontend/src-tauri/api/_internal/pydantic/plugin/_loader.py**
  - Imports: `__future__`
  - Imports: `collections`
  - Imports: `importlib`
  - Imports: `os`
  - Imports: `typing`
  - Imports: `warnings`
- **meridian_frontend/src-tauri/api/_internal/pydantic/plugin/_schema_validator.py**
  - Imports: `__future__`
  - Imports: `collections`
  - Imports: `functools`
  - Imports: `pydantic_core`
  - Imports: `typing`
  - Imports: `typing_extensions`
- **meridian_frontend/src-tauri/api/_internal/pydantic/root_model.py**
  - Imports: `__future__`
  - Imports: `copy`
  - Imports: `pydantic_core`
  - Imports: `typing`
  - Imports: `typing_extensions`
- **meridian_frontend/src-tauri/api/_internal/pydantic/type_adapter.py**
  - Imports: `__future__`
  - Imports: `a`
  - Imports: `collections`
  - Imports: `dataclasses`
  - Imports: `pydantic`
  - Imports: `pydantic_core`
  - Imports: `sys`
  - Imports: `the`
  - Imports: `types`
  - Imports: `typing`
  - Imports: `typing_extensions`
- **meridian_frontend/src-tauri/api/_internal/pydantic/types.py**
  - Imports: `__future__`
  - Imports: `annotated_types`
  - Imports: `base64`
  - Imports: `collections`
  - Imports: `dataclasses`
  - Imports: `datetime`
  - Imports: `decimal`
  - Imports: `enum`
  - Imports: `json`
  - Imports: `math`
  - Imports: `pathlib`
  - Imports: `pydantic`
  - Imports: `pydantic_core`
  - Imports: `re`
  - Imports: `types`
  - Imports: `typing`
  - Imports: `typing_extensions`
  - Imports: `uuid`
- **meridian_frontend/src-tauri/api/_internal/pydantic/v1/__init__.py**
  - Imports: `pydantic`
- **meridian_frontend/src-tauri/api/_internal/pydantic/v1/_hypothesis_plugin.py**
  - Imports: `contextlib`
  - Imports: `datetime`
  - Imports: `email_validator`
  - Imports: `fractions`
  - Imports: `hypothesis`
  - Imports: `ipaddress`
  - Imports: `json`
  - Imports: `math`
  - Imports: `pydantic`
  - Imports: `typing`
- **meridian_frontend/src-tauri/api/_internal/pydantic/v1/annotated_types.py**
  - Imports: `pydantic`
  - Imports: `sys`
  - Imports: `typing`
  - Imports: `typing_extensions`
- **meridian_frontend/src-tauri/api/_internal/pydantic/v1/class_validators.py**
  - Imports: `collections`
  - Imports: `functools`
  - Imports: `inspect`
  - Imports: `itertools`
  - Imports: `pydantic`
  - Imports: `types`
  - Imports: `typing`
  - Imports: `warnings`
- **meridian_frontend/src-tauri/api/_internal/pydantic/v1/color.py**
  - Imports: `colorsys`
  - Imports: `math`
  - Imports: `pydantic`
  - Imports: `re`
  - Imports: `typing`
- **meridian_frontend/src-tauri/api/_internal/pydantic/v1/config.py**
  - Imports: `enum`
  - Imports: `json`
  - Imports: `pydantic`
  - Imports: `typing`
  - Imports: `typing_extensions`
- **meridian_frontend/src-tauri/api/_internal/pydantic/v1/dataclasses.py**
  - Imports: `contextlib`
  - Imports: `copy`
  - Imports: `dataclasses`
  - Imports: `functools`
  - Imports: `pydantic`
  - Imports: `sys`
  - Imports: `typing`
  - Imports: `typing_extensions`
- **meridian_frontend/src-tauri/api/_internal/pydantic/v1/datetime_parse.py**
  - Imports: `datetime`
  - Imports: `pydantic`
  - Imports: `re`
  - Imports: `typing`
- **meridian_frontend/src-tauri/api/_internal/pydantic/v1/decorator.py**
  - Imports: `functools`
  - Imports: `inspect`
  - Imports: `pydantic`
  - Imports: `typing`
- **meridian_frontend/src-tauri/api/_internal/pydantic/v1/env_settings.py**
  - Imports: `dotenv`
  - Imports: `os`
  - Imports: `pathlib`
  - Imports: `pydantic`
  - Imports: `typing`
  - Imports: `warnings`
- **meridian_frontend/src-tauri/api/_internal/pydantic/v1/error_wrappers.py**
  - Imports: `json`
  - Imports: `pydantic`
  - Imports: `typing`
  - Imports: `typing_extensions`
- **meridian_frontend/src-tauri/api/_internal/pydantic/v1/errors.py**
  - Imports: `decimal`
  - Imports: `pathlib`
  - Imports: `pydantic`
  - Imports: `typing`
- **meridian_frontend/src-tauri/api/_internal/pydantic/v1/fields.py**
  - Imports: `collections`
  - Imports: `copy`
  - Imports: `pydantic`
  - Imports: `re`
  - Imports: `typing`
  - Imports: `typing_extensions`
- **meridian_frontend/src-tauri/api/_internal/pydantic/v1/generics.py**
  - Imports: `functools`
  - Imports: `operator`
  - Imports: `pydantic`
  - Imports: `sys`
  - Imports: `types`
  - Imports: `typing`
  - Imports: `typing_extensions`
  - Imports: `weakref`
- **meridian_frontend/src-tauri/api/_internal/pydantic/v1/json.py**
  - Imports: `collections`
  - Imports: `dataclasses`
  - Imports: `datetime`
  - Imports: `decimal`
  - Imports: `enum`
  - Imports: `ipaddress`
  - Imports: `pathlib`
  - Imports: `pydantic`
  - Imports: `re`
  - Imports: `types`
  - Imports: `typing`
  - Imports: `uuid`
- **meridian_frontend/src-tauri/api/_internal/pydantic/v1/main.py**
  - Imports: `abc`
  - Imports: `annotationlib`
  - Imports: `copy`
  - Imports: `enum`
  - Imports: `functools`
  - Imports: `inspect`
  - Imports: `pathlib`
  - Imports: `pydantic`
  - Imports: `sys`
  - Imports: `types`
  - Imports: `typing`
  - Imports: `typing_extensions`
  - Imports: `warnings`
- **meridian_frontend/src-tauri/api/_internal/pydantic/v1/mypy.py**
  - Imports: `configparser`
  - Imports: `mypy`
  - Imports: `pydantic`
  - Imports: `sys`
  - Imports: `toml`
  - Imports: `tomli`
  - Imports: `tomllib`
  - Imports: `typing`
  - Imports: `warnings`
- **meridian_frontend/src-tauri/api/_internal/pydantic/v1/networks.py**
  - Imports: `email_validator`
  - Imports: `ipaddress`
  - Imports: `pydantic`
  - Imports: `re`
  - Imports: `typing`
  - Imports: `typing_extensions`
- **meridian_frontend/src-tauri/api/_internal/pydantic/v1/parse.py**
  - Imports: `enum`
  - Imports: `json`
  - Imports: `pathlib`
  - Imports: `pickle`
  - Imports: `pydantic`
  - Imports: `typing`
- **meridian_frontend/src-tauri/api/_internal/pydantic/v1/schema.py**
  - Imports: `collections`
  - Imports: `dataclasses`
  - Imports: `datetime`
  - Imports: `decimal`
  - Imports: `enum`
  - Imports: `inspect`
  - Imports: `ipaddress`
  - Imports: `pathlib`
  - Imports: `pydantic`
  - Imports: `re`
  - Imports: `typing`
  - Imports: `typing_extensions`
  - Imports: `uuid`
  - Imports: `warnings`
- **meridian_frontend/src-tauri/api/_internal/pydantic/v1/tools.py**
  - Imports: `functools`
  - Imports: `json`
  - Imports: `pathlib`
  - Imports: `pydantic`
  - Imports: `typing`
- **meridian_frontend/src-tauri/api/_internal/pydantic/v1/types.py**
  - Imports: `abc`
  - Imports: `datetime`
  - Imports: `decimal`
  - Imports: `enum`
  - Imports: `math`
  - Imports: `pathlib`
  - Imports: `pydantic`
  - Imports: `re`
  - Imports: `types`
  - Imports: `typing`
  - Imports: `typing_extensions`
  - Imports: `uuid`
  - Imports: `warnings`
  - Imports: `weakref`
- **meridian_frontend/src-tauri/api/_internal/pydantic/v1/typing.py**
  - Imports: `collections`
  - Imports: `functools`
  - Imports: `operator`
  - Imports: `os`
  - Imports: `pydantic`
  - Imports: `sys`
  - Imports: `types`
  - Imports: `typing`
  - Imports: `typing_extensions`
- **meridian_frontend/src-tauri/api/_internal/pydantic/v1/utils.py**
  - Imports: `collections`
  - Imports: `copy`
  - Imports: `importlib`
  - Imports: `inspect`
  - Imports: `itertools`
  - Imports: `keyword`
  - Imports: `pathlib`
  - Imports: `pydantic`
  - Imports: `types`
  - Imports: `typing`
  - Imports: `typing_extensions`
  - Imports: `warnings`
  - Imports: `weakref`
- **meridian_frontend/src-tauri/api/_internal/pydantic/v1/validators.py**
  - Imports: `collections`
  - Imports: `datetime`
  - Imports: `decimal`
  - Imports: `enum`
  - Imports: `ipaddress`
  - Imports: `math`
  - Imports: `pathlib`
  - Imports: `pydantic`
  - Imports: `re`
  - Imports: `typing`
  - Imports: `typing_extensions`
  - Imports: `uuid`
  - Imports: `warnings`
- **meridian_frontend/src-tauri/api/_internal/pydantic/v1/version.py**
  - Imports: `cython`
  - Imports: `importlib`
  - Imports: `pathlib`
  - Imports: `platform`
  - Imports: `sys`
- **meridian_frontend/src-tauri/api/_internal/pydantic/validate_call_decorator.py**
  - Imports: `__future__`
  - Imports: `functools`
  - Imports: `inspect`
  - Imports: `types`
  - Imports: `typing`
- **meridian_frontend/src-tauri/api/_internal/pydantic/version.py**
  - Imports: `__future__`
  - Imports: `importlib`
  - Imports: `pathlib`
  - Imports: `platform`
  - Imports: `pydantic_core`
  - Imports: `sys`
- **meridian_frontend/src-tauri/api/_internal/pydantic/warnings.py**
  - Imports: `__future__`
- **meridian_frontend/src-tauri/api/_internal/starlette/_exception_handler.py**
  - Imports: `__future__`
  - Imports: `starlette`
  - Imports: `typing`
- **meridian_frontend/src-tauri/api/_internal/starlette/_utils.py**
  - Imports: `__future__`
  - Imports: `anyio`
  - Imports: `asyncio`
  - Imports: `collections`
  - Imports: `contextlib`
  - Imports: `exceptiongroup`
  - Imports: `functools`
  - Imports: `inspect`
  - Imports: `starlette`
  - Imports: `sys`
  - Imports: `typing`
  - Imports: `typing_extensions`
- **meridian_frontend/src-tauri/api/_internal/starlette/applications.py**
  - Imports: `__future__`
  - Imports: `collections`
  - Imports: `starlette`
  - Imports: `typing`
- **meridian_frontend/src-tauri/api/_internal/starlette/authentication.py**
  - Imports: `__future__`
  - Imports: `collections`
  - Imports: `functools`
  - Imports: `inspect`
  - Imports: `starlette`
  - Imports: `typing`
  - Imports: `urllib`
- **meridian_frontend/src-tauri/api/_internal/starlette/background.py**
  - Imports: `__future__`
  - Imports: `collections`
  - Imports: `starlette`
  - Imports: `typing`
- **meridian_frontend/src-tauri/api/_internal/starlette/concurrency.py**
  - Imports: `__future__`
  - Imports: `anyio`
  - Imports: `collections`
  - Imports: `functools`
  - Imports: `starlette`
  - Imports: `typing`
  - Imports: `warnings`
- **meridian_frontend/src-tauri/api/_internal/starlette/config.py**
  - Imports: `__future__`
  - Imports: `collections`
  - Imports: `os`
  - Imports: `pathlib`
  - Imports: `typing`
  - Imports: `warnings`
- **meridian_frontend/src-tauri/api/_internal/starlette/convertors.py**
  - Imports: `__future__`
  - Imports: `math`
  - Imports: `typing`
  - Imports: `uuid`
- **meridian_frontend/src-tauri/api/_internal/starlette/datastructures.py**
  - Imports: `__future__`
  - Imports: `collections`
  - Imports: `re`
  - Imports: `shlex`
  - Imports: `starlette`
  - Imports: `typing`
  - Imports: `urllib`
- **meridian_frontend/src-tauri/api/_internal/starlette/endpoints.py**
  - Imports: `__future__`
  - Imports: `collections`
  - Imports: `json`
  - Imports: `starlette`
  - Imports: `typing`
- **meridian_frontend/src-tauri/api/_internal/starlette/exceptions.py**
  - Imports: `__future__`
  - Imports: `collections`
  - Imports: `http`
- **meridian_frontend/src-tauri/api/_internal/starlette/formparsers.py**
  - Imports: `__future__`
  - Imports: `collections`
  - Imports: `dataclasses`
  - Imports: `enum`
  - Imports: `multipart`
  - Imports: `python_multipart`
  - Imports: `starlette`
  - Imports: `tempfile`
  - Imports: `typing`
  - Imports: `urllib`
- **meridian_frontend/src-tauri/api/_internal/starlette/middleware/__init__.py**
  - Imports: `__future__`
  - Imports: `collections`
  - Imports: `typing`
- **meridian_frontend/src-tauri/api/_internal/starlette/middleware/authentication.py**
  - Imports: `__future__`
  - Imports: `collections`
  - Imports: `starlette`
- **meridian_frontend/src-tauri/api/_internal/starlette/middleware/base.py**
  - Imports: `__future__`
  - Imports: `anyio`
  - Imports: `collections`
  - Imports: `starlette`
  - Imports: `typing`
- **meridian_frontend/src-tauri/api/_internal/starlette/middleware/cors.py**
  - Imports: `__future__`
  - Imports: `collections`
  - Imports: `functools`
  - Imports: `re`
  - Imports: `starlette`
- **meridian_frontend/src-tauri/api/_internal/starlette/middleware/errors.py**
  - Imports: `__future__`
  - Imports: `html`
  - Imports: `inspect`
  - Imports: `starlette`
  - Imports: `sys`
  - Imports: `traceback`
- **meridian_frontend/src-tauri/api/_internal/starlette/middleware/exceptions.py**
  - Imports: `__future__`
  - Imports: `collections`
  - Imports: `starlette`
  - Imports: `typing`
- **meridian_frontend/src-tauri/api/_internal/starlette/middleware/gzip.py**
  - Imports: `gzip`
  - Imports: `io`
  - Imports: `starlette`
  - Imports: `typing`
- **meridian_frontend/src-tauri/api/_internal/starlette/middleware/httpsredirect.py**
  - Imports: `starlette`
- **meridian_frontend/src-tauri/api/_internal/starlette/middleware/sessions.py**
  - Imports: `__future__`
  - Imports: `base64`
  - Imports: `itsdangerous`
  - Imports: `json`
  - Imports: `starlette`
  - Imports: `typing`
- **meridian_frontend/src-tauri/api/_internal/starlette/middleware/trustedhost.py**
  - Imports: `__future__`
  - Imports: `collections`
  - Imports: `starlette`
- **meridian_frontend/src-tauri/api/_internal/starlette/middleware/wsgi.py**
  - Imports: `__future__`
  - Imports: `anyio`
  - Imports: `collections`
  - Imports: `io`
  - Imports: `math`
  - Imports: `starlette`
  - Imports: `sys`
  - Imports: `typing`
  - Imports: `warnings`
- **meridian_frontend/src-tauri/api/_internal/starlette/requests.py**
  - Imports: `__future__`
  - Imports: `anyio`
  - Imports: `collections`
  - Imports: `http`
  - Imports: `json`
  - Imports: `multipart`
  - Imports: `python_multipart`
  - Imports: `starlette`
  - Imports: `sys`
  - Imports: `typing`
  - Imports: `typing_extensions`
- **meridian_frontend/src-tauri/api/_internal/starlette/responses.py**
  - Imports: `__future__`
  - Imports: `anyio`
  - Imports: `collections`
  - Imports: `datetime`
  - Imports: `email`
  - Imports: `functools`
  - Imports: `hashlib`
  - Imports: `http`
  - Imports: `json`
  - Imports: `mimetypes`
  - Imports: `os`
  - Imports: `secrets`
  - Imports: `starlette`
  - Imports: `stat`
  - Imports: `sys`
  - Imports: `typing`
  - Imports: `urllib`
- **meridian_frontend/src-tauri/api/_internal/starlette/routing.py**
  - Imports: `__future__`
  - Imports: `collections`
  - Imports: `contextlib`
  - Imports: `enum`
  - Imports: `functools`
  - Imports: `inspect`
  - Imports: `re`
  - Imports: `starlette`
  - Imports: `traceback`
  - Imports: `types`
  - Imports: `typing`
  - Imports: `warnings`
- **meridian_frontend/src-tauri/api/_internal/starlette/schemas.py**
  - Imports: `__future__`
  - Imports: `collections`
  - Imports: `inspect`
  - Imports: `re`
  - Imports: `starlette`
  - Imports: `typing`
  - Imports: `yaml`
- **meridian_frontend/src-tauri/api/_internal/starlette/staticfiles.py**
  - Imports: `__future__`
  - Imports: `anyio`
  - Imports: `email`
  - Imports: `errno`
  - Imports: `importlib`
  - Imports: `os`
  - Imports: `starlette`
  - Imports: `stat`
  - Imports: `typing`
- **meridian_frontend/src-tauri/api/_internal/starlette/status.py**
  - Imports: `__future__`
  - Imports: `starlette`
  - Imports: `warnings`
- **meridian_frontend/src-tauri/api/_internal/starlette/templating.py**
  - Imports: `__future__`
  - Imports: `collections`
  - Imports: `jinja2`
  - Imports: `os`
  - Imports: `starlette`
  - Imports: `typing`
- **meridian_frontend/src-tauri/api/_internal/starlette/testclient.py**
  - Imports: `__future__`
  - Imports: `anyio`
  - Imports: `collections`
  - Imports: `concurrent`
  - Imports: `contextlib`
  - Imports: `httpx`
  - Imports: `httpx2`
  - Imports: `inspect`
  - Imports: `io`
  - Imports: `json`
  - Imports: `math`
  - Imports: `starlette`
  - Imports: `sys`
  - Imports: `types`
  - Imports: `typing`
  - Imports: `typing_extensions`
  - Imports: `urllib`
  - Imports: `warnings`
- **meridian_frontend/src-tauri/api/_internal/starlette/types.py**
  - Imports: `collections`
  - Imports: `contextlib`
  - Imports: `starlette`
  - Imports: `typing`
- **meridian_frontend/src-tauri/api/_internal/starlette/websockets.py**
  - Imports: `__future__`
  - Imports: `collections`
  - Imports: `enum`
  - Imports: `json`
  - Imports: `starlette`
  - Imports: `typing`
- **meridian_frontend/src-tauri/api/_internal/uvicorn/__init__.py**
  - Imports: `uvicorn`
- **meridian_frontend/src-tauri/api/_internal/uvicorn/__main__.py**
  - Imports: `uvicorn`
- **meridian_frontend/src-tauri/api/_internal/uvicorn/_compat.py**
  - Imports: `__future__`
  - Imports: `asyncio`
  - Imports: `collections`
  - Imports: `inspect`
  - Imports: `sys`
  - Imports: `typing`
- **meridian_frontend/src-tauri/api/_internal/uvicorn/_subprocess.py**
  - Imports: `__future__`
  - Imports: `collections`
  - Imports: `multiprocessing`
  - Imports: `os`
  - Imports: `socket`
  - Imports: `sys`
  - Imports: `uvicorn`
- **meridian_frontend/src-tauri/api/_internal/uvicorn/_types.py**
  - Imports: `__future__`
  - Imports: `collections`
  - Imports: `sys`
  - Imports: `types`
  - Imports: `typing`
  - Imports: `typing_extensions`
- **meridian_frontend/src-tauri/api/_internal/uvicorn/config.py**
  - Imports: `__future__`
  - Imports: `asyncio`
  - Imports: `click`
  - Imports: `collections`
  - Imports: `configparser`
  - Imports: `dotenv`
  - Imports: `inspect`
  - Imports: `json`
  - Imports: `logging`
  - Imports: `os`
  - Imports: `pathlib`
  - Imports: `socket`
  - Imports: `ssl`
  - Imports: `sys`
  - Imports: `typing`
  - Imports: `uvicorn`
  - Imports: `yaml`
- **meridian_frontend/src-tauri/api/_internal/uvicorn/importer.py**
  - Imports: `importlib`
  - Imports: `typing`
- **meridian_frontend/src-tauri/api/_internal/uvicorn/lifespan/off.py**
  - Imports: `__future__`
  - Imports: `typing`
  - Imports: `uvicorn`
- **meridian_frontend/src-tauri/api/_internal/uvicorn/lifespan/on.py**
  - Imports: `__future__`
  - Imports: `asyncio`
  - Imports: `logging`
  - Imports: `typing`
  - Imports: `uvicorn`
- **meridian_frontend/src-tauri/api/_internal/uvicorn/logging.py**
  - Imports: `__future__`
  - Imports: `click`
  - Imports: `copy`
  - Imports: `http`
  - Imports: `logging`
  - Imports: `sys`
  - Imports: `typing`
- **meridian_frontend/src-tauri/api/_internal/uvicorn/loops/asyncio.py**
  - Imports: `__future__`
  - Imports: `asyncio`
  - Imports: `collections`
  - Imports: `sys`
- **meridian_frontend/src-tauri/api/_internal/uvicorn/loops/auto.py**
  - Imports: `__future__`
  - Imports: `asyncio`
  - Imports: `collections`
  - Imports: `uvicorn`
  - Imports: `uvloop`
- **meridian_frontend/src-tauri/api/_internal/uvicorn/loops/uvloop.py**
  - Imports: `__future__`
  - Imports: `asyncio`
  - Imports: `collections`
  - Imports: `uvloop`
- **meridian_frontend/src-tauri/api/_internal/uvicorn/main.py**
  - Imports: `__future__`
  - Imports: `asyncio`
  - Imports: `click`
  - Imports: `collections`
  - Imports: `configparser`
  - Imports: `logging`
  - Imports: `os`
  - Imports: `platform`
  - Imports: `ssl`
  - Imports: `sys`
  - Imports: `typing`
  - Imports: `uvicorn`
  - Imports: `warnings`
- **meridian_frontend/src-tauri/api/_internal/uvicorn/middleware/asgi2.py**
  - Imports: `uvicorn`
- **meridian_frontend/src-tauri/api/_internal/uvicorn/middleware/message_logger.py**
  - Imports: `logging`
  - Imports: `typing`
  - Imports: `uvicorn`
- **meridian_frontend/src-tauri/api/_internal/uvicorn/middleware/proxy_headers.py**
  - Imports: `__future__`
  - Imports: `ipaddress`
  - Imports: `uvicorn`
- **meridian_frontend/src-tauri/api/_internal/uvicorn/middleware/wsgi.py**
  - Imports: `__future__`
  - Imports: `a2wsgi`
  - Imports: `asyncio`
  - Imports: `collections`
  - Imports: `concurrent`
  - Imports: `io`
  - Imports: `sys`
  - Imports: `uvicorn`
  - Imports: `warnings`
- **meridian_frontend/src-tauri/api/_internal/uvicorn/protocols/http/auto.py**
  - Imports: `__future__`
  - Imports: `asyncio`
  - Imports: `httptools`
  - Imports: `uvicorn`
- **meridian_frontend/src-tauri/api/_internal/uvicorn/protocols/http/flow_control.py**
  - Imports: `asyncio`
  - Imports: `uvicorn`
- **meridian_frontend/src-tauri/api/_internal/uvicorn/protocols/http/h11_impl.py**
  - Imports: `__future__`
  - Imports: `asyncio`
  - Imports: `collections`
  - Imports: `contextvars`
  - Imports: `h11`
  - Imports: `http`
  - Imports: `logging`
  - Imports: `sys`
  - Imports: `typing`
  - Imports: `urllib`
  - Imports: `uvicorn`
- **meridian_frontend/src-tauri/api/_internal/uvicorn/protocols/http/httptools_impl.py**
  - Imports: `__future__`
  - Imports: `asyncio`
  - Imports: `collections`
  - Imports: `contextvars`
  - Imports: `http`
  - Imports: `httptools`
  - Imports: `logging`
  - Imports: `re`
  - Imports: `sys`
  - Imports: `typing`
  - Imports: `urllib`
  - Imports: `uvicorn`
- **meridian_frontend/src-tauri/api/_internal/uvicorn/protocols/utils.py**
  - Imports: `__future__`
  - Imports: `asyncio`
  - Imports: `socket`
  - Imports: `urllib`
  - Imports: `uvicorn`
- **meridian_frontend/src-tauri/api/_internal/uvicorn/protocols/websockets/auto.py**
  - Imports: `__future__`
  - Imports: `asyncio`
  - Imports: `collections`
  - Imports: `uvicorn`
  - Imports: `websockets`
  - Imports: `wsproto`
- **meridian_frontend/src-tauri/api/_internal/uvicorn/protocols/websockets/websockets_impl.py**
  - Imports: `__future__`
  - Imports: `asyncio`
  - Imports: `collections`
  - Imports: `http`
  - Imports: `logging`
  - Imports: `typing`
  - Imports: `urllib`
  - Imports: `uvicorn`
  - Imports: `websockets`
- **meridian_frontend/src-tauri/api/_internal/uvicorn/protocols/websockets/websockets_sansio_impl.py**
  - Imports: `__future__`
  - Imports: `asyncio`
  - Imports: `http`
  - Imports: `logging`
  - Imports: `random`
  - Imports: `struct`
  - Imports: `sys`
  - Imports: `typing`
  - Imports: `typing_extensions`
  - Imports: `urllib`
  - Imports: `uvicorn`
  - Imports: `websockets`
- **meridian_frontend/src-tauri/api/_internal/uvicorn/protocols/websockets/wsproto_impl.py**
  - Imports: `__future__`
  - Imports: `asyncio`
  - Imports: `io`
  - Imports: `logging`
  - Imports: `random`
  - Imports: `struct`
  - Imports: `typing`
  - Imports: `urllib`
  - Imports: `uvicorn`
  - Imports: `wsproto`
- **meridian_frontend/src-tauri/api/_internal/uvicorn/server.py**
  - Imports: `__future__`
  - Imports: `asyncio`
  - Imports: `click`
  - Imports: `collections`
  - Imports: `contextlib`
  - Imports: `email`
  - Imports: `functools`
  - Imports: `logging`
  - Imports: `os`
  - Imports: `platform`
  - Imports: `random`
  - Imports: `signal`
  - Imports: `socket`
  - Imports: `sys`
  - Imports: `threading`
  - Imports: `time`
  - Imports: `types`
  - Imports: `typing`
  - Imports: `uvicorn`
- **meridian_frontend/src-tauri/api/_internal/uvicorn/supervisors/__init__.py**
  - Imports: `__future__`
  - Imports: `typing`
  - Imports: `uvicorn`
- **meridian_frontend/src-tauri/api/_internal/uvicorn/supervisors/basereload.py**
  - Imports: `__future__`
  - Imports: `click`
  - Imports: `collections`
  - Imports: `logging`
  - Imports: `os`
  - Imports: `pathlib`
  - Imports: `signal`
  - Imports: `socket`
  - Imports: `sys`
  - Imports: `threading`
  - Imports: `types`
  - Imports: `uvicorn`
- **meridian_frontend/src-tauri/api/_internal/uvicorn/supervisors/multiprocess.py**
  - Imports: `__future__`
  - Imports: `click`
  - Imports: `collections`
  - Imports: `logging`
  - Imports: `multiprocessing`
  - Imports: `os`
  - Imports: `signal`
  - Imports: `socket`
  - Imports: `threading`
  - Imports: `typing`
  - Imports: `uvicorn`
- **meridian_frontend/src-tauri/api/_internal/uvicorn/supervisors/statreload.py**
  - Imports: `__future__`
  - Imports: `collections`
  - Imports: `logging`
  - Imports: `pathlib`
  - Imports: `socket`
  - Imports: `uvicorn`
- **meridian_frontend/src-tauri/api/_internal/uvicorn/supervisors/watchfilesreload.py**
  - Imports: `__future__`
  - Imports: `collections`
  - Imports: `pathlib`
  - Imports: `socket`
  - Imports: `uvicorn`
  - Imports: `watchfiles`
- **meridian_frontend/src-tauri/api/_internal/uvicorn/workers.py**
  - Imports: `__future__`
  - Imports: `asyncio`
  - Imports: `gunicorn`
  - Imports: `logging`
  - Imports: `signal`
  - Imports: `sys`
  - Imports: `typing`
  - Imports: `uvicorn`
  - Imports: `warnings`
- **meridian_frontend/src-tauri/api/_internal/websockets/__init__.py**
  - Imports: `__future__`
  - Imports: `typing`
- **meridian_frontend/src-tauri/api/_internal/websockets/asyncio/client.py**
  - Imports: `__future__`
  - Imports: `asyncio`
  - Imports: `collections`
  - Imports: `logging`
  - Imports: `os`
  - Imports: `python_socks`
  - Imports: `socket`
  - Imports: `ssl`
  - Imports: `those`
  - Imports: `traceback`
  - Imports: `types`
  - Imports: `typing`
  - Imports: `urllib`
  - Imports: `websockets`
- **meridian_frontend/src-tauri/api/_internal/websockets/asyncio/connection.py**
  - Imports: `__future__`
  - Imports: `asyncio`
  - Imports: `collections`
  - Imports: `contextlib`
  - Imports: `logging`
  - Imports: `random`
  - Imports: `slow`
  - Imports: `struct`
  - Imports: `traceback`
  - Imports: `types`
  - Imports: `typing`
  - Imports: `uuid`
  - Imports: `weakref`
- **meridian_frontend/src-tauri/api/_internal/websockets/asyncio/messages.py**
  - Imports: `__future__`
  - Imports: `asyncio`
  - Imports: `codecs`
  - Imports: `collections`
  - Imports: `typing`
- **meridian_frontend/src-tauri/api/_internal/websockets/asyncio/router.py**
  - Imports: `__future__`
  - Imports: `http`
  - Imports: `ssl`
  - Imports: `typing`
  - Imports: `urllib`
  - Imports: `websockets`
  - Imports: `werkzeug`
- **meridian_frontend/src-tauri/api/_internal/websockets/asyncio/server.py**
  - Imports: `__future__`
  - Imports: `asyncio`
  - Imports: `collections`
  - Imports: `hmac`
  - Imports: `http`
  - Imports: `logging`
  - Imports: `re`
  - Imports: `socket`
  - Imports: `types`
  - Imports: `typing`
  - Imports: `websockets`
- **meridian_frontend/src-tauri/api/_internal/websockets/auth.py**
  - Imports: `__future__`
  - Imports: `warnings`
- **meridian_frontend/src-tauri/api/_internal/websockets/cli.py**
  - Imports: `__future__`
  - Imports: `argparse`
  - Imports: `asyncio`
  - Imports: `itertools`
  - Imports: `os`
  - Imports: `readline`
  - Imports: `ssl`
  - Imports: `sys`
  - Imports: `threading`
  - Imports: `typing`
- **meridian_frontend/src-tauri/api/_internal/websockets/client.py**
  - Imports: `__future__`
  - Imports: `collections`
  - Imports: `os`
  - Imports: `random`
  - Imports: `typing`
  - Imports: `warnings`
- **meridian_frontend/src-tauri/api/_internal/websockets/connection.py**
  - Imports: `__future__`
  - Imports: `warnings`
- **meridian_frontend/src-tauri/api/_internal/websockets/datastructures.py**
  - Imports: `__future__`
  - Imports: `collections`
  - Imports: `re`
  - Imports: `typing`
- **meridian_frontend/src-tauri/api/_internal/websockets/exceptions.py**
  - Imports: `__future__`
  - Imports: `warnings`
- **meridian_frontend/src-tauri/api/_internal/websockets/extensions/base.py**
  - Imports: `__future__`
  - Imports: `collections`
- **meridian_frontend/src-tauri/api/_internal/websockets/extensions/permessage_deflate.py**
  - Imports: `__future__`
  - Imports: `collections`
  - Imports: `typing`
  - Imports: `zlib`
- **meridian_frontend/src-tauri/api/_internal/websockets/frames.py**
  - Imports: `__future__`
  - Imports: `collections`
  - Imports: `dataclasses`
  - Imports: `enum`
  - Imports: `io`
  - Imports: `os`
  - Imports: `secrets`
  - Imports: `struct`
  - Imports: `typing`
- **meridian_frontend/src-tauri/api/_internal/websockets/headers.py**
  - Imports: `__future__`
  - Imports: `base64`
  - Imports: `binascii`
  - Imports: `collections`
  - Imports: `ipaddress`
  - Imports: `re`
  - Imports: `typing`
- **meridian_frontend/src-tauri/api/_internal/websockets/http11.py**
  - Imports: `__future__`
  - Imports: `collections`
  - Imports: `dataclasses`
  - Imports: `os`
  - Imports: `re`
  - Imports: `sys`
  - Imports: `the`
  - Imports: `typing`
  - Imports: `warnings`
- **meridian_frontend/src-tauri/api/_internal/websockets/imports.py**
  - Imports: `__future__`
  - Imports: `collections`
  - Imports: `typing`
  - Imports: `warnings`
- **meridian_frontend/src-tauri/api/_internal/websockets/legacy/__init__.py**
  - Imports: `__future__`
  - Imports: `warnings`
- **meridian_frontend/src-tauri/api/_internal/websockets/legacy/auth.py**
  - Imports: `__future__`
  - Imports: `collections`
  - Imports: `functools`
  - Imports: `hmac`
  - Imports: `http`
  - Imports: `typing`
- **meridian_frontend/src-tauri/api/_internal/websockets/legacy/client.py**
  - Imports: `__future__`
  - Imports: `asyncio`
  - Imports: `collections`
  - Imports: `functools`
  - Imports: `logging`
  - Imports: `os`
  - Imports: `random`
  - Imports: `traceback`
  - Imports: `types`
  - Imports: `typing`
  - Imports: `urllib`
  - Imports: `warnings`
- **meridian_frontend/src-tauri/api/_internal/websockets/legacy/exceptions.py**
  - Imports: `http`
- **meridian_frontend/src-tauri/api/_internal/websockets/legacy/framing.py**
  - Imports: `__future__`
  - Imports: `collections`
  - Imports: `struct`
  - Imports: `typing`
- **meridian_frontend/src-tauri/api/_internal/websockets/legacy/handshake.py**
  - Imports: `__future__`
  - Imports: `base64`
  - Imports: `binascii`
- **meridian_frontend/src-tauri/api/_internal/websockets/legacy/http.py**
  - Imports: `__future__`
  - Imports: `asyncio`
  - Imports: `os`
  - Imports: `re`
- **meridian_frontend/src-tauri/api/_internal/websockets/legacy/protocol.py**
  - Imports: `__future__`
  - Imports: `asyncio`
  - Imports: `codecs`
  - Imports: `collections`
  - Imports: `logging`
  - Imports: `random`
  - Imports: `slow`
  - Imports: `ssl`
  - Imports: `struct`
  - Imports: `time`
  - Imports: `traceback`
  - Imports: `typing`
  - Imports: `uuid`
  - Imports: `warnings`
  - Imports: `weakref`
- **meridian_frontend/src-tauri/api/_internal/websockets/legacy/server.py**
  - Imports: `__future__`
  - Imports: `asyncio`
  - Imports: `collections`
  - Imports: `email`
  - Imports: `functools`
  - Imports: `http`
  - Imports: `inspect`
  - Imports: `logging`
  - Imports: `shutting`
  - Imports: `socket`
  - Imports: `types`
  - Imports: `typing`
  - Imports: `warnings`
- **meridian_frontend/src-tauri/api/_internal/websockets/protocol.py**
  - Imports: `__future__`
  - Imports: `collections`
  - Imports: `enum`
  - Imports: `logging`
  - Imports: `uuid`
- **meridian_frontend/src-tauri/api/_internal/websockets/proxy.py**
  - Imports: `__future__`
  - Imports: `dataclasses`
  - Imports: `urllib`
- **meridian_frontend/src-tauri/api/_internal/websockets/server.py**
  - Imports: `__future__`
  - Imports: `base64`
  - Imports: `binascii`
  - Imports: `collections`
  - Imports: `email`
  - Imports: `http`
  - Imports: `re`
  - Imports: `typing`
  - Imports: `warnings`
- **meridian_frontend/src-tauri/api/_internal/websockets/streams.py**
  - Imports: `__future__`
  - Imports: `collections`
- **meridian_frontend/src-tauri/api/_internal/websockets/sync/client.py**
  - Imports: `__future__`
  - Imports: ```uri```
  - Imports: `collections`
  - Imports: `logging`
  - Imports: `os`
  - Imports: `python_socks`
  - Imports: `socket`
  - Imports: `ssl`
  - Imports: `threading`
  - Imports: `time`
  - Imports: `traceback`
  - Imports: `types`
  - Imports: `typing`
  - Imports: `urllib`
  - Imports: `warnings`
  - Imports: `websockets`
- **meridian_frontend/src-tauri/api/_internal/websockets/sync/connection.py**
  - Imports: `__future__`
  - Imports: `collections`
  - Imports: `concurrent`
  - Imports: `contextlib`
  - Imports: `logging`
  - Imports: `random`
  - Imports: `socket`
  - Imports: `struct`
  - Imports: `threading`
  - Imports: `time`
  - Imports: `traceback`
  - Imports: `types`
  - Imports: `typing`
  - Imports: `uuid`
  - Imports: `weakref`
- **meridian_frontend/src-tauri/api/_internal/websockets/sync/messages.py**
  - Imports: `__future__`
  - Imports: `codecs`
  - Imports: `queue`
  - Imports: `threading`
  - Imports: `typing`
- **meridian_frontend/src-tauri/api/_internal/websockets/sync/router.py**
  - Imports: `__future__`
  - Imports: `http`
  - Imports: `ssl`
  - Imports: `typing`
  - Imports: `urllib`
  - Imports: `websockets`
  - Imports: `werkzeug`
- **meridian_frontend/src-tauri/api/_internal/websockets/sync/server.py**
  - Imports: `__future__`
  - Imports: `another`
  - Imports: `collections`
  - Imports: `concurrent`
  - Imports: `hmac`
  - Imports: `http`
  - Imports: `logging`
  - Imports: `os`
  - Imports: `re`
  - Imports: `selectors`
  - Imports: `socket`
  - Imports: `ssl`
  - Imports: `sys`
  - Imports: `threading`
  - Imports: `time`
  - Imports: `types`
  - Imports: `typing`
  - Imports: `warnings`
  - Imports: `websockets`
- **meridian_frontend/src-tauri/api/_internal/websockets/sync/utils.py**
  - Imports: `__future__`
  - Imports: `time`
- **meridian_frontend/src-tauri/api/_internal/websockets/trio/client.py**
  - Imports: `__future__`
  - Imports: ```uri```
  - Imports: `collections`
  - Imports: `logging`
  - Imports: `os`
  - Imports: `python_socks`
  - Imports: `ssl`
  - Imports: `traceback`
  - Imports: `trio`
  - Imports: `types`
  - Imports: `typing`
  - Imports: `urllib`
  - Imports: `websockets`
- **meridian_frontend/src-tauri/api/_internal/websockets/trio/connection.py**
  - Imports: `__future__`
  - Imports: `collections`
  - Imports: `contextlib`
  - Imports: `logging`
  - Imports: `random`
  - Imports: `struct`
  - Imports: `traceback`
  - Imports: `trio`
  - Imports: `types`
  - Imports: `typing`
  - Imports: `uuid`
  - Imports: `weakref`
- **meridian_frontend/src-tauri/api/_internal/websockets/trio/messages.py**
  - Imports: `__future__`
  - Imports: `codecs`
  - Imports: `collections`
  - Imports: `math`
  - Imports: `trio`
  - Imports: `typing`
- **meridian_frontend/src-tauri/api/_internal/websockets/trio/router.py**
  - Imports: `__future__`
  - Imports: `http`
  - Imports: `ssl`
  - Imports: `trio`
  - Imports: `typing`
  - Imports: `urllib`
  - Imports: `websockets`
  - Imports: `werkzeug`
- **meridian_frontend/src-tauri/api/_internal/websockets/trio/server.py**
  - Imports: `__future__`
  - Imports: `collections`
  - Imports: `functools`
  - Imports: `http`
  - Imports: `logging`
  - Imports: `re`
  - Imports: `ssl`
  - Imports: `trio`
  - Imports: `types`
  - Imports: `typing`
  - Imports: `websockets`
- **meridian_frontend/src-tauri/api/_internal/websockets/trio/utils.py**
  - Imports: `trio`
- **meridian_frontend/src-tauri/api/_internal/websockets/typing.py**
  - Imports: `__future__`
  - Imports: `http`
  - Imports: `logging`
  - Imports: `os`
  - Imports: `typing`
- **meridian_frontend/src-tauri/api/_internal/websockets/uri.py**
  - Imports: `__future__`
  - Imports: `dataclasses`
  - Imports: `urllib`
- **meridian_frontend/src-tauri/api/_internal/websockets/utils.py**
  - Imports: `__future__`
  - Imports: `base64`
  - Imports: `hashlib`
  - Imports: `secrets`
  - Imports: `socket`
  - Imports: `sys`
- **meridian_frontend/src-tauri/api/_internal/websockets/version.py**
  - Imports: `__future__`
  - Imports: `importlib`
  - Imports: `pathlib`
  - Imports: `re`
  - Imports: `subprocess`
- **meridian_frontend/src/AppContext.tsx**
  - Imports: `config`
  - Imports: `core`
  - Imports: `event`
  - Imports: `react`
  - Imports: `types`
- **meridian_frontend/src/Mascot.tsx**
  - Imports: `AppContext`
  - Imports: `config`
  - Imports: `core`
  - Imports: `event`
  - Imports: `react`
  - Imports: `streamingAudioPlayer`
  - Imports: `window`
- **meridian_frontend/src/Mascot3DCharacter.tsx**
  - Imports: `animejs`
  - Imports: `react`
  - Imports: `three`
- **meridian_frontend/src/MobileApp.tsx**
  - Imports: `DropdownNav`
  - Imports: `LiveThoughtCarousel`
  - Imports: `VoiceOrbHUD`
  - Imports: `lucide-react`
  - Imports: `react`
- **meridian_frontend/src/components/AgentStatusStream.tsx**
  - Imports: `config`
  - Imports: `lucide-react`
  - Imports: `react`
- **meridian_frontend/src/components/CommandPalette.tsx**
  - Imports: `lucide-react`
  - Imports: `react`
- **meridian_frontend/src/components/DevAutomationPanel.tsx**
  - Imports: `config`
  - Imports: `lucide-react`
  - Imports: `react`
- **meridian_frontend/src/components/DeveloperSuitePanel.tsx**
  - Imports: `config`
  - Imports: `lucide-react`
  - Imports: `react`
- **meridian_frontend/src/components/LocalModelManager.tsx**
  - Imports: `ToastContext`
  - Imports: `config`
  - Imports: `lucide-react`
  - Imports: `react`
- **meridian_frontend/src/components/MemoryConsolidationView.tsx**
  - Imports: `config`
  - Imports: `lucide-react`
  - Imports: `react`
- **meridian_frontend/src/components/NavRail.tsx**
  - Imports: `AppContext`
  - Imports: `Mascot`
  - Imports: `core`
  - Imports: `react`
  - Imports: `window`
- **meridian_frontend/src/components/PerceptionHUD.tsx**
  - Imports: `lucide-react`
  - Imports: `react`
- **meridian_frontend/src/components/ProactiveGuardBanner.tsx**
  - Imports: `config`
  - Imports: `event`
  - Imports: `lucide-react`
  - Imports: `react`
- **meridian_frontend/src/components/ProfileHeader.tsx**
  - Imports: `react`
- **meridian_frontend/src/components/RightDrawer.tsx**
  - Imports: `AppContext`
  - Imports: `DataBadge`
  - Imports: `ProgressArc`
  - Imports: `lucide-react`
  - Imports: `react`
- **meridian_frontend/src/components/ServerConnectionModal.tsx**
  - Imports: `config`
  - Imports: `react`
- **meridian_frontend/src/components/Shell.tsx**
  - Imports: `AmbientParticles`
  - Imports: `AppContext`
  - Imports: `Clipboard`
  - Imports: `CommandPalette`
  - Imports: `ConnectionBanner`
  - Imports: `Jobs`
  - Imports: `NavRail`
  - Imports: `ProactiveGuardBanner`
  - Imports: `Productivity`
  - Imports: `RightDrawer`
  - Imports: `StatusBar`
  - Imports: `Timeline`
  - Imports: `ToastContext`
  - Imports: `react`
- **meridian_frontend/src/components/StatusBar.tsx**
  - Imports: `AppContext`
  - Imports: `MobilePairingModal`
  - Imports: `config`
  - Imports: `lucide-react`
  - Imports: `react`
- **meridian_frontend/src/components/mobile/DropdownNav.tsx**
  - Imports: `lucide-react`
  - Imports: `react`
- **meridian_frontend/src/components/mobile/LiveThoughtCarousel.tsx**
  - Imports: `lucide-react`
  - Imports: `react`
- **meridian_frontend/src/components/mobile/MobilePairingModal.tsx**
  - Imports: `config`
  - Imports: `lucide-react`
  - Imports: `react`
- **meridian_frontend/src/components/mobile/VoiceOrbHUD.tsx**
  - Imports: `lucide-react`
  - Imports: `react`
- **meridian_frontend/src/components/ui/AmbientParticles.tsx**
  - Imports: `react`
  - Imports: `useMemoryOptimizer`
- **meridian_frontend/src/components/ui/CodeDiffViewer.tsx**
  - Imports: `lucide-react`
  - Imports: `react`
- **meridian_frontend/src/components/ui/ConnectionBanner.tsx**
  - Imports: `AppContext`
  - Imports: `config`
  - Imports: `lucide-react`
  - Imports: `react`
- **meridian_frontend/src/components/ui/DataBadge.tsx**
  - Imports: `react`
- **meridian_frontend/src/components/ui/GlowCard.tsx**
  - Imports: `react`
- **meridian_frontend/src/components/ui/HoloButton.tsx**
  - Imports: `lucide-react`
  - Imports: `react`
- **meridian_frontend/src/components/ui/ProgressArc.tsx**
  - Imports: `react`
- **meridian_frontend/src/components/ui/TerminalLine.tsx**
  - Imports: `react`
- **meridian_frontend/src/components/ui/ToastContext.tsx**
  - Imports: `lucide-react`
  - Imports: `react`
- **meridian_frontend/src/hooks/useMemoryOptimizer.ts**
  - Imports: `react`
- **meridian_frontend/src/main.tsx**
  - Imports: `AppContext`
  - Imports: `BackendSetup`
  - Imports: `BootSequence`
  - Imports: `OnboardingWizard`
  - Imports: `SetupWizard`
  - Imports: `Shell`
  - Imports: `client`
  - Imports: `config`
  - Imports: `core`
  - Imports: `index.css`
  - Imports: `react`
- **meridian_frontend/src/services/oauthService.ts**
  - Imports: `config`
- **meridian_frontend/src/services/streamingAudioPlayer.ts**
  - Imports: `config`
- **meridian_frontend/src/startup/BackendSetup.tsx**
  - Imports: `config`
  - Imports: `core`
  - Imports: `lucide-react`
  - Imports: `react`
- **meridian_frontend/src/startup/BootSequence.tsx**
  - Imports: `Mascot`
  - Imports: `config`
  - Imports: `react`
- **meridian_frontend/src/startup/OnboardingWizard.tsx**
  - Imports: `config`
  - Imports: `react`
- **meridian_frontend/src/startup/SetupWizard.tsx**
  - Imports: `HoloButton`
  - Imports: `config`
  - Imports: `keyLock`
  - Imports: `lucide-react`
  - Imports: `react`
- **meridian_frontend/src/views/Clipboard.tsx**
  - Imports: `AppContext`
  - Imports: `HoloButton`
  - Imports: `config`
  - Imports: `lucide-react`
  - Imports: `react`
  - Imports: `types`
- **meridian_frontend/src/views/Jobs.tsx**
  - Imports: `GlowCard`
  - Imports: `HoloButton`
  - Imports: `config`
  - Imports: `lucide-react`
  - Imports: `react`
  - Imports: `types`
- **meridian_frontend/src/views/MemoryEditor.tsx**
  - Imports: `config`
  - Imports: `lucide-react`
  - Imports: `react`
- **meridian_frontend/src/views/Productivity.tsx**
  - Imports: `AgentStatusStream`
  - Imports: `DevAutomationPanel`
  - Imports: `DeveloperSuitePanel`
  - Imports: `GlowCard`
  - Imports: `HoloButton`
  - Imports: `LocalModelManager`
  - Imports: `MemoryConsolidationView`
  - Imports: `ProgressArc`
  - Imports: `config`
  - Imports: `lucide-react`
  - Imports: `react`
  - Imports: `types`
- **meridian_frontend/src/views/Settings.tsx**
  - Imports: `AiModelsTab`
  - Imports: `AppContext`
  - Imports: `GlowCard`
  - Imports: `HoloButton`
  - Imports: `IntegrationsTab`
  - Imports: `MascotTab`
  - Imports: `MultiModeTab`
  - Imports: `PasswordInput`
  - Imports: `ProgressArc`
  - Imports: `SpendAirGapTab`
  - Imports: `SystemGuardTab`
  - Imports: `VoiceTab`
  - Imports: `config`
  - Imports: `core`
  - Imports: `event`
  - Imports: `lucide-react`
  - Imports: `react`
  - Imports: `types`
  - Imports: `useMemoryOptimizer`
- **meridian_frontend/src/views/SwarmDebate.tsx**
  - Imports: `HoloButton`
  - Imports: `TerminalLine`
  - Imports: `config`
  - Imports: `lucide-react`
  - Imports: `react`
- **meridian_frontend/src/views/Timeline.tsx**
  - Imports: `CodeDiffViewer`
  - Imports: `GlowCard`
  - Imports: `HoloButton`
  - Imports: `config`
  - Imports: `core`
  - Imports: `dompurify`
  - Imports: `event`
  - Imports: `lucide-react`
  - Imports: `marked`
  - Imports: `react`
  - Imports: `streamingAudioPlayer`
  - Imports: `types`
- **meridian_frontend/src/views/WorkflowBuilder.tsx**
  - Imports: `config`
  - Imports: `react`
- **meridian_frontend/src/views/settings/AiModelsTab.tsx**
  - Imports: `GlowCard`
  - Imports: `HoloButton`
  - Imports: `PasswordInput`
  - Imports: `lucide-react`
  - Imports: `react`
- **meridian_frontend/src/views/settings/IntegrationsTab.tsx**
  - Imports: `GlowCard`
  - Imports: `HoloButton`
  - Imports: `PasswordInput`
  - Imports: `config`
  - Imports: `lucide-react`
  - Imports: `react`
- **meridian_frontend/src/views/settings/MascotTab.tsx**
  - Imports: `GlowCard`
  - Imports: `lucide-react`
  - Imports: `react`
- **meridian_frontend/src/views/settings/MultiModeTab.tsx**
  - Imports: `GlowCard`
  - Imports: `HoloButton`
  - Imports: `config`
  - Imports: `react`
- **meridian_frontend/src/views/settings/PasswordInput.tsx**
  - Imports: `lucide-react`
  - Imports: `react`
- **meridian_frontend/src/views/settings/SpendAirGapTab.tsx**
  - Imports: `GlowCard`
  - Imports: `HoloButton`
  - Imports: `react`
- **meridian_frontend/src/views/settings/SystemGuardTab.tsx**
  - Imports: `GlowCard`
  - Imports: `HoloButton`
  - Imports: `lucide-react`
  - Imports: `react`
- **meridian_frontend/src/views/settings/VoiceTab.tsx**
  - Imports: `GlowCard`
  - Imports: `HoloButton`
  - Imports: `lucide-react`
  - Imports: `react`
- **meridian_frontend/vite.config.ts**
  - Imports: `path`
  - Imports: `plugin-react`
  - Imports: `url`
  - Imports: `vite`
- **meridian_mobile/build_apk.py**
  - Imports: `os`
  - Imports: `subprocess`
  - Imports: `sys`
- **meridian_mobile/ios/Flutter/ephemeral/flutter_lldb_helper.py**
  - Imports: `lldb`
- **plugins/get_system_platform_info.py**
  - Imports: `platform`
- **setup_db.py**
  - Imports: `os`
  - Imports: `sqlite3`
- **setup_startup.py**
  - Imports: `os`
  - Imports: `platform`
  - Imports: `subprocess`
  - Imports: `sys`
- **verify_system.py**
  - Imports: `httpx`
  - Imports: `os`
  - Imports: `platform`
  - Imports: `pyaudio`
  - Imports: `pymongo`
  - Imports: `socket`
  - Imports: `sounddevice`
  - Imports: `sqlite3`
  - Imports: `subprocess`
  - Imports: `sys`