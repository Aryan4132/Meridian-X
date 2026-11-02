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
    N21["chat.py [meridian_backend/src/api]"]
    N22["deps.py [meridian_backend/src/api]"]
    N23["mcp.py [meridian_backend/src/api]"]
    N24["models_mgmt.py [meridian_backend/src/api]"]
    N25["perception.py [meridian_backend/src/api]"]
    N26["profile.py [meridian_backend/src/api]"]
    N27["rag.py [meridian_backend/src/api]"]
    N28["scheduler.py [meridian_backend/src/api]"]
    N29["swarm.py [meridian_backend/src/api]"]
    N30["system.py [meridian_backend/src/api]"]
    N31["vault.py [meridian_backend/src/api]"]
    N32["voice.py [meridian_backend/src/api]"]
    N33["websockets.py [meridian_backend/src/api]"]
    N34["workspace.py [meridian_backend/src/api]"]
    N35["__init__.py [meridian_backend/src/api]"]
    N36["action_journal.py [meridian_backend/src/core]"]
    N37["agent_status_stream.py [meridian_backend/src/core]"]
    N38["ar_bridge.py [meridian_backend/src/core]"]
    N39["atomic_storage.py [meridian_backend/src/core]"]
    N40["audit_logger.py [meridian_backend/src/core]"]
    N41["auth.py [meridian_backend/src/core]"]
    N42["behavior_monitor.py [meridian_backend/src/core]"]
    N43["boilerplate_genie.py [meridian_backend/src/core]"]
    N44["breach_sentinel.py [meridian_backend/src/core]"]
    N45["bus.py [meridian_backend/src/core]"]
    N46["camera_sentinel.py [meridian_backend/src/core]"]
    N47["checkpoints.py [meridian_backend/src/core]"]
    N48["clipboard.py [meridian_backend/src/core]"]
    N49["code_graph.py [meridian_backend/src/core]"]
    N50["cognitive_graph.py [meridian_backend/src/core]"]
    N51["commit_whisperer.py [meridian_backend/src/core]"]
    N52["config.py [meridian_backend/src/core]"]
    N53["confirmations.py [meridian_backend/src/core]"]
    N54["consensus_engine.py [meridian_backend/src/core]"]
    N55["deep_project_context.py [meridian_backend/src/core]"]
    N56["dev_automation.py [meridian_backend/src/core]"]
    N57["discord_bridge.py [meridian_backend/src/core]"]
    N58["discord_utils.py [meridian_backend/src/core]"]
    N59["doc_generator.py [meridian_backend/src/core]"]
    N60["doc_indexer.py [meridian_backend/src/core]"]
    N61["elevated_runner.py [meridian_backend/src/core]"]
    N62["emergency_lockdown.py [meridian_backend/src/core]"]
    N63["error_diagnostics.py [meridian_backend/src/core]"]
    N64["experiment_runner.py [meridian_backend/src/core]"]
    N65["explain_code_engine.py [meridian_backend/src/core]"]
    N66["exporter.py [meridian_backend/src/core]"]
    N67["fim_sentinel.py [meridian_backend/src/core]"]
    N68["gaze_tracker.py [meridian_backend/src/core]"]
    N69["governor.py [meridian_backend/src/core]"]
    N70["graph_rag.py [meridian_backend/src/core]"]
    N71["graph_sync.py [meridian_backend/src/core]"]
    N72["hardware_detector.py [meridian_backend/src/core]"]
    N73["history_manager.py [meridian_backend/src/core]"]
    N74["lifespan.py [meridian_backend/src/core]"]
    N75["llm_auth.py [meridian_backend/src/core]"]
    N76["llm_client.py [meridian_backend/src/core]"]
    N77["llm_clients.py [meridian_backend/src/core]"]
    N78["llm_provider.py [meridian_backend/src/core]"]
    N79["local_model_manager.py [meridian_backend/src/core]"]
    N80["logger.py [meridian_backend/src/core]"]
    N81["logging_config.py [meridian_backend/src/core]"]
    N82["loop.py [meridian_backend/src/core]"]
    N83["loop_dispatcher.py [meridian_backend/src/core]"]
    N84["loop_executor.py [meridian_backend/src/core]"]
    N85["loop_parser.py [meridian_backend/src/core]"]
    N86["loop_planning.py [meridian_backend/src/core]"]
    N87["loop_stream.py [meridian_backend/src/core]"]
    N88["lsp_client.py [meridian_backend/src/core]"]
    N89["malware_scanner.py [meridian_backend/src/core]"]
    N90["mcp_client.py [meridian_backend/src/core]"]
    N91["mcp_executor.py [meridian_backend/src/core]"]
    N92["memory_backup.py [meridian_backend/src/core]"]
    N93["memory_consolidation.py [meridian_backend/src/core]"]
    N94["memory_editor.py [meridian_backend/src/core]"]
    N95["mobile_bridge.py [meridian_backend/src/core]"]
    N96["mode.py [meridian_backend/src/core]"]
    N97["neural_rag.py [meridian_backend/src/core]"]
    N98["oauth_manager.py [meridian_backend/src/core]"]
    N99["ollama_manager.py [meridian_backend/src/core]"]
    N100["p2p.py [meridian_backend/src/core]"]
    N101["p2p_crypto.py [meridian_backend/src/core]"]
    N102["p2p_discovery.py [meridian_backend/src/core]"]
    N103["p2p_pairing.py [meridian_backend/src/core]"]
    N104["perception.py [meridian_backend/src/core]"]
    N105["persistence_sentinel.py [meridian_backend/src/core]"]
    N106["personal_crm.py [meridian_backend/src/core]"]
    N107["plugins.py [meridian_backend/src/core]"]
    N108["polyglot.py [meridian_backend/src/core]"]
    N109["predictive_engine.py [meridian_backend/src/core]"]
    N110["presence_briefing.py [meridian_backend/src/core]"]
    N111["proactive_system_guard.py [meridian_backend/src/core]"]
    N112["prompt_injection.py [meridian_backend/src/core]"]
    N113["prompt_templates.py [meridian_backend/src/core]"]
    N114["rag_optimizer.py [meridian_backend/src/core]"]
    N115["reflection_engine.py [meridian_backend/src/core]"]
    N116["response_models.py [meridian_backend/src/core]"]
    N117["sandbox_runner.py [meridian_backend/src/core]"]
    N118["scheduler.py [meridian_backend/src/core]"]
    N119["screen_sense.py [meridian_backend/src/core]"]
    N120["security_middleware.py [meridian_backend/src/core]"]
    N121["self_evolving_tooling.py [meridian_backend/src/core]"]
    N122["silent_workflow_guardian.py [meridian_backend/src/core]"]
    N123["skills_loader.py [meridian_backend/src/core]"]
    N124["sos_protocol.py [meridian_backend/src/core]"]
    N125["speculative.py [meridian_backend/src/core]"]
    N126["swarm.py [meridian_backend/src/core]"]
    N127["system_defense.py [meridian_backend/src/core]"]
    N128["telegram_bridge.py [meridian_backend/src/core]"]
    N129["temporal_memory.py [meridian_backend/src/core]"]
    N130["tool_indexer.py [meridian_backend/src/core]"]
    N131["tool_regression_sentinel.py [meridian_backend/src/core]"]
    N132["triggers.py [meridian_backend/src/core]"]
    N133["updater.py [meridian_backend/src/core]"]
    N134["vault.py [meridian_backend/src/core]"]
    N135["vision.py [meridian_backend/src/core]"]
    N136["vision_face.py [meridian_backend/src/core]"]
    N137["vision_gesture.py [meridian_backend/src/core]"]
    N138["watcher.py [meridian_backend/src/core]"]
    N139["what_broke_detective.py [meridian_backend/src/core]"]
    N140["workflow_engine.py [meridian_backend/src/core]"]
    N141["workspace_orchestrator.py [meridian_backend/src/core]"]
    N142["commits.py [meridian_backend/src/core/proactive]"]
    N143["dispatcher.py [meridian_backend/src/core/proactive]"]
    N144["ergonomics.py [meridian_backend/src/core/proactive]"]
    N145["guard.py [meridian_backend/src/core/proactive]"]
    N146["__init__.py [meridian_backend/src/core/proactive]"]
    N147["cache.py [meridian_backend/src/db]"]
    N148["connection.py [meridian_backend/src/db]"]
    N149["contacts.py [meridian_backend/src/db]"]
    N150["conversations.py [meridian_backend/src/db]"]
    N151["embeddings.py [meridian_backend/src/db]"]
    N152["logs.py [meridian_backend/src/db]"]
    N153["memory.py [meridian_backend/src/db]"]
    N154["parsers.py [meridian_backend/src/db]"]
    N155["profile.py [meridian_backend/src/db]"]
    N156["rag.py [meridian_backend/src/db]"]
    N157["vectors.py [meridian_backend/src/db]"]
    N158["__init__.py [meridian_backend/src/db]"]
    N159["auto_reviewer.py [meridian_backend/src/tools]"]
    N160["bill_radar.py [meridian_backend/src/tools]"]
    N161["bookmark_manager.py [meridian_backend/src/tools]"]
    N162["browser_agent.py [meridian_backend/src/tools]"]
    N163["browser_use_agent.py [meridian_backend/src/tools]"]
    N164["cam_guard.py [meridian_backend/src/tools]"]
    N165["chrome_manager.py [meridian_backend/src/tools]"]
    N166["clipboard.py [meridian_backend/src/tools]"]
    N167["communication.py [meridian_backend/src/tools]"]
    N168["db_query.py [meridian_backend/src/tools]"]
    N169["desktop.py [meridian_backend/src/tools]"]
    N170["detonation_sandbox.py [meridian_backend/src/tools]"]
    N171["developer.py [meridian_backend/src/tools]"]
    N172["dns_shield.py [meridian_backend/src/tools]"]
    N173["documents.py [meridian_backend/src/tools]"]
    N174["documents_office.py [meridian_backend/src/tools]"]
    N175["documents_slides.py [meridian_backend/src/tools]"]
    N176["dynamic_manager.py [meridian_backend/src/tools]"]
    N177["expiry_sentinel.py [meridian_backend/src/tools]"]
    N178["exporter.py [meridian_backend/src/tools]"]
    N179["external_connectors.py [meridian_backend/src/tools]"]
    N180["filesystem.py [meridian_backend/src/tools]"]
    N181["file_janitor.py [meridian_backend/src/tools]"]
    N182["finance_sentinel.py [meridian_backend/src/tools]"]
    N183["geo_location.py [meridian_backend/src/tools]"]
    N184["health_ingest.py [meridian_backend/src/tools]"]
    N185["household.py [meridian_backend/src/tools]"]
    N186["knowledge.py [meridian_backend/src/tools]"]
    N187["learning_queue.py [meridian_backend/src/tools]"]
    N188["mcp_marketplace.py [meridian_backend/src/tools]"]
    N189["network_guardian.py [meridian_backend/src/tools]"]
    N190["networth_tracker.py [meridian_backend/src/tools]"]
    N191["ollama_manager.py [meridian_backend/src/tools]"]
    N192["papercoder.py [meridian_backend/src/tools]"]
    N193["password_auditor.py [meridian_backend/src/tools]"]
    N194["phishing_guard.py [meridian_backend/src/tools]"]
    N195["phone_agent.py [meridian_backend/src/tools]"]
    N196["price_watcher.py [meridian_backend/src/tools]"]
    N197["recording.py [meridian_backend/src/tools]"]
    N198["registry.py [meridian_backend/src/tools]"]
    N199["review.py [meridian_backend/src/tools]"]
    N200["scheduler.py [meridian_backend/src/tools]"]
    N201["screenshot_memory.py [meridian_backend/src/tools]"]
    N202["search_hub.py [meridian_backend/src/tools]"]
    N203["security_auditor.py [meridian_backend/src/tools]"]
    N204["shell.py [meridian_backend/src/tools]"]
    N205["system.py [meridian_backend/src/tools]"]
    N206["system_windows.py [meridian_backend/src/tools]"]
    N207["task_scheduler.py [meridian_backend/src/tools]"]
    N208["totp_generator.py [meridian_backend/src/tools]"]
    N209["travel_butler.py [meridian_backend/src/tools]"]
    N210["usb_watchdog.py [meridian_backend/src/tools]"]
    N211["vault.py [meridian_backend/src/tools]"]
    N212["video_editor.py [meridian_backend/src/tools]"]
    N213["voice.py [meridian_backend/src/tools]"]
    N214["watcher.py [meridian_backend/src/tools]"]
    N215["web.py [meridian_backend/src/tools]"]
    N216["web_browser.py [meridian_backend/src/tools]"]
    N217["web_scraper.py [meridian_backend/src/tools]"]
    N218["wellness.py [meridian_backend/src/tools]"]
    N219["whatsapp_manager.py [meridian_backend/src/tools]"]
    N220["wifi_assessor.py [meridian_backend/src/tools]"]
    N221["workspace_layout.py [meridian_backend/src/tools]"]
    N222["ambient_listener.py [meridian_backend/src/voice]"]
    N223["duplex.py [meridian_backend/src/voice]"]
    N224["polyglot.py [meridian_backend/src/voice]"]
    N225["stt.py [meridian_backend/src/voice]"]
    N226["tts.py [meridian_backend/src/voice]"]
    N227["vad.py [meridian_backend/src/voice]"]
    N228["voice_biometrics.py [meridian_backend/src/voice]"]
    N229["wakeword.py [meridian_backend/src/voice]"]
    N230["conftest.py [meridian_backend/tests]"]
    N231["run_tests.py [meridian_backend/tests]"]
    N232["test_advanced_proactive.py [meridian_backend/tests]"]
    N233["test_atomic_storage.py [meridian_backend/tests]"]
    N234["test_audit_bugfixes.py [meridian_backend/tests]"]
    N235["test_audit_remediation.py [meridian_backend/tests]"]
    N236["test_auto_bug_fixer.py [meridian_backend/tests]"]
    N237["test_backend_improvements.py [meridian_backend/tests]"]
    N238["test_backlog_features.py [meridian_backend/tests]"]
    N239["test_backlog_sprint.py [meridian_backend/tests]"]
    N240["test_bridges.py [meridian_backend/tests]"]
    N241["test_browser_agent.py [meridian_backend/tests]"]
    N242["test_browser_fallback.py [meridian_backend/tests]"]
    N243["test_browser_frame.py [meridian_backend/tests]"]
    N244["test_browser_use.py [meridian_backend/tests]"]
    N245["test_butler_media.py [meridian_backend/tests]"]
    N246["test_chat_abort.py [meridian_backend/tests]"]
    N247["test_cognitive_graph.py [meridian_backend/tests]"]
    N248["test_config.py [meridian_backend/tests]"]
    N249["test_consensus_gate.py [meridian_backend/tests]"]
    N250["test_context_budget.py [meridian_backend/tests]"]
    N251["test_custom_password_auth.py [meridian_backend/tests]"]
    N252["test_database.py [meridian_backend/tests]"]
    N253["test_day10_features.py [meridian_backend/tests]"]
    N254["test_day11_features.py [meridian_backend/tests]"]
    N255["test_day12_features.py [meridian_backend/tests]"]
    N256["test_day13_features.py [meridian_backend/tests]"]
    N257["test_day14_day15_features.py [meridian_backend/tests]"]
    N258["test_day16_17_18_features.py [meridian_backend/tests]"]
    N259["test_day3_features.py [meridian_backend/tests]"]
    N260["test_day4_features.py [meridian_backend/tests]"]
    N261["test_day5_features.py [meridian_backend/tests]"]
    N262["test_day6_features.py [meridian_backend/tests]"]
    N263["test_day7_features.py [meridian_backend/tests]"]
    N264["test_day8_features.py [meridian_backend/tests]"]
    N265["test_day9_features.py [meridian_backend/tests]"]
    N266["test_dev_intelligence_suite.py [meridian_backend/tests]"]
    N267["test_document_tools.py [meridian_backend/tests]"]
    N268["test_error_diagnostics.py [meridian_backend/tests]"]
    N269["test_exhaustive_fallback.py [meridian_backend/tests]"]
    N270["test_full_proactive_suite.py [meridian_backend/tests]"]
    N271["test_geo_location.py [meridian_backend/tests]"]
    N272["test_hybrid_rag.py [meridian_backend/tests]"]
    N273["test_jarvis_perception.py [meridian_backend/tests]"]
    N274["test_known_errors_remediation.py [meridian_backend/tests]"]
    N275["test_llm_provider.py [meridian_backend/tests]"]
    N276["test_logging.py [meridian_backend/tests]"]
    N277["test_loop_parser.py [meridian_backend/tests]"]
    N278["test_loop_submodules.py [meridian_backend/tests]"]
    N279["test_mobile_websocket.py [meridian_backend/tests]"]
    N280["test_model_source.py [meridian_backend/tests]"]
    N281["test_multimode_routing.py [meridian_backend/tests]"]
    N282["test_multi_os.py [meridian_backend/tests]"]
    N283["test_new_features.py [meridian_backend/tests]"]
    N284["test_oauth.py [meridian_backend/tests]"]
    N285["test_p2p.py [meridian_backend/tests]"]
    N286["test_perception_bridge.py [meridian_backend/tests]"]
    N287["test_proactive.py [meridian_backend/tests]"]
    N288["test_proactive_mode.py [meridian_backend/tests]"]
    N289["test_proactive_notifications.py [meridian_backend/tests]"]
    N290["test_reflection_engine.py [meridian_backend/tests]"]
    N291["test_research_optimization.py [meridian_backend/tests]"]
    N292["test_response_resilience.py [meridian_backend/tests]"]
    N293["test_security_features.py [meridian_backend/tests]"]
    N294["test_silero_vad.py [meridian_backend/tests]"]
    N295["test_skill_packs.py [meridian_backend/tests]"]
    N296["test_sprint24_hardening.py [meridian_backend/tests]"]
    N297["test_sprint25_hardening.py [meridian_backend/tests]"]
    N298["test_sprint27_hardening.py [meridian_backend/tests]"]
    N299["test_sprint28_hardening.py [meridian_backend/tests]"]
    N300["test_sprint2_features.py [meridian_backend/tests]"]
    N301["test_sprint40.py [meridian_backend/tests]"]
    N302["test_sprint45.py [meridian_backend/tests]"]
    N303["test_standalone_bridge.py [meridian_backend/tests]"]
    N304["test_stream_resiliency.py [meridian_backend/tests]"]
    N305["test_swarm.py [meridian_backend/tests]"]
    N306["test_swarm_routing.py [meridian_backend/tests]"]
    N307["test_system_hardening.py [meridian_backend/tests]"]
    N308["test_tools.py [meridian_backend/tests]"]
    N309["test_tool_intelligence.py [meridian_backend/tests]"]
    N310["test_tool_modernization.py [meridian_backend/tests]"]
    N311["test_tool_regression.py [meridian_backend/tests]"]
    N312["test_user_delight_tools.py [meridian_backend/tests]"]
    N313["test_vault.py [meridian_backend/tests]"]
    N314["test_video_editor.py [meridian_backend/tests]"]
    N315["test_voice_hardening.py [meridian_backend/tests]"]
    N316["test_voice_speed.py [meridian_backend/tests]"]
    N317["test_wakeword_continuous.py [meridian_backend/tests]"]
    N318["test_wakeword_onnx.py [meridian_backend/tests]"]
    N319["test_web_guards.py [meridian_backend/tests]"]
    N320["test_workflow.py [meridian_backend/tests]"]
    N321["vite.config.ts [meridian_frontend]"]
    N322["AppContext.tsx [meridian_frontend/src]"]
    N323["main.tsx [meridian_frontend/src]"]
    N324["Mascot.tsx [meridian_frontend/src]"]
    N325["Mascot3DCharacter.tsx [meridian_frontend/src]"]
    N326["MobileApp.tsx [meridian_frontend/src]"]
    N327["AgentStatusStream.tsx [meridian_frontend/src/components]"]
    N328["CommandPalette.tsx [meridian_frontend/src/components]"]
    N329["DevAutomationPanel.tsx [meridian_frontend/src/components]"]
    N330["DeveloperSuitePanel.tsx [meridian_frontend/src/components]"]
    N331["LocalModelManager.tsx [meridian_frontend/src/components]"]
    N332["MemoryConsolidationView.tsx [meridian_frontend/src/components]"]
    N333["NavRail.tsx [meridian_frontend/src/components]"]
    N334["PerceptionHUD.tsx [meridian_frontend/src/components]"]
    N335["ProactiveGuardBanner.tsx [meridian_frontend/src/components]"]
    N336["ProfileHeader.tsx [meridian_frontend/src/components]"]
    N337["RightDrawer.tsx [meridian_frontend/src/components]"]
    N338["ServerConnectionModal.tsx [meridian_frontend/src/components]"]
    N339["Shell.tsx [meridian_frontend/src/components]"]
    N340["StatusBar.tsx [meridian_frontend/src/components]"]
    N341["DropdownNav.tsx [meridian_frontend/src/components/mobile]"]
    N342["LiveThoughtCarousel.tsx [meridian_frontend/src/components/mobile]"]
    N343["MobilePairingModal.tsx [meridian_frontend/src/components/mobile]"]
    N344["VoiceOrbHUD.tsx [meridian_frontend/src/components/mobile]"]
    N345["AmbientParticles.tsx [meridian_frontend/src/components/ui]"]
    N346["CodeDiffViewer.tsx [meridian_frontend/src/components/ui]"]
    N347["ConnectionBanner.tsx [meridian_frontend/src/components/ui]"]
    N348["DataBadge.tsx [meridian_frontend/src/components/ui]"]
    N349["GlowCard.tsx [meridian_frontend/src/components/ui]"]
    N350["HoloButton.tsx [meridian_frontend/src/components/ui]"]
    N351["ProgressArc.tsx [meridian_frontend/src/components/ui]"]
    N352["TerminalLine.tsx [meridian_frontend/src/components/ui]"]
    N353["ToastContext.tsx [meridian_frontend/src/components/ui]"]
    N354["useMemoryOptimizer.ts [meridian_frontend/src/hooks]"]
    N355["oauthService.ts [meridian_frontend/src/services]"]
    N356["streamingAudioPlayer.ts [meridian_frontend/src/services]"]
    N357["BackendSetup.tsx [meridian_frontend/src/startup]"]
    N358["BootSequence.tsx [meridian_frontend/src/startup]"]
    N359["OnboardingWizard.tsx [meridian_frontend/src/startup]"]
    N360["SetupWizard.tsx [meridian_frontend/src/startup]"]
    N361["Clipboard.tsx [meridian_frontend/src/views]"]
    N362["Jobs.tsx [meridian_frontend/src/views]"]
    N363["MemoryEditor.tsx [meridian_frontend/src/views]"]
    N364["Productivity.tsx [meridian_frontend/src/views]"]
    N365["Settings.tsx [meridian_frontend/src/views]"]
    N366["SwarmDebate.tsx [meridian_frontend/src/views]"]
    N367["Timeline.tsx [meridian_frontend/src/views]"]
    N368["WorkflowBuilder.tsx [meridian_frontend/src/views]"]
    N369["AiModelsTab.tsx [meridian_frontend/src/views/settings]"]
    N370["IntegrationsTab.tsx [meridian_frontend/src/views/settings]"]
    N371["MascotTab.tsx [meridian_frontend/src/views/settings]"]
    N372["MultiModeTab.tsx [meridian_frontend/src/views/settings]"]
    N373["PasswordInput.tsx [meridian_frontend/src/views/settings]"]
    N374["SpendAirGapTab.tsx [meridian_frontend/src/views/settings]"]
    N375["SystemGuardTab.tsx [meridian_frontend/src/views/settings]"]
    N376["VoiceTab.tsx [meridian_frontend/src/views/settings]"]
    N377["config.py [meridian_frontend/src-tauri/api/_internal/cv2]"]
    N378["load_config_py3.py [meridian_frontend/src-tauri/api/_internal/cv2]"]
    N379["__init__.py [meridian_frontend/src-tauri/api/_internal/cv2]"]
    N380["__init__.py [meridian_frontend/src-tauri/api/_internal/cv2/data]"]
    N381["__init__.py [meridian_frontend/src-tauri/api/_internal/cv2/mat_wrapper]"]
    N382["version.py [meridian_frontend/src-tauri/api/_internal/cv2/misc]"]
    N383["__init__.py [meridian_frontend/src-tauri/api/_internal/cv2/typing]"]
    N384["__init__.py [meridian_frontend/src-tauri/api/_internal/cv2/utils]"]
    N385["applications.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N386["background.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N387["cli.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N388["concurrency.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N389["datastructures.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N390["encoders.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N391["exceptions.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N392["exception_handlers.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N393["logger.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N394["params.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N395["param_functions.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N396["requests.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N397["responses.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N398["routing.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N399["sse.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N400["staticfiles.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N401["templating.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N402["testclient.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N403["types.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N404["utils.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N405["websockets.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N406["__init__.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N407["__main__.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N408["models.py [meridian_frontend/src-tauri/api/_internal/fastapi/dependencies]"]
    N409["utils.py [meridian_frontend/src-tauri/api/_internal/fastapi/dependencies]"]
    N410["asyncexitstack.py [meridian_frontend/src-tauri/api/_internal/fastapi/middleware]"]
    N411["cors.py [meridian_frontend/src-tauri/api/_internal/fastapi/middleware]"]
    N412["gzip.py [meridian_frontend/src-tauri/api/_internal/fastapi/middleware]"]
    N413["httpsredirect.py [meridian_frontend/src-tauri/api/_internal/fastapi/middleware]"]
    N414["trustedhost.py [meridian_frontend/src-tauri/api/_internal/fastapi/middleware]"]
    N415["wsgi.py [meridian_frontend/src-tauri/api/_internal/fastapi/middleware]"]
    N416["__init__.py [meridian_frontend/src-tauri/api/_internal/fastapi/middleware]"]
    N417["docs.py [meridian_frontend/src-tauri/api/_internal/fastapi/openapi]"]
    N418["models.py [meridian_frontend/src-tauri/api/_internal/fastapi/openapi]"]
    N419["utils.py [meridian_frontend/src-tauri/api/_internal/fastapi/openapi]"]
    N420["api_key.py [meridian_frontend/src-tauri/api/_internal/fastapi/security]"]
    N421["base.py [meridian_frontend/src-tauri/api/_internal/fastapi/security]"]
    N422["http.py [meridian_frontend/src-tauri/api/_internal/fastapi/security]"]
    N423["oauth2.py [meridian_frontend/src-tauri/api/_internal/fastapi/security]"]
    N424["open_id_connect_url.py [meridian_frontend/src-tauri/api/_internal/fastapi/security]"]
    N425["shared.py [meridian_frontend/src-tauri/api/_internal/fastapi/_compat]"]
    N426["v2.py [meridian_frontend/src-tauri/api/_internal/fastapi/_compat]"]
    N427["coreBundle.js [meridian_frontend/src-tauri/api/_internal/playwright/driver/package/lib]"]
    N428["utilsBundle.js [meridian_frontend/src-tauri/api/_internal/playwright/driver/package/lib]"]
    N429["structs.d.ts [meridian_frontend/src-tauri/api/_internal/playwright/driver/package/types]"]
    N430["types.d.ts [meridian_frontend/src-tauri/api/_internal/playwright/driver/package/types]"]
    N431["aliases.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N432["alias_generators.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N433["annotated_handlers.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N434["color.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N435["config.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N436["dataclasses.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N437["errors.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N438["fields.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N439["functional_serializers.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N440["functional_validators.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N441["json_schema.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N442["main.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N443["mypy.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N444["networks.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N445["root_model.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N446["types.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N447["type_adapter.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N448["validate_call_decorator.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N449["version.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N450["warnings.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N451["_migration.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N452["__init__.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N453["class_validators.py [meridian_frontend/src-tauri/api/_internal/pydantic/deprecated]"]
    N454["config.py [meridian_frontend/src-tauri/api/_internal/pydantic/deprecated]"]
    N455["copy_internals.py [meridian_frontend/src-tauri/api/_internal/pydantic/deprecated]"]
    N456["decorator.py [meridian_frontend/src-tauri/api/_internal/pydantic/deprecated]"]
    N457["json.py [meridian_frontend/src-tauri/api/_internal/pydantic/deprecated]"]
    N458["parse.py [meridian_frontend/src-tauri/api/_internal/pydantic/deprecated]"]
    N459["tools.py [meridian_frontend/src-tauri/api/_internal/pydantic/deprecated]"]
    N460["arguments_schema.py [meridian_frontend/src-tauri/api/_internal/pydantic/experimental]"]
    N461["missing_sentinel.py [meridian_frontend/src-tauri/api/_internal/pydantic/experimental]"]
    N462["pipeline.py [meridian_frontend/src-tauri/api/_internal/pydantic/experimental]"]
    N463["_loader.py [meridian_frontend/src-tauri/api/_internal/pydantic/plugin]"]
    N464["_schema_validator.py [meridian_frontend/src-tauri/api/_internal/pydantic/plugin]"]
    N465["__init__.py [meridian_frontend/src-tauri/api/_internal/pydantic/plugin]"]
    N466["annotated_types.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N467["class_validators.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N468["color.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N469["config.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N470["dataclasses.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N471["datetime_parse.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N472["decorator.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N473["env_settings.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N474["errors.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N475["error_wrappers.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N476["fields.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N477["generics.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N478["json.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N479["main.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N480["mypy.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N481["networks.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N482["parse.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N483["schema.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N484["tools.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N485["types.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N486["typing.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N487["utils.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N488["validators.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N489["version.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N490["_hypothesis_plugin.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N491["__init__.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N492["_config.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N493["_core_metadata.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N494["_core_utils.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N495["_dataclasses.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N496["_decorators.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N497["_decorators_v1.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N498["_discriminated_union.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N499["_docs_extraction.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N500["_fields.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N501["_forward_ref.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N502["_generate_schema.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N503["_generics.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N504["_git.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N505["_import_utils.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N506["_internal_dataclass.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N507["_known_annotated_metadata.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N508["_mock_val_ser.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N509["_model_construction.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N510["_namespace_utils.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N511["_repr.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N512["_schema_gather.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N513["_schema_generation_shared.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N514["_serializers.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N515["_signature.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N516["_typing_extra.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N517["_utils.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N518["_validate_call.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N519["_validators.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N520["applications.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N521["authentication.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N522["background.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N523["concurrency.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N524["config.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N525["convertors.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N526["datastructures.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N527["endpoints.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N528["exceptions.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N529["formparsers.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N530["requests.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N531["responses.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N532["routing.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N533["schemas.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N534["staticfiles.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N535["status.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N536["templating.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N537["testclient.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N538["types.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N539["websockets.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N540["_exception_handler.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N541["_utils.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N542["authentication.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N543["base.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N544["cors.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N545["errors.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N546["exceptions.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N547["gzip.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N548["httpsredirect.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N549["sessions.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N550["trustedhost.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N551["wsgi.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N552["__init__.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N553["config.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N554["importer.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N555["logging.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N556["main.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N557["server.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N558["workers.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N559["_compat.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N560["_subprocess.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N561["_types.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N562["__init__.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N563["__main__.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N564["off.py [meridian_frontend/src-tauri/api/_internal/uvicorn/lifespan]"]
    N565["on.py [meridian_frontend/src-tauri/api/_internal/uvicorn/lifespan]"]
    N566["asyncio.py [meridian_frontend/src-tauri/api/_internal/uvicorn/loops]"]
    N567["auto.py [meridian_frontend/src-tauri/api/_internal/uvicorn/loops]"]
    N568["uvloop.py [meridian_frontend/src-tauri/api/_internal/uvicorn/loops]"]
    N569["asgi2.py [meridian_frontend/src-tauri/api/_internal/uvicorn/middleware]"]
    N570["message_logger.py [meridian_frontend/src-tauri/api/_internal/uvicorn/middleware]"]
    N571["proxy_headers.py [meridian_frontend/src-tauri/api/_internal/uvicorn/middleware]"]
    N572["wsgi.py [meridian_frontend/src-tauri/api/_internal/uvicorn/middleware]"]
    N573["utils.py [meridian_frontend/src-tauri/api/_internal/uvicorn/protocols]"]
    N574["auto.py [meridian_frontend/src-tauri/api/_internal/uvicorn/protocols/http]"]
    N575["flow_control.py [meridian_frontend/src-tauri/api/_internal/uvicorn/protocols/http]"]
    N576["h11_impl.py [meridian_frontend/src-tauri/api/_internal/uvicorn/protocols/http]"]
    N577["httptools_impl.py [meridian_frontend/src-tauri/api/_internal/uvicorn/protocols/http]"]
    N578["auto.py [meridian_frontend/src-tauri/api/_internal/uvicorn/protocols/websockets]"]
    N579["websockets_impl.py [meridian_frontend/src-tauri/api/_internal/uvicorn/protocols/websockets]"]
    N580["websockets_sansio_impl.py [meridian_frontend/src-tauri/api/_internal/uvicorn/protocols/websockets]"]
    N581["wsproto_impl.py [meridian_frontend/src-tauri/api/_internal/uvicorn/protocols/websockets]"]
    N582["basereload.py [meridian_frontend/src-tauri/api/_internal/uvicorn/supervisors]"]
    N583["multiprocess.py [meridian_frontend/src-tauri/api/_internal/uvicorn/supervisors]"]
    N584["statreload.py [meridian_frontend/src-tauri/api/_internal/uvicorn/supervisors]"]
    N585["watchfilesreload.py [meridian_frontend/src-tauri/api/_internal/uvicorn/supervisors]"]
    N586["__init__.py [meridian_frontend/src-tauri/api/_internal/uvicorn/supervisors]"]
    N587["auth.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N588["cli.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N589["client.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N590["connection.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N591["datastructures.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N592["exceptions.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N593["frames.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N594["headers.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N595["http11.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N596["imports.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N597["protocol.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N598["proxy.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N599["server.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N600["streams.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N601["typing.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N602["uri.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N603["utils.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N604["version.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N605["__init__.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N606["client.py [meridian_frontend/src-tauri/api/_internal/websockets/asyncio]"]
    N607["connection.py [meridian_frontend/src-tauri/api/_internal/websockets/asyncio]"]
    N608["messages.py [meridian_frontend/src-tauri/api/_internal/websockets/asyncio]"]
    N609["router.py [meridian_frontend/src-tauri/api/_internal/websockets/asyncio]"]
    N610["server.py [meridian_frontend/src-tauri/api/_internal/websockets/asyncio]"]
    N611["base.py [meridian_frontend/src-tauri/api/_internal/websockets/extensions]"]
    N612["permessage_deflate.py [meridian_frontend/src-tauri/api/_internal/websockets/extensions]"]
    N613["auth.py [meridian_frontend/src-tauri/api/_internal/websockets/legacy]"]
    N614["client.py [meridian_frontend/src-tauri/api/_internal/websockets/legacy]"]
    N615["exceptions.py [meridian_frontend/src-tauri/api/_internal/websockets/legacy]"]
    N616["framing.py [meridian_frontend/src-tauri/api/_internal/websockets/legacy]"]
    N617["handshake.py [meridian_frontend/src-tauri/api/_internal/websockets/legacy]"]
    N618["http.py [meridian_frontend/src-tauri/api/_internal/websockets/legacy]"]
    N619["protocol.py [meridian_frontend/src-tauri/api/_internal/websockets/legacy]"]
    N620["server.py [meridian_frontend/src-tauri/api/_internal/websockets/legacy]"]
    N621["__init__.py [meridian_frontend/src-tauri/api/_internal/websockets/legacy]"]
    N622["client.py [meridian_frontend/src-tauri/api/_internal/websockets/sync]"]
    N623["connection.py [meridian_frontend/src-tauri/api/_internal/websockets/sync]"]
    N624["messages.py [meridian_frontend/src-tauri/api/_internal/websockets/sync]"]
    N625["router.py [meridian_frontend/src-tauri/api/_internal/websockets/sync]"]
    N626["server.py [meridian_frontend/src-tauri/api/_internal/websockets/sync]"]
    N627["utils.py [meridian_frontend/src-tauri/api/_internal/websockets/sync]"]
    N628["client.py [meridian_frontend/src-tauri/api/_internal/websockets/trio]"]
    N629["connection.py [meridian_frontend/src-tauri/api/_internal/websockets/trio]"]
    N630["messages.py [meridian_frontend/src-tauri/api/_internal/websockets/trio]"]
    N631["router.py [meridian_frontend/src-tauri/api/_internal/websockets/trio]"]
    N632["server.py [meridian_frontend/src-tauri/api/_internal/websockets/trio]"]
    N633["utils.py [meridian_frontend/src-tauri/api/_internal/websockets/trio]"]
    N634["build_apk.py [meridian_mobile]"]
    N635["flutter_lldb_helper.py [meridian_mobile/ios/Flutter/ephemeral]"]
    N636["get_system_platform_info.py [plugins]"]

    N1 --> N457
    N1 --> N478
    N1 --> N486
    N1 --> N601
    N2 --> N457
    N2 --> N478
    N2 --> N486
    N2 --> N601
    N3 --> N457
    N3 --> N478
    N4 --> N457
    N4 --> N478
    N4 --> N486
    N4 --> N601
    N5 --> N566
    N5 --> N457
    N5 --> N478
    N5 --> N15
    N5 --> N14
    N9 --> N457
    N9 --> N478
    N9 --> N486
    N9 --> N601
    N10 --> N436
    N10 --> N470
    N13 --> N10
    N13 --> N52
    N13 --> N377
    N13 --> N435
    N13 --> N454
    N13 --> N469
    N13 --> N524
    N13 --> N553
    N13 --> N12
    N13 --> N11
    N14 --> N457
    N14 --> N478
    N14 --> N555
    N14 --> N566
    N14 --> N486
    N14 --> N601
    N14 --> N15
    N16 --> N457
    N16 --> N478
    N16 --> N566
    N16 --> N555
    N16 --> N486
    N16 --> N601
    N20 --> N457
    N20 --> N478
    N20 --> N486
    N20 --> N601
    N20 --> N15
    N21 --> N457
    N21 --> N478
    N21 --> N566
    N21 --> N486
    N21 --> N601
    N21 --> N15
    N22 --> N457
    N22 --> N478
    N22 --> N555
    N22 --> N486
    N22 --> N601
    N22 --> N15
    N23 --> N457
    N23 --> N478
    N23 --> N486
    N23 --> N601
    N24 --> N457
    N24 --> N478
    N24 --> N486
    N24 --> N601
    N24 --> N15
    N25 --> N486
    N25 --> N601
    N26 --> N486
    N26 --> N601
    N26 --> N15
    N27 --> N486
    N27 --> N601
    N27 --> N15
    N28 --> N457
    N28 --> N478
    N28 --> N486
    N28 --> N601
    N28 --> N15
    N29 --> N457
    N29 --> N478
    N29 --> N555
    N29 --> N566
    N29 --> N486
    N29 --> N601
    N29 --> N15
    N30 --> N457
    N30 --> N478
    N30 --> N486
    N30 --> N601
    N30 --> N15
    N30 --> N566
    N31 --> N486
    N31 --> N601
    N32 --> N555
    N32 --> N486
    N32 --> N601
    N33 --> N457
    N33 --> N478
    N33 --> N566
    N33 --> N486
    N33 --> N601
    N34 --> N457
    N34 --> N478
    N34 --> N486
    N34 --> N601
    N34 --> N15
    N36 --> N457
    N36 --> N478
    N36 --> N555
    N36 --> N486
    N36 --> N601
    N36 --> N15
    N37 --> N566
    N37 --> N555
    N37 --> N486
    N37 --> N601
    N38 --> N555
    N38 --> N486
    N38 --> N601
    N39 --> N457
    N39 --> N478
    N39 --> N555
    N39 --> N486
    N39 --> N601
    N40 --> N457
    N40 --> N478
    N40 --> N555
    N41 --> N486
    N41 --> N601
    N41 --> N457
    N41 --> N478
    N42 --> N555
    N42 --> N486
    N42 --> N601
    N43 --> N555
    N43 --> N486
    N43 --> N601
    N44 --> N555
    N44 --> N486
    N44 --> N601
    N44 --> N457
    N44 --> N478
    N45 --> N566
    N45 --> N486
    N45 --> N601
    N46 --> N555
    N46 --> N486
    N46 --> N601
    N47 --> N566
    N47 --> N486
    N47 --> N601
    N48 --> N486
    N48 --> N601
    N48 --> N15
    N49 --> N486
    N49 --> N601
    N50 --> N457
    N50 --> N478
    N50 --> N555
    N50 --> N486
    N50 --> N601
    N51 --> N555
    N51 --> N486
    N51 --> N601
    N53 --> N566
    N53 --> N486
    N53 --> N601
    N53 --> N15
    N54 --> N457
    N54 --> N478
    N54 --> N555
    N54 --> N486
    N54 --> N601
    N54 --> N566
    N54 --> N15
    N55 --> N555
    N55 --> N486
    N55 --> N601
    N56 --> N566
    N56 --> N555
    N56 --> N486
    N56 --> N601
    N57 --> N566
    N57 --> N486
    N57 --> N601
    N57 --> N15
    N58 --> N486
    N58 --> N601
    N60 --> N457
    N60 --> N478
    N60 --> N555
    N60 --> N486
    N60 --> N601
    N60 --> N15
    N61 --> N555
    N61 --> N486
    N61 --> N601
    N62 --> N555
    N62 --> N486
    N62 --> N601
    N63 --> N486
    N63 --> N601
    N64 --> N555
    N64 --> N486
    N64 --> N601
    N65 --> N555
    N65 --> N486
    N65 --> N601
    N66 --> N486
    N66 --> N601
    N66 --> N15
    N67 --> N555
    N67 --> N486
    N67 --> N601
    N68 --> N555
    N68 --> N486
    N68 --> N601
    N69 --> N486
    N69 --> N601
    N70 --> N457
    N70 --> N478
    N70 --> N486
    N70 --> N601
    N71 --> N457
    N71 --> N478
    N71 --> N486
    N71 --> N601
    N72 --> N555
    N72 --> N486
    N72 --> N601
    N72 --> N450
    N72 --> N457
    N72 --> N478
    N74 --> N566
    N74 --> N555
    N74 --> N15
    N75 --> N555
    N75 --> N486
    N75 --> N601
    N75 --> N15
    N76 --> N566
    N76 --> N555
    N76 --> N486
    N76 --> N601
    N76 --> N15
    N77 --> N486
    N77 --> N601
    N77 --> N15
    N78 --> N457
    N78 --> N478
    N78 --> N555
    N78 --> N566
    N78 --> N486
    N78 --> N601
    N78 --> N15
    N79 --> N555
    N79 --> N566
    N79 --> N486
    N79 --> N601
    N79 --> N15
    N79 --> N457
    N79 --> N478
    N80 --> N457
    N80 --> N478
    N80 --> N555
    N80 --> N486
    N80 --> N601
    N81 --> N555
    N81 --> N457
    N81 --> N478
    N82 --> N457
    N82 --> N478
    N82 --> N566
    N82 --> N486
    N82 --> N601
    N82 --> N15
    N83 --> N457
    N83 --> N478
    N83 --> N566
    N83 --> N486
    N83 --> N601
    N83 --> N15
    N84 --> N457
    N84 --> N478
    N84 --> N486
    N84 --> N601
    N84 --> N15
    N85 --> N457
    N85 --> N478
    N85 --> N566
    N85 --> N486
    N85 --> N601
    N85 --> N15
    N86 --> N457
    N86 --> N478
    N86 --> N566
    N86 --> N486
    N86 --> N601
    N86 --> N15
    N87 --> N457
    N87 --> N478
    N87 --> N566
    N87 --> N486
    N87 --> N601
    N87 --> N15
    N88 --> N457
    N88 --> N478
    N88 --> N566
    N88 --> N486
    N88 --> N601
    N89 --> N555
    N89 --> N486
    N89 --> N601
    N90 --> N457
    N90 --> N478
    N90 --> N566
    N90 --> N555
    N90 --> N486
    N90 --> N601
    N91 --> N566
    N91 --> N457
    N91 --> N478
    N91 --> N555
    N91 --> N486
    N91 --> N601
    N92 --> N457
    N92 --> N478
    N92 --> N486
    N92 --> N601
    N93 --> N555
    N93 --> N566
    N93 --> N457
    N93 --> N478
    N93 --> N486
    N93 --> N601
    N93 --> N15
    N94 --> N457
    N94 --> N478
    N94 --> N486
    N94 --> N601
    N94 --> N15
    N95 --> N457
    N95 --> N478
    N95 --> N555
    N95 --> N486
    N95 --> N601
    N95 --> N15
    N95 --> N566
    N96 --> N486
    N96 --> N601
    N96 --> N15
    N96 --> N457
    N96 --> N478
    N97 --> N486
    N97 --> N601
    N98 --> N457
    N98 --> N478
    N98 --> N486
    N98 --> N601
    N99 --> N555
    N99 --> N566
    N99 --> N486
    N99 --> N601
    N99 --> N457
    N99 --> N478
    N100 --> N457
    N100 --> N478
    N100 --> N486
    N100 --> N601
    N100 --> N15
    N102 --> N486
    N102 --> N601
    N103 --> N486
    N103 --> N601
    N104 --> N555
    N104 --> N486
    N104 --> N601
    N105 --> N555
    N105 --> N486
    N105 --> N601
    N106 --> N555
    N106 --> N486
    N106 --> N601
    N106 --> N15
    N107 --> N486
    N107 --> N601
    N108 --> N555
    N108 --> N486
    N108 --> N601
    N109 --> N555
    N109 --> N486
    N109 --> N601
    N110 --> N555
    N110 --> N486
    N110 --> N601
    N111 --> N555
    N111 --> N486
    N111 --> N601
    N112 --> N555
    N112 --> N486
    N112 --> N601
    N113 --> N457
    N113 --> N478
    N113 --> N486
    N113 --> N601
    N114 --> N486
    N114 --> N601
    N115 --> N457
    N115 --> N478
    N115 --> N555
    N115 --> N486
    N115 --> N601
    N116 --> N486
    N116 --> N601
    N117 --> N555
    N117 --> N486
    N117 --> N601
    N118 --> N566
    N118 --> N450
    N118 --> N15
    N118 --> N457
    N118 --> N478
    N119 --> N566
    N119 --> N555
    N119 --> N486
    N119 --> N601
    N120 --> N555
    N120 --> N486
    N120 --> N601
    N121 --> N555
    N121 --> N486
    N121 --> N601
    N122 --> N555
    N122 --> N486
    N122 --> N601
    N123 --> N555
    N123 --> N486
    N123 --> N601
    N124 --> N555
    N124 --> N486
    N124 --> N601
    N124 --> N15
    N125 --> N457
    N125 --> N478
    N125 --> N566
    N125 --> N486
    N125 --> N601
    N125 --> N15
    N126 --> N566
    N126 --> N457
    N126 --> N478
    N126 --> N486
    N126 --> N601
    N126 --> N15
    N127 --> N555
    N127 --> N486
    N127 --> N601
    N128 --> N486
    N128 --> N601
    N128 --> N566
    N128 --> N15
    N129 --> N486
    N129 --> N601
    N130 --> N486
    N130 --> N601
    N131 --> N555
    N131 --> N486
    N131 --> N601
    N132 --> N486
    N132 --> N601
    N133 --> N555
    N133 --> N486
    N133 --> N601
    N134 --> N457
    N134 --> N478
    N134 --> N486
    N134 --> N601
    N135 --> N555
    N135 --> N486
    N135 --> N601
    N135 --> N15
    N136 --> N555
    N136 --> N486
    N136 --> N601
    N137 --> N555
    N137 --> N486
    N137 --> N601
    N138 --> N555
    N138 --> N486
    N138 --> N601
    N139 --> N555
    N139 --> N486
    N139 --> N601
    N140 --> N457
    N140 --> N478
    N140 --> N486
    N140 --> N601
    N141 --> N555
    N141 --> N486
    N141 --> N601
    N142 --> N486
    N142 --> N601
    N142 --> N15
    N142 --> N14
    N143 --> N566
    N143 --> N486
    N143 --> N601
    N144 --> N486
    N144 --> N601
    N145 --> N555
    N145 --> N486
    N145 --> N601
    N145 --> N15
    N147 --> N486
    N147 --> N601
    N148 --> N486
    N148 --> N601
    N149 --> N486
    N149 --> N601
    N150 --> N486
    N150 --> N601
    N151 --> N486
    N151 --> N601
    N152 --> N486
    N152 --> N601
    N153 --> N457
    N153 --> N478
    N155 --> N457
    N155 --> N478
    N155 --> N486
    N155 --> N601
    N156 --> N457
    N156 --> N478
    N156 --> N486
    N156 --> N601
    N157 --> N486
    N157 --> N601
    N159 --> N486
    N159 --> N601
    N160 --> N457
    N160 --> N478
    N160 --> N486
    N160 --> N601
    N161 --> N555
    N161 --> N486
    N161 --> N601
    N162 --> N457
    N162 --> N478
    N162 --> N555
    N162 --> N486
    N162 --> N601
    N163 --> N457
    N163 --> N478
    N163 --> N486
    N163 --> N601
    N163 --> N566
    N163 --> N15
    N164 --> N486
    N164 --> N601
    N165 --> N486
    N165 --> N601
    N165 --> N15
    N166 --> N486
    N166 --> N601
    N166 --> N15
    N166 --> N457
    N166 --> N478
    N167 --> N555
    N167 --> N486
    N167 --> N601
    N167 --> N15
    N168 --> N486
    N168 --> N601
    N168 --> N15
    N169 --> N486
    N169 --> N601
    N169 --> N15
    N170 --> N486
    N170 --> N601
    N171 --> N566
    N171 --> N486
    N171 --> N601
    N172 --> N486
    N172 --> N601
    N173 --> N486
    N173 --> N601
    N174 --> N486
    N174 --> N601
    N175 --> N486
    N175 --> N601
    N176 --> N555
    N176 --> N486
    N176 --> N601
    N177 --> N457
    N177 --> N478
    N177 --> N486
    N177 --> N601
    N178 --> N457
    N178 --> N478
    N178 --> N486
    N178 --> N601
    N178 --> N15
    N179 --> N457
    N179 --> N478
    N179 --> N396
    N179 --> N530
    N179 --> N486
    N179 --> N601
    N180 --> N486
    N180 --> N601
    N181 --> N486
    N181 --> N601
    N182 --> N457
    N182 --> N478
    N182 --> N486
    N182 --> N601
    N183 --> N486
    N183 --> N601
    N184 --> N486
    N184 --> N601
    N185 --> N457
    N185 --> N478
    N185 --> N486
    N185 --> N601
    N186 --> N486
    N186 --> N601
    N186 --> N15
    N187 --> N555
    N187 --> N486
    N187 --> N601
    N188 --> N457
    N188 --> N478
    N188 --> N486
    N188 --> N601
    N189 --> N486
    N189 --> N601
    N190 --> N555
    N190 --> N486
    N190 --> N601
    N191 --> N15
    N192 --> N457
    N192 --> N478
    N192 --> N486
    N192 --> N601
    N192 --> N436
    N192 --> N470
    N192 --> N10
    N192 --> N52
    N192 --> N377
    N192 --> N435
    N192 --> N454
    N192 --> N469
    N192 --> N524
    N192 --> N553
    N192 --> N12
    N192 --> N11
    N193 --> N486
    N193 --> N601
    N194 --> N486
    N194 --> N601
    N195 --> N457
    N195 --> N478
    N195 --> N566
    N195 --> N555
    N195 --> N486
    N195 --> N601
    N195 --> N15
    N196 --> N555
    N196 --> N486
    N196 --> N601
    N197 --> N457
    N197 --> N478
    N197 --> N15
    N198 --> N566
    N198 --> N486
    N198 --> N601
    N198 --> N15
    N198 --> N457
    N198 --> N478
    N199 --> N486
    N199 --> N601
    N199 --> N15
    N201 --> N457
    N201 --> N478
    N201 --> N486
    N201 --> N601
    N202 --> N486
    N202 --> N601
    N202 --> N15
    N203 --> N486
    N203 --> N601
    N204 --> N486
    N204 --> N601
    N204 --> N15
    N205 --> N15
    N208 --> N486
    N208 --> N601
    N209 --> N457
    N209 --> N478
    N209 --> N486
    N209 --> N601
    N210 --> N486
    N210 --> N601
    N211 --> N486
    N211 --> N601
    N211 --> N457
    N211 --> N478
    N212 --> N555
    N212 --> N486
    N212 --> N601
    N214 --> N486
    N214 --> N601
    N215 --> N486
    N215 --> N601
    N215 --> N15
    N216 --> N457
    N216 --> N478
    N216 --> N486
    N216 --> N601
    N216 --> N15
    N217 --> N486
    N217 --> N601
    N217 --> N15
    N218 --> N486
    N218 --> N601
    N219 --> N457
    N219 --> N478
    N219 --> N555
    N219 --> N486
    N219 --> N601
    N219 --> N15
    N220 --> N555
    N220 --> N486
    N220 --> N601
    N221 --> N555
    N221 --> N486
    N221 --> N601
    N222 --> N566
    N222 --> N555
    N222 --> N486
    N222 --> N601
    N223 --> N486
    N223 --> N601
    N224 --> N555
    N224 --> N486
    N224 --> N601
    N225 --> N555
    N225 --> N15
    N226 --> N555
    N226 --> N486
    N226 --> N601
    N226 --> N15
    N227 --> N486
    N227 --> N601
    N228 --> N486
    N228 --> N601
    N229 --> N555
    N229 --> N486
    N229 --> N601
    N229 --> N15
    N233 --> N457
    N233 --> N478
    N234 --> N566
    N234 --> N457
    N234 --> N478
    N236 --> N566
    N236 --> N14
    N238 --> N15
    N239 --> N14
    N245 --> N15
    N246 --> N14
    N250 --> N15
    N252 --> N15
    N253 --> N566
    N259 --> N15
    N260 --> N15
    N261 --> N14
    N263 --> N457
    N263 --> N478
    N263 --> N15
    N265 --> N457
    N265 --> N478
    N265 --> N15
    N265 --> N566
    N266 --> N566
    N266 --> N14
    N269 --> N457
    N269 --> N478
    N272 --> N15
    N275 --> N566
    N276 --> N555
    N276 --> N457
    N276 --> N478
    N277 --> N457
    N277 --> N478
    N278 --> N566
    N279 --> N457
    N279 --> N478
    N279 --> N14
    N279 --> N566
    N280 --> N15
    N281 --> N457
    N281 --> N478
    N281 --> N15
    N281 --> N14
    N283 --> N566
    N283 --> N14
    N285 --> N15
    N286 --> N14
    N287 --> N566
    N288 --> N457
    N288 --> N478
    N289 --> N566
    N289 --> N14
    N291 --> N457
    N291 --> N478
    N292 --> N457
    N292 --> N478
    N293 --> N14
    N293 --> N486
    N293 --> N601
    N293 --> N566
    N296 --> N14
    N297 --> N457
    N297 --> N478
    N298 --> N555
    N299 --> N15
    N300 --> N14
    N301 --> N566
    N302 --> N457
    N302 --> N478
    N302 --> N4
    N303 --> N457
    N303 --> N478
    N303 --> N16
    N304 --> N566
    N305 --> N566
    N307 --> N457
    N307 --> N478
    N308 --> N457
    N308 --> N478
    N309 --> N457
    N309 --> N478
    N310 --> N566
    N316 --> N14
    N317 --> N14
    N318 --> N14
    N322 --> N403
    N322 --> N430
    N322 --> N446
    N322 --> N485
    N322 --> N538
    N322 --> N10
    N322 --> N52
    N322 --> N377
    N322 --> N435
    N322 --> N454
    N322 --> N469
    N322 --> N524
    N322 --> N553
    N323 --> N589
    N323 --> N606
    N323 --> N614
    N323 --> N622
    N323 --> N628
    N323 --> N358
    N323 --> N360
    N323 --> N339
    N323 --> N322
    N323 --> N10
    N323 --> N52
    N323 --> N377
    N323 --> N435
    N323 --> N454
    N323 --> N469
    N323 --> N524
    N323 --> N553
    N323 --> N359
    N323 --> N357
    N324 --> N10
    N324 --> N52
    N324 --> N377
    N324 --> N435
    N324 --> N454
    N324 --> N469
    N324 --> N524
    N324 --> N553
    N324 --> N322
    N324 --> N356
    N326 --> N341
    N326 --> N344
    N326 --> N342
    N327 --> N10
    N327 --> N52
    N327 --> N377
    N327 --> N435
    N327 --> N454
    N327 --> N469
    N327 --> N524
    N327 --> N553
    N329 --> N10
    N329 --> N52
    N329 --> N377
    N329 --> N435
    N329 --> N454
    N329 --> N469
    N329 --> N524
    N329 --> N553
    N330 --> N10
    N330 --> N52
    N330 --> N377
    N330 --> N435
    N330 --> N454
    N330 --> N469
    N330 --> N524
    N330 --> N553
    N331 --> N353
    N331 --> N10
    N331 --> N52
    N331 --> N377
    N331 --> N435
    N331 --> N454
    N331 --> N469
    N331 --> N524
    N331 --> N553
    N332 --> N10
    N332 --> N52
    N332 --> N377
    N332 --> N435
    N332 --> N454
    N332 --> N469
    N332 --> N524
    N332 --> N553
    N333 --> N322
    N333 --> N324
    N335 --> N10
    N335 --> N52
    N335 --> N377
    N335 --> N435
    N335 --> N454
    N335 --> N469
    N335 --> N524
    N335 --> N553
    N337 --> N322
    N337 --> N351
    N337 --> N348
    N338 --> N10
    N338 --> N52
    N338 --> N377
    N338 --> N435
    N338 --> N454
    N338 --> N469
    N338 --> N524
    N338 --> N553
    N339 --> N322
    N339 --> N333
    N339 --> N340
    N339 --> N337
    N339 --> N328
    N339 --> N353
    N339 --> N367
    N339 --> N362
    N339 --> N361
    N339 --> N364
    N339 --> N345
    N339 --> N335
    N339 --> N347
    N340 --> N343
    N340 --> N322
    N340 --> N10
    N340 --> N52
    N340 --> N377
    N340 --> N435
    N340 --> N454
    N340 --> N469
    N340 --> N524
    N340 --> N553
    N343 --> N10
    N343 --> N52
    N343 --> N377
    N343 --> N435
    N343 --> N454
    N343 --> N469
    N343 --> N524
    N343 --> N553
    N345 --> N354
    N347 --> N322
    N347 --> N10
    N347 --> N52
    N347 --> N377
    N347 --> N435
    N347 --> N454
    N347 --> N469
    N347 --> N524
    N347 --> N553
    N355 --> N10
    N355 --> N52
    N355 --> N377
    N355 --> N435
    N355 --> N454
    N355 --> N469
    N355 --> N524
    N355 --> N553
    N356 --> N10
    N356 --> N52
    N356 --> N377
    N356 --> N435
    N356 --> N454
    N356 --> N469
    N356 --> N524
    N356 --> N553
    N357 --> N10
    N357 --> N52
    N357 --> N377
    N357 --> N435
    N357 --> N454
    N357 --> N469
    N357 --> N524
    N357 --> N553
    N358 --> N10
    N358 --> N52
    N358 --> N377
    N358 --> N435
    N358 --> N454
    N358 --> N469
    N358 --> N524
    N358 --> N553
    N358 --> N324
    N359 --> N10
    N359 --> N52
    N359 --> N377
    N359 --> N435
    N359 --> N454
    N359 --> N469
    N359 --> N524
    N359 --> N553
    N360 --> N350
    N360 --> N10
    N360 --> N52
    N360 --> N377
    N360 --> N435
    N360 --> N454
    N360 --> N469
    N360 --> N524
    N360 --> N553
    N361 --> N403
    N361 --> N430
    N361 --> N446
    N361 --> N485
    N361 --> N538
    N361 --> N322
    N361 --> N350
    N361 --> N10
    N361 --> N52
    N361 --> N377
    N361 --> N435
    N361 --> N454
    N361 --> N469
    N361 --> N524
    N361 --> N553
    N362 --> N403
    N362 --> N430
    N362 --> N446
    N362 --> N485
    N362 --> N538
    N362 --> N350
    N362 --> N349
    N362 --> N10
    N362 --> N52
    N362 --> N377
    N362 --> N435
    N362 --> N454
    N362 --> N469
    N362 --> N524
    N362 --> N553
    N363 --> N10
    N363 --> N52
    N363 --> N377
    N363 --> N435
    N363 --> N454
    N363 --> N469
    N363 --> N524
    N363 --> N553
    N364 --> N403
    N364 --> N430
    N364 --> N446
    N364 --> N485
    N364 --> N538
    N364 --> N351
    N364 --> N350
    N364 --> N349
    N364 --> N10
    N364 --> N52
    N364 --> N377
    N364 --> N435
    N364 --> N454
    N364 --> N469
    N364 --> N524
    N364 --> N553
    N364 --> N331
    N364 --> N332
    N364 --> N329
    N364 --> N327
    N364 --> N330
    N365 --> N10
    N365 --> N52
    N365 --> N377
    N365 --> N435
    N365 --> N454
    N365 --> N469
    N365 --> N524
    N365 --> N553
    N365 --> N403
    N365 --> N430
    N365 --> N446
    N365 --> N485
    N365 --> N538
    N365 --> N322
    N365 --> N354
    N365 --> N351
    N365 --> N350
    N365 --> N349
    N365 --> N371
    N365 --> N376
    N365 --> N370
    N365 --> N369
    N365 --> N372
    N365 --> N375
    N365 --> N374
    N365 --> N373
    N366 --> N352
    N366 --> N350
    N366 --> N10
    N366 --> N52
    N366 --> N377
    N366 --> N435
    N366 --> N454
    N366 --> N469
    N366 --> N524
    N366 --> N553
    N367 --> N403
    N367 --> N430
    N367 --> N446
    N367 --> N485
    N367 --> N538
    N367 --> N350
    N367 --> N349
    N367 --> N10
    N367 --> N52
    N367 --> N377
    N367 --> N435
    N367 --> N454
    N367 --> N469
    N367 --> N524
    N367 --> N553
    N367 --> N356
    N367 --> N346
    N368 --> N10
    N368 --> N52
    N368 --> N377
    N368 --> N435
    N368 --> N454
    N368 --> N469
    N368 --> N524
    N368 --> N553
    N369 --> N349
    N369 --> N350
    N369 --> N373
    N370 --> N349
    N370 --> N350
    N370 --> N373
    N370 --> N10
    N370 --> N52
    N370 --> N377
    N370 --> N435
    N370 --> N454
    N370 --> N469
    N370 --> N524
    N370 --> N553
    N371 --> N349
    N372 --> N349
    N372 --> N350
    N372 --> N10
    N372 --> N52
    N372 --> N377
    N372 --> N435
    N372 --> N454
    N372 --> N469
    N372 --> N524
    N372 --> N553
    N374 --> N349
    N374 --> N350
    N375 --> N349
    N375 --> N350
    N376 --> N349
    N376 --> N350
    N381 --> N486
    N381 --> N601
    N383 --> N486
    N383 --> N601
    N385 --> N486
    N385 --> N601
    N386 --> N486
    N386 --> N601
    N388 --> N486
    N388 --> N601
    N389 --> N486
    N389 --> N601
    N390 --> N436
    N390 --> N470
    N390 --> N403
    N390 --> N430
    N390 --> N446
    N390 --> N485
    N390 --> N538
    N390 --> N486
    N390 --> N601
    N391 --> N486
    N391 --> N601
    N393 --> N555
    N394 --> N450
    N394 --> N436
    N394 --> N470
    N394 --> N486
    N394 --> N601
    N395 --> N486
    N395 --> N601
    N397 --> N486
    N397 --> N601
    N398 --> N457
    N398 --> N478
    N398 --> N403
    N398 --> N430
    N398 --> N446
    N398 --> N485
    N398 --> N538
    N398 --> N436
    N398 --> N470
    N398 --> N486
    N398 --> N601
    N399 --> N486
    N399 --> N601
    N403 --> N430
    N403 --> N446
    N403 --> N485
    N403 --> N538
    N403 --> N486
    N403 --> N601
    N404 --> N450
    N404 --> N486
    N404 --> N601
    N408 --> N436
    N408 --> N470
    N408 --> N486
    N408 --> N601
    N408 --> N566
    N409 --> N436
    N409 --> N470
    N409 --> N486
    N409 --> N601
    N417 --> N457
    N417 --> N478
    N417 --> N486
    N417 --> N601
    N418 --> N486
    N418 --> N601
    N419 --> N422
    N419 --> N618
    N419 --> N450
    N419 --> N486
    N419 --> N601
    N420 --> N486
    N420 --> N601
    N422 --> N486
    N422 --> N601
    N423 --> N486
    N423 --> N601
    N424 --> N486
    N424 --> N601
    N425 --> N403
    N425 --> N430
    N425 --> N446
    N425 --> N485
    N425 --> N538
    N425 --> N486
    N425 --> N601
    N425 --> N450
    N425 --> N436
    N425 --> N470
    N426 --> N450
    N426 --> N436
    N426 --> N470
    N426 --> N486
    N426 --> N601
    N429 --> N403
    N429 --> N430
    N429 --> N446
    N429 --> N485
    N429 --> N538
    N430 --> N597
    N430 --> N619
    N430 --> N429
    N431 --> N436
    N431 --> N470
    N431 --> N486
    N431 --> N601
    N433 --> N486
    N433 --> N601
    N434 --> N486
    N434 --> N601
    N435 --> N450
    N435 --> N486
    N435 --> N601
    N436 --> N470
    N436 --> N403
    N436 --> N430
    N436 --> N446
    N436 --> N485
    N436 --> N538
    N436 --> N486
    N436 --> N601
    N436 --> N450
    N437 --> N486
    N437 --> N601
    N438 --> N436
    N438 --> N470
    N438 --> N486
    N438 --> N601
    N438 --> N450
    N438 --> N466
    N439 --> N436
    N439 --> N470
    N439 --> N486
    N439 --> N601
    N440 --> N436
    N440 --> N470
    N440 --> N450
    N440 --> N486
    N440 --> N601
    N441 --> N436
    N441 --> N470
    N441 --> N450
    N441 --> N486
    N441 --> N601
    N442 --> N403
    N442 --> N430
    N442 --> N446
    N442 --> N485
    N442 --> N538
    N442 --> N450
    N442 --> N486
    N442 --> N601
    N442 --> N457
    N442 --> N478
    N443 --> N486
    N443 --> N601
    N443 --> N480
    N443 --> N450
    N444 --> N436
    N444 --> N470
    N444 --> N486
    N444 --> N601
    N445 --> N486
    N445 --> N601
    N446 --> N436
    N446 --> N470
    N446 --> N403
    N446 --> N430
    N446 --> N485
    N446 --> N538
    N446 --> N486
    N446 --> N601
    N446 --> N466
    N446 --> N457
    N446 --> N478
    N447 --> N403
    N447 --> N430
    N447 --> N446
    N447 --> N485
    N447 --> N538
    N447 --> N436
    N447 --> N470
    N447 --> N486
    N447 --> N601
    N448 --> N403
    N448 --> N430
    N448 --> N446
    N448 --> N485
    N448 --> N538
    N448 --> N486
    N448 --> N601
    N451 --> N486
    N451 --> N601
    N451 --> N450
    N452 --> N486
    N452 --> N601
    N452 --> N450
    N453 --> N403
    N453 --> N430
    N453 --> N446
    N453 --> N485
    N453 --> N538
    N453 --> N486
    N453 --> N601
    N453 --> N450
    N454 --> N450
    N454 --> N486
    N454 --> N601
    N455 --> N486
    N455 --> N601
    N456 --> N450
    N456 --> N486
    N456 --> N601
    N457 --> N450
    N457 --> N403
    N457 --> N430
    N457 --> N446
    N457 --> N485
    N457 --> N538
    N457 --> N486
    N457 --> N601
    N457 --> N436
    N457 --> N470
    N458 --> N457
    N458 --> N478
    N458 --> N450
    N458 --> N486
    N458 --> N601
    N459 --> N457
    N459 --> N478
    N459 --> N450
    N459 --> N486
    N459 --> N601
    N460 --> N486
    N460 --> N601
    N462 --> N436
    N462 --> N470
    N462 --> N486
    N462 --> N601
    N462 --> N466
    N462 --> N403
    N462 --> N430
    N462 --> N446
    N462 --> N485
    N462 --> N538
    N463 --> N450
    N463 --> N486
    N463 --> N601
    N464 --> N486
    N464 --> N601
    N465 --> N486
    N465 --> N601
    N466 --> N486
    N466 --> N601
    N467 --> N450
    N467 --> N403
    N467 --> N430
    N467 --> N446
    N467 --> N485
    N467 --> N538
    N467 --> N486
    N467 --> N601
    N468 --> N486
    N468 --> N601
    N469 --> N457
    N469 --> N478
    N469 --> N486
    N469 --> N601
    N470 --> N436
    N470 --> N486
    N470 --> N601
    N471 --> N486
    N471 --> N601
    N472 --> N486
    N472 --> N601
    N473 --> N450
    N473 --> N486
    N473 --> N601
    N474 --> N486
    N474 --> N601
    N475 --> N457
    N475 --> N478
    N475 --> N486
    N475 --> N601
    N476 --> N486
    N476 --> N601
    N477 --> N403
    N477 --> N430
    N477 --> N446
    N477 --> N485
    N477 --> N538
    N477 --> N486
    N477 --> N601
    N478 --> N403
    N478 --> N430
    N478 --> N446
    N478 --> N485
    N478 --> N538
    N478 --> N486
    N478 --> N601
    N478 --> N436
    N478 --> N470
    N479 --> N450
    N479 --> N403
    N479 --> N430
    N479 --> N446
    N479 --> N485
    N479 --> N538
    N479 --> N486
    N479 --> N601
    N480 --> N486
    N480 --> N601
    N480 --> N443
    N480 --> N450
    N481 --> N486
    N481 --> N601
    N482 --> N457
    N482 --> N478
    N482 --> N486
    N482 --> N601
    N483 --> N450
    N483 --> N436
    N483 --> N470
    N483 --> N486
    N483 --> N601
    N484 --> N457
    N484 --> N478
    N484 --> N486
    N484 --> N601
    N485 --> N450
    N485 --> N403
    N485 --> N430
    N485 --> N446
    N485 --> N538
    N485 --> N486
    N485 --> N601
    N486 --> N601
    N486 --> N403
    N486 --> N430
    N486 --> N446
    N486 --> N485
    N486 --> N538
    N487 --> N450
    N487 --> N403
    N487 --> N430
    N487 --> N446
    N487 --> N485
    N487 --> N538
    N487 --> N486
    N487 --> N601
    N488 --> N486
    N488 --> N601
    N488 --> N450
    N490 --> N457
    N490 --> N478
    N490 --> N486
    N490 --> N601
    N492 --> N450
    N492 --> N486
    N492 --> N601
    N493 --> N486
    N493 --> N601
    N493 --> N450
    N494 --> N486
    N494 --> N601
    N495 --> N436
    N495 --> N470
    N495 --> N450
    N495 --> N486
    N495 --> N601
    N496 --> N403
    N496 --> N430
    N496 --> N446
    N496 --> N485
    N496 --> N538
    N496 --> N436
    N496 --> N470
    N496 --> N486
    N496 --> N601
    N497 --> N486
    N497 --> N601
    N498 --> N486
    N498 --> N601
    N499 --> N486
    N499 --> N601
    N500 --> N436
    N500 --> N470
    N500 --> N450
    N500 --> N486
    N500 --> N601
    N500 --> N466
    N501 --> N436
    N501 --> N470
    N501 --> N486
    N501 --> N601
    N502 --> N436
    N502 --> N470
    N502 --> N486
    N502 --> N601
    N502 --> N450
    N502 --> N403
    N502 --> N430
    N502 --> N446
    N502 --> N485
    N502 --> N538
    N503 --> N403
    N503 --> N430
    N503 --> N446
    N503 --> N485
    N503 --> N538
    N503 --> N486
    N503 --> N601
    N505 --> N486
    N505 --> N601
    N507 --> N486
    N507 --> N601
    N507 --> N466
    N508 --> N486
    N508 --> N601
    N509 --> N486
    N509 --> N601
    N509 --> N450
    N509 --> N403
    N509 --> N430
    N509 --> N446
    N509 --> N485
    N509 --> N538
    N510 --> N486
    N510 --> N601
    N511 --> N403
    N511 --> N430
    N511 --> N446
    N511 --> N485
    N511 --> N538
    N511 --> N486
    N511 --> N601
    N512 --> N436
    N512 --> N470
    N512 --> N486
    N512 --> N601
    N513 --> N486
    N513 --> N601
    N514 --> N486
    N514 --> N601
    N515 --> N436
    N515 --> N470
    N515 --> N486
    N515 --> N601
    N516 --> N403
    N516 --> N430
    N516 --> N446
    N516 --> N485
    N516 --> N538
    N516 --> N486
    N516 --> N601
    N517 --> N436
    N517 --> N470
    N517 --> N450
    N517 --> N403
    N517 --> N430
    N517 --> N446
    N517 --> N485
    N517 --> N538
    N517 --> N486
    N517 --> N601
    N518 --> N486
    N518 --> N601
    N519 --> N486
    N519 --> N601
    N520 --> N486
    N520 --> N601
    N521 --> N486
    N521 --> N601
    N522 --> N486
    N522 --> N601
    N523 --> N450
    N523 --> N486
    N523 --> N601
    N524 --> N450
    N524 --> N486
    N524 --> N601
    N525 --> N486
    N525 --> N601
    N526 --> N486
    N526 --> N601
    N527 --> N457
    N527 --> N478
    N527 --> N486
    N527 --> N601
    N528 --> N422
    N528 --> N618
    N529 --> N436
    N529 --> N470
    N529 --> N486
    N529 --> N601
    N530 --> N457
    N530 --> N478
    N530 --> N422
    N530 --> N618
    N530 --> N486
    N530 --> N601
    N531 --> N422
    N531 --> N618
    N531 --> N457
    N531 --> N478
    N531 --> N486
    N531 --> N601
    N532 --> N403
    N532 --> N430
    N532 --> N446
    N532 --> N485
    N532 --> N538
    N532 --> N450
    N532 --> N486
    N532 --> N601
    N533 --> N486
    N533 --> N601
    N534 --> N486
    N534 --> N601
    N535 --> N450
    N536 --> N486
    N536 --> N601
    N537 --> N457
    N537 --> N478
    N537 --> N450
    N537 --> N403
    N537 --> N430
    N537 --> N446
    N537 --> N485
    N537 --> N538
    N537 --> N486
    N537 --> N601
    N538 --> N486
    N538 --> N601
    N539 --> N457
    N539 --> N478
    N539 --> N486
    N539 --> N601
    N540 --> N486
    N540 --> N601
    N541 --> N486
    N541 --> N601
    N541 --> N566
    N543 --> N486
    N543 --> N601
    N546 --> N486
    N546 --> N601
    N547 --> N412
    N547 --> N486
    N547 --> N601
    N549 --> N457
    N549 --> N478
    N549 --> N486
    N549 --> N601
    N551 --> N450
    N551 --> N486
    N551 --> N601
    N552 --> N486
    N552 --> N601
    N553 --> N566
    N553 --> N457
    N553 --> N478
    N553 --> N555
    N553 --> N486
    N553 --> N601
    N554 --> N486
    N554 --> N601
    N555 --> N422
    N555 --> N618
    N555 --> N486
    N555 --> N601
    N556 --> N566
    N556 --> N555
    N556 --> N450
    N556 --> N486
    N556 --> N601
    N557 --> N566
    N557 --> N555
    N557 --> N403
    N557 --> N430
    N557 --> N446
    N557 --> N485
    N557 --> N538
    N557 --> N486
    N557 --> N601
    N558 --> N566
    N558 --> N555
    N558 --> N450
    N558 --> N486
    N558 --> N601
    N559 --> N566
    N559 --> N486
    N559 --> N601
    N561 --> N403
    N561 --> N430
    N561 --> N446
    N561 --> N485
    N561 --> N538
    N561 --> N486
    N561 --> N601
    N564 --> N486
    N564 --> N601
    N565 --> N566
    N565 --> N555
    N565 --> N486
    N565 --> N601
    N567 --> N566
    N567 --> N568
    N568 --> N566
    N570 --> N555
    N570 --> N486
    N570 --> N601
    N572 --> N566
    N572 --> N450
    N573 --> N566
    N574 --> N566
    N575 --> N566
    N576 --> N566
    N576 --> N422
    N576 --> N618
    N576 --> N555
    N576 --> N486
    N576 --> N601
    N577 --> N566
    N577 --> N422
    N577 --> N618
    N577 --> N555
    N577 --> N486
    N577 --> N601
    N578 --> N566
    N578 --> N33
    N578 --> N405
    N578 --> N539
    N579 --> N566
    N579 --> N422
    N579 --> N618
    N579 --> N555
    N579 --> N486
    N579 --> N601
    N579 --> N33
    N579 --> N405
    N579 --> N539
    N580 --> N566
    N580 --> N555
    N580 --> N422
    N580 --> N618
    N580 --> N486
    N580 --> N601
    N580 --> N33
    N580 --> N405
    N580 --> N539
    N581 --> N566
    N581 --> N555
    N581 --> N486
    N581 --> N601
    N582 --> N555
    N582 --> N403
    N582 --> N430
    N582 --> N446
    N582 --> N485
    N582 --> N538
    N583 --> N555
    N583 --> N486
    N583 --> N601
    N584 --> N555
    N586 --> N486
    N586 --> N601
    N587 --> N450
    N588 --> N566
    N588 --> N486
    N588 --> N601
    N589 --> N450
    N589 --> N486
    N589 --> N601
    N590 --> N450
    N591 --> N486
    N591 --> N601
    N592 --> N450
    N593 --> N436
    N593 --> N470
    N593 --> N486
    N593 --> N601
    N594 --> N486
    N594 --> N601
    N595 --> N436
    N595 --> N470
    N595 --> N450
    N595 --> N486
    N595 --> N601
    N596 --> N450
    N596 --> N486
    N596 --> N601
    N597 --> N555
    N598 --> N436
    N598 --> N470
    N599 --> N422
    N599 --> N618
    N599 --> N450
    N599 --> N486
    N599 --> N601
    N601 --> N422
    N601 --> N618
    N601 --> N555
    N601 --> N486
    N602 --> N436
    N602 --> N470
    N605 --> N486
    N605 --> N601
    N606 --> N566
    N606 --> N555
    N606 --> N403
    N606 --> N430
    N606 --> N446
    N606 --> N485
    N606 --> N538
    N606 --> N486
    N606 --> N601
    N606 --> N33
    N606 --> N405
    N606 --> N539
    N607 --> N566
    N607 --> N555
    N607 --> N403
    N607 --> N430
    N607 --> N446
    N607 --> N485
    N607 --> N538
    N607 --> N486
    N607 --> N601
    N608 --> N566
    N608 --> N486
    N608 --> N601
    N609 --> N422
    N609 --> N618
    N609 --> N486
    N609 --> N601
    N609 --> N33
    N609 --> N405
    N609 --> N539
    N610 --> N566
    N610 --> N422
    N610 --> N618
    N610 --> N555
    N610 --> N403
    N610 --> N430
    N610 --> N446
    N610 --> N485
    N610 --> N538
    N610 --> N486
    N610 --> N601
    N610 --> N33
    N610 --> N405
    N610 --> N539
    N612 --> N486
    N612 --> N601
    N613 --> N422
    N613 --> N618
    N613 --> N486
    N613 --> N601
    N614 --> N566
    N614 --> N555
    N614 --> N450
    N614 --> N403
    N614 --> N430
    N614 --> N446
    N614 --> N485
    N614 --> N538
    N614 --> N486
    N614 --> N601
    N615 --> N422
    N615 --> N618
    N616 --> N486
    N616 --> N601
    N618 --> N566
    N619 --> N566
    N619 --> N555
    N619 --> N450
    N619 --> N486
    N619 --> N601
    N620 --> N566
    N620 --> N422
    N620 --> N618
    N620 --> N555
    N620 --> N450
    N620 --> N403
    N620 --> N430
    N620 --> N446
    N620 --> N485
    N620 --> N538
    N620 --> N486
    N620 --> N601
    N621 --> N450
    N622 --> N555
    N622 --> N450
    N622 --> N403
    N622 --> N430
    N622 --> N446
    N622 --> N485
    N622 --> N538
    N622 --> N486
    N622 --> N601
    N622 --> N33
    N622 --> N405
    N622 --> N539
    N623 --> N555
    N623 --> N403
    N623 --> N430
    N623 --> N446
    N623 --> N485
    N623 --> N538
    N623 --> N486
    N623 --> N601
    N624 --> N486
    N624 --> N601
    N625 --> N422
    N625 --> N618
    N625 --> N486
    N625 --> N601
    N625 --> N33
    N625 --> N405
    N625 --> N539
    N626 --> N422
    N626 --> N618
    N626 --> N555
    N626 --> N450
    N626 --> N403
    N626 --> N430
    N626 --> N446
    N626 --> N485
    N626 --> N538
    N626 --> N486
    N626 --> N601
    N626 --> N33
    N626 --> N405
    N626 --> N539
    N628 --> N555
    N628 --> N403
    N628 --> N430
    N628 --> N446
    N628 --> N485
    N628 --> N538
    N628 --> N486
    N628 --> N601
    N628 --> N33
    N628 --> N405
    N628 --> N539
    N629 --> N555
    N629 --> N403
    N629 --> N430
    N629 --> N446
    N629 --> N485
    N629 --> N538
    N629 --> N486
    N629 --> N601
    N630 --> N486
    N630 --> N601
    N631 --> N422
    N631 --> N618
    N631 --> N486
    N631 --> N601
    N631 --> N33
    N631 --> N405
    N631 --> N539
    N632 --> N422
    N632 --> N618
    N632 --> N555
    N632 --> N403
    N632 --> N430
    N632 --> N446
    N632 --> N485
    N632 --> N538
    N632 --> N486
    N632 --> N601
    N632 --> N33
    N632 --> N405
    N632 --> N539
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