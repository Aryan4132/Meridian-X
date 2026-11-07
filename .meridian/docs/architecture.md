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
    N39["ar_bridge.py [meridian_backend/src/core]"]
    N40["atomic_storage.py [meridian_backend/src/core]"]
    N41["audit_logger.py [meridian_backend/src/core]"]
    N42["auth.py [meridian_backend/src/core]"]
    N43["behavior_monitor.py [meridian_backend/src/core]"]
    N44["boilerplate_genie.py [meridian_backend/src/core]"]
    N45["breach_sentinel.py [meridian_backend/src/core]"]
    N46["browser_extension_hub.py [meridian_backend/src/core]"]
    N47["bus.py [meridian_backend/src/core]"]
    N48["camera_sentinel.py [meridian_backend/src/core]"]
    N49["checkpoints.py [meridian_backend/src/core]"]
    N50["clipboard.py [meridian_backend/src/core]"]
    N51["code_graph.py [meridian_backend/src/core]"]
    N52["cognitive_graph.py [meridian_backend/src/core]"]
    N53["commit_whisperer.py [meridian_backend/src/core]"]
    N54["config.py [meridian_backend/src/core]"]
    N55["confirmations.py [meridian_backend/src/core]"]
    N56["consensus_engine.py [meridian_backend/src/core]"]
    N57["deep_project_context.py [meridian_backend/src/core]"]
    N58["dev_automation.py [meridian_backend/src/core]"]
    N59["discord_bridge.py [meridian_backend/src/core]"]
    N60["discord_utils.py [meridian_backend/src/core]"]
    N61["doc_generator.py [meridian_backend/src/core]"]
    N62["doc_indexer.py [meridian_backend/src/core]"]
    N63["elevated_runner.py [meridian_backend/src/core]"]
    N64["emergency_lockdown.py [meridian_backend/src/core]"]
    N65["error_diagnostics.py [meridian_backend/src/core]"]
    N66["experiment_runner.py [meridian_backend/src/core]"]
    N67["explain_code_engine.py [meridian_backend/src/core]"]
    N68["exporter.py [meridian_backend/src/core]"]
    N69["fim_sentinel.py [meridian_backend/src/core]"]
    N70["gaze_tracker.py [meridian_backend/src/core]"]
    N71["governor.py [meridian_backend/src/core]"]
    N72["graph_rag.py [meridian_backend/src/core]"]
    N73["graph_sync.py [meridian_backend/src/core]"]
    N74["hardware_detector.py [meridian_backend/src/core]"]
    N75["history_manager.py [meridian_backend/src/core]"]
    N76["lifespan.py [meridian_backend/src/core]"]
    N77["llm_auth.py [meridian_backend/src/core]"]
    N78["llm_client.py [meridian_backend/src/core]"]
    N79["llm_clients.py [meridian_backend/src/core]"]
    N80["llm_provider.py [meridian_backend/src/core]"]
    N81["local_model_manager.py [meridian_backend/src/core]"]
    N82["logger.py [meridian_backend/src/core]"]
    N83["logging_config.py [meridian_backend/src/core]"]
    N84["loop.py [meridian_backend/src/core]"]
    N85["loop_dispatcher.py [meridian_backend/src/core]"]
    N86["loop_executor.py [meridian_backend/src/core]"]
    N87["loop_parser.py [meridian_backend/src/core]"]
    N88["loop_planning.py [meridian_backend/src/core]"]
    N89["loop_stream.py [meridian_backend/src/core]"]
    N90["lsp_client.py [meridian_backend/src/core]"]
    N91["malware_scanner.py [meridian_backend/src/core]"]
    N92["mcp_client.py [meridian_backend/src/core]"]
    N93["mcp_executor.py [meridian_backend/src/core]"]
    N94["memory_backup.py [meridian_backend/src/core]"]
    N95["memory_consolidation.py [meridian_backend/src/core]"]
    N96["memory_editor.py [meridian_backend/src/core]"]
    N97["mobile_bridge.py [meridian_backend/src/core]"]
    N98["mode.py [meridian_backend/src/core]"]
    N99["neural_rag.py [meridian_backend/src/core]"]
    N100["oauth_manager.py [meridian_backend/src/core]"]
    N101["ollama_manager.py [meridian_backend/src/core]"]
    N102["p2p.py [meridian_backend/src/core]"]
    N103["p2p_crypto.py [meridian_backend/src/core]"]
    N104["p2p_discovery.py [meridian_backend/src/core]"]
    N105["p2p_pairing.py [meridian_backend/src/core]"]
    N106["perception.py [meridian_backend/src/core]"]
    N107["persistence_sentinel.py [meridian_backend/src/core]"]
    N108["personal_crm.py [meridian_backend/src/core]"]
    N109["plugins.py [meridian_backend/src/core]"]
    N110["polyglot.py [meridian_backend/src/core]"]
    N111["predictive_engine.py [meridian_backend/src/core]"]
    N112["presence_briefing.py [meridian_backend/src/core]"]
    N113["proactive_system_guard.py [meridian_backend/src/core]"]
    N114["prompt_injection.py [meridian_backend/src/core]"]
    N115["prompt_templates.py [meridian_backend/src/core]"]
    N116["rag_optimizer.py [meridian_backend/src/core]"]
    N117["reflection_engine.py [meridian_backend/src/core]"]
    N118["response_models.py [meridian_backend/src/core]"]
    N119["sandbox_runner.py [meridian_backend/src/core]"]
    N120["scheduler.py [meridian_backend/src/core]"]
    N121["screen_sense.py [meridian_backend/src/core]"]
    N122["security_middleware.py [meridian_backend/src/core]"]
    N123["self_evolving_tooling.py [meridian_backend/src/core]"]
    N124["silent_workflow_guardian.py [meridian_backend/src/core]"]
    N125["skills_loader.py [meridian_backend/src/core]"]
    N126["sos_protocol.py [meridian_backend/src/core]"]
    N127["speculative.py [meridian_backend/src/core]"]
    N128["swarm.py [meridian_backend/src/core]"]
    N129["system_defense.py [meridian_backend/src/core]"]
    N130["telegram_bridge.py [meridian_backend/src/core]"]
    N131["temporal_memory.py [meridian_backend/src/core]"]
    N132["tool_indexer.py [meridian_backend/src/core]"]
    N133["tool_regression_sentinel.py [meridian_backend/src/core]"]
    N134["triggers.py [meridian_backend/src/core]"]
    N135["updater.py [meridian_backend/src/core]"]
    N136["vault.py [meridian_backend/src/core]"]
    N137["vision.py [meridian_backend/src/core]"]
    N138["vision_face.py [meridian_backend/src/core]"]
    N139["vision_gesture.py [meridian_backend/src/core]"]
    N140["watcher.py [meridian_backend/src/core]"]
    N141["what_broke_detective.py [meridian_backend/src/core]"]
    N142["workflow_engine.py [meridian_backend/src/core]"]
    N143["workspace_orchestrator.py [meridian_backend/src/core]"]
    N144["commits.py [meridian_backend/src/core/proactive]"]
    N145["dispatcher.py [meridian_backend/src/core/proactive]"]
    N146["ergonomics.py [meridian_backend/src/core/proactive]"]
    N147["guard.py [meridian_backend/src/core/proactive]"]
    N148["__init__.py [meridian_backend/src/core/proactive]"]
    N149["cache.py [meridian_backend/src/db]"]
    N150["connection.py [meridian_backend/src/db]"]
    N151["contacts.py [meridian_backend/src/db]"]
    N152["conversations.py [meridian_backend/src/db]"]
    N153["embeddings.py [meridian_backend/src/db]"]
    N154["logs.py [meridian_backend/src/db]"]
    N155["memory.py [meridian_backend/src/db]"]
    N156["parsers.py [meridian_backend/src/db]"]
    N157["profile.py [meridian_backend/src/db]"]
    N158["rag.py [meridian_backend/src/db]"]
    N159["vectors.py [meridian_backend/src/db]"]
    N160["__init__.py [meridian_backend/src/db]"]
    N161["auto_reviewer.py [meridian_backend/src/tools]"]
    N162["bill_radar.py [meridian_backend/src/tools]"]
    N163["bookmark_manager.py [meridian_backend/src/tools]"]
    N164["browser_agent.py [meridian_backend/src/tools]"]
    N165["browser_extension_tools.py [meridian_backend/src/tools]"]
    N166["browser_use_agent.py [meridian_backend/src/tools]"]
    N167["cam_guard.py [meridian_backend/src/tools]"]
    N168["chrome_manager.py [meridian_backend/src/tools]"]
    N169["clipboard.py [meridian_backend/src/tools]"]
    N170["communication.py [meridian_backend/src/tools]"]
    N171["db_query.py [meridian_backend/src/tools]"]
    N172["desktop.py [meridian_backend/src/tools]"]
    N173["detonation_sandbox.py [meridian_backend/src/tools]"]
    N174["developer.py [meridian_backend/src/tools]"]
    N175["dns_shield.py [meridian_backend/src/tools]"]
    N176["documents.py [meridian_backend/src/tools]"]
    N177["documents_office.py [meridian_backend/src/tools]"]
    N178["documents_slides.py [meridian_backend/src/tools]"]
    N179["dynamic_manager.py [meridian_backend/src/tools]"]
    N180["expiry_sentinel.py [meridian_backend/src/tools]"]
    N181["exporter.py [meridian_backend/src/tools]"]
    N182["external_connectors.py [meridian_backend/src/tools]"]
    N183["filesystem.py [meridian_backend/src/tools]"]
    N184["file_janitor.py [meridian_backend/src/tools]"]
    N185["finance_sentinel.py [meridian_backend/src/tools]"]
    N186["geo_location.py [meridian_backend/src/tools]"]
    N187["health_ingest.py [meridian_backend/src/tools]"]
    N188["household.py [meridian_backend/src/tools]"]
    N189["knowledge.py [meridian_backend/src/tools]"]
    N190["learning_queue.py [meridian_backend/src/tools]"]
    N191["mcp_marketplace.py [meridian_backend/src/tools]"]
    N192["network_guardian.py [meridian_backend/src/tools]"]
    N193["networth_tracker.py [meridian_backend/src/tools]"]
    N194["ollama_manager.py [meridian_backend/src/tools]"]
    N195["papercoder.py [meridian_backend/src/tools]"]
    N196["password_auditor.py [meridian_backend/src/tools]"]
    N197["phishing_guard.py [meridian_backend/src/tools]"]
    N198["phone_agent.py [meridian_backend/src/tools]"]
    N199["price_watcher.py [meridian_backend/src/tools]"]
    N200["recording.py [meridian_backend/src/tools]"]
    N201["registry.py [meridian_backend/src/tools]"]
    N202["review.py [meridian_backend/src/tools]"]
    N203["scheduler.py [meridian_backend/src/tools]"]
    N204["screenshot_memory.py [meridian_backend/src/tools]"]
    N205["search_hub.py [meridian_backend/src/tools]"]
    N206["security_auditor.py [meridian_backend/src/tools]"]
    N207["shell.py [meridian_backend/src/tools]"]
    N208["system.py [meridian_backend/src/tools]"]
    N209["system_windows.py [meridian_backend/src/tools]"]
    N210["task_scheduler.py [meridian_backend/src/tools]"]
    N211["totp_generator.py [meridian_backend/src/tools]"]
    N212["travel_butler.py [meridian_backend/src/tools]"]
    N213["usb_watchdog.py [meridian_backend/src/tools]"]
    N214["vault.py [meridian_backend/src/tools]"]
    N215["video_editor.py [meridian_backend/src/tools]"]
    N216["voice.py [meridian_backend/src/tools]"]
    N217["watcher.py [meridian_backend/src/tools]"]
    N218["web.py [meridian_backend/src/tools]"]
    N219["web_browser.py [meridian_backend/src/tools]"]
    N220["web_scraper.py [meridian_backend/src/tools]"]
    N221["wellness.py [meridian_backend/src/tools]"]
    N222["whatsapp_manager.py [meridian_backend/src/tools]"]
    N223["wifi_assessor.py [meridian_backend/src/tools]"]
    N224["workspace_layout.py [meridian_backend/src/tools]"]
    N225["ambient_listener.py [meridian_backend/src/voice]"]
    N226["duplex.py [meridian_backend/src/voice]"]
    N227["polyglot.py [meridian_backend/src/voice]"]
    N228["stt.py [meridian_backend/src/voice]"]
    N229["tts.py [meridian_backend/src/voice]"]
    N230["vad.py [meridian_backend/src/voice]"]
    N231["voice_biometrics.py [meridian_backend/src/voice]"]
    N232["wakeword.py [meridian_backend/src/voice]"]
    N233["conftest.py [meridian_backend/tests]"]
    N234["run_tests.py [meridian_backend/tests]"]
    N235["test_advanced_proactive.py [meridian_backend/tests]"]
    N236["test_atomic_storage.py [meridian_backend/tests]"]
    N237["test_audit_bugfixes.py [meridian_backend/tests]"]
    N238["test_audit_remediation.py [meridian_backend/tests]"]
    N239["test_auto_bug_fixer.py [meridian_backend/tests]"]
    N240["test_backend_improvements.py [meridian_backend/tests]"]
    N241["test_backlog_features.py [meridian_backend/tests]"]
    N242["test_backlog_sprint.py [meridian_backend/tests]"]
    N243["test_bridges.py [meridian_backend/tests]"]
    N244["test_browser_agent.py [meridian_backend/tests]"]
    N245["test_browser_extension.py [meridian_backend/tests]"]
    N246["test_browser_fallback.py [meridian_backend/tests]"]
    N247["test_browser_frame.py [meridian_backend/tests]"]
    N248["test_browser_use.py [meridian_backend/tests]"]
    N249["test_butler_media.py [meridian_backend/tests]"]
    N250["test_chat_abort.py [meridian_backend/tests]"]
    N251["test_cognitive_graph.py [meridian_backend/tests]"]
    N252["test_config.py [meridian_backend/tests]"]
    N253["test_consensus_gate.py [meridian_backend/tests]"]
    N254["test_context_budget.py [meridian_backend/tests]"]
    N255["test_custom_password_auth.py [meridian_backend/tests]"]
    N256["test_database.py [meridian_backend/tests]"]
    N257["test_day10_features.py [meridian_backend/tests]"]
    N258["test_day11_features.py [meridian_backend/tests]"]
    N259["test_day12_features.py [meridian_backend/tests]"]
    N260["test_day13_features.py [meridian_backend/tests]"]
    N261["test_day14_day15_features.py [meridian_backend/tests]"]
    N262["test_day16_17_18_features.py [meridian_backend/tests]"]
    N263["test_day3_features.py [meridian_backend/tests]"]
    N264["test_day4_features.py [meridian_backend/tests]"]
    N265["test_day5_features.py [meridian_backend/tests]"]
    N266["test_day6_features.py [meridian_backend/tests]"]
    N267["test_day7_features.py [meridian_backend/tests]"]
    N268["test_day8_features.py [meridian_backend/tests]"]
    N269["test_day9_features.py [meridian_backend/tests]"]
    N270["test_dev_intelligence_suite.py [meridian_backend/tests]"]
    N271["test_document_tools.py [meridian_backend/tests]"]
    N272["test_error_diagnostics.py [meridian_backend/tests]"]
    N273["test_exhaustive_fallback.py [meridian_backend/tests]"]
    N274["test_full_proactive_suite.py [meridian_backend/tests]"]
    N275["test_geo_location.py [meridian_backend/tests]"]
    N276["test_hybrid_rag.py [meridian_backend/tests]"]
    N277["test_jarvis_perception.py [meridian_backend/tests]"]
    N278["test_known_errors_remediation.py [meridian_backend/tests]"]
    N279["test_llm_provider.py [meridian_backend/tests]"]
    N280["test_logging.py [meridian_backend/tests]"]
    N281["test_loop_parser.py [meridian_backend/tests]"]
    N282["test_loop_submodules.py [meridian_backend/tests]"]
    N283["test_mobile_websocket.py [meridian_backend/tests]"]
    N284["test_model_source.py [meridian_backend/tests]"]
    N285["test_multimode_routing.py [meridian_backend/tests]"]
    N286["test_multi_os.py [meridian_backend/tests]"]
    N287["test_new_features.py [meridian_backend/tests]"]
    N288["test_oauth.py [meridian_backend/tests]"]
    N289["test_p2p.py [meridian_backend/tests]"]
    N290["test_perception_bridge.py [meridian_backend/tests]"]
    N291["test_proactive.py [meridian_backend/tests]"]
    N292["test_proactive_mode.py [meridian_backend/tests]"]
    N293["test_proactive_notifications.py [meridian_backend/tests]"]
    N294["test_reflection_engine.py [meridian_backend/tests]"]
    N295["test_research_optimization.py [meridian_backend/tests]"]
    N296["test_response_resilience.py [meridian_backend/tests]"]
    N297["test_security_features.py [meridian_backend/tests]"]
    N298["test_silero_vad.py [meridian_backend/tests]"]
    N299["test_skill_packs.py [meridian_backend/tests]"]
    N300["test_sprint24_hardening.py [meridian_backend/tests]"]
    N301["test_sprint25_hardening.py [meridian_backend/tests]"]
    N302["test_sprint27_hardening.py [meridian_backend/tests]"]
    N303["test_sprint28_hardening.py [meridian_backend/tests]"]
    N304["test_sprint2_features.py [meridian_backend/tests]"]
    N305["test_sprint40.py [meridian_backend/tests]"]
    N306["test_sprint45.py [meridian_backend/tests]"]
    N307["test_standalone_bridge.py [meridian_backend/tests]"]
    N308["test_stream_resiliency.py [meridian_backend/tests]"]
    N309["test_swarm.py [meridian_backend/tests]"]
    N310["test_swarm_routing.py [meridian_backend/tests]"]
    N311["test_system_hardening.py [meridian_backend/tests]"]
    N312["test_tools.py [meridian_backend/tests]"]
    N313["test_tool_intelligence.py [meridian_backend/tests]"]
    N314["test_tool_modernization.py [meridian_backend/tests]"]
    N315["test_tool_regression.py [meridian_backend/tests]"]
    N316["test_user_delight_tools.py [meridian_backend/tests]"]
    N317["test_vault.py [meridian_backend/tests]"]
    N318["test_video_editor.py [meridian_backend/tests]"]
    N319["test_voice_hardening.py [meridian_backend/tests]"]
    N320["test_voice_speed.py [meridian_backend/tests]"]
    N321["test_wakeword_continuous.py [meridian_backend/tests]"]
    N322["test_wakeword_onnx.py [meridian_backend/tests]"]
    N323["test_web_guards.py [meridian_backend/tests]"]
    N324["test_workflow.py [meridian_backend/tests]"]
    N325["vite.config.ts [meridian_frontend]"]
    N326["AppContext.tsx [meridian_frontend/src]"]
    N327["main.tsx [meridian_frontend/src]"]
    N328["Mascot.tsx [meridian_frontend/src]"]
    N329["Mascot3DCharacter.tsx [meridian_frontend/src]"]
    N330["MobileApp.tsx [meridian_frontend/src]"]
    N331["AgentStatusStream.tsx [meridian_frontend/src/components]"]
    N332["CommandPalette.tsx [meridian_frontend/src/components]"]
    N333["DevAutomationPanel.tsx [meridian_frontend/src/components]"]
    N334["DeveloperSuitePanel.tsx [meridian_frontend/src/components]"]
    N335["LocalModelManager.tsx [meridian_frontend/src/components]"]
    N336["MemoryConsolidationView.tsx [meridian_frontend/src/components]"]
    N337["NavRail.tsx [meridian_frontend/src/components]"]
    N338["PerceptionHUD.tsx [meridian_frontend/src/components]"]
    N339["ProactiveGuardBanner.tsx [meridian_frontend/src/components]"]
    N340["ProfileHeader.tsx [meridian_frontend/src/components]"]
    N341["RightDrawer.tsx [meridian_frontend/src/components]"]
    N342["ServerConnectionModal.tsx [meridian_frontend/src/components]"]
    N343["Shell.tsx [meridian_frontend/src/components]"]
    N344["StatusBar.tsx [meridian_frontend/src/components]"]
    N345["DropdownNav.tsx [meridian_frontend/src/components/mobile]"]
    N346["LiveThoughtCarousel.tsx [meridian_frontend/src/components/mobile]"]
    N347["MobilePairingModal.tsx [meridian_frontend/src/components/mobile]"]
    N348["VoiceOrbHUD.tsx [meridian_frontend/src/components/mobile]"]
    N349["AmbientParticles.tsx [meridian_frontend/src/components/ui]"]
    N350["CodeDiffViewer.tsx [meridian_frontend/src/components/ui]"]
    N351["ConnectionBanner.tsx [meridian_frontend/src/components/ui]"]
    N352["DataBadge.tsx [meridian_frontend/src/components/ui]"]
    N353["GlowCard.tsx [meridian_frontend/src/components/ui]"]
    N354["HoloButton.tsx [meridian_frontend/src/components/ui]"]
    N355["ProgressArc.tsx [meridian_frontend/src/components/ui]"]
    N356["TerminalLine.tsx [meridian_frontend/src/components/ui]"]
    N357["ToastContext.tsx [meridian_frontend/src/components/ui]"]
    N358["useMemoryOptimizer.ts [meridian_frontend/src/hooks]"]
    N359["oauthService.ts [meridian_frontend/src/services]"]
    N360["streamingAudioPlayer.ts [meridian_frontend/src/services]"]
    N361["BackendSetup.tsx [meridian_frontend/src/startup]"]
    N362["BootSequence.tsx [meridian_frontend/src/startup]"]
    N363["OnboardingWizard.tsx [meridian_frontend/src/startup]"]
    N364["SetupWizard.tsx [meridian_frontend/src/startup]"]
    N365["Clipboard.tsx [meridian_frontend/src/views]"]
    N366["Jobs.tsx [meridian_frontend/src/views]"]
    N367["MemoryEditor.tsx [meridian_frontend/src/views]"]
    N368["Productivity.tsx [meridian_frontend/src/views]"]
    N369["Settings.tsx [meridian_frontend/src/views]"]
    N370["SwarmDebate.tsx [meridian_frontend/src/views]"]
    N371["Timeline.tsx [meridian_frontend/src/views]"]
    N372["WorkflowBuilder.tsx [meridian_frontend/src/views]"]
    N373["AiModelsTab.tsx [meridian_frontend/src/views/settings]"]
    N374["IntegrationsTab.tsx [meridian_frontend/src/views/settings]"]
    N375["MascotTab.tsx [meridian_frontend/src/views/settings]"]
    N376["MultiModeTab.tsx [meridian_frontend/src/views/settings]"]
    N377["PasswordInput.tsx [meridian_frontend/src/views/settings]"]
    N378["SpendAirGapTab.tsx [meridian_frontend/src/views/settings]"]
    N379["SystemGuardTab.tsx [meridian_frontend/src/views/settings]"]
    N380["VoiceTab.tsx [meridian_frontend/src/views/settings]"]
    N381["config.py [meridian_frontend/src-tauri/api/_internal/cv2]"]
    N382["load_config_py3.py [meridian_frontend/src-tauri/api/_internal/cv2]"]
    N383["__init__.py [meridian_frontend/src-tauri/api/_internal/cv2]"]
    N384["__init__.py [meridian_frontend/src-tauri/api/_internal/cv2/data]"]
    N385["__init__.py [meridian_frontend/src-tauri/api/_internal/cv2/mat_wrapper]"]
    N386["version.py [meridian_frontend/src-tauri/api/_internal/cv2/misc]"]
    N387["__init__.py [meridian_frontend/src-tauri/api/_internal/cv2/typing]"]
    N388["__init__.py [meridian_frontend/src-tauri/api/_internal/cv2/utils]"]
    N389["applications.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N390["background.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N391["cli.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N392["concurrency.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N393["datastructures.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N394["encoders.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N395["exceptions.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N396["exception_handlers.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N397["logger.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N398["params.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N399["param_functions.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N400["requests.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N401["responses.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N402["routing.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N403["sse.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N404["staticfiles.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N405["templating.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N406["testclient.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N407["types.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N408["utils.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N409["websockets.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N410["__init__.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N411["__main__.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N412["models.py [meridian_frontend/src-tauri/api/_internal/fastapi/dependencies]"]
    N413["utils.py [meridian_frontend/src-tauri/api/_internal/fastapi/dependencies]"]
    N414["asyncexitstack.py [meridian_frontend/src-tauri/api/_internal/fastapi/middleware]"]
    N415["cors.py [meridian_frontend/src-tauri/api/_internal/fastapi/middleware]"]
    N416["gzip.py [meridian_frontend/src-tauri/api/_internal/fastapi/middleware]"]
    N417["httpsredirect.py [meridian_frontend/src-tauri/api/_internal/fastapi/middleware]"]
    N418["trustedhost.py [meridian_frontend/src-tauri/api/_internal/fastapi/middleware]"]
    N419["wsgi.py [meridian_frontend/src-tauri/api/_internal/fastapi/middleware]"]
    N420["__init__.py [meridian_frontend/src-tauri/api/_internal/fastapi/middleware]"]
    N421["docs.py [meridian_frontend/src-tauri/api/_internal/fastapi/openapi]"]
    N422["models.py [meridian_frontend/src-tauri/api/_internal/fastapi/openapi]"]
    N423["utils.py [meridian_frontend/src-tauri/api/_internal/fastapi/openapi]"]
    N424["api_key.py [meridian_frontend/src-tauri/api/_internal/fastapi/security]"]
    N425["base.py [meridian_frontend/src-tauri/api/_internal/fastapi/security]"]
    N426["http.py [meridian_frontend/src-tauri/api/_internal/fastapi/security]"]
    N427["oauth2.py [meridian_frontend/src-tauri/api/_internal/fastapi/security]"]
    N428["open_id_connect_url.py [meridian_frontend/src-tauri/api/_internal/fastapi/security]"]
    N429["shared.py [meridian_frontend/src-tauri/api/_internal/fastapi/_compat]"]
    N430["v2.py [meridian_frontend/src-tauri/api/_internal/fastapi/_compat]"]
    N431["coreBundle.js [meridian_frontend/src-tauri/api/_internal/playwright/driver/package/lib]"]
    N432["utilsBundle.js [meridian_frontend/src-tauri/api/_internal/playwright/driver/package/lib]"]
    N433["structs.d.ts [meridian_frontend/src-tauri/api/_internal/playwright/driver/package/types]"]
    N434["types.d.ts [meridian_frontend/src-tauri/api/_internal/playwright/driver/package/types]"]
    N435["aliases.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N436["alias_generators.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N437["annotated_handlers.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N438["color.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N439["config.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N440["dataclasses.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N441["errors.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N442["fields.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N443["functional_serializers.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N444["functional_validators.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N445["json_schema.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N446["main.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N447["mypy.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N448["networks.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N449["root_model.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N450["types.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N451["type_adapter.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N452["validate_call_decorator.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N453["version.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N454["warnings.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N455["_migration.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N456["__init__.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N457["class_validators.py [meridian_frontend/src-tauri/api/_internal/pydantic/deprecated]"]
    N458["config.py [meridian_frontend/src-tauri/api/_internal/pydantic/deprecated]"]
    N459["copy_internals.py [meridian_frontend/src-tauri/api/_internal/pydantic/deprecated]"]
    N460["decorator.py [meridian_frontend/src-tauri/api/_internal/pydantic/deprecated]"]
    N461["json.py [meridian_frontend/src-tauri/api/_internal/pydantic/deprecated]"]
    N462["parse.py [meridian_frontend/src-tauri/api/_internal/pydantic/deprecated]"]
    N463["tools.py [meridian_frontend/src-tauri/api/_internal/pydantic/deprecated]"]
    N464["arguments_schema.py [meridian_frontend/src-tauri/api/_internal/pydantic/experimental]"]
    N465["missing_sentinel.py [meridian_frontend/src-tauri/api/_internal/pydantic/experimental]"]
    N466["pipeline.py [meridian_frontend/src-tauri/api/_internal/pydantic/experimental]"]
    N467["_loader.py [meridian_frontend/src-tauri/api/_internal/pydantic/plugin]"]
    N468["_schema_validator.py [meridian_frontend/src-tauri/api/_internal/pydantic/plugin]"]
    N469["__init__.py [meridian_frontend/src-tauri/api/_internal/pydantic/plugin]"]
    N470["annotated_types.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N471["class_validators.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N472["color.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N473["config.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N474["dataclasses.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N475["datetime_parse.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N476["decorator.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N477["env_settings.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N478["errors.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N479["error_wrappers.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N480["fields.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N481["generics.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N482["json.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N483["main.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N484["mypy.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N485["networks.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N486["parse.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N487["schema.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N488["tools.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N489["types.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N490["typing.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N491["utils.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N492["validators.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N493["version.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N494["_hypothesis_plugin.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N495["__init__.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N496["_config.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N497["_core_metadata.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N498["_core_utils.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N499["_dataclasses.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N500["_decorators.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N501["_decorators_v1.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N502["_discriminated_union.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N503["_docs_extraction.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N504["_fields.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N505["_forward_ref.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N506["_generate_schema.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N507["_generics.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N508["_git.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N509["_import_utils.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N510["_internal_dataclass.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N511["_known_annotated_metadata.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N512["_mock_val_ser.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N513["_model_construction.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N514["_namespace_utils.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N515["_repr.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N516["_schema_gather.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N517["_schema_generation_shared.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N518["_serializers.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N519["_signature.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N520["_typing_extra.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N521["_utils.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N522["_validate_call.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N523["_validators.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N524["applications.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N525["authentication.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N526["background.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N527["concurrency.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N528["config.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N529["convertors.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N530["datastructures.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N531["endpoints.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N532["exceptions.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N533["formparsers.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N534["requests.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N535["responses.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N536["routing.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N537["schemas.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N538["staticfiles.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N539["status.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N540["templating.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N541["testclient.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N542["types.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N543["websockets.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N544["_exception_handler.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N545["_utils.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N546["authentication.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N547["base.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N548["cors.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N549["errors.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N550["exceptions.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N551["gzip.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N552["httpsredirect.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N553["sessions.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N554["trustedhost.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N555["wsgi.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N556["__init__.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N557["config.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N558["importer.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N559["logging.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N560["main.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N561["server.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N562["workers.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N563["_compat.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N564["_subprocess.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N565["_types.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N566["__init__.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N567["__main__.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N568["off.py [meridian_frontend/src-tauri/api/_internal/uvicorn/lifespan]"]
    N569["on.py [meridian_frontend/src-tauri/api/_internal/uvicorn/lifespan]"]
    N570["asyncio.py [meridian_frontend/src-tauri/api/_internal/uvicorn/loops]"]
    N571["auto.py [meridian_frontend/src-tauri/api/_internal/uvicorn/loops]"]
    N572["uvloop.py [meridian_frontend/src-tauri/api/_internal/uvicorn/loops]"]
    N573["asgi2.py [meridian_frontend/src-tauri/api/_internal/uvicorn/middleware]"]
    N574["message_logger.py [meridian_frontend/src-tauri/api/_internal/uvicorn/middleware]"]
    N575["proxy_headers.py [meridian_frontend/src-tauri/api/_internal/uvicorn/middleware]"]
    N576["wsgi.py [meridian_frontend/src-tauri/api/_internal/uvicorn/middleware]"]
    N577["utils.py [meridian_frontend/src-tauri/api/_internal/uvicorn/protocols]"]
    N578["auto.py [meridian_frontend/src-tauri/api/_internal/uvicorn/protocols/http]"]
    N579["flow_control.py [meridian_frontend/src-tauri/api/_internal/uvicorn/protocols/http]"]
    N580["h11_impl.py [meridian_frontend/src-tauri/api/_internal/uvicorn/protocols/http]"]
    N581["httptools_impl.py [meridian_frontend/src-tauri/api/_internal/uvicorn/protocols/http]"]
    N582["auto.py [meridian_frontend/src-tauri/api/_internal/uvicorn/protocols/websockets]"]
    N583["websockets_impl.py [meridian_frontend/src-tauri/api/_internal/uvicorn/protocols/websockets]"]
    N584["websockets_sansio_impl.py [meridian_frontend/src-tauri/api/_internal/uvicorn/protocols/websockets]"]
    N585["wsproto_impl.py [meridian_frontend/src-tauri/api/_internal/uvicorn/protocols/websockets]"]
    N586["basereload.py [meridian_frontend/src-tauri/api/_internal/uvicorn/supervisors]"]
    N587["multiprocess.py [meridian_frontend/src-tauri/api/_internal/uvicorn/supervisors]"]
    N588["statreload.py [meridian_frontend/src-tauri/api/_internal/uvicorn/supervisors]"]
    N589["watchfilesreload.py [meridian_frontend/src-tauri/api/_internal/uvicorn/supervisors]"]
    N590["__init__.py [meridian_frontend/src-tauri/api/_internal/uvicorn/supervisors]"]
    N591["auth.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N592["cli.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N593["client.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N594["connection.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N595["datastructures.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N596["exceptions.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N597["frames.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N598["headers.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N599["http11.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N600["imports.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N601["protocol.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N602["proxy.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N603["server.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N604["streams.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N605["typing.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N606["uri.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N607["utils.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N608["version.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N609["__init__.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N610["client.py [meridian_frontend/src-tauri/api/_internal/websockets/asyncio]"]
    N611["connection.py [meridian_frontend/src-tauri/api/_internal/websockets/asyncio]"]
    N612["messages.py [meridian_frontend/src-tauri/api/_internal/websockets/asyncio]"]
    N613["router.py [meridian_frontend/src-tauri/api/_internal/websockets/asyncio]"]
    N614["server.py [meridian_frontend/src-tauri/api/_internal/websockets/asyncio]"]
    N615["base.py [meridian_frontend/src-tauri/api/_internal/websockets/extensions]"]
    N616["permessage_deflate.py [meridian_frontend/src-tauri/api/_internal/websockets/extensions]"]
    N617["auth.py [meridian_frontend/src-tauri/api/_internal/websockets/legacy]"]
    N618["client.py [meridian_frontend/src-tauri/api/_internal/websockets/legacy]"]
    N619["exceptions.py [meridian_frontend/src-tauri/api/_internal/websockets/legacy]"]
    N620["framing.py [meridian_frontend/src-tauri/api/_internal/websockets/legacy]"]
    N621["handshake.py [meridian_frontend/src-tauri/api/_internal/websockets/legacy]"]
    N622["http.py [meridian_frontend/src-tauri/api/_internal/websockets/legacy]"]
    N623["protocol.py [meridian_frontend/src-tauri/api/_internal/websockets/legacy]"]
    N624["server.py [meridian_frontend/src-tauri/api/_internal/websockets/legacy]"]
    N625["__init__.py [meridian_frontend/src-tauri/api/_internal/websockets/legacy]"]
    N626["client.py [meridian_frontend/src-tauri/api/_internal/websockets/sync]"]
    N627["connection.py [meridian_frontend/src-tauri/api/_internal/websockets/sync]"]
    N628["messages.py [meridian_frontend/src-tauri/api/_internal/websockets/sync]"]
    N629["router.py [meridian_frontend/src-tauri/api/_internal/websockets/sync]"]
    N630["server.py [meridian_frontend/src-tauri/api/_internal/websockets/sync]"]
    N631["utils.py [meridian_frontend/src-tauri/api/_internal/websockets/sync]"]
    N632["client.py [meridian_frontend/src-tauri/api/_internal/websockets/trio]"]
    N633["connection.py [meridian_frontend/src-tauri/api/_internal/websockets/trio]"]
    N634["messages.py [meridian_frontend/src-tauri/api/_internal/websockets/trio]"]
    N635["router.py [meridian_frontend/src-tauri/api/_internal/websockets/trio]"]
    N636["server.py [meridian_frontend/src-tauri/api/_internal/websockets/trio]"]
    N637["utils.py [meridian_frontend/src-tauri/api/_internal/websockets/trio]"]
    N638["build_apk.py [meridian_mobile]"]
    N639["flutter_lldb_helper.py [meridian_mobile/ios/Flutter/ephemeral]"]
    N640["get_system_platform_info.py [plugins]"]

    N1 --> N461
    N1 --> N482
    N1 --> N490
    N1 --> N605
    N2 --> N461
    N2 --> N482
    N2 --> N490
    N2 --> N605
    N3 --> N461
    N3 --> N482
    N4 --> N461
    N4 --> N482
    N4 --> N490
    N4 --> N605
    N5 --> N570
    N5 --> N461
    N5 --> N482
    N5 --> N15
    N5 --> N14
    N9 --> N461
    N9 --> N482
    N9 --> N490
    N9 --> N605
    N10 --> N440
    N10 --> N474
    N13 --> N10
    N13 --> N54
    N13 --> N381
    N13 --> N439
    N13 --> N458
    N13 --> N473
    N13 --> N528
    N13 --> N557
    N13 --> N12
    N13 --> N11
    N14 --> N461
    N14 --> N482
    N14 --> N559
    N14 --> N570
    N14 --> N490
    N14 --> N605
    N14 --> N15
    N16 --> N461
    N16 --> N482
    N16 --> N570
    N16 --> N559
    N16 --> N490
    N16 --> N605
    N20 --> N461
    N20 --> N482
    N20 --> N490
    N20 --> N605
    N20 --> N15
    N21 --> N461
    N21 --> N482
    N21 --> N559
    N21 --> N490
    N21 --> N605
    N22 --> N461
    N22 --> N482
    N22 --> N570
    N22 --> N490
    N22 --> N605
    N22 --> N15
    N23 --> N461
    N23 --> N482
    N23 --> N559
    N23 --> N490
    N23 --> N605
    N23 --> N15
    N24 --> N461
    N24 --> N482
    N24 --> N490
    N24 --> N605
    N25 --> N461
    N25 --> N482
    N25 --> N490
    N25 --> N605
    N25 --> N15
    N26 --> N490
    N26 --> N605
    N27 --> N490
    N27 --> N605
    N27 --> N15
    N28 --> N490
    N28 --> N605
    N28 --> N15
    N29 --> N461
    N29 --> N482
    N29 --> N490
    N29 --> N605
    N29 --> N15
    N30 --> N461
    N30 --> N482
    N30 --> N559
    N30 --> N570
    N30 --> N490
    N30 --> N605
    N30 --> N15
    N31 --> N461
    N31 --> N482
    N31 --> N490
    N31 --> N605
    N31 --> N15
    N31 --> N570
    N32 --> N490
    N32 --> N605
    N33 --> N559
    N33 --> N490
    N33 --> N605
    N34 --> N461
    N34 --> N482
    N34 --> N570
    N34 --> N490
    N34 --> N605
    N35 --> N461
    N35 --> N482
    N35 --> N490
    N35 --> N605
    N35 --> N15
    N37 --> N461
    N37 --> N482
    N37 --> N559
    N37 --> N490
    N37 --> N605
    N37 --> N15
    N38 --> N570
    N38 --> N559
    N38 --> N490
    N38 --> N605
    N39 --> N559
    N39 --> N490
    N39 --> N605
    N40 --> N461
    N40 --> N482
    N40 --> N559
    N40 --> N490
    N40 --> N605
    N41 --> N461
    N41 --> N482
    N41 --> N559
    N42 --> N490
    N42 --> N605
    N42 --> N461
    N42 --> N482
    N43 --> N559
    N43 --> N490
    N43 --> N605
    N44 --> N559
    N44 --> N490
    N44 --> N605
    N45 --> N559
    N45 --> N490
    N45 --> N605
    N45 --> N461
    N45 --> N482
    N46 --> N570
    N46 --> N461
    N46 --> N482
    N46 --> N559
    N46 --> N490
    N46 --> N605
    N47 --> N570
    N47 --> N490
    N47 --> N605
    N48 --> N559
    N48 --> N490
    N48 --> N605
    N49 --> N570
    N49 --> N490
    N49 --> N605
    N50 --> N490
    N50 --> N605
    N50 --> N15
    N51 --> N490
    N51 --> N605
    N52 --> N461
    N52 --> N482
    N52 --> N559
    N52 --> N490
    N52 --> N605
    N53 --> N559
    N53 --> N490
    N53 --> N605
    N55 --> N570
    N55 --> N490
    N55 --> N605
    N55 --> N15
    N56 --> N461
    N56 --> N482
    N56 --> N559
    N56 --> N490
    N56 --> N605
    N56 --> N570
    N56 --> N15
    N57 --> N559
    N57 --> N490
    N57 --> N605
    N58 --> N570
    N58 --> N559
    N58 --> N490
    N58 --> N605
    N59 --> N570
    N59 --> N490
    N59 --> N605
    N59 --> N15
    N60 --> N490
    N60 --> N605
    N62 --> N461
    N62 --> N482
    N62 --> N559
    N62 --> N490
    N62 --> N605
    N62 --> N15
    N63 --> N559
    N63 --> N490
    N63 --> N605
    N64 --> N559
    N64 --> N490
    N64 --> N605
    N65 --> N490
    N65 --> N605
    N66 --> N559
    N66 --> N490
    N66 --> N605
    N67 --> N559
    N67 --> N490
    N67 --> N605
    N68 --> N490
    N68 --> N605
    N68 --> N15
    N69 --> N559
    N69 --> N490
    N69 --> N605
    N70 --> N559
    N70 --> N490
    N70 --> N605
    N71 --> N490
    N71 --> N605
    N72 --> N461
    N72 --> N482
    N72 --> N490
    N72 --> N605
    N73 --> N461
    N73 --> N482
    N73 --> N490
    N73 --> N605
    N74 --> N559
    N74 --> N490
    N74 --> N605
    N74 --> N454
    N74 --> N461
    N74 --> N482
    N76 --> N570
    N76 --> N559
    N76 --> N15
    N77 --> N559
    N77 --> N490
    N77 --> N605
    N77 --> N15
    N78 --> N570
    N78 --> N559
    N78 --> N490
    N78 --> N605
    N78 --> N15
    N79 --> N490
    N79 --> N605
    N79 --> N15
    N80 --> N461
    N80 --> N482
    N80 --> N559
    N80 --> N570
    N80 --> N490
    N80 --> N605
    N80 --> N15
    N81 --> N559
    N81 --> N570
    N81 --> N490
    N81 --> N605
    N81 --> N15
    N81 --> N461
    N81 --> N482
    N82 --> N461
    N82 --> N482
    N82 --> N559
    N82 --> N490
    N82 --> N605
    N83 --> N559
    N83 --> N461
    N83 --> N482
    N84 --> N461
    N84 --> N482
    N84 --> N570
    N84 --> N490
    N84 --> N605
    N84 --> N15
    N85 --> N461
    N85 --> N482
    N85 --> N570
    N85 --> N490
    N85 --> N605
    N85 --> N15
    N86 --> N461
    N86 --> N482
    N86 --> N490
    N86 --> N605
    N86 --> N15
    N87 --> N461
    N87 --> N482
    N87 --> N570
    N87 --> N490
    N87 --> N605
    N87 --> N15
    N88 --> N461
    N88 --> N482
    N88 --> N570
    N88 --> N490
    N88 --> N605
    N88 --> N15
    N89 --> N461
    N89 --> N482
    N89 --> N570
    N89 --> N490
    N89 --> N605
    N89 --> N15
    N90 --> N461
    N90 --> N482
    N90 --> N570
    N90 --> N490
    N90 --> N605
    N91 --> N559
    N91 --> N490
    N91 --> N605
    N92 --> N461
    N92 --> N482
    N92 --> N570
    N92 --> N559
    N92 --> N490
    N92 --> N605
    N93 --> N570
    N93 --> N461
    N93 --> N482
    N93 --> N559
    N93 --> N490
    N93 --> N605
    N94 --> N461
    N94 --> N482
    N94 --> N490
    N94 --> N605
    N95 --> N559
    N95 --> N570
    N95 --> N461
    N95 --> N482
    N95 --> N490
    N95 --> N605
    N95 --> N15
    N96 --> N461
    N96 --> N482
    N96 --> N490
    N96 --> N605
    N96 --> N15
    N97 --> N461
    N97 --> N482
    N97 --> N559
    N97 --> N490
    N97 --> N605
    N97 --> N15
    N97 --> N570
    N98 --> N490
    N98 --> N605
    N98 --> N15
    N98 --> N461
    N98 --> N482
    N99 --> N490
    N99 --> N605
    N100 --> N461
    N100 --> N482
    N100 --> N490
    N100 --> N605
    N101 --> N559
    N101 --> N570
    N101 --> N490
    N101 --> N605
    N101 --> N461
    N101 --> N482
    N102 --> N461
    N102 --> N482
    N102 --> N490
    N102 --> N605
    N102 --> N15
    N104 --> N490
    N104 --> N605
    N105 --> N490
    N105 --> N605
    N106 --> N559
    N106 --> N490
    N106 --> N605
    N107 --> N559
    N107 --> N490
    N107 --> N605
    N108 --> N559
    N108 --> N490
    N108 --> N605
    N108 --> N15
    N109 --> N490
    N109 --> N605
    N110 --> N559
    N110 --> N490
    N110 --> N605
    N111 --> N559
    N111 --> N490
    N111 --> N605
    N112 --> N559
    N112 --> N490
    N112 --> N605
    N113 --> N559
    N113 --> N490
    N113 --> N605
    N114 --> N559
    N114 --> N490
    N114 --> N605
    N115 --> N461
    N115 --> N482
    N115 --> N490
    N115 --> N605
    N116 --> N490
    N116 --> N605
    N117 --> N461
    N117 --> N482
    N117 --> N559
    N117 --> N490
    N117 --> N605
    N118 --> N490
    N118 --> N605
    N119 --> N559
    N119 --> N490
    N119 --> N605
    N120 --> N570
    N120 --> N454
    N120 --> N15
    N120 --> N461
    N120 --> N482
    N121 --> N570
    N121 --> N559
    N121 --> N490
    N121 --> N605
    N122 --> N559
    N122 --> N490
    N122 --> N605
    N123 --> N559
    N123 --> N490
    N123 --> N605
    N124 --> N559
    N124 --> N490
    N124 --> N605
    N125 --> N559
    N125 --> N490
    N125 --> N605
    N126 --> N559
    N126 --> N490
    N126 --> N605
    N126 --> N15
    N127 --> N461
    N127 --> N482
    N127 --> N570
    N127 --> N490
    N127 --> N605
    N127 --> N15
    N128 --> N570
    N128 --> N461
    N128 --> N482
    N128 --> N490
    N128 --> N605
    N128 --> N15
    N129 --> N559
    N129 --> N490
    N129 --> N605
    N130 --> N490
    N130 --> N605
    N130 --> N570
    N130 --> N15
    N131 --> N490
    N131 --> N605
    N132 --> N490
    N132 --> N605
    N133 --> N559
    N133 --> N490
    N133 --> N605
    N134 --> N490
    N134 --> N605
    N135 --> N559
    N135 --> N490
    N135 --> N605
    N136 --> N461
    N136 --> N482
    N136 --> N490
    N136 --> N605
    N137 --> N559
    N137 --> N490
    N137 --> N605
    N137 --> N15
    N138 --> N559
    N138 --> N490
    N138 --> N605
    N139 --> N559
    N139 --> N490
    N139 --> N605
    N140 --> N559
    N140 --> N490
    N140 --> N605
    N141 --> N559
    N141 --> N490
    N141 --> N605
    N142 --> N461
    N142 --> N482
    N142 --> N490
    N142 --> N605
    N143 --> N559
    N143 --> N490
    N143 --> N605
    N144 --> N490
    N144 --> N605
    N144 --> N15
    N144 --> N14
    N145 --> N570
    N145 --> N490
    N145 --> N605
    N146 --> N490
    N146 --> N605
    N147 --> N559
    N147 --> N490
    N147 --> N605
    N147 --> N15
    N149 --> N490
    N149 --> N605
    N150 --> N490
    N150 --> N605
    N151 --> N490
    N151 --> N605
    N152 --> N490
    N152 --> N605
    N153 --> N490
    N153 --> N605
    N154 --> N490
    N154 --> N605
    N155 --> N461
    N155 --> N482
    N157 --> N461
    N157 --> N482
    N157 --> N490
    N157 --> N605
    N158 --> N461
    N158 --> N482
    N158 --> N490
    N158 --> N605
    N159 --> N490
    N159 --> N605
    N161 --> N490
    N161 --> N605
    N162 --> N461
    N162 --> N482
    N162 --> N490
    N162 --> N605
    N163 --> N559
    N163 --> N490
    N163 --> N605
    N164 --> N461
    N164 --> N482
    N164 --> N559
    N164 --> N490
    N164 --> N605
    N165 --> N570
    N165 --> N490
    N165 --> N605
    N166 --> N461
    N166 --> N482
    N166 --> N490
    N166 --> N605
    N166 --> N570
    N166 --> N15
    N167 --> N490
    N167 --> N605
    N168 --> N490
    N168 --> N605
    N168 --> N15
    N169 --> N490
    N169 --> N605
    N169 --> N15
    N169 --> N461
    N169 --> N482
    N170 --> N559
    N170 --> N490
    N170 --> N605
    N170 --> N15
    N171 --> N490
    N171 --> N605
    N171 --> N15
    N172 --> N490
    N172 --> N605
    N172 --> N15
    N173 --> N490
    N173 --> N605
    N174 --> N570
    N174 --> N490
    N174 --> N605
    N175 --> N490
    N175 --> N605
    N176 --> N490
    N176 --> N605
    N177 --> N490
    N177 --> N605
    N178 --> N490
    N178 --> N605
    N179 --> N559
    N179 --> N490
    N179 --> N605
    N180 --> N461
    N180 --> N482
    N180 --> N490
    N180 --> N605
    N181 --> N461
    N181 --> N482
    N181 --> N490
    N181 --> N605
    N181 --> N15
    N182 --> N461
    N182 --> N482
    N182 --> N400
    N182 --> N534
    N182 --> N490
    N182 --> N605
    N183 --> N490
    N183 --> N605
    N184 --> N490
    N184 --> N605
    N185 --> N461
    N185 --> N482
    N185 --> N490
    N185 --> N605
    N186 --> N490
    N186 --> N605
    N187 --> N490
    N187 --> N605
    N188 --> N461
    N188 --> N482
    N188 --> N490
    N188 --> N605
    N189 --> N490
    N189 --> N605
    N189 --> N15
    N190 --> N559
    N190 --> N490
    N190 --> N605
    N191 --> N461
    N191 --> N482
    N191 --> N490
    N191 --> N605
    N192 --> N490
    N192 --> N605
    N193 --> N559
    N193 --> N490
    N193 --> N605
    N194 --> N15
    N195 --> N461
    N195 --> N482
    N195 --> N490
    N195 --> N605
    N195 --> N440
    N195 --> N474
    N195 --> N10
    N195 --> N54
    N195 --> N381
    N195 --> N439
    N195 --> N458
    N195 --> N473
    N195 --> N528
    N195 --> N557
    N195 --> N12
    N195 --> N11
    N196 --> N490
    N196 --> N605
    N197 --> N490
    N197 --> N605
    N198 --> N461
    N198 --> N482
    N198 --> N570
    N198 --> N559
    N198 --> N490
    N198 --> N605
    N198 --> N15
    N199 --> N559
    N199 --> N490
    N199 --> N605
    N200 --> N461
    N200 --> N482
    N200 --> N15
    N201 --> N570
    N201 --> N490
    N201 --> N605
    N201 --> N15
    N201 --> N461
    N201 --> N482
    N202 --> N490
    N202 --> N605
    N202 --> N15
    N204 --> N461
    N204 --> N482
    N204 --> N490
    N204 --> N605
    N205 --> N490
    N205 --> N605
    N205 --> N15
    N206 --> N490
    N206 --> N605
    N207 --> N490
    N207 --> N605
    N207 --> N15
    N208 --> N15
    N211 --> N490
    N211 --> N605
    N212 --> N461
    N212 --> N482
    N212 --> N490
    N212 --> N605
    N213 --> N490
    N213 --> N605
    N214 --> N490
    N214 --> N605
    N214 --> N461
    N214 --> N482
    N215 --> N559
    N215 --> N490
    N215 --> N605
    N217 --> N490
    N217 --> N605
    N218 --> N490
    N218 --> N605
    N218 --> N15
    N219 --> N461
    N219 --> N482
    N219 --> N490
    N219 --> N605
    N219 --> N15
    N220 --> N490
    N220 --> N605
    N220 --> N15
    N221 --> N490
    N221 --> N605
    N222 --> N461
    N222 --> N482
    N222 --> N559
    N222 --> N490
    N222 --> N605
    N222 --> N15
    N223 --> N559
    N223 --> N490
    N223 --> N605
    N224 --> N559
    N224 --> N490
    N224 --> N605
    N225 --> N570
    N225 --> N559
    N225 --> N490
    N225 --> N605
    N226 --> N490
    N226 --> N605
    N227 --> N559
    N227 --> N490
    N227 --> N605
    N228 --> N559
    N228 --> N15
    N229 --> N559
    N229 --> N490
    N229 --> N605
    N229 --> N15
    N230 --> N490
    N230 --> N605
    N231 --> N490
    N231 --> N605
    N232 --> N559
    N232 --> N490
    N232 --> N605
    N232 --> N15
    N236 --> N461
    N236 --> N482
    N237 --> N570
    N237 --> N461
    N237 --> N482
    N239 --> N570
    N239 --> N14
    N241 --> N15
    N242 --> N14
    N245 --> N570
    N249 --> N15
    N250 --> N14
    N254 --> N15
    N256 --> N15
    N257 --> N570
    N263 --> N15
    N264 --> N15
    N265 --> N14
    N267 --> N461
    N267 --> N482
    N267 --> N15
    N269 --> N461
    N269 --> N482
    N269 --> N15
    N269 --> N570
    N270 --> N570
    N270 --> N14
    N273 --> N461
    N273 --> N482
    N276 --> N15
    N279 --> N570
    N280 --> N559
    N280 --> N461
    N280 --> N482
    N281 --> N461
    N281 --> N482
    N282 --> N570
    N283 --> N461
    N283 --> N482
    N283 --> N14
    N283 --> N570
    N284 --> N15
    N285 --> N461
    N285 --> N482
    N285 --> N15
    N285 --> N14
    N287 --> N570
    N287 --> N14
    N289 --> N15
    N290 --> N14
    N291 --> N570
    N292 --> N461
    N292 --> N482
    N293 --> N570
    N293 --> N14
    N295 --> N461
    N295 --> N482
    N296 --> N461
    N296 --> N482
    N297 --> N14
    N297 --> N490
    N297 --> N605
    N297 --> N570
    N300 --> N14
    N301 --> N461
    N301 --> N482
    N302 --> N559
    N303 --> N15
    N304 --> N14
    N305 --> N570
    N306 --> N461
    N306 --> N482
    N306 --> N4
    N307 --> N461
    N307 --> N482
    N307 --> N16
    N308 --> N570
    N309 --> N570
    N311 --> N461
    N311 --> N482
    N312 --> N461
    N312 --> N482
    N313 --> N461
    N313 --> N482
    N314 --> N570
    N320 --> N14
    N321 --> N14
    N322 --> N14
    N326 --> N407
    N326 --> N434
    N326 --> N450
    N326 --> N489
    N326 --> N542
    N326 --> N10
    N326 --> N54
    N326 --> N381
    N326 --> N439
    N326 --> N458
    N326 --> N473
    N326 --> N528
    N326 --> N557
    N327 --> N593
    N327 --> N610
    N327 --> N618
    N327 --> N626
    N327 --> N632
    N327 --> N362
    N327 --> N364
    N327 --> N343
    N327 --> N326
    N327 --> N10
    N327 --> N54
    N327 --> N381
    N327 --> N439
    N327 --> N458
    N327 --> N473
    N327 --> N528
    N327 --> N557
    N327 --> N363
    N327 --> N361
    N328 --> N10
    N328 --> N54
    N328 --> N381
    N328 --> N439
    N328 --> N458
    N328 --> N473
    N328 --> N528
    N328 --> N557
    N328 --> N326
    N328 --> N360
    N330 --> N345
    N330 --> N348
    N330 --> N346
    N331 --> N10
    N331 --> N54
    N331 --> N381
    N331 --> N439
    N331 --> N458
    N331 --> N473
    N331 --> N528
    N331 --> N557
    N333 --> N10
    N333 --> N54
    N333 --> N381
    N333 --> N439
    N333 --> N458
    N333 --> N473
    N333 --> N528
    N333 --> N557
    N334 --> N10
    N334 --> N54
    N334 --> N381
    N334 --> N439
    N334 --> N458
    N334 --> N473
    N334 --> N528
    N334 --> N557
    N335 --> N357
    N335 --> N10
    N335 --> N54
    N335 --> N381
    N335 --> N439
    N335 --> N458
    N335 --> N473
    N335 --> N528
    N335 --> N557
    N336 --> N10
    N336 --> N54
    N336 --> N381
    N336 --> N439
    N336 --> N458
    N336 --> N473
    N336 --> N528
    N336 --> N557
    N337 --> N326
    N337 --> N328
    N339 --> N10
    N339 --> N54
    N339 --> N381
    N339 --> N439
    N339 --> N458
    N339 --> N473
    N339 --> N528
    N339 --> N557
    N341 --> N326
    N341 --> N355
    N341 --> N352
    N342 --> N10
    N342 --> N54
    N342 --> N381
    N342 --> N439
    N342 --> N458
    N342 --> N473
    N342 --> N528
    N342 --> N557
    N343 --> N326
    N343 --> N337
    N343 --> N344
    N343 --> N341
    N343 --> N332
    N343 --> N357
    N343 --> N371
    N343 --> N366
    N343 --> N365
    N343 --> N368
    N343 --> N349
    N343 --> N339
    N343 --> N351
    N344 --> N347
    N344 --> N326
    N344 --> N10
    N344 --> N54
    N344 --> N381
    N344 --> N439
    N344 --> N458
    N344 --> N473
    N344 --> N528
    N344 --> N557
    N347 --> N10
    N347 --> N54
    N347 --> N381
    N347 --> N439
    N347 --> N458
    N347 --> N473
    N347 --> N528
    N347 --> N557
    N349 --> N358
    N351 --> N326
    N351 --> N10
    N351 --> N54
    N351 --> N381
    N351 --> N439
    N351 --> N458
    N351 --> N473
    N351 --> N528
    N351 --> N557
    N359 --> N10
    N359 --> N54
    N359 --> N381
    N359 --> N439
    N359 --> N458
    N359 --> N473
    N359 --> N528
    N359 --> N557
    N360 --> N10
    N360 --> N54
    N360 --> N381
    N360 --> N439
    N360 --> N458
    N360 --> N473
    N360 --> N528
    N360 --> N557
    N361 --> N10
    N361 --> N54
    N361 --> N381
    N361 --> N439
    N361 --> N458
    N361 --> N473
    N361 --> N528
    N361 --> N557
    N362 --> N10
    N362 --> N54
    N362 --> N381
    N362 --> N439
    N362 --> N458
    N362 --> N473
    N362 --> N528
    N362 --> N557
    N362 --> N328
    N363 --> N10
    N363 --> N54
    N363 --> N381
    N363 --> N439
    N363 --> N458
    N363 --> N473
    N363 --> N528
    N363 --> N557
    N364 --> N354
    N364 --> N10
    N364 --> N54
    N364 --> N381
    N364 --> N439
    N364 --> N458
    N364 --> N473
    N364 --> N528
    N364 --> N557
    N365 --> N407
    N365 --> N434
    N365 --> N450
    N365 --> N489
    N365 --> N542
    N365 --> N326
    N365 --> N354
    N365 --> N10
    N365 --> N54
    N365 --> N381
    N365 --> N439
    N365 --> N458
    N365 --> N473
    N365 --> N528
    N365 --> N557
    N366 --> N407
    N366 --> N434
    N366 --> N450
    N366 --> N489
    N366 --> N542
    N366 --> N354
    N366 --> N353
    N366 --> N10
    N366 --> N54
    N366 --> N381
    N366 --> N439
    N366 --> N458
    N366 --> N473
    N366 --> N528
    N366 --> N557
    N367 --> N10
    N367 --> N54
    N367 --> N381
    N367 --> N439
    N367 --> N458
    N367 --> N473
    N367 --> N528
    N367 --> N557
    N368 --> N407
    N368 --> N434
    N368 --> N450
    N368 --> N489
    N368 --> N542
    N368 --> N355
    N368 --> N354
    N368 --> N353
    N368 --> N10
    N368 --> N54
    N368 --> N381
    N368 --> N439
    N368 --> N458
    N368 --> N473
    N368 --> N528
    N368 --> N557
    N368 --> N335
    N368 --> N336
    N368 --> N333
    N368 --> N331
    N368 --> N334
    N369 --> N10
    N369 --> N54
    N369 --> N381
    N369 --> N439
    N369 --> N458
    N369 --> N473
    N369 --> N528
    N369 --> N557
    N369 --> N407
    N369 --> N434
    N369 --> N450
    N369 --> N489
    N369 --> N542
    N369 --> N326
    N369 --> N358
    N369 --> N355
    N369 --> N354
    N369 --> N353
    N369 --> N375
    N369 --> N380
    N369 --> N374
    N369 --> N373
    N369 --> N376
    N369 --> N379
    N369 --> N378
    N369 --> N377
    N370 --> N356
    N370 --> N354
    N370 --> N10
    N370 --> N54
    N370 --> N381
    N370 --> N439
    N370 --> N458
    N370 --> N473
    N370 --> N528
    N370 --> N557
    N371 --> N407
    N371 --> N434
    N371 --> N450
    N371 --> N489
    N371 --> N542
    N371 --> N354
    N371 --> N353
    N371 --> N10
    N371 --> N54
    N371 --> N381
    N371 --> N439
    N371 --> N458
    N371 --> N473
    N371 --> N528
    N371 --> N557
    N371 --> N360
    N371 --> N350
    N372 --> N10
    N372 --> N54
    N372 --> N381
    N372 --> N439
    N372 --> N458
    N372 --> N473
    N372 --> N528
    N372 --> N557
    N373 --> N353
    N373 --> N354
    N373 --> N377
    N374 --> N353
    N374 --> N354
    N374 --> N377
    N374 --> N10
    N374 --> N54
    N374 --> N381
    N374 --> N439
    N374 --> N458
    N374 --> N473
    N374 --> N528
    N374 --> N557
    N375 --> N353
    N376 --> N353
    N376 --> N354
    N376 --> N10
    N376 --> N54
    N376 --> N381
    N376 --> N439
    N376 --> N458
    N376 --> N473
    N376 --> N528
    N376 --> N557
    N378 --> N353
    N378 --> N354
    N379 --> N353
    N379 --> N354
    N380 --> N353
    N380 --> N354
    N385 --> N490
    N385 --> N605
    N387 --> N490
    N387 --> N605
    N389 --> N490
    N389 --> N605
    N390 --> N490
    N390 --> N605
    N392 --> N490
    N392 --> N605
    N393 --> N490
    N393 --> N605
    N394 --> N440
    N394 --> N474
    N394 --> N407
    N394 --> N434
    N394 --> N450
    N394 --> N489
    N394 --> N542
    N394 --> N490
    N394 --> N605
    N395 --> N490
    N395 --> N605
    N397 --> N559
    N398 --> N454
    N398 --> N440
    N398 --> N474
    N398 --> N490
    N398 --> N605
    N399 --> N490
    N399 --> N605
    N401 --> N490
    N401 --> N605
    N402 --> N461
    N402 --> N482
    N402 --> N407
    N402 --> N434
    N402 --> N450
    N402 --> N489
    N402 --> N542
    N402 --> N440
    N402 --> N474
    N402 --> N490
    N402 --> N605
    N403 --> N490
    N403 --> N605
    N407 --> N434
    N407 --> N450
    N407 --> N489
    N407 --> N542
    N407 --> N490
    N407 --> N605
    N408 --> N454
    N408 --> N490
    N408 --> N605
    N412 --> N440
    N412 --> N474
    N412 --> N490
    N412 --> N605
    N412 --> N570
    N413 --> N440
    N413 --> N474
    N413 --> N490
    N413 --> N605
    N421 --> N461
    N421 --> N482
    N421 --> N490
    N421 --> N605
    N422 --> N490
    N422 --> N605
    N423 --> N426
    N423 --> N622
    N423 --> N454
    N423 --> N490
    N423 --> N605
    N424 --> N490
    N424 --> N605
    N426 --> N490
    N426 --> N605
    N427 --> N490
    N427 --> N605
    N428 --> N490
    N428 --> N605
    N429 --> N407
    N429 --> N434
    N429 --> N450
    N429 --> N489
    N429 --> N542
    N429 --> N490
    N429 --> N605
    N429 --> N454
    N429 --> N440
    N429 --> N474
    N430 --> N454
    N430 --> N440
    N430 --> N474
    N430 --> N490
    N430 --> N605
    N433 --> N407
    N433 --> N434
    N433 --> N450
    N433 --> N489
    N433 --> N542
    N434 --> N601
    N434 --> N623
    N434 --> N433
    N435 --> N440
    N435 --> N474
    N435 --> N490
    N435 --> N605
    N437 --> N490
    N437 --> N605
    N438 --> N490
    N438 --> N605
    N439 --> N454
    N439 --> N490
    N439 --> N605
    N440 --> N474
    N440 --> N407
    N440 --> N434
    N440 --> N450
    N440 --> N489
    N440 --> N542
    N440 --> N490
    N440 --> N605
    N440 --> N454
    N441 --> N490
    N441 --> N605
    N442 --> N440
    N442 --> N474
    N442 --> N490
    N442 --> N605
    N442 --> N454
    N442 --> N470
    N443 --> N440
    N443 --> N474
    N443 --> N490
    N443 --> N605
    N444 --> N440
    N444 --> N474
    N444 --> N454
    N444 --> N490
    N444 --> N605
    N445 --> N440
    N445 --> N474
    N445 --> N454
    N445 --> N490
    N445 --> N605
    N446 --> N407
    N446 --> N434
    N446 --> N450
    N446 --> N489
    N446 --> N542
    N446 --> N454
    N446 --> N490
    N446 --> N605
    N446 --> N461
    N446 --> N482
    N447 --> N490
    N447 --> N605
    N447 --> N484
    N447 --> N454
    N448 --> N440
    N448 --> N474
    N448 --> N490
    N448 --> N605
    N449 --> N490
    N449 --> N605
    N450 --> N440
    N450 --> N474
    N450 --> N407
    N450 --> N434
    N450 --> N489
    N450 --> N542
    N450 --> N490
    N450 --> N605
    N450 --> N470
    N450 --> N461
    N450 --> N482
    N451 --> N407
    N451 --> N434
    N451 --> N450
    N451 --> N489
    N451 --> N542
    N451 --> N440
    N451 --> N474
    N451 --> N490
    N451 --> N605
    N452 --> N407
    N452 --> N434
    N452 --> N450
    N452 --> N489
    N452 --> N542
    N452 --> N490
    N452 --> N605
    N455 --> N490
    N455 --> N605
    N455 --> N454
    N456 --> N490
    N456 --> N605
    N456 --> N454
    N457 --> N407
    N457 --> N434
    N457 --> N450
    N457 --> N489
    N457 --> N542
    N457 --> N490
    N457 --> N605
    N457 --> N454
    N458 --> N454
    N458 --> N490
    N458 --> N605
    N459 --> N490
    N459 --> N605
    N460 --> N454
    N460 --> N490
    N460 --> N605
    N461 --> N454
    N461 --> N407
    N461 --> N434
    N461 --> N450
    N461 --> N489
    N461 --> N542
    N461 --> N490
    N461 --> N605
    N461 --> N440
    N461 --> N474
    N462 --> N461
    N462 --> N482
    N462 --> N454
    N462 --> N490
    N462 --> N605
    N463 --> N461
    N463 --> N482
    N463 --> N454
    N463 --> N490
    N463 --> N605
    N464 --> N490
    N464 --> N605
    N466 --> N440
    N466 --> N474
    N466 --> N490
    N466 --> N605
    N466 --> N470
    N466 --> N407
    N466 --> N434
    N466 --> N450
    N466 --> N489
    N466 --> N542
    N467 --> N454
    N467 --> N490
    N467 --> N605
    N468 --> N490
    N468 --> N605
    N469 --> N490
    N469 --> N605
    N470 --> N490
    N470 --> N605
    N471 --> N454
    N471 --> N407
    N471 --> N434
    N471 --> N450
    N471 --> N489
    N471 --> N542
    N471 --> N490
    N471 --> N605
    N472 --> N490
    N472 --> N605
    N473 --> N461
    N473 --> N482
    N473 --> N490
    N473 --> N605
    N474 --> N440
    N474 --> N490
    N474 --> N605
    N475 --> N490
    N475 --> N605
    N476 --> N490
    N476 --> N605
    N477 --> N454
    N477 --> N490
    N477 --> N605
    N478 --> N490
    N478 --> N605
    N479 --> N461
    N479 --> N482
    N479 --> N490
    N479 --> N605
    N480 --> N490
    N480 --> N605
    N481 --> N407
    N481 --> N434
    N481 --> N450
    N481 --> N489
    N481 --> N542
    N481 --> N490
    N481 --> N605
    N482 --> N407
    N482 --> N434
    N482 --> N450
    N482 --> N489
    N482 --> N542
    N482 --> N490
    N482 --> N605
    N482 --> N440
    N482 --> N474
    N483 --> N454
    N483 --> N407
    N483 --> N434
    N483 --> N450
    N483 --> N489
    N483 --> N542
    N483 --> N490
    N483 --> N605
    N484 --> N490
    N484 --> N605
    N484 --> N447
    N484 --> N454
    N485 --> N490
    N485 --> N605
    N486 --> N461
    N486 --> N482
    N486 --> N490
    N486 --> N605
    N487 --> N454
    N487 --> N440
    N487 --> N474
    N487 --> N490
    N487 --> N605
    N488 --> N461
    N488 --> N482
    N488 --> N490
    N488 --> N605
    N489 --> N454
    N489 --> N407
    N489 --> N434
    N489 --> N450
    N489 --> N542
    N489 --> N490
    N489 --> N605
    N490 --> N605
    N490 --> N407
    N490 --> N434
    N490 --> N450
    N490 --> N489
    N490 --> N542
    N491 --> N454
    N491 --> N407
    N491 --> N434
    N491 --> N450
    N491 --> N489
    N491 --> N542
    N491 --> N490
    N491 --> N605
    N492 --> N490
    N492 --> N605
    N492 --> N454
    N494 --> N461
    N494 --> N482
    N494 --> N490
    N494 --> N605
    N496 --> N454
    N496 --> N490
    N496 --> N605
    N497 --> N490
    N497 --> N605
    N497 --> N454
    N498 --> N490
    N498 --> N605
    N499 --> N440
    N499 --> N474
    N499 --> N454
    N499 --> N490
    N499 --> N605
    N500 --> N407
    N500 --> N434
    N500 --> N450
    N500 --> N489
    N500 --> N542
    N500 --> N440
    N500 --> N474
    N500 --> N490
    N500 --> N605
    N501 --> N490
    N501 --> N605
    N502 --> N490
    N502 --> N605
    N503 --> N490
    N503 --> N605
    N504 --> N440
    N504 --> N474
    N504 --> N454
    N504 --> N490
    N504 --> N605
    N504 --> N470
    N505 --> N440
    N505 --> N474
    N505 --> N490
    N505 --> N605
    N506 --> N440
    N506 --> N474
    N506 --> N490
    N506 --> N605
    N506 --> N454
    N506 --> N407
    N506 --> N434
    N506 --> N450
    N506 --> N489
    N506 --> N542
    N507 --> N407
    N507 --> N434
    N507 --> N450
    N507 --> N489
    N507 --> N542
    N507 --> N490
    N507 --> N605
    N509 --> N490
    N509 --> N605
    N511 --> N490
    N511 --> N605
    N511 --> N470
    N512 --> N490
    N512 --> N605
    N513 --> N490
    N513 --> N605
    N513 --> N454
    N513 --> N407
    N513 --> N434
    N513 --> N450
    N513 --> N489
    N513 --> N542
    N514 --> N490
    N514 --> N605
    N515 --> N407
    N515 --> N434
    N515 --> N450
    N515 --> N489
    N515 --> N542
    N515 --> N490
    N515 --> N605
    N516 --> N440
    N516 --> N474
    N516 --> N490
    N516 --> N605
    N517 --> N490
    N517 --> N605
    N518 --> N490
    N518 --> N605
    N519 --> N440
    N519 --> N474
    N519 --> N490
    N519 --> N605
    N520 --> N407
    N520 --> N434
    N520 --> N450
    N520 --> N489
    N520 --> N542
    N520 --> N490
    N520 --> N605
    N521 --> N440
    N521 --> N474
    N521 --> N454
    N521 --> N407
    N521 --> N434
    N521 --> N450
    N521 --> N489
    N521 --> N542
    N521 --> N490
    N521 --> N605
    N522 --> N490
    N522 --> N605
    N523 --> N490
    N523 --> N605
    N524 --> N490
    N524 --> N605
    N525 --> N490
    N525 --> N605
    N526 --> N490
    N526 --> N605
    N527 --> N454
    N527 --> N490
    N527 --> N605
    N528 --> N454
    N528 --> N490
    N528 --> N605
    N529 --> N490
    N529 --> N605
    N530 --> N490
    N530 --> N605
    N531 --> N461
    N531 --> N482
    N531 --> N490
    N531 --> N605
    N532 --> N426
    N532 --> N622
    N533 --> N440
    N533 --> N474
    N533 --> N490
    N533 --> N605
    N534 --> N461
    N534 --> N482
    N534 --> N426
    N534 --> N622
    N534 --> N490
    N534 --> N605
    N535 --> N426
    N535 --> N622
    N535 --> N461
    N535 --> N482
    N535 --> N490
    N535 --> N605
    N536 --> N407
    N536 --> N434
    N536 --> N450
    N536 --> N489
    N536 --> N542
    N536 --> N454
    N536 --> N490
    N536 --> N605
    N537 --> N490
    N537 --> N605
    N538 --> N490
    N538 --> N605
    N539 --> N454
    N540 --> N490
    N540 --> N605
    N541 --> N461
    N541 --> N482
    N541 --> N454
    N541 --> N407
    N541 --> N434
    N541 --> N450
    N541 --> N489
    N541 --> N542
    N541 --> N490
    N541 --> N605
    N542 --> N490
    N542 --> N605
    N543 --> N461
    N543 --> N482
    N543 --> N490
    N543 --> N605
    N544 --> N490
    N544 --> N605
    N545 --> N490
    N545 --> N605
    N545 --> N570
    N547 --> N490
    N547 --> N605
    N550 --> N490
    N550 --> N605
    N551 --> N416
    N551 --> N490
    N551 --> N605
    N553 --> N461
    N553 --> N482
    N553 --> N490
    N553 --> N605
    N555 --> N454
    N555 --> N490
    N555 --> N605
    N556 --> N490
    N556 --> N605
    N557 --> N570
    N557 --> N461
    N557 --> N482
    N557 --> N559
    N557 --> N490
    N557 --> N605
    N558 --> N490
    N558 --> N605
    N559 --> N426
    N559 --> N622
    N559 --> N490
    N559 --> N605
    N560 --> N570
    N560 --> N559
    N560 --> N454
    N560 --> N490
    N560 --> N605
    N561 --> N570
    N561 --> N559
    N561 --> N407
    N561 --> N434
    N561 --> N450
    N561 --> N489
    N561 --> N542
    N561 --> N490
    N561 --> N605
    N562 --> N570
    N562 --> N559
    N562 --> N454
    N562 --> N490
    N562 --> N605
    N563 --> N570
    N563 --> N490
    N563 --> N605
    N565 --> N407
    N565 --> N434
    N565 --> N450
    N565 --> N489
    N565 --> N542
    N565 --> N490
    N565 --> N605
    N568 --> N490
    N568 --> N605
    N569 --> N570
    N569 --> N559
    N569 --> N490
    N569 --> N605
    N571 --> N570
    N571 --> N572
    N572 --> N570
    N574 --> N559
    N574 --> N490
    N574 --> N605
    N576 --> N570
    N576 --> N454
    N577 --> N570
    N578 --> N570
    N579 --> N570
    N580 --> N570
    N580 --> N426
    N580 --> N622
    N580 --> N559
    N580 --> N490
    N580 --> N605
    N581 --> N570
    N581 --> N426
    N581 --> N622
    N581 --> N559
    N581 --> N490
    N581 --> N605
    N582 --> N570
    N582 --> N34
    N582 --> N409
    N582 --> N543
    N583 --> N570
    N583 --> N426
    N583 --> N622
    N583 --> N559
    N583 --> N490
    N583 --> N605
    N583 --> N34
    N583 --> N409
    N583 --> N543
    N584 --> N570
    N584 --> N559
    N584 --> N426
    N584 --> N622
    N584 --> N490
    N584 --> N605
    N584 --> N34
    N584 --> N409
    N584 --> N543
    N585 --> N570
    N585 --> N559
    N585 --> N490
    N585 --> N605
    N586 --> N559
    N586 --> N407
    N586 --> N434
    N586 --> N450
    N586 --> N489
    N586 --> N542
    N587 --> N559
    N587 --> N490
    N587 --> N605
    N588 --> N559
    N590 --> N490
    N590 --> N605
    N591 --> N454
    N592 --> N570
    N592 --> N490
    N592 --> N605
    N593 --> N454
    N593 --> N490
    N593 --> N605
    N594 --> N454
    N595 --> N490
    N595 --> N605
    N596 --> N454
    N597 --> N440
    N597 --> N474
    N597 --> N490
    N597 --> N605
    N598 --> N490
    N598 --> N605
    N599 --> N440
    N599 --> N474
    N599 --> N454
    N599 --> N490
    N599 --> N605
    N600 --> N454
    N600 --> N490
    N600 --> N605
    N601 --> N559
    N602 --> N440
    N602 --> N474
    N603 --> N426
    N603 --> N622
    N603 --> N454
    N603 --> N490
    N603 --> N605
    N605 --> N426
    N605 --> N622
    N605 --> N559
    N605 --> N490
    N606 --> N440
    N606 --> N474
    N609 --> N490
    N609 --> N605
    N610 --> N570
    N610 --> N559
    N610 --> N407
    N610 --> N434
    N610 --> N450
    N610 --> N489
    N610 --> N542
    N610 --> N490
    N610 --> N605
    N610 --> N34
    N610 --> N409
    N610 --> N543
    N611 --> N570
    N611 --> N559
    N611 --> N407
    N611 --> N434
    N611 --> N450
    N611 --> N489
    N611 --> N542
    N611 --> N490
    N611 --> N605
    N612 --> N570
    N612 --> N490
    N612 --> N605
    N613 --> N426
    N613 --> N622
    N613 --> N490
    N613 --> N605
    N613 --> N34
    N613 --> N409
    N613 --> N543
    N614 --> N570
    N614 --> N426
    N614 --> N622
    N614 --> N559
    N614 --> N407
    N614 --> N434
    N614 --> N450
    N614 --> N489
    N614 --> N542
    N614 --> N490
    N614 --> N605
    N614 --> N34
    N614 --> N409
    N614 --> N543
    N616 --> N490
    N616 --> N605
    N617 --> N426
    N617 --> N622
    N617 --> N490
    N617 --> N605
    N618 --> N570
    N618 --> N559
    N618 --> N454
    N618 --> N407
    N618 --> N434
    N618 --> N450
    N618 --> N489
    N618 --> N542
    N618 --> N490
    N618 --> N605
    N619 --> N426
    N619 --> N622
    N620 --> N490
    N620 --> N605
    N622 --> N570
    N623 --> N570
    N623 --> N559
    N623 --> N454
    N623 --> N490
    N623 --> N605
    N624 --> N570
    N624 --> N426
    N624 --> N622
    N624 --> N559
    N624 --> N454
    N624 --> N407
    N624 --> N434
    N624 --> N450
    N624 --> N489
    N624 --> N542
    N624 --> N490
    N624 --> N605
    N625 --> N454
    N626 --> N559
    N626 --> N454
    N626 --> N407
    N626 --> N434
    N626 --> N450
    N626 --> N489
    N626 --> N542
    N626 --> N490
    N626 --> N605
    N626 --> N34
    N626 --> N409
    N626 --> N543
    N627 --> N559
    N627 --> N407
    N627 --> N434
    N627 --> N450
    N627 --> N489
    N627 --> N542
    N627 --> N490
    N627 --> N605
    N628 --> N490
    N628 --> N605
    N629 --> N426
    N629 --> N622
    N629 --> N490
    N629 --> N605
    N629 --> N34
    N629 --> N409
    N629 --> N543
    N630 --> N426
    N630 --> N622
    N630 --> N559
    N630 --> N454
    N630 --> N407
    N630 --> N434
    N630 --> N450
    N630 --> N489
    N630 --> N542
    N630 --> N490
    N630 --> N605
    N630 --> N34
    N630 --> N409
    N630 --> N543
    N632 --> N559
    N632 --> N407
    N632 --> N434
    N632 --> N450
    N632 --> N489
    N632 --> N542
    N632 --> N490
    N632 --> N605
    N632 --> N34
    N632 --> N409
    N632 --> N543
    N633 --> N559
    N633 --> N407
    N633 --> N434
    N633 --> N450
    N633 --> N489
    N633 --> N542
    N633 --> N490
    N633 --> N605
    N634 --> N490
    N634 --> N605
    N635 --> N426
    N635 --> N622
    N635 --> N490
    N635 --> N605
    N635 --> N34
    N635 --> N409
    N635 --> N543
    N636 --> N426
    N636 --> N622
    N636 --> N559
    N636 --> N407
    N636 --> N434
    N636 --> N450
    N636 --> N489
    N636 --> N542
    N636 --> N490
    N636 --> N605
    N636 --> N34
    N636 --> N409
    N636 --> N543
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