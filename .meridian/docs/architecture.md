# Workspace Architecture & Component Map
Generated automatically by Meridian-X.

## Component Dependency Graph
```mermaid
graph TD
    N1["build_mobile.py []"]
    N2["build_standalone.py []"]
    N3["bump_version.py []"]
    N4["main.py []"]
    N5["setup_db.py []"]
    N6["setup_startup.py []"]
    N7["verify_system.py []"]
    N8["analyze_music_cues.py [.agents/skills/brag/scripts]"]
    N9["config.py [generated_repos/attention_is_all_you_need__transformer_]"]
    N10["dataset.py [generated_repos/attention_is_all_you_need__transformer_]"]
    N11["model.py [generated_repos/attention_is_all_you_need__transformer_]"]
    N12["trainer.py [generated_repos/attention_is_all_you_need__transformer_]"]
    N13["api.py [meridian_backend]"]
    N14["database.py [meridian_backend]"]
    N15["mobile_bridge_service.py [meridian_backend]"]
    N16["tests_run.py [meridian_backend]"]
    N17["ProfileHeader.tsx [meridian_backend/meridian_frontend/src/components]"]
    N18["__init__.py [meridian_backend/src]"]
    N19["automation.py [meridian_backend/src/api]"]
    N20["chat.py [meridian_backend/src/api]"]
    N21["deps.py [meridian_backend/src/api]"]
    N22["mcp.py [meridian_backend/src/api]"]
    N23["models_mgmt.py [meridian_backend/src/api]"]
    N24["perception.py [meridian_backend/src/api]"]
    N25["profile.py [meridian_backend/src/api]"]
    N26["rag.py [meridian_backend/src/api]"]
    N27["scheduler.py [meridian_backend/src/api]"]
    N28["swarm.py [meridian_backend/src/api]"]
    N29["system.py [meridian_backend/src/api]"]
    N30["vault.py [meridian_backend/src/api]"]
    N31["voice.py [meridian_backend/src/api]"]
    N32["workspace.py [meridian_backend/src/api]"]
    N33["__init__.py [meridian_backend/src/api]"]
    N34["action_journal.py [meridian_backend/src/core]"]
    N35["agent_status_stream.py [meridian_backend/src/core]"]
    N36["ar_bridge.py [meridian_backend/src/core]"]
    N37["atomic_storage.py [meridian_backend/src/core]"]
    N38["audit_logger.py [meridian_backend/src/core]"]
    N39["auth.py [meridian_backend/src/core]"]
    N40["behavior_monitor.py [meridian_backend/src/core]"]
    N41["boilerplate_genie.py [meridian_backend/src/core]"]
    N42["breach_sentinel.py [meridian_backend/src/core]"]
    N43["bus.py [meridian_backend/src/core]"]
    N44["camera_sentinel.py [meridian_backend/src/core]"]
    N45["checkpoints.py [meridian_backend/src/core]"]
    N46["clipboard.py [meridian_backend/src/core]"]
    N47["code_graph.py [meridian_backend/src/core]"]
    N48["cognitive_graph.py [meridian_backend/src/core]"]
    N49["commit_whisperer.py [meridian_backend/src/core]"]
    N50["config.py [meridian_backend/src/core]"]
    N51["confirmations.py [meridian_backend/src/core]"]
    N52["consensus_engine.py [meridian_backend/src/core]"]
    N53["deep_project_context.py [meridian_backend/src/core]"]
    N54["dev_automation.py [meridian_backend/src/core]"]
    N55["discord_bridge.py [meridian_backend/src/core]"]
    N56["discord_utils.py [meridian_backend/src/core]"]
    N57["doc_generator.py [meridian_backend/src/core]"]
    N58["doc_indexer.py [meridian_backend/src/core]"]
    N59["elevated_runner.py [meridian_backend/src/core]"]
    N60["emergency_lockdown.py [meridian_backend/src/core]"]
    N61["experiment_runner.py [meridian_backend/src/core]"]
    N62["explain_code_engine.py [meridian_backend/src/core]"]
    N63["exporter.py [meridian_backend/src/core]"]
    N64["fim_sentinel.py [meridian_backend/src/core]"]
    N65["gaze_tracker.py [meridian_backend/src/core]"]
    N66["governor.py [meridian_backend/src/core]"]
    N67["graph_rag.py [meridian_backend/src/core]"]
    N68["graph_sync.py [meridian_backend/src/core]"]
    N69["hardware_detector.py [meridian_backend/src/core]"]
    N70["history_manager.py [meridian_backend/src/core]"]
    N71["llm_auth.py [meridian_backend/src/core]"]
    N72["llm_client.py [meridian_backend/src/core]"]
    N73["llm_clients.py [meridian_backend/src/core]"]
    N74["llm_provider.py [meridian_backend/src/core]"]
    N75["local_model_manager.py [meridian_backend/src/core]"]
    N76["logger.py [meridian_backend/src/core]"]
    N77["logging_config.py [meridian_backend/src/core]"]
    N78["loop.py [meridian_backend/src/core]"]
    N79["loop_dispatcher.py [meridian_backend/src/core]"]
    N80["loop_executor.py [meridian_backend/src/core]"]
    N81["loop_parser.py [meridian_backend/src/core]"]
    N82["loop_planning.py [meridian_backend/src/core]"]
    N83["loop_stream.py [meridian_backend/src/core]"]
    N84["lsp_client.py [meridian_backend/src/core]"]
    N85["malware_scanner.py [meridian_backend/src/core]"]
    N86["mcp_client.py [meridian_backend/src/core]"]
    N87["mcp_executor.py [meridian_backend/src/core]"]
    N88["memory_backup.py [meridian_backend/src/core]"]
    N89["memory_consolidation.py [meridian_backend/src/core]"]
    N90["memory_editor.py [meridian_backend/src/core]"]
    N91["mobile_bridge.py [meridian_backend/src/core]"]
    N92["mode.py [meridian_backend/src/core]"]
    N93["neural_rag.py [meridian_backend/src/core]"]
    N94["oauth_manager.py [meridian_backend/src/core]"]
    N95["ollama_manager.py [meridian_backend/src/core]"]
    N96["p2p.py [meridian_backend/src/core]"]
    N97["p2p_crypto.py [meridian_backend/src/core]"]
    N98["p2p_discovery.py [meridian_backend/src/core]"]
    N99["p2p_pairing.py [meridian_backend/src/core]"]
    N100["perception.py [meridian_backend/src/core]"]
    N101["persistence_sentinel.py [meridian_backend/src/core]"]
    N102["personal_crm.py [meridian_backend/src/core]"]
    N103["plugins.py [meridian_backend/src/core]"]
    N104["polyglot.py [meridian_backend/src/core]"]
    N105["predictive_engine.py [meridian_backend/src/core]"]
    N106["presence_briefing.py [meridian_backend/src/core]"]
    N107["proactive_system_guard.py [meridian_backend/src/core]"]
    N108["prompt_injection.py [meridian_backend/src/core]"]
    N109["prompt_templates.py [meridian_backend/src/core]"]
    N110["rag_optimizer.py [meridian_backend/src/core]"]
    N111["response_models.py [meridian_backend/src/core]"]
    N112["sandbox_runner.py [meridian_backend/src/core]"]
    N113["scheduler.py [meridian_backend/src/core]"]
    N114["screen_sense.py [meridian_backend/src/core]"]
    N115["security_middleware.py [meridian_backend/src/core]"]
    N116["self_evolving_tooling.py [meridian_backend/src/core]"]
    N117["silent_workflow_guardian.py [meridian_backend/src/core]"]
    N118["skills_loader.py [meridian_backend/src/core]"]
    N119["sos_protocol.py [meridian_backend/src/core]"]
    N120["speculative.py [meridian_backend/src/core]"]
    N121["swarm.py [meridian_backend/src/core]"]
    N122["system_defense.py [meridian_backend/src/core]"]
    N123["telegram_bridge.py [meridian_backend/src/core]"]
    N124["temporal_memory.py [meridian_backend/src/core]"]
    N125["tool_regression_sentinel.py [meridian_backend/src/core]"]
    N126["triggers.py [meridian_backend/src/core]"]
    N127["updater.py [meridian_backend/src/core]"]
    N128["vault.py [meridian_backend/src/core]"]
    N129["vision.py [meridian_backend/src/core]"]
    N130["vision_face.py [meridian_backend/src/core]"]
    N131["vision_gesture.py [meridian_backend/src/core]"]
    N132["watcher.py [meridian_backend/src/core]"]
    N133["what_broke_detective.py [meridian_backend/src/core]"]
    N134["workflow_engine.py [meridian_backend/src/core]"]
    N135["workspace_orchestrator.py [meridian_backend/src/core]"]
    N136["commits.py [meridian_backend/src/core/proactive]"]
    N137["dispatcher.py [meridian_backend/src/core/proactive]"]
    N138["ergonomics.py [meridian_backend/src/core/proactive]"]
    N139["guard.py [meridian_backend/src/core/proactive]"]
    N140["__init__.py [meridian_backend/src/core/proactive]"]
    N141["cache.py [meridian_backend/src/db]"]
    N142["connection.py [meridian_backend/src/db]"]
    N143["contacts.py [meridian_backend/src/db]"]
    N144["conversations.py [meridian_backend/src/db]"]
    N145["embeddings.py [meridian_backend/src/db]"]
    N146["logs.py [meridian_backend/src/db]"]
    N147["memory.py [meridian_backend/src/db]"]
    N148["parsers.py [meridian_backend/src/db]"]
    N149["profile.py [meridian_backend/src/db]"]
    N150["rag.py [meridian_backend/src/db]"]
    N151["vectors.py [meridian_backend/src/db]"]
    N152["__init__.py [meridian_backend/src/db]"]
    N153["auto_reviewer.py [meridian_backend/src/tools]"]
    N154["bill_radar.py [meridian_backend/src/tools]"]
    N155["bookmark_manager.py [meridian_backend/src/tools]"]
    N156["browser_agent.py [meridian_backend/src/tools]"]
    N157["browser_use_agent.py [meridian_backend/src/tools]"]
    N158["cam_guard.py [meridian_backend/src/tools]"]
    N159["chrome_manager.py [meridian_backend/src/tools]"]
    N160["clipboard.py [meridian_backend/src/tools]"]
    N161["communication.py [meridian_backend/src/tools]"]
    N162["db_query.py [meridian_backend/src/tools]"]
    N163["desktop.py [meridian_backend/src/tools]"]
    N164["detonation_sandbox.py [meridian_backend/src/tools]"]
    N165["developer.py [meridian_backend/src/tools]"]
    N166["dns_shield.py [meridian_backend/src/tools]"]
    N167["documents.py [meridian_backend/src/tools]"]
    N168["documents_office.py [meridian_backend/src/tools]"]
    N169["documents_slides.py [meridian_backend/src/tools]"]
    N170["dynamic_manager.py [meridian_backend/src/tools]"]
    N171["expiry_sentinel.py [meridian_backend/src/tools]"]
    N172["exporter.py [meridian_backend/src/tools]"]
    N173["external_connectors.py [meridian_backend/src/tools]"]
    N174["filesystem.py [meridian_backend/src/tools]"]
    N175["file_janitor.py [meridian_backend/src/tools]"]
    N176["finance_sentinel.py [meridian_backend/src/tools]"]
    N177["geo_location.py [meridian_backend/src/tools]"]
    N178["health_ingest.py [meridian_backend/src/tools]"]
    N179["household.py [meridian_backend/src/tools]"]
    N180["knowledge.py [meridian_backend/src/tools]"]
    N181["learning_queue.py [meridian_backend/src/tools]"]
    N182["mcp_marketplace.py [meridian_backend/src/tools]"]
    N183["network_guardian.py [meridian_backend/src/tools]"]
    N184["networth_tracker.py [meridian_backend/src/tools]"]
    N185["ollama_manager.py [meridian_backend/src/tools]"]
    N186["papercoder.py [meridian_backend/src/tools]"]
    N187["password_auditor.py [meridian_backend/src/tools]"]
    N188["phishing_guard.py [meridian_backend/src/tools]"]
    N189["phone_agent.py [meridian_backend/src/tools]"]
    N190["price_watcher.py [meridian_backend/src/tools]"]
    N191["recording.py [meridian_backend/src/tools]"]
    N192["registry.py [meridian_backend/src/tools]"]
    N193["review.py [meridian_backend/src/tools]"]
    N194["scheduler.py [meridian_backend/src/tools]"]
    N195["screenshot_memory.py [meridian_backend/src/tools]"]
    N196["search_hub.py [meridian_backend/src/tools]"]
    N197["security_auditor.py [meridian_backend/src/tools]"]
    N198["shell.py [meridian_backend/src/tools]"]
    N199["system.py [meridian_backend/src/tools]"]
    N200["system_windows.py [meridian_backend/src/tools]"]
    N201["task_scheduler.py [meridian_backend/src/tools]"]
    N202["totp_generator.py [meridian_backend/src/tools]"]
    N203["travel_butler.py [meridian_backend/src/tools]"]
    N204["usb_watchdog.py [meridian_backend/src/tools]"]
    N205["vault.py [meridian_backend/src/tools]"]
    N206["video_editor.py [meridian_backend/src/tools]"]
    N207["voice.py [meridian_backend/src/tools]"]
    N208["watcher.py [meridian_backend/src/tools]"]
    N209["web.py [meridian_backend/src/tools]"]
    N210["web_browser.py [meridian_backend/src/tools]"]
    N211["web_scraper.py [meridian_backend/src/tools]"]
    N212["wellness.py [meridian_backend/src/tools]"]
    N213["whatsapp_manager.py [meridian_backend/src/tools]"]
    N214["wifi_assessor.py [meridian_backend/src/tools]"]
    N215["workspace_layout.py [meridian_backend/src/tools]"]
    N216["ambient_listener.py [meridian_backend/src/voice]"]
    N217["duplex.py [meridian_backend/src/voice]"]
    N218["polyglot.py [meridian_backend/src/voice]"]
    N219["stt.py [meridian_backend/src/voice]"]
    N220["tts.py [meridian_backend/src/voice]"]
    N221["vad.py [meridian_backend/src/voice]"]
    N222["voice_biometrics.py [meridian_backend/src/voice]"]
    N223["wakeword.py [meridian_backend/src/voice]"]
    N224["conftest.py [meridian_backend/tests]"]
    N225["run_tests.py [meridian_backend/tests]"]
    N226["test_advanced_proactive.py [meridian_backend/tests]"]
    N227["test_atomic_storage.py [meridian_backend/tests]"]
    N228["test_audit_bugfixes.py [meridian_backend/tests]"]
    N229["test_audit_remediation.py [meridian_backend/tests]"]
    N230["test_auto_bug_fixer.py [meridian_backend/tests]"]
    N231["test_backend_improvements.py [meridian_backend/tests]"]
    N232["test_backlog_features.py [meridian_backend/tests]"]
    N233["test_backlog_sprint.py [meridian_backend/tests]"]
    N234["test_bridges.py [meridian_backend/tests]"]
    N235["test_browser_agent.py [meridian_backend/tests]"]
    N236["test_browser_fallback.py [meridian_backend/tests]"]
    N237["test_browser_frame.py [meridian_backend/tests]"]
    N238["test_browser_use.py [meridian_backend/tests]"]
    N239["test_butler_media.py [meridian_backend/tests]"]
    N240["test_chat_abort.py [meridian_backend/tests]"]
    N241["test_cognitive_graph.py [meridian_backend/tests]"]
    N242["test_config.py [meridian_backend/tests]"]
    N243["test_consensus_gate.py [meridian_backend/tests]"]
    N244["test_context_budget.py [meridian_backend/tests]"]
    N245["test_custom_password_auth.py [meridian_backend/tests]"]
    N246["test_database.py [meridian_backend/tests]"]
    N247["test_day10_features.py [meridian_backend/tests]"]
    N248["test_day11_features.py [meridian_backend/tests]"]
    N249["test_day12_features.py [meridian_backend/tests]"]
    N250["test_day13_features.py [meridian_backend/tests]"]
    N251["test_day14_day15_features.py [meridian_backend/tests]"]
    N252["test_day16_17_18_features.py [meridian_backend/tests]"]
    N253["test_day3_features.py [meridian_backend/tests]"]
    N254["test_day4_features.py [meridian_backend/tests]"]
    N255["test_day5_features.py [meridian_backend/tests]"]
    N256["test_day6_features.py [meridian_backend/tests]"]
    N257["test_day7_features.py [meridian_backend/tests]"]
    N258["test_day8_features.py [meridian_backend/tests]"]
    N259["test_day9_features.py [meridian_backend/tests]"]
    N260["test_dev_intelligence_suite.py [meridian_backend/tests]"]
    N261["test_document_tools.py [meridian_backend/tests]"]
    N262["test_exhaustive_fallback.py [meridian_backend/tests]"]
    N263["test_full_proactive_suite.py [meridian_backend/tests]"]
    N264["test_geo_location.py [meridian_backend/tests]"]
    N265["test_hybrid_rag.py [meridian_backend/tests]"]
    N266["test_jarvis_perception.py [meridian_backend/tests]"]
    N267["test_known_errors_remediation.py [meridian_backend/tests]"]
    N268["test_llm_provider.py [meridian_backend/tests]"]
    N269["test_logging.py [meridian_backend/tests]"]
    N270["test_loop_parser.py [meridian_backend/tests]"]
    N271["test_loop_submodules.py [meridian_backend/tests]"]
    N272["test_mobile_websocket.py [meridian_backend/tests]"]
    N273["test_model_source.py [meridian_backend/tests]"]
    N274["test_multimode_routing.py [meridian_backend/tests]"]
    N275["test_multi_os.py [meridian_backend/tests]"]
    N276["test_new_features.py [meridian_backend/tests]"]
    N277["test_oauth.py [meridian_backend/tests]"]
    N278["test_p2p.py [meridian_backend/tests]"]
    N279["test_perception_bridge.py [meridian_backend/tests]"]
    N280["test_proactive.py [meridian_backend/tests]"]
    N281["test_proactive_mode.py [meridian_backend/tests]"]
    N282["test_proactive_notifications.py [meridian_backend/tests]"]
    N283["test_research_optimization.py [meridian_backend/tests]"]
    N284["test_response_resilience.py [meridian_backend/tests]"]
    N285["test_security_features.py [meridian_backend/tests]"]
    N286["test_silero_vad.py [meridian_backend/tests]"]
    N287["test_skill_packs.py [meridian_backend/tests]"]
    N288["test_sprint24_hardening.py [meridian_backend/tests]"]
    N289["test_sprint25_hardening.py [meridian_backend/tests]"]
    N290["test_sprint27_hardening.py [meridian_backend/tests]"]
    N291["test_sprint28_hardening.py [meridian_backend/tests]"]
    N292["test_sprint2_features.py [meridian_backend/tests]"]
    N293["test_standalone_bridge.py [meridian_backend/tests]"]
    N294["test_stream_resiliency.py [meridian_backend/tests]"]
    N295["test_swarm.py [meridian_backend/tests]"]
    N296["test_swarm_routing.py [meridian_backend/tests]"]
    N297["test_system_hardening.py [meridian_backend/tests]"]
    N298["test_tools.py [meridian_backend/tests]"]
    N299["test_tool_modernization.py [meridian_backend/tests]"]
    N300["test_tool_regression.py [meridian_backend/tests]"]
    N301["test_vault.py [meridian_backend/tests]"]
    N302["test_video_editor.py [meridian_backend/tests]"]
    N303["test_voice_hardening.py [meridian_backend/tests]"]
    N304["test_voice_speed.py [meridian_backend/tests]"]
    N305["test_wakeword_continuous.py [meridian_backend/tests]"]
    N306["test_wakeword_onnx.py [meridian_backend/tests]"]
    N307["test_web_guards.py [meridian_backend/tests]"]
    N308["test_workflow.py [meridian_backend/tests]"]
    N309["vite.config.ts [meridian_frontend]"]
    N310["AppContext.tsx [meridian_frontend/src]"]
    N311["main.tsx [meridian_frontend/src]"]
    N312["Mascot.tsx [meridian_frontend/src]"]
    N313["Mascot3DCharacter.tsx [meridian_frontend/src]"]
    N314["MobileApp.tsx [meridian_frontend/src]"]
    N315["AgentStatusStream.tsx [meridian_frontend/src/components]"]
    N316["CommandPalette.tsx [meridian_frontend/src/components]"]
    N317["DevAutomationPanel.tsx [meridian_frontend/src/components]"]
    N318["DeveloperSuitePanel.tsx [meridian_frontend/src/components]"]
    N319["LocalModelManager.tsx [meridian_frontend/src/components]"]
    N320["MemoryConsolidationView.tsx [meridian_frontend/src/components]"]
    N321["NavRail.tsx [meridian_frontend/src/components]"]
    N322["PerceptionHUD.tsx [meridian_frontend/src/components]"]
    N323["ProactiveGuardBanner.tsx [meridian_frontend/src/components]"]
    N324["ProfileHeader.tsx [meridian_frontend/src/components]"]
    N325["RightDrawer.tsx [meridian_frontend/src/components]"]
    N326["ServerConnectionModal.tsx [meridian_frontend/src/components]"]
    N327["Shell.tsx [meridian_frontend/src/components]"]
    N328["StatusBar.tsx [meridian_frontend/src/components]"]
    N329["DropdownNav.tsx [meridian_frontend/src/components/mobile]"]
    N330["LiveThoughtCarousel.tsx [meridian_frontend/src/components/mobile]"]
    N331["VoiceOrbHUD.tsx [meridian_frontend/src/components/mobile]"]
    N332["AmbientParticles.tsx [meridian_frontend/src/components/ui]"]
    N333["CodeDiffViewer.tsx [meridian_frontend/src/components/ui]"]
    N334["DataBadge.tsx [meridian_frontend/src/components/ui]"]
    N335["GlowCard.tsx [meridian_frontend/src/components/ui]"]
    N336["HoloButton.tsx [meridian_frontend/src/components/ui]"]
    N337["ProgressArc.tsx [meridian_frontend/src/components/ui]"]
    N338["TerminalLine.tsx [meridian_frontend/src/components/ui]"]
    N339["ToastContext.tsx [meridian_frontend/src/components/ui]"]
    N340["useMemoryOptimizer.ts [meridian_frontend/src/hooks]"]
    N341["oauthService.ts [meridian_frontend/src/services]"]
    N342["streamingAudioPlayer.ts [meridian_frontend/src/services]"]
    N343["BackendSetup.tsx [meridian_frontend/src/startup]"]
    N344["BootSequence.tsx [meridian_frontend/src/startup]"]
    N345["OnboardingWizard.tsx [meridian_frontend/src/startup]"]
    N346["SetupWizard.tsx [meridian_frontend/src/startup]"]
    N347["Clipboard.tsx [meridian_frontend/src/views]"]
    N348["Jobs.tsx [meridian_frontend/src/views]"]
    N349["MemoryEditor.tsx [meridian_frontend/src/views]"]
    N350["Productivity.tsx [meridian_frontend/src/views]"]
    N351["Settings.tsx [meridian_frontend/src/views]"]
    N352["SwarmDebate.tsx [meridian_frontend/src/views]"]
    N353["Timeline.tsx [meridian_frontend/src/views]"]
    N354["WorkflowBuilder.tsx [meridian_frontend/src/views]"]
    N355["AiModelsTab.tsx [meridian_frontend/src/views/settings]"]
    N356["IntegrationsTab.tsx [meridian_frontend/src/views/settings]"]
    N357["MascotTab.tsx [meridian_frontend/src/views/settings]"]
    N358["MultiModeTab.tsx [meridian_frontend/src/views/settings]"]
    N359["PasswordInput.tsx [meridian_frontend/src/views/settings]"]
    N360["SpendAirGapTab.tsx [meridian_frontend/src/views/settings]"]
    N361["SystemGuardTab.tsx [meridian_frontend/src/views/settings]"]
    N362["VoiceTab.tsx [meridian_frontend/src/views/settings]"]
    N363["config.py [meridian_frontend/src-tauri/api/_internal/cv2]"]
    N364["load_config_py3.py [meridian_frontend/src-tauri/api/_internal/cv2]"]
    N365["__init__.py [meridian_frontend/src-tauri/api/_internal/cv2]"]
    N366["__init__.py [meridian_frontend/src-tauri/api/_internal/cv2/data]"]
    N367["__init__.py [meridian_frontend/src-tauri/api/_internal/cv2/mat_wrapper]"]
    N368["version.py [meridian_frontend/src-tauri/api/_internal/cv2/misc]"]
    N369["__init__.py [meridian_frontend/src-tauri/api/_internal/cv2/typing]"]
    N370["__init__.py [meridian_frontend/src-tauri/api/_internal/cv2/utils]"]
    N371["applications.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N372["background.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N373["cli.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N374["concurrency.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N375["datastructures.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N376["encoders.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N377["exceptions.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N378["exception_handlers.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N379["logger.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N380["params.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N381["param_functions.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N382["requests.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N383["responses.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N384["routing.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N385["sse.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N386["staticfiles.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N387["templating.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N388["testclient.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N389["types.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N390["utils.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N391["websockets.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N392["__init__.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N393["__main__.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N394["models.py [meridian_frontend/src-tauri/api/_internal/fastapi/dependencies]"]
    N395["utils.py [meridian_frontend/src-tauri/api/_internal/fastapi/dependencies]"]
    N396["asyncexitstack.py [meridian_frontend/src-tauri/api/_internal/fastapi/middleware]"]
    N397["cors.py [meridian_frontend/src-tauri/api/_internal/fastapi/middleware]"]
    N398["gzip.py [meridian_frontend/src-tauri/api/_internal/fastapi/middleware]"]
    N399["httpsredirect.py [meridian_frontend/src-tauri/api/_internal/fastapi/middleware]"]
    N400["trustedhost.py [meridian_frontend/src-tauri/api/_internal/fastapi/middleware]"]
    N401["wsgi.py [meridian_frontend/src-tauri/api/_internal/fastapi/middleware]"]
    N402["__init__.py [meridian_frontend/src-tauri/api/_internal/fastapi/middleware]"]
    N403["docs.py [meridian_frontend/src-tauri/api/_internal/fastapi/openapi]"]
    N404["models.py [meridian_frontend/src-tauri/api/_internal/fastapi/openapi]"]
    N405["utils.py [meridian_frontend/src-tauri/api/_internal/fastapi/openapi]"]
    N406["api_key.py [meridian_frontend/src-tauri/api/_internal/fastapi/security]"]
    N407["base.py [meridian_frontend/src-tauri/api/_internal/fastapi/security]"]
    N408["http.py [meridian_frontend/src-tauri/api/_internal/fastapi/security]"]
    N409["oauth2.py [meridian_frontend/src-tauri/api/_internal/fastapi/security]"]
    N410["open_id_connect_url.py [meridian_frontend/src-tauri/api/_internal/fastapi/security]"]
    N411["shared.py [meridian_frontend/src-tauri/api/_internal/fastapi/_compat]"]
    N412["v2.py [meridian_frontend/src-tauri/api/_internal/fastapi/_compat]"]
    N413["coreBundle.js [meridian_frontend/src-tauri/api/_internal/playwright/driver/package/lib]"]
    N414["utilsBundle.js [meridian_frontend/src-tauri/api/_internal/playwright/driver/package/lib]"]
    N415["structs.d.ts [meridian_frontend/src-tauri/api/_internal/playwright/driver/package/types]"]
    N416["types.d.ts [meridian_frontend/src-tauri/api/_internal/playwright/driver/package/types]"]
    N417["aliases.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N418["alias_generators.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N419["annotated_handlers.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N420["color.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N421["config.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N422["dataclasses.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N423["errors.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N424["fields.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N425["functional_serializers.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N426["functional_validators.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N427["json_schema.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N428["main.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N429["mypy.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N430["networks.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N431["root_model.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N432["types.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N433["type_adapter.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N434["validate_call_decorator.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N435["version.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N436["warnings.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N437["_migration.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N438["__init__.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N439["class_validators.py [meridian_frontend/src-tauri/api/_internal/pydantic/deprecated]"]
    N440["config.py [meridian_frontend/src-tauri/api/_internal/pydantic/deprecated]"]
    N441["copy_internals.py [meridian_frontend/src-tauri/api/_internal/pydantic/deprecated]"]
    N442["decorator.py [meridian_frontend/src-tauri/api/_internal/pydantic/deprecated]"]
    N443["json.py [meridian_frontend/src-tauri/api/_internal/pydantic/deprecated]"]
    N444["parse.py [meridian_frontend/src-tauri/api/_internal/pydantic/deprecated]"]
    N445["tools.py [meridian_frontend/src-tauri/api/_internal/pydantic/deprecated]"]
    N446["arguments_schema.py [meridian_frontend/src-tauri/api/_internal/pydantic/experimental]"]
    N447["missing_sentinel.py [meridian_frontend/src-tauri/api/_internal/pydantic/experimental]"]
    N448["pipeline.py [meridian_frontend/src-tauri/api/_internal/pydantic/experimental]"]
    N449["_loader.py [meridian_frontend/src-tauri/api/_internal/pydantic/plugin]"]
    N450["_schema_validator.py [meridian_frontend/src-tauri/api/_internal/pydantic/plugin]"]
    N451["__init__.py [meridian_frontend/src-tauri/api/_internal/pydantic/plugin]"]
    N452["annotated_types.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N453["class_validators.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N454["color.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N455["config.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N456["dataclasses.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N457["datetime_parse.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N458["decorator.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N459["env_settings.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N460["errors.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N461["error_wrappers.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N462["fields.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N463["generics.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N464["json.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N465["main.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N466["mypy.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N467["networks.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N468["parse.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N469["schema.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N470["tools.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N471["types.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N472["typing.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N473["utils.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N474["validators.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N475["version.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N476["_hypothesis_plugin.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N477["__init__.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N478["_config.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N479["_core_metadata.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N480["_core_utils.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N481["_dataclasses.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N482["_decorators.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N483["_decorators_v1.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N484["_discriminated_union.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N485["_docs_extraction.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N486["_fields.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N487["_forward_ref.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N488["_generate_schema.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N489["_generics.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N490["_git.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N491["_import_utils.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N492["_internal_dataclass.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N493["_known_annotated_metadata.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N494["_mock_val_ser.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N495["_model_construction.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N496["_namespace_utils.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N497["_repr.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N498["_schema_gather.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N499["_schema_generation_shared.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N500["_serializers.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N501["_signature.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N502["_typing_extra.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N503["_utils.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N504["_validate_call.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N505["_validators.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N506["applications.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N507["authentication.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N508["background.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N509["concurrency.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N510["config.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N511["convertors.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N512["datastructures.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N513["endpoints.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N514["exceptions.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N515["formparsers.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N516["requests.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N517["responses.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N518["routing.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N519["schemas.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N520["staticfiles.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N521["status.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N522["templating.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N523["testclient.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N524["types.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N525["websockets.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N526["_exception_handler.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N527["_utils.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N528["authentication.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N529["base.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N530["cors.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N531["errors.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N532["exceptions.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N533["gzip.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N534["httpsredirect.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N535["sessions.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N536["trustedhost.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N537["wsgi.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N538["__init__.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N539["config.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N540["importer.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N541["logging.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N542["main.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N543["server.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N544["workers.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N545["_compat.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N546["_subprocess.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N547["_types.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N548["__init__.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N549["__main__.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N550["off.py [meridian_frontend/src-tauri/api/_internal/uvicorn/lifespan]"]
    N551["on.py [meridian_frontend/src-tauri/api/_internal/uvicorn/lifespan]"]
    N552["asyncio.py [meridian_frontend/src-tauri/api/_internal/uvicorn/loops]"]
    N553["auto.py [meridian_frontend/src-tauri/api/_internal/uvicorn/loops]"]
    N554["uvloop.py [meridian_frontend/src-tauri/api/_internal/uvicorn/loops]"]
    N555["asgi2.py [meridian_frontend/src-tauri/api/_internal/uvicorn/middleware]"]
    N556["message_logger.py [meridian_frontend/src-tauri/api/_internal/uvicorn/middleware]"]
    N557["proxy_headers.py [meridian_frontend/src-tauri/api/_internal/uvicorn/middleware]"]
    N558["wsgi.py [meridian_frontend/src-tauri/api/_internal/uvicorn/middleware]"]
    N559["utils.py [meridian_frontend/src-tauri/api/_internal/uvicorn/protocols]"]
    N560["auto.py [meridian_frontend/src-tauri/api/_internal/uvicorn/protocols/http]"]
    N561["flow_control.py [meridian_frontend/src-tauri/api/_internal/uvicorn/protocols/http]"]
    N562["h11_impl.py [meridian_frontend/src-tauri/api/_internal/uvicorn/protocols/http]"]
    N563["httptools_impl.py [meridian_frontend/src-tauri/api/_internal/uvicorn/protocols/http]"]
    N564["auto.py [meridian_frontend/src-tauri/api/_internal/uvicorn/protocols/websockets]"]
    N565["websockets_impl.py [meridian_frontend/src-tauri/api/_internal/uvicorn/protocols/websockets]"]
    N566["websockets_sansio_impl.py [meridian_frontend/src-tauri/api/_internal/uvicorn/protocols/websockets]"]
    N567["wsproto_impl.py [meridian_frontend/src-tauri/api/_internal/uvicorn/protocols/websockets]"]
    N568["basereload.py [meridian_frontend/src-tauri/api/_internal/uvicorn/supervisors]"]
    N569["multiprocess.py [meridian_frontend/src-tauri/api/_internal/uvicorn/supervisors]"]
    N570["statreload.py [meridian_frontend/src-tauri/api/_internal/uvicorn/supervisors]"]
    N571["watchfilesreload.py [meridian_frontend/src-tauri/api/_internal/uvicorn/supervisors]"]
    N572["__init__.py [meridian_frontend/src-tauri/api/_internal/uvicorn/supervisors]"]
    N573["auth.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N574["cli.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N575["client.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N576["connection.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N577["datastructures.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N578["exceptions.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N579["frames.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N580["headers.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N581["http11.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N582["imports.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N583["protocol.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N584["proxy.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N585["server.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N586["streams.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N587["typing.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N588["uri.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N589["utils.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N590["version.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N591["__init__.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N592["client.py [meridian_frontend/src-tauri/api/_internal/websockets/asyncio]"]
    N593["connection.py [meridian_frontend/src-tauri/api/_internal/websockets/asyncio]"]
    N594["messages.py [meridian_frontend/src-tauri/api/_internal/websockets/asyncio]"]
    N595["router.py [meridian_frontend/src-tauri/api/_internal/websockets/asyncio]"]
    N596["server.py [meridian_frontend/src-tauri/api/_internal/websockets/asyncio]"]
    N597["base.py [meridian_frontend/src-tauri/api/_internal/websockets/extensions]"]
    N598["permessage_deflate.py [meridian_frontend/src-tauri/api/_internal/websockets/extensions]"]
    N599["auth.py [meridian_frontend/src-tauri/api/_internal/websockets/legacy]"]
    N600["client.py [meridian_frontend/src-tauri/api/_internal/websockets/legacy]"]
    N601["exceptions.py [meridian_frontend/src-tauri/api/_internal/websockets/legacy]"]
    N602["framing.py [meridian_frontend/src-tauri/api/_internal/websockets/legacy]"]
    N603["handshake.py [meridian_frontend/src-tauri/api/_internal/websockets/legacy]"]
    N604["http.py [meridian_frontend/src-tauri/api/_internal/websockets/legacy]"]
    N605["protocol.py [meridian_frontend/src-tauri/api/_internal/websockets/legacy]"]
    N606["server.py [meridian_frontend/src-tauri/api/_internal/websockets/legacy]"]
    N607["__init__.py [meridian_frontend/src-tauri/api/_internal/websockets/legacy]"]
    N608["client.py [meridian_frontend/src-tauri/api/_internal/websockets/sync]"]
    N609["connection.py [meridian_frontend/src-tauri/api/_internal/websockets/sync]"]
    N610["messages.py [meridian_frontend/src-tauri/api/_internal/websockets/sync]"]
    N611["router.py [meridian_frontend/src-tauri/api/_internal/websockets/sync]"]
    N612["server.py [meridian_frontend/src-tauri/api/_internal/websockets/sync]"]
    N613["utils.py [meridian_frontend/src-tauri/api/_internal/websockets/sync]"]
    N614["client.py [meridian_frontend/src-tauri/api/_internal/websockets/trio]"]
    N615["connection.py [meridian_frontend/src-tauri/api/_internal/websockets/trio]"]
    N616["messages.py [meridian_frontend/src-tauri/api/_internal/websockets/trio]"]
    N617["router.py [meridian_frontend/src-tauri/api/_internal/websockets/trio]"]
    N618["server.py [meridian_frontend/src-tauri/api/_internal/websockets/trio]"]
    N619["utils.py [meridian_frontend/src-tauri/api/_internal/websockets/trio]"]
    N620["build_apk.py [meridian_mobile]"]
    N621["flutter_lldb_helper.py [meridian_mobile/ios/Flutter/ephemeral]"]
    N622["get_system_platform_info.py [plugins]"]

    N1 --> N443
    N1 --> N464
    N1 --> N472
    N1 --> N587
    N2 --> N443
    N2 --> N464
    N2 --> N472
    N2 --> N587
    N3 --> N443
    N3 --> N464
    N4 --> N552
    N4 --> N443
    N4 --> N464
    N4 --> N14
    N4 --> N13
    N8 --> N443
    N8 --> N464
    N8 --> N472
    N8 --> N587
    N9 --> N422
    N9 --> N456
    N12 --> N9
    N12 --> N50
    N12 --> N363
    N12 --> N421
    N12 --> N440
    N12 --> N455
    N12 --> N510
    N12 --> N539
    N12 --> N11
    N12 --> N10
    N13 --> N443
    N13 --> N464
    N13 --> N541
    N13 --> N552
    N13 --> N472
    N13 --> N587
    N13 --> N14
    N15 --> N443
    N15 --> N464
    N15 --> N552
    N15 --> N541
    N15 --> N472
    N15 --> N587
    N19 --> N443
    N19 --> N464
    N19 --> N472
    N19 --> N587
    N19 --> N14
    N20 --> N443
    N20 --> N464
    N20 --> N552
    N20 --> N472
    N20 --> N587
    N20 --> N14
    N21 --> N443
    N21 --> N464
    N21 --> N541
    N21 --> N472
    N21 --> N587
    N21 --> N14
    N22 --> N443
    N22 --> N464
    N22 --> N472
    N22 --> N587
    N23 --> N443
    N23 --> N464
    N23 --> N472
    N23 --> N587
    N23 --> N14
    N24 --> N472
    N24 --> N587
    N25 --> N472
    N25 --> N587
    N25 --> N14
    N26 --> N472
    N26 --> N587
    N26 --> N14
    N27 --> N443
    N27 --> N464
    N27 --> N472
    N27 --> N587
    N27 --> N14
    N28 --> N443
    N28 --> N464
    N28 --> N541
    N28 --> N552
    N28 --> N472
    N28 --> N587
    N28 --> N14
    N29 --> N443
    N29 --> N464
    N29 --> N472
    N29 --> N587
    N29 --> N14
    N29 --> N552
    N30 --> N472
    N30 --> N587
    N31 --> N541
    N31 --> N472
    N31 --> N587
    N32 --> N443
    N32 --> N464
    N32 --> N472
    N32 --> N587
    N32 --> N14
    N34 --> N443
    N34 --> N464
    N34 --> N541
    N34 --> N472
    N34 --> N587
    N34 --> N14
    N35 --> N552
    N35 --> N541
    N35 --> N472
    N35 --> N587
    N36 --> N541
    N36 --> N472
    N36 --> N587
    N37 --> N443
    N37 --> N464
    N37 --> N541
    N37 --> N472
    N37 --> N587
    N38 --> N443
    N38 --> N464
    N38 --> N541
    N39 --> N472
    N39 --> N587
    N39 --> N443
    N39 --> N464
    N40 --> N541
    N40 --> N472
    N40 --> N587
    N41 --> N541
    N41 --> N472
    N41 --> N587
    N42 --> N541
    N42 --> N472
    N42 --> N587
    N42 --> N443
    N42 --> N464
    N43 --> N552
    N43 --> N472
    N43 --> N587
    N44 --> N541
    N44 --> N472
    N44 --> N587
    N45 --> N552
    N45 --> N472
    N45 --> N587
    N46 --> N472
    N46 --> N587
    N46 --> N14
    N47 --> N472
    N47 --> N587
    N48 --> N443
    N48 --> N464
    N48 --> N541
    N48 --> N472
    N48 --> N587
    N49 --> N541
    N49 --> N472
    N49 --> N587
    N51 --> N552
    N51 --> N472
    N51 --> N587
    N51 --> N14
    N52 --> N443
    N52 --> N464
    N52 --> N541
    N52 --> N472
    N52 --> N587
    N52 --> N552
    N52 --> N14
    N53 --> N541
    N53 --> N472
    N53 --> N587
    N54 --> N552
    N54 --> N541
    N54 --> N472
    N54 --> N587
    N55 --> N552
    N55 --> N472
    N55 --> N587
    N55 --> N14
    N56 --> N472
    N56 --> N587
    N58 --> N443
    N58 --> N464
    N58 --> N541
    N58 --> N472
    N58 --> N587
    N58 --> N14
    N59 --> N541
    N59 --> N472
    N59 --> N587
    N60 --> N541
    N60 --> N472
    N60 --> N587
    N61 --> N541
    N61 --> N472
    N61 --> N587
    N62 --> N541
    N62 --> N472
    N62 --> N587
    N63 --> N472
    N63 --> N587
    N63 --> N14
    N64 --> N541
    N64 --> N472
    N64 --> N587
    N65 --> N541
    N65 --> N472
    N65 --> N587
    N66 --> N472
    N66 --> N587
    N67 --> N443
    N67 --> N464
    N67 --> N472
    N67 --> N587
    N68 --> N443
    N68 --> N464
    N68 --> N472
    N68 --> N587
    N69 --> N541
    N69 --> N472
    N69 --> N587
    N69 --> N436
    N69 --> N443
    N69 --> N464
    N71 --> N541
    N71 --> N472
    N71 --> N587
    N71 --> N14
    N72 --> N552
    N72 --> N541
    N72 --> N472
    N72 --> N587
    N72 --> N14
    N73 --> N472
    N73 --> N587
    N73 --> N14
    N74 --> N443
    N74 --> N464
    N74 --> N541
    N74 --> N552
    N74 --> N472
    N74 --> N587
    N74 --> N14
    N75 --> N541
    N75 --> N552
    N75 --> N472
    N75 --> N587
    N75 --> N14
    N75 --> N443
    N75 --> N464
    N76 --> N443
    N76 --> N464
    N76 --> N541
    N76 --> N472
    N76 --> N587
    N77 --> N541
    N77 --> N443
    N77 --> N464
    N78 --> N443
    N78 --> N464
    N78 --> N552
    N78 --> N472
    N78 --> N587
    N78 --> N14
    N79 --> N443
    N79 --> N464
    N79 --> N552
    N79 --> N472
    N79 --> N587
    N79 --> N14
    N80 --> N443
    N80 --> N464
    N80 --> N472
    N80 --> N587
    N80 --> N14
    N81 --> N443
    N81 --> N464
    N81 --> N552
    N81 --> N472
    N81 --> N587
    N81 --> N14
    N82 --> N443
    N82 --> N464
    N82 --> N552
    N82 --> N472
    N82 --> N587
    N82 --> N14
    N83 --> N443
    N83 --> N464
    N83 --> N552
    N83 --> N472
    N83 --> N587
    N83 --> N14
    N84 --> N443
    N84 --> N464
    N84 --> N552
    N84 --> N472
    N84 --> N587
    N85 --> N541
    N85 --> N472
    N85 --> N587
    N86 --> N443
    N86 --> N464
    N86 --> N552
    N86 --> N541
    N86 --> N472
    N86 --> N587
    N87 --> N552
    N87 --> N443
    N87 --> N464
    N87 --> N541
    N87 --> N472
    N87 --> N587
    N88 --> N443
    N88 --> N464
    N88 --> N472
    N88 --> N587
    N89 --> N541
    N89 --> N552
    N89 --> N443
    N89 --> N464
    N89 --> N472
    N89 --> N587
    N89 --> N14
    N90 --> N443
    N90 --> N464
    N90 --> N472
    N90 --> N587
    N90 --> N14
    N91 --> N443
    N91 --> N464
    N91 --> N541
    N91 --> N472
    N91 --> N587
    N91 --> N14
    N91 --> N552
    N92 --> N472
    N92 --> N587
    N92 --> N14
    N92 --> N443
    N92 --> N464
    N93 --> N472
    N93 --> N587
    N94 --> N443
    N94 --> N464
    N94 --> N472
    N94 --> N587
    N95 --> N541
    N95 --> N552
    N95 --> N472
    N95 --> N587
    N95 --> N443
    N95 --> N464
    N96 --> N443
    N96 --> N464
    N96 --> N472
    N96 --> N587
    N96 --> N14
    N98 --> N472
    N98 --> N587
    N99 --> N472
    N99 --> N587
    N100 --> N541
    N100 --> N472
    N100 --> N587
    N101 --> N541
    N101 --> N472
    N101 --> N587
    N102 --> N541
    N102 --> N472
    N102 --> N587
    N102 --> N14
    N103 --> N472
    N103 --> N587
    N104 --> N541
    N104 --> N472
    N104 --> N587
    N105 --> N541
    N105 --> N472
    N105 --> N587
    N106 --> N541
    N106 --> N472
    N106 --> N587
    N107 --> N541
    N107 --> N472
    N107 --> N587
    N108 --> N541
    N108 --> N472
    N108 --> N587
    N109 --> N443
    N109 --> N464
    N109 --> N472
    N109 --> N587
    N110 --> N472
    N110 --> N587
    N111 --> N472
    N111 --> N587
    N112 --> N541
    N112 --> N472
    N112 --> N587
    N113 --> N552
    N113 --> N436
    N113 --> N14
    N113 --> N443
    N113 --> N464
    N114 --> N552
    N114 --> N541
    N114 --> N472
    N114 --> N587
    N115 --> N541
    N115 --> N472
    N115 --> N587
    N116 --> N541
    N116 --> N472
    N116 --> N587
    N117 --> N541
    N117 --> N472
    N117 --> N587
    N118 --> N541
    N118 --> N472
    N118 --> N587
    N119 --> N541
    N119 --> N472
    N119 --> N587
    N119 --> N14
    N120 --> N443
    N120 --> N464
    N120 --> N552
    N120 --> N472
    N120 --> N587
    N120 --> N14
    N121 --> N552
    N121 --> N443
    N121 --> N464
    N121 --> N472
    N121 --> N587
    N121 --> N14
    N122 --> N541
    N122 --> N472
    N122 --> N587
    N123 --> N472
    N123 --> N587
    N123 --> N552
    N123 --> N14
    N124 --> N472
    N124 --> N587
    N125 --> N541
    N125 --> N472
    N125 --> N587
    N126 --> N472
    N126 --> N587
    N127 --> N541
    N127 --> N472
    N127 --> N587
    N128 --> N443
    N128 --> N464
    N128 --> N472
    N128 --> N587
    N129 --> N541
    N129 --> N472
    N129 --> N587
    N129 --> N14
    N130 --> N541
    N130 --> N472
    N130 --> N587
    N131 --> N541
    N131 --> N472
    N131 --> N587
    N132 --> N541
    N132 --> N472
    N132 --> N587
    N133 --> N541
    N133 --> N472
    N133 --> N587
    N134 --> N443
    N134 --> N464
    N134 --> N472
    N134 --> N587
    N135 --> N541
    N135 --> N472
    N135 --> N587
    N136 --> N472
    N136 --> N587
    N136 --> N14
    N136 --> N13
    N137 --> N552
    N137 --> N472
    N137 --> N587
    N138 --> N472
    N138 --> N587
    N139 --> N541
    N139 --> N472
    N139 --> N587
    N139 --> N14
    N141 --> N472
    N141 --> N587
    N142 --> N472
    N142 --> N587
    N143 --> N472
    N143 --> N587
    N144 --> N472
    N144 --> N587
    N145 --> N472
    N145 --> N587
    N146 --> N472
    N146 --> N587
    N147 --> N443
    N147 --> N464
    N149 --> N443
    N149 --> N464
    N149 --> N472
    N149 --> N587
    N150 --> N443
    N150 --> N464
    N150 --> N472
    N150 --> N587
    N151 --> N472
    N151 --> N587
    N153 --> N472
    N153 --> N587
    N154 --> N443
    N154 --> N464
    N154 --> N472
    N154 --> N587
    N155 --> N541
    N155 --> N472
    N155 --> N587
    N156 --> N443
    N156 --> N464
    N156 --> N541
    N156 --> N472
    N156 --> N587
    N157 --> N443
    N157 --> N464
    N157 --> N472
    N157 --> N587
    N157 --> N552
    N157 --> N14
    N158 --> N472
    N158 --> N587
    N159 --> N472
    N159 --> N587
    N159 --> N14
    N160 --> N472
    N160 --> N587
    N160 --> N14
    N161 --> N541
    N161 --> N472
    N161 --> N587
    N161 --> N14
    N162 --> N472
    N162 --> N587
    N162 --> N14
    N163 --> N472
    N163 --> N587
    N163 --> N14
    N164 --> N472
    N164 --> N587
    N165 --> N552
    N165 --> N472
    N165 --> N587
    N166 --> N472
    N166 --> N587
    N167 --> N472
    N167 --> N587
    N168 --> N472
    N168 --> N587
    N169 --> N472
    N169 --> N587
    N170 --> N541
    N170 --> N472
    N170 --> N587
    N171 --> N443
    N171 --> N464
    N171 --> N472
    N171 --> N587
    N172 --> N443
    N172 --> N464
    N172 --> N472
    N172 --> N587
    N172 --> N14
    N173 --> N443
    N173 --> N464
    N173 --> N382
    N173 --> N516
    N173 --> N472
    N173 --> N587
    N174 --> N472
    N174 --> N587
    N175 --> N472
    N175 --> N587
    N176 --> N443
    N176 --> N464
    N176 --> N472
    N176 --> N587
    N177 --> N472
    N177 --> N587
    N178 --> N472
    N178 --> N587
    N179 --> N443
    N179 --> N464
    N179 --> N472
    N179 --> N587
    N180 --> N472
    N180 --> N587
    N180 --> N14
    N181 --> N541
    N181 --> N472
    N181 --> N587
    N182 --> N443
    N182 --> N464
    N182 --> N472
    N182 --> N587
    N183 --> N472
    N183 --> N587
    N184 --> N541
    N184 --> N472
    N184 --> N587
    N185 --> N14
    N186 --> N443
    N186 --> N464
    N186 --> N472
    N186 --> N587
    N186 --> N422
    N186 --> N456
    N186 --> N9
    N186 --> N50
    N186 --> N363
    N186 --> N421
    N186 --> N440
    N186 --> N455
    N186 --> N510
    N186 --> N539
    N186 --> N11
    N186 --> N10
    N187 --> N472
    N187 --> N587
    N188 --> N472
    N188 --> N587
    N189 --> N443
    N189 --> N464
    N189 --> N552
    N189 --> N541
    N189 --> N472
    N189 --> N587
    N189 --> N14
    N190 --> N541
    N190 --> N472
    N190 --> N587
    N191 --> N443
    N191 --> N464
    N191 --> N14
    N192 --> N552
    N192 --> N472
    N192 --> N587
    N192 --> N14
    N192 --> N443
    N192 --> N464
    N193 --> N472
    N193 --> N587
    N193 --> N14
    N195 --> N443
    N195 --> N464
    N195 --> N472
    N195 --> N587
    N196 --> N472
    N196 --> N587
    N196 --> N14
    N197 --> N472
    N197 --> N587
    N198 --> N472
    N198 --> N587
    N198 --> N14
    N199 --> N14
    N202 --> N472
    N202 --> N587
    N203 --> N443
    N203 --> N464
    N203 --> N472
    N203 --> N587
    N204 --> N472
    N204 --> N587
    N205 --> N472
    N205 --> N587
    N205 --> N443
    N205 --> N464
    N206 --> N541
    N206 --> N472
    N206 --> N587
    N208 --> N472
    N208 --> N587
    N209 --> N472
    N209 --> N587
    N209 --> N14
    N210 --> N443
    N210 --> N464
    N210 --> N472
    N210 --> N587
    N210 --> N14
    N211 --> N472
    N211 --> N587
    N211 --> N14
    N212 --> N472
    N212 --> N587
    N213 --> N443
    N213 --> N464
    N213 --> N541
    N213 --> N472
    N213 --> N587
    N213 --> N14
    N214 --> N541
    N214 --> N472
    N214 --> N587
    N215 --> N541
    N215 --> N472
    N215 --> N587
    N216 --> N552
    N216 --> N541
    N216 --> N472
    N216 --> N587
    N217 --> N472
    N217 --> N587
    N218 --> N541
    N218 --> N472
    N218 --> N587
    N219 --> N541
    N219 --> N14
    N220 --> N541
    N220 --> N472
    N220 --> N587
    N220 --> N14
    N221 --> N472
    N221 --> N587
    N222 --> N472
    N222 --> N587
    N223 --> N541
    N223 --> N472
    N223 --> N587
    N223 --> N14
    N227 --> N443
    N227 --> N464
    N228 --> N552
    N228 --> N443
    N228 --> N464
    N230 --> N552
    N230 --> N13
    N232 --> N14
    N233 --> N13
    N239 --> N14
    N240 --> N13
    N244 --> N14
    N246 --> N14
    N247 --> N552
    N253 --> N14
    N254 --> N14
    N255 --> N13
    N257 --> N443
    N257 --> N464
    N257 --> N14
    N259 --> N443
    N259 --> N464
    N259 --> N14
    N259 --> N552
    N260 --> N552
    N260 --> N13
    N262 --> N443
    N262 --> N464
    N265 --> N14
    N268 --> N552
    N269 --> N541
    N269 --> N443
    N269 --> N464
    N270 --> N443
    N270 --> N464
    N271 --> N552
    N272 --> N443
    N272 --> N464
    N272 --> N13
    N272 --> N552
    N273 --> N14
    N274 --> N443
    N274 --> N464
    N274 --> N14
    N274 --> N13
    N276 --> N552
    N276 --> N13
    N278 --> N14
    N279 --> N13
    N280 --> N552
    N281 --> N443
    N281 --> N464
    N282 --> N552
    N282 --> N13
    N283 --> N443
    N283 --> N464
    N284 --> N443
    N284 --> N464
    N285 --> N13
    N285 --> N472
    N285 --> N587
    N285 --> N552
    N288 --> N13
    N289 --> N443
    N289 --> N464
    N290 --> N541
    N291 --> N14
    N292 --> N13
    N293 --> N443
    N293 --> N464
    N293 --> N15
    N294 --> N552
    N295 --> N552
    N297 --> N443
    N297 --> N464
    N298 --> N443
    N298 --> N464
    N299 --> N552
    N304 --> N13
    N305 --> N13
    N306 --> N13
    N310 --> N389
    N310 --> N416
    N310 --> N432
    N310 --> N471
    N310 --> N524
    N310 --> N9
    N310 --> N50
    N310 --> N363
    N310 --> N421
    N310 --> N440
    N310 --> N455
    N310 --> N510
    N310 --> N539
    N311 --> N575
    N311 --> N592
    N311 --> N600
    N311 --> N608
    N311 --> N614
    N311 --> N312
    N311 --> N344
    N311 --> N346
    N311 --> N327
    N311 --> N310
    N311 --> N9
    N311 --> N50
    N311 --> N363
    N311 --> N421
    N311 --> N440
    N311 --> N455
    N311 --> N510
    N311 --> N539
    N311 --> N345
    N311 --> N343
    N312 --> N313
    N312 --> N9
    N312 --> N50
    N312 --> N363
    N312 --> N421
    N312 --> N440
    N312 --> N455
    N312 --> N510
    N312 --> N539
    N312 --> N310
    N312 --> N342
    N314 --> N329
    N314 --> N331
    N314 --> N330
    N315 --> N9
    N315 --> N50
    N315 --> N363
    N315 --> N421
    N315 --> N440
    N315 --> N455
    N315 --> N510
    N315 --> N539
    N317 --> N9
    N317 --> N50
    N317 --> N363
    N317 --> N421
    N317 --> N440
    N317 --> N455
    N317 --> N510
    N317 --> N539
    N318 --> N9
    N318 --> N50
    N318 --> N363
    N318 --> N421
    N318 --> N440
    N318 --> N455
    N318 --> N510
    N318 --> N539
    N319 --> N339
    N319 --> N9
    N319 --> N50
    N319 --> N363
    N319 --> N421
    N319 --> N440
    N319 --> N455
    N319 --> N510
    N319 --> N539
    N320 --> N9
    N320 --> N50
    N320 --> N363
    N320 --> N421
    N320 --> N440
    N320 --> N455
    N320 --> N510
    N320 --> N539
    N321 --> N310
    N321 --> N312
    N323 --> N9
    N323 --> N50
    N323 --> N363
    N323 --> N421
    N323 --> N440
    N323 --> N455
    N323 --> N510
    N323 --> N539
    N325 --> N310
    N325 --> N337
    N325 --> N334
    N326 --> N9
    N326 --> N50
    N326 --> N363
    N326 --> N421
    N326 --> N440
    N326 --> N455
    N326 --> N510
    N326 --> N539
    N327 --> N310
    N327 --> N321
    N327 --> N328
    N327 --> N325
    N327 --> N316
    N327 --> N339
    N327 --> N353
    N327 --> N348
    N327 --> N347
    N327 --> N350
    N327 --> N332
    N327 --> N323
    N328 --> N310
    N328 --> N9
    N328 --> N50
    N328 --> N363
    N328 --> N421
    N328 --> N440
    N328 --> N455
    N328 --> N510
    N328 --> N539
    N328 --> N334
    N332 --> N340
    N341 --> N9
    N341 --> N50
    N341 --> N363
    N341 --> N421
    N341 --> N440
    N341 --> N455
    N341 --> N510
    N341 --> N539
    N342 --> N9
    N342 --> N50
    N342 --> N363
    N342 --> N421
    N342 --> N440
    N342 --> N455
    N342 --> N510
    N342 --> N539
    N343 --> N9
    N343 --> N50
    N343 --> N363
    N343 --> N421
    N343 --> N440
    N343 --> N455
    N343 --> N510
    N343 --> N539
    N344 --> N9
    N344 --> N50
    N344 --> N363
    N344 --> N421
    N344 --> N440
    N344 --> N455
    N344 --> N510
    N344 --> N539
    N344 --> N312
    N345 --> N9
    N345 --> N50
    N345 --> N363
    N345 --> N421
    N345 --> N440
    N345 --> N455
    N345 --> N510
    N345 --> N539
    N346 --> N336
    N346 --> N9
    N346 --> N50
    N346 --> N363
    N346 --> N421
    N346 --> N440
    N346 --> N455
    N346 --> N510
    N346 --> N539
    N347 --> N389
    N347 --> N416
    N347 --> N432
    N347 --> N471
    N347 --> N524
    N347 --> N310
    N347 --> N336
    N347 --> N9
    N347 --> N50
    N347 --> N363
    N347 --> N421
    N347 --> N440
    N347 --> N455
    N347 --> N510
    N347 --> N539
    N348 --> N389
    N348 --> N416
    N348 --> N432
    N348 --> N471
    N348 --> N524
    N348 --> N336
    N348 --> N335
    N348 --> N9
    N348 --> N50
    N348 --> N363
    N348 --> N421
    N348 --> N440
    N348 --> N455
    N348 --> N510
    N348 --> N539
    N349 --> N9
    N349 --> N50
    N349 --> N363
    N349 --> N421
    N349 --> N440
    N349 --> N455
    N349 --> N510
    N349 --> N539
    N350 --> N389
    N350 --> N416
    N350 --> N432
    N350 --> N471
    N350 --> N524
    N350 --> N337
    N350 --> N336
    N350 --> N335
    N350 --> N9
    N350 --> N50
    N350 --> N363
    N350 --> N421
    N350 --> N440
    N350 --> N455
    N350 --> N510
    N350 --> N539
    N350 --> N319
    N350 --> N320
    N350 --> N317
    N350 --> N315
    N350 --> N318
    N351 --> N9
    N351 --> N50
    N351 --> N363
    N351 --> N421
    N351 --> N440
    N351 --> N455
    N351 --> N510
    N351 --> N539
    N351 --> N389
    N351 --> N416
    N351 --> N432
    N351 --> N471
    N351 --> N524
    N351 --> N310
    N351 --> N340
    N351 --> N337
    N351 --> N336
    N351 --> N335
    N351 --> N357
    N351 --> N362
    N351 --> N356
    N351 --> N355
    N351 --> N358
    N351 --> N361
    N351 --> N360
    N351 --> N359
    N352 --> N338
    N352 --> N336
    N352 --> N9
    N352 --> N50
    N352 --> N363
    N352 --> N421
    N352 --> N440
    N352 --> N455
    N352 --> N510
    N352 --> N539
    N353 --> N389
    N353 --> N416
    N353 --> N432
    N353 --> N471
    N353 --> N524
    N353 --> N336
    N353 --> N335
    N353 --> N9
    N353 --> N50
    N353 --> N363
    N353 --> N421
    N353 --> N440
    N353 --> N455
    N353 --> N510
    N353 --> N539
    N353 --> N342
    N353 --> N333
    N354 --> N9
    N354 --> N50
    N354 --> N363
    N354 --> N421
    N354 --> N440
    N354 --> N455
    N354 --> N510
    N354 --> N539
    N355 --> N335
    N355 --> N336
    N355 --> N359
    N356 --> N335
    N356 --> N336
    N356 --> N359
    N356 --> N9
    N356 --> N50
    N356 --> N363
    N356 --> N421
    N356 --> N440
    N356 --> N455
    N356 --> N510
    N356 --> N539
    N357 --> N335
    N358 --> N335
    N358 --> N336
    N358 --> N9
    N358 --> N50
    N358 --> N363
    N358 --> N421
    N358 --> N440
    N358 --> N455
    N358 --> N510
    N358 --> N539
    N360 --> N335
    N360 --> N336
    N361 --> N335
    N361 --> N336
    N362 --> N335
    N362 --> N336
    N367 --> N472
    N367 --> N587
    N369 --> N472
    N369 --> N587
    N371 --> N472
    N371 --> N587
    N372 --> N472
    N372 --> N587
    N374 --> N472
    N374 --> N587
    N375 --> N472
    N375 --> N587
    N376 --> N422
    N376 --> N456
    N376 --> N389
    N376 --> N416
    N376 --> N432
    N376 --> N471
    N376 --> N524
    N376 --> N472
    N376 --> N587
    N377 --> N472
    N377 --> N587
    N379 --> N541
    N380 --> N436
    N380 --> N422
    N380 --> N456
    N380 --> N472
    N380 --> N587
    N381 --> N472
    N381 --> N587
    N383 --> N472
    N383 --> N587
    N384 --> N443
    N384 --> N464
    N384 --> N389
    N384 --> N416
    N384 --> N432
    N384 --> N471
    N384 --> N524
    N384 --> N422
    N384 --> N456
    N384 --> N472
    N384 --> N587
    N385 --> N472
    N385 --> N587
    N389 --> N416
    N389 --> N432
    N389 --> N471
    N389 --> N524
    N389 --> N472
    N389 --> N587
    N390 --> N436
    N390 --> N472
    N390 --> N587
    N394 --> N422
    N394 --> N456
    N394 --> N472
    N394 --> N587
    N394 --> N552
    N395 --> N422
    N395 --> N456
    N395 --> N472
    N395 --> N587
    N403 --> N443
    N403 --> N464
    N403 --> N472
    N403 --> N587
    N404 --> N472
    N404 --> N587
    N405 --> N408
    N405 --> N604
    N405 --> N436
    N405 --> N472
    N405 --> N587
    N406 --> N472
    N406 --> N587
    N408 --> N472
    N408 --> N587
    N409 --> N472
    N409 --> N587
    N410 --> N472
    N410 --> N587
    N411 --> N389
    N411 --> N416
    N411 --> N432
    N411 --> N471
    N411 --> N524
    N411 --> N472
    N411 --> N587
    N411 --> N436
    N411 --> N422
    N411 --> N456
    N412 --> N436
    N412 --> N422
    N412 --> N456
    N412 --> N472
    N412 --> N587
    N415 --> N389
    N415 --> N416
    N415 --> N432
    N415 --> N471
    N415 --> N524
    N416 --> N583
    N416 --> N605
    N416 --> N415
    N417 --> N422
    N417 --> N456
    N417 --> N472
    N417 --> N587
    N419 --> N472
    N419 --> N587
    N420 --> N472
    N420 --> N587
    N421 --> N436
    N421 --> N472
    N421 --> N587
    N422 --> N456
    N422 --> N389
    N422 --> N416
    N422 --> N432
    N422 --> N471
    N422 --> N524
    N422 --> N472
    N422 --> N587
    N422 --> N436
    N423 --> N472
    N423 --> N587
    N424 --> N422
    N424 --> N456
    N424 --> N472
    N424 --> N587
    N424 --> N436
    N424 --> N452
    N425 --> N422
    N425 --> N456
    N425 --> N472
    N425 --> N587
    N426 --> N422
    N426 --> N456
    N426 --> N436
    N426 --> N472
    N426 --> N587
    N427 --> N422
    N427 --> N456
    N427 --> N436
    N427 --> N472
    N427 --> N587
    N428 --> N389
    N428 --> N416
    N428 --> N432
    N428 --> N471
    N428 --> N524
    N428 --> N436
    N428 --> N472
    N428 --> N587
    N428 --> N443
    N428 --> N464
    N429 --> N472
    N429 --> N587
    N429 --> N466
    N429 --> N436
    N430 --> N422
    N430 --> N456
    N430 --> N472
    N430 --> N587
    N431 --> N472
    N431 --> N587
    N432 --> N422
    N432 --> N456
    N432 --> N389
    N432 --> N416
    N432 --> N471
    N432 --> N524
    N432 --> N472
    N432 --> N587
    N432 --> N452
    N432 --> N443
    N432 --> N464
    N433 --> N389
    N433 --> N416
    N433 --> N432
    N433 --> N471
    N433 --> N524
    N433 --> N422
    N433 --> N456
    N433 --> N472
    N433 --> N587
    N434 --> N389
    N434 --> N416
    N434 --> N432
    N434 --> N471
    N434 --> N524
    N434 --> N472
    N434 --> N587
    N437 --> N472
    N437 --> N587
    N437 --> N436
    N438 --> N472
    N438 --> N587
    N438 --> N436
    N439 --> N389
    N439 --> N416
    N439 --> N432
    N439 --> N471
    N439 --> N524
    N439 --> N472
    N439 --> N587
    N439 --> N436
    N440 --> N436
    N440 --> N472
    N440 --> N587
    N441 --> N472
    N441 --> N587
    N442 --> N436
    N442 --> N472
    N442 --> N587
    N443 --> N436
    N443 --> N389
    N443 --> N416
    N443 --> N432
    N443 --> N471
    N443 --> N524
    N443 --> N472
    N443 --> N587
    N443 --> N422
    N443 --> N456
    N444 --> N443
    N444 --> N464
    N444 --> N436
    N444 --> N472
    N444 --> N587
    N445 --> N443
    N445 --> N464
    N445 --> N436
    N445 --> N472
    N445 --> N587
    N446 --> N472
    N446 --> N587
    N448 --> N422
    N448 --> N456
    N448 --> N472
    N448 --> N587
    N448 --> N452
    N448 --> N389
    N448 --> N416
    N448 --> N432
    N448 --> N471
    N448 --> N524
    N449 --> N436
    N449 --> N472
    N449 --> N587
    N450 --> N472
    N450 --> N587
    N451 --> N472
    N451 --> N587
    N452 --> N472
    N452 --> N587
    N453 --> N436
    N453 --> N389
    N453 --> N416
    N453 --> N432
    N453 --> N471
    N453 --> N524
    N453 --> N472
    N453 --> N587
    N454 --> N472
    N454 --> N587
    N455 --> N443
    N455 --> N464
    N455 --> N472
    N455 --> N587
    N456 --> N422
    N456 --> N472
    N456 --> N587
    N457 --> N472
    N457 --> N587
    N458 --> N472
    N458 --> N587
    N459 --> N436
    N459 --> N472
    N459 --> N587
    N460 --> N472
    N460 --> N587
    N461 --> N443
    N461 --> N464
    N461 --> N472
    N461 --> N587
    N462 --> N472
    N462 --> N587
    N463 --> N389
    N463 --> N416
    N463 --> N432
    N463 --> N471
    N463 --> N524
    N463 --> N472
    N463 --> N587
    N464 --> N389
    N464 --> N416
    N464 --> N432
    N464 --> N471
    N464 --> N524
    N464 --> N472
    N464 --> N587
    N464 --> N422
    N464 --> N456
    N465 --> N436
    N465 --> N389
    N465 --> N416
    N465 --> N432
    N465 --> N471
    N465 --> N524
    N465 --> N472
    N465 --> N587
    N466 --> N472
    N466 --> N587
    N466 --> N429
    N466 --> N436
    N467 --> N472
    N467 --> N587
    N468 --> N443
    N468 --> N464
    N468 --> N472
    N468 --> N587
    N469 --> N436
    N469 --> N422
    N469 --> N456
    N469 --> N472
    N469 --> N587
    N470 --> N443
    N470 --> N464
    N470 --> N472
    N470 --> N587
    N471 --> N436
    N471 --> N389
    N471 --> N416
    N471 --> N432
    N471 --> N524
    N471 --> N472
    N471 --> N587
    N472 --> N587
    N472 --> N389
    N472 --> N416
    N472 --> N432
    N472 --> N471
    N472 --> N524
    N473 --> N436
    N473 --> N389
    N473 --> N416
    N473 --> N432
    N473 --> N471
    N473 --> N524
    N473 --> N472
    N473 --> N587
    N474 --> N472
    N474 --> N587
    N474 --> N436
    N476 --> N443
    N476 --> N464
    N476 --> N472
    N476 --> N587
    N478 --> N436
    N478 --> N472
    N478 --> N587
    N479 --> N472
    N479 --> N587
    N479 --> N436
    N480 --> N472
    N480 --> N587
    N481 --> N422
    N481 --> N456
    N481 --> N436
    N481 --> N472
    N481 --> N587
    N482 --> N389
    N482 --> N416
    N482 --> N432
    N482 --> N471
    N482 --> N524
    N482 --> N422
    N482 --> N456
    N482 --> N472
    N482 --> N587
    N483 --> N472
    N483 --> N587
    N484 --> N472
    N484 --> N587
    N485 --> N472
    N485 --> N587
    N486 --> N422
    N486 --> N456
    N486 --> N436
    N486 --> N472
    N486 --> N587
    N486 --> N452
    N487 --> N422
    N487 --> N456
    N487 --> N472
    N487 --> N587
    N488 --> N422
    N488 --> N456
    N488 --> N472
    N488 --> N587
    N488 --> N436
    N488 --> N389
    N488 --> N416
    N488 --> N432
    N488 --> N471
    N488 --> N524
    N489 --> N389
    N489 --> N416
    N489 --> N432
    N489 --> N471
    N489 --> N524
    N489 --> N472
    N489 --> N587
    N491 --> N472
    N491 --> N587
    N493 --> N472
    N493 --> N587
    N493 --> N452
    N494 --> N472
    N494 --> N587
    N495 --> N472
    N495 --> N587
    N495 --> N436
    N495 --> N389
    N495 --> N416
    N495 --> N432
    N495 --> N471
    N495 --> N524
    N496 --> N472
    N496 --> N587
    N497 --> N389
    N497 --> N416
    N497 --> N432
    N497 --> N471
    N497 --> N524
    N497 --> N472
    N497 --> N587
    N498 --> N422
    N498 --> N456
    N498 --> N472
    N498 --> N587
    N499 --> N472
    N499 --> N587
    N500 --> N472
    N500 --> N587
    N501 --> N422
    N501 --> N456
    N501 --> N472
    N501 --> N587
    N502 --> N389
    N502 --> N416
    N502 --> N432
    N502 --> N471
    N502 --> N524
    N502 --> N472
    N502 --> N587
    N503 --> N422
    N503 --> N456
    N503 --> N436
    N503 --> N389
    N503 --> N416
    N503 --> N432
    N503 --> N471
    N503 --> N524
    N503 --> N472
    N503 --> N587
    N504 --> N472
    N504 --> N587
    N505 --> N472
    N505 --> N587
    N506 --> N472
    N506 --> N587
    N507 --> N472
    N507 --> N587
    N508 --> N472
    N508 --> N587
    N509 --> N436
    N509 --> N472
    N509 --> N587
    N510 --> N436
    N510 --> N472
    N510 --> N587
    N511 --> N472
    N511 --> N587
    N512 --> N472
    N512 --> N587
    N513 --> N443
    N513 --> N464
    N513 --> N472
    N513 --> N587
    N514 --> N408
    N514 --> N604
    N515 --> N422
    N515 --> N456
    N515 --> N472
    N515 --> N587
    N516 --> N443
    N516 --> N464
    N516 --> N408
    N516 --> N604
    N516 --> N472
    N516 --> N587
    N517 --> N408
    N517 --> N604
    N517 --> N443
    N517 --> N464
    N517 --> N472
    N517 --> N587
    N518 --> N389
    N518 --> N416
    N518 --> N432
    N518 --> N471
    N518 --> N524
    N518 --> N436
    N518 --> N472
    N518 --> N587
    N519 --> N472
    N519 --> N587
    N520 --> N472
    N520 --> N587
    N521 --> N436
    N522 --> N472
    N522 --> N587
    N523 --> N443
    N523 --> N464
    N523 --> N436
    N523 --> N389
    N523 --> N416
    N523 --> N432
    N523 --> N471
    N523 --> N524
    N523 --> N472
    N523 --> N587
    N524 --> N472
    N524 --> N587
    N525 --> N443
    N525 --> N464
    N525 --> N472
    N525 --> N587
    N526 --> N472
    N526 --> N587
    N527 --> N472
    N527 --> N587
    N527 --> N552
    N529 --> N472
    N529 --> N587
    N532 --> N472
    N532 --> N587
    N533 --> N398
    N533 --> N472
    N533 --> N587
    N535 --> N443
    N535 --> N464
    N535 --> N472
    N535 --> N587
    N537 --> N436
    N537 --> N472
    N537 --> N587
    N538 --> N472
    N538 --> N587
    N539 --> N552
    N539 --> N443
    N539 --> N464
    N539 --> N541
    N539 --> N472
    N539 --> N587
    N540 --> N472
    N540 --> N587
    N541 --> N408
    N541 --> N604
    N541 --> N472
    N541 --> N587
    N542 --> N552
    N542 --> N541
    N542 --> N436
    N542 --> N472
    N542 --> N587
    N543 --> N552
    N543 --> N541
    N543 --> N389
    N543 --> N416
    N543 --> N432
    N543 --> N471
    N543 --> N524
    N543 --> N472
    N543 --> N587
    N544 --> N552
    N544 --> N541
    N544 --> N436
    N544 --> N472
    N544 --> N587
    N545 --> N552
    N545 --> N472
    N545 --> N587
    N547 --> N389
    N547 --> N416
    N547 --> N432
    N547 --> N471
    N547 --> N524
    N547 --> N472
    N547 --> N587
    N550 --> N472
    N550 --> N587
    N551 --> N552
    N551 --> N541
    N551 --> N472
    N551 --> N587
    N553 --> N552
    N553 --> N554
    N554 --> N552
    N556 --> N541
    N556 --> N472
    N556 --> N587
    N558 --> N552
    N558 --> N436
    N559 --> N552
    N560 --> N552
    N561 --> N552
    N562 --> N552
    N562 --> N408
    N562 --> N604
    N562 --> N541
    N562 --> N472
    N562 --> N587
    N563 --> N552
    N563 --> N408
    N563 --> N604
    N563 --> N541
    N563 --> N472
    N563 --> N587
    N564 --> N552
    N564 --> N391
    N564 --> N525
    N565 --> N552
    N565 --> N408
    N565 --> N604
    N565 --> N541
    N565 --> N472
    N565 --> N587
    N565 --> N391
    N565 --> N525
    N566 --> N552
    N566 --> N541
    N566 --> N408
    N566 --> N604
    N566 --> N472
    N566 --> N587
    N566 --> N391
    N566 --> N525
    N567 --> N552
    N567 --> N541
    N567 --> N472
    N567 --> N587
    N568 --> N541
    N568 --> N389
    N568 --> N416
    N568 --> N432
    N568 --> N471
    N568 --> N524
    N569 --> N541
    N569 --> N472
    N569 --> N587
    N570 --> N541
    N572 --> N472
    N572 --> N587
    N573 --> N436
    N574 --> N552
    N574 --> N472
    N574 --> N587
    N575 --> N436
    N575 --> N472
    N575 --> N587
    N576 --> N436
    N577 --> N472
    N577 --> N587
    N578 --> N436
    N579 --> N422
    N579 --> N456
    N579 --> N472
    N579 --> N587
    N580 --> N472
    N580 --> N587
    N581 --> N422
    N581 --> N456
    N581 --> N436
    N581 --> N472
    N581 --> N587
    N582 --> N436
    N582 --> N472
    N582 --> N587
    N583 --> N541
    N584 --> N422
    N584 --> N456
    N585 --> N408
    N585 --> N604
    N585 --> N436
    N585 --> N472
    N585 --> N587
    N587 --> N408
    N587 --> N604
    N587 --> N541
    N587 --> N472
    N588 --> N422
    N588 --> N456
    N591 --> N472
    N591 --> N587
    N592 --> N552
    N592 --> N541
    N592 --> N389
    N592 --> N416
    N592 --> N432
    N592 --> N471
    N592 --> N524
    N592 --> N472
    N592 --> N587
    N592 --> N391
    N592 --> N525
    N593 --> N552
    N593 --> N541
    N593 --> N389
    N593 --> N416
    N593 --> N432
    N593 --> N471
    N593 --> N524
    N593 --> N472
    N593 --> N587
    N594 --> N552
    N594 --> N472
    N594 --> N587
    N595 --> N408
    N595 --> N604
    N595 --> N472
    N595 --> N587
    N595 --> N391
    N595 --> N525
    N596 --> N552
    N596 --> N408
    N596 --> N604
    N596 --> N541
    N596 --> N389
    N596 --> N416
    N596 --> N432
    N596 --> N471
    N596 --> N524
    N596 --> N472
    N596 --> N587
    N596 --> N391
    N596 --> N525
    N598 --> N472
    N598 --> N587
    N599 --> N408
    N599 --> N604
    N599 --> N472
    N599 --> N587
    N600 --> N552
    N600 --> N541
    N600 --> N436
    N600 --> N389
    N600 --> N416
    N600 --> N432
    N600 --> N471
    N600 --> N524
    N600 --> N472
    N600 --> N587
    N601 --> N408
    N601 --> N604
    N602 --> N472
    N602 --> N587
    N604 --> N552
    N605 --> N552
    N605 --> N541
    N605 --> N436
    N605 --> N472
    N605 --> N587
    N606 --> N552
    N606 --> N408
    N606 --> N604
    N606 --> N541
    N606 --> N436
    N606 --> N389
    N606 --> N416
    N606 --> N432
    N606 --> N471
    N606 --> N524
    N606 --> N472
    N606 --> N587
    N607 --> N436
    N608 --> N541
    N608 --> N436
    N608 --> N389
    N608 --> N416
    N608 --> N432
    N608 --> N471
    N608 --> N524
    N608 --> N472
    N608 --> N587
    N608 --> N391
    N608 --> N525
    N609 --> N541
    N609 --> N389
    N609 --> N416
    N609 --> N432
    N609 --> N471
    N609 --> N524
    N609 --> N472
    N609 --> N587
    N610 --> N472
    N610 --> N587
    N611 --> N408
    N611 --> N604
    N611 --> N472
    N611 --> N587
    N611 --> N391
    N611 --> N525
    N612 --> N408
    N612 --> N604
    N612 --> N541
    N612 --> N436
    N612 --> N389
    N612 --> N416
    N612 --> N432
    N612 --> N471
    N612 --> N524
    N612 --> N472
    N612 --> N587
    N612 --> N391
    N612 --> N525
    N614 --> N541
    N614 --> N389
    N614 --> N416
    N614 --> N432
    N614 --> N471
    N614 --> N524
    N614 --> N472
    N614 --> N587
    N614 --> N391
    N614 --> N525
    N615 --> N541
    N615 --> N389
    N615 --> N416
    N615 --> N432
    N615 --> N471
    N615 --> N524
    N615 --> N472
    N615 --> N587
    N616 --> N472
    N616 --> N587
    N617 --> N408
    N617 --> N604
    N617 --> N472
    N617 --> N587
    N617 --> N391
    N617 --> N525
    N618 --> N408
    N618 --> N604
    N618 --> N541
    N618 --> N389
    N618 --> N416
    N618 --> N432
    N618 --> N471
    N618 --> N524
    N618 --> N472
    N618 --> N587
    N618 --> N391
    N618 --> N525
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
  - Imports: `threading`
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
  - Imports: `json`
  - Imports: `os`
  - Imports: `platform`
  - Imports: `psutil`
  - Imports: `pydantic`
  - Imports: `random`
  - Imports: `shutil`
  - Imports: `signal`
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
- **meridian_backend/src/core/bus.py**
  - Imports: `asyncio`
  - Imports: `typing`
- **meridian_backend/src/core/camera_sentinel.py**
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
- **meridian_backend/src/core/response_models.py**
  - Imports: `pydantic`
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
- **meridian_backend/src/tools/chrome_manager.py**
  - Imports: `database`
  - Imports: `os`
  - Imports: `playwright`
  - Imports: `shutil`
  - Imports: `subprocess`
  - Imports: `sys`
  - Imports: `time`
  - Imports: `typing`
  - Imports: `webbrowser`
- **meridian_backend/src/tools/clipboard.py**
  - Imports: `bson`
  - Imports: `database`
  - Imports: `platform`
  - Imports: `pyperclip`
  - Imports: `shutil`
  - Imports: `time`
  - Imports: `typing`
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
- **meridian_backend/src/tools/health_ingest.py**
  - Imports: `time`
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
  - Imports: `sys`
  - Imports: `tempfile`
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
  - Imports: `Mascot3DCharacter`
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
  - Imports: `DataBadge`
  - Imports: `config`
  - Imports: `react`
- **meridian_frontend/src/components/mobile/DropdownNav.tsx**
  - Imports: `lucide-react`
  - Imports: `react`
- **meridian_frontend/src/components/mobile/LiveThoughtCarousel.tsx**
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
  - Imports: `Mascot`
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