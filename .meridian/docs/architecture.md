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
    N17["__init__.py [meridian_backend/src]"]
    N18["automation.py [meridian_backend/src/api]"]
    N19["chat.py [meridian_backend/src/api]"]
    N20["deps.py [meridian_backend/src/api]"]
    N21["mcp.py [meridian_backend/src/api]"]
    N22["models_mgmt.py [meridian_backend/src/api]"]
    N23["perception.py [meridian_backend/src/api]"]
    N24["profile.py [meridian_backend/src/api]"]
    N25["rag.py [meridian_backend/src/api]"]
    N26["scheduler.py [meridian_backend/src/api]"]
    N27["swarm.py [meridian_backend/src/api]"]
    N28["system.py [meridian_backend/src/api]"]
    N29["vault.py [meridian_backend/src/api]"]
    N30["voice.py [meridian_backend/src/api]"]
    N31["workspace.py [meridian_backend/src/api]"]
    N32["__init__.py [meridian_backend/src/api]"]
    N33["action_journal.py [meridian_backend/src/core]"]
    N34["agent_status_stream.py [meridian_backend/src/core]"]
    N35["ar_bridge.py [meridian_backend/src/core]"]
    N36["atomic_storage.py [meridian_backend/src/core]"]
    N37["audit_logger.py [meridian_backend/src/core]"]
    N38["auth.py [meridian_backend/src/core]"]
    N39["behavior_monitor.py [meridian_backend/src/core]"]
    N40["boilerplate_genie.py [meridian_backend/src/core]"]
    N41["breach_sentinel.py [meridian_backend/src/core]"]
    N42["bus.py [meridian_backend/src/core]"]
    N43["camera_sentinel.py [meridian_backend/src/core]"]
    N44["checkpoints.py [meridian_backend/src/core]"]
    N45["clipboard.py [meridian_backend/src/core]"]
    N46["code_graph.py [meridian_backend/src/core]"]
    N47["cognitive_graph.py [meridian_backend/src/core]"]
    N48["commit_whisperer.py [meridian_backend/src/core]"]
    N49["config.py [meridian_backend/src/core]"]
    N50["confirmations.py [meridian_backend/src/core]"]
    N51["consensus_engine.py [meridian_backend/src/core]"]
    N52["deep_project_context.py [meridian_backend/src/core]"]
    N53["dev_automation.py [meridian_backend/src/core]"]
    N54["discord_bridge.py [meridian_backend/src/core]"]
    N55["discord_utils.py [meridian_backend/src/core]"]
    N56["doc_generator.py [meridian_backend/src/core]"]
    N57["doc_indexer.py [meridian_backend/src/core]"]
    N58["elevated_runner.py [meridian_backend/src/core]"]
    N59["emergency_lockdown.py [meridian_backend/src/core]"]
    N60["experiment_runner.py [meridian_backend/src/core]"]
    N61["explain_code_engine.py [meridian_backend/src/core]"]
    N62["exporter.py [meridian_backend/src/core]"]
    N63["fim_sentinel.py [meridian_backend/src/core]"]
    N64["gaze_tracker.py [meridian_backend/src/core]"]
    N65["governor.py [meridian_backend/src/core]"]
    N66["graph_rag.py [meridian_backend/src/core]"]
    N67["graph_sync.py [meridian_backend/src/core]"]
    N68["hardware_detector.py [meridian_backend/src/core]"]
    N69["history_manager.py [meridian_backend/src/core]"]
    N70["llm_auth.py [meridian_backend/src/core]"]
    N71["llm_client.py [meridian_backend/src/core]"]
    N72["llm_clients.py [meridian_backend/src/core]"]
    N73["llm_provider.py [meridian_backend/src/core]"]
    N74["local_model_manager.py [meridian_backend/src/core]"]
    N75["logger.py [meridian_backend/src/core]"]
    N76["logging_config.py [meridian_backend/src/core]"]
    N77["loop.py [meridian_backend/src/core]"]
    N78["loop_dispatcher.py [meridian_backend/src/core]"]
    N79["loop_executor.py [meridian_backend/src/core]"]
    N80["loop_parser.py [meridian_backend/src/core]"]
    N81["loop_planning.py [meridian_backend/src/core]"]
    N82["loop_stream.py [meridian_backend/src/core]"]
    N83["lsp_client.py [meridian_backend/src/core]"]
    N84["malware_scanner.py [meridian_backend/src/core]"]
    N85["mcp_client.py [meridian_backend/src/core]"]
    N86["mcp_executor.py [meridian_backend/src/core]"]
    N87["memory_backup.py [meridian_backend/src/core]"]
    N88["memory_consolidation.py [meridian_backend/src/core]"]
    N89["memory_editor.py [meridian_backend/src/core]"]
    N90["mobile_bridge.py [meridian_backend/src/core]"]
    N91["mode.py [meridian_backend/src/core]"]
    N92["neural_rag.py [meridian_backend/src/core]"]
    N93["oauth_manager.py [meridian_backend/src/core]"]
    N94["ollama_manager.py [meridian_backend/src/core]"]
    N95["p2p.py [meridian_backend/src/core]"]
    N96["p2p_crypto.py [meridian_backend/src/core]"]
    N97["p2p_discovery.py [meridian_backend/src/core]"]
    N98["p2p_pairing.py [meridian_backend/src/core]"]
    N99["perception.py [meridian_backend/src/core]"]
    N100["persistence_sentinel.py [meridian_backend/src/core]"]
    N101["personal_crm.py [meridian_backend/src/core]"]
    N102["plugins.py [meridian_backend/src/core]"]
    N103["polyglot.py [meridian_backend/src/core]"]
    N104["predictive_engine.py [meridian_backend/src/core]"]
    N105["presence_briefing.py [meridian_backend/src/core]"]
    N106["proactive_system_guard.py [meridian_backend/src/core]"]
    N107["prompt_injection.py [meridian_backend/src/core]"]
    N108["prompt_templates.py [meridian_backend/src/core]"]
    N109["rag_optimizer.py [meridian_backend/src/core]"]
    N110["response_models.py [meridian_backend/src/core]"]
    N111["sandbox_runner.py [meridian_backend/src/core]"]
    N112["scheduler.py [meridian_backend/src/core]"]
    N113["screen_sense.py [meridian_backend/src/core]"]
    N114["security_middleware.py [meridian_backend/src/core]"]
    N115["self_evolving_tooling.py [meridian_backend/src/core]"]
    N116["silent_workflow_guardian.py [meridian_backend/src/core]"]
    N117["skills_loader.py [meridian_backend/src/core]"]
    N118["sos_protocol.py [meridian_backend/src/core]"]
    N119["speculative.py [meridian_backend/src/core]"]
    N120["swarm.py [meridian_backend/src/core]"]
    N121["system_defense.py [meridian_backend/src/core]"]
    N122["telegram_bridge.py [meridian_backend/src/core]"]
    N123["temporal_memory.py [meridian_backend/src/core]"]
    N124["tool_regression_sentinel.py [meridian_backend/src/core]"]
    N125["triggers.py [meridian_backend/src/core]"]
    N126["updater.py [meridian_backend/src/core]"]
    N127["vault.py [meridian_backend/src/core]"]
    N128["vision.py [meridian_backend/src/core]"]
    N129["vision_face.py [meridian_backend/src/core]"]
    N130["vision_gesture.py [meridian_backend/src/core]"]
    N131["watcher.py [meridian_backend/src/core]"]
    N132["what_broke_detective.py [meridian_backend/src/core]"]
    N133["workflow_engine.py [meridian_backend/src/core]"]
    N134["workspace_orchestrator.py [meridian_backend/src/core]"]
    N135["commits.py [meridian_backend/src/core/proactive]"]
    N136["dispatcher.py [meridian_backend/src/core/proactive]"]
    N137["ergonomics.py [meridian_backend/src/core/proactive]"]
    N138["guard.py [meridian_backend/src/core/proactive]"]
    N139["__init__.py [meridian_backend/src/core/proactive]"]
    N140["auto_reviewer.py [meridian_backend/src/tools]"]
    N141["bill_radar.py [meridian_backend/src/tools]"]
    N142["bookmark_manager.py [meridian_backend/src/tools]"]
    N143["browser_agent.py [meridian_backend/src/tools]"]
    N144["browser_use_agent.py [meridian_backend/src/tools]"]
    N145["cam_guard.py [meridian_backend/src/tools]"]
    N146["chrome_manager.py [meridian_backend/src/tools]"]
    N147["clipboard.py [meridian_backend/src/tools]"]
    N148["communication.py [meridian_backend/src/tools]"]
    N149["db_query.py [meridian_backend/src/tools]"]
    N150["desktop.py [meridian_backend/src/tools]"]
    N151["detonation_sandbox.py [meridian_backend/src/tools]"]
    N152["developer.py [meridian_backend/src/tools]"]
    N153["dns_shield.py [meridian_backend/src/tools]"]
    N154["documents.py [meridian_backend/src/tools]"]
    N155["documents_office.py [meridian_backend/src/tools]"]
    N156["documents_slides.py [meridian_backend/src/tools]"]
    N157["dynamic_manager.py [meridian_backend/src/tools]"]
    N158["expiry_sentinel.py [meridian_backend/src/tools]"]
    N159["exporter.py [meridian_backend/src/tools]"]
    N160["external_connectors.py [meridian_backend/src/tools]"]
    N161["filesystem.py [meridian_backend/src/tools]"]
    N162["file_janitor.py [meridian_backend/src/tools]"]
    N163["finance_sentinel.py [meridian_backend/src/tools]"]
    N164["geo_location.py [meridian_backend/src/tools]"]
    N165["health_ingest.py [meridian_backend/src/tools]"]
    N166["household.py [meridian_backend/src/tools]"]
    N167["knowledge.py [meridian_backend/src/tools]"]
    N168["learning_queue.py [meridian_backend/src/tools]"]
    N169["mcp_marketplace.py [meridian_backend/src/tools]"]
    N170["network_guardian.py [meridian_backend/src/tools]"]
    N171["networth_tracker.py [meridian_backend/src/tools]"]
    N172["ollama_manager.py [meridian_backend/src/tools]"]
    N173["papercoder.py [meridian_backend/src/tools]"]
    N174["password_auditor.py [meridian_backend/src/tools]"]
    N175["phishing_guard.py [meridian_backend/src/tools]"]
    N176["phone_agent.py [meridian_backend/src/tools]"]
    N177["price_watcher.py [meridian_backend/src/tools]"]
    N178["recording.py [meridian_backend/src/tools]"]
    N179["registry.py [meridian_backend/src/tools]"]
    N180["review.py [meridian_backend/src/tools]"]
    N181["scheduler.py [meridian_backend/src/tools]"]
    N182["screenshot_memory.py [meridian_backend/src/tools]"]
    N183["search_hub.py [meridian_backend/src/tools]"]
    N184["security_auditor.py [meridian_backend/src/tools]"]
    N185["shell.py [meridian_backend/src/tools]"]
    N186["system.py [meridian_backend/src/tools]"]
    N187["system_windows.py [meridian_backend/src/tools]"]
    N188["task_scheduler.py [meridian_backend/src/tools]"]
    N189["totp_generator.py [meridian_backend/src/tools]"]
    N190["travel_butler.py [meridian_backend/src/tools]"]
    N191["usb_watchdog.py [meridian_backend/src/tools]"]
    N192["vault.py [meridian_backend/src/tools]"]
    N193["video_editor.py [meridian_backend/src/tools]"]
    N194["voice.py [meridian_backend/src/tools]"]
    N195["watcher.py [meridian_backend/src/tools]"]
    N196["web.py [meridian_backend/src/tools]"]
    N197["web_browser.py [meridian_backend/src/tools]"]
    N198["web_scraper.py [meridian_backend/src/tools]"]
    N199["wellness.py [meridian_backend/src/tools]"]
    N200["whatsapp_manager.py [meridian_backend/src/tools]"]
    N201["wifi_assessor.py [meridian_backend/src/tools]"]
    N202["workspace_layout.py [meridian_backend/src/tools]"]
    N203["ambient_listener.py [meridian_backend/src/voice]"]
    N204["duplex.py [meridian_backend/src/voice]"]
    N205["polyglot.py [meridian_backend/src/voice]"]
    N206["stt.py [meridian_backend/src/voice]"]
    N207["tts.py [meridian_backend/src/voice]"]
    N208["vad.py [meridian_backend/src/voice]"]
    N209["voice_biometrics.py [meridian_backend/src/voice]"]
    N210["wakeword.py [meridian_backend/src/voice]"]
    N211["conftest.py [meridian_backend/tests]"]
    N212["run_tests.py [meridian_backend/tests]"]
    N213["test_advanced_proactive.py [meridian_backend/tests]"]
    N214["test_atomic_storage.py [meridian_backend/tests]"]
    N215["test_audit_remediation.py [meridian_backend/tests]"]
    N216["test_auto_bug_fixer.py [meridian_backend/tests]"]
    N217["test_backend_improvements.py [meridian_backend/tests]"]
    N218["test_backlog_features.py [meridian_backend/tests]"]
    N219["test_backlog_sprint.py [meridian_backend/tests]"]
    N220["test_bridges.py [meridian_backend/tests]"]
    N221["test_browser_agent.py [meridian_backend/tests]"]
    N222["test_browser_fallback.py [meridian_backend/tests]"]
    N223["test_browser_use.py [meridian_backend/tests]"]
    N224["test_butler_media.py [meridian_backend/tests]"]
    N225["test_chat_abort.py [meridian_backend/tests]"]
    N226["test_cognitive_graph.py [meridian_backend/tests]"]
    N227["test_config.py [meridian_backend/tests]"]
    N228["test_consensus_gate.py [meridian_backend/tests]"]
    N229["test_context_budget.py [meridian_backend/tests]"]
    N230["test_custom_password_auth.py [meridian_backend/tests]"]
    N231["test_database.py [meridian_backend/tests]"]
    N232["test_day10_features.py [meridian_backend/tests]"]
    N233["test_day11_features.py [meridian_backend/tests]"]
    N234["test_day12_features.py [meridian_backend/tests]"]
    N235["test_day13_features.py [meridian_backend/tests]"]
    N236["test_day14_day15_features.py [meridian_backend/tests]"]
    N237["test_day16_17_18_features.py [meridian_backend/tests]"]
    N238["test_day3_features.py [meridian_backend/tests]"]
    N239["test_day4_features.py [meridian_backend/tests]"]
    N240["test_day5_features.py [meridian_backend/tests]"]
    N241["test_day6_features.py [meridian_backend/tests]"]
    N242["test_day7_features.py [meridian_backend/tests]"]
    N243["test_day8_features.py [meridian_backend/tests]"]
    N244["test_day9_features.py [meridian_backend/tests]"]
    N245["test_dev_intelligence_suite.py [meridian_backend/tests]"]
    N246["test_document_tools.py [meridian_backend/tests]"]
    N247["test_full_proactive_suite.py [meridian_backend/tests]"]
    N248["test_geo_location.py [meridian_backend/tests]"]
    N249["test_jarvis_perception.py [meridian_backend/tests]"]
    N250["test_known_errors_remediation.py [meridian_backend/tests]"]
    N251["test_llm_provider.py [meridian_backend/tests]"]
    N252["test_logging.py [meridian_backend/tests]"]
    N253["test_loop_parser.py [meridian_backend/tests]"]
    N254["test_loop_submodules.py [meridian_backend/tests]"]
    N255["test_mobile_websocket.py [meridian_backend/tests]"]
    N256["test_model_source.py [meridian_backend/tests]"]
    N257["test_multi_os.py [meridian_backend/tests]"]
    N258["test_new_features.py [meridian_backend/tests]"]
    N259["test_oauth.py [meridian_backend/tests]"]
    N260["test_p2p.py [meridian_backend/tests]"]
    N261["test_proactive.py [meridian_backend/tests]"]
    N262["test_proactive_mode.py [meridian_backend/tests]"]
    N263["test_proactive_notifications.py [meridian_backend/tests]"]
    N264["test_research_optimization.py [meridian_backend/tests]"]
    N265["test_response_resilience.py [meridian_backend/tests]"]
    N266["test_security_features.py [meridian_backend/tests]"]
    N267["test_silero_vad.py [meridian_backend/tests]"]
    N268["test_skill_packs.py [meridian_backend/tests]"]
    N269["test_sprint24_hardening.py [meridian_backend/tests]"]
    N270["test_sprint25_hardening.py [meridian_backend/tests]"]
    N271["test_sprint27_hardening.py [meridian_backend/tests]"]
    N272["test_sprint28_hardening.py [meridian_backend/tests]"]
    N273["test_sprint2_features.py [meridian_backend/tests]"]
    N274["test_standalone_bridge.py [meridian_backend/tests]"]
    N275["test_stream_resiliency.py [meridian_backend/tests]"]
    N276["test_swarm.py [meridian_backend/tests]"]
    N277["test_tools.py [meridian_backend/tests]"]
    N278["test_tool_modernization.py [meridian_backend/tests]"]
    N279["test_tool_regression.py [meridian_backend/tests]"]
    N280["test_vault.py [meridian_backend/tests]"]
    N281["test_video_editor.py [meridian_backend/tests]"]
    N282["test_voice_speed.py [meridian_backend/tests]"]
    N283["test_wakeword_continuous.py [meridian_backend/tests]"]
    N284["test_wakeword_onnx.py [meridian_backend/tests]"]
    N285["test_web_guards.py [meridian_backend/tests]"]
    N286["test_workflow.py [meridian_backend/tests]"]
    N287["vite.config.ts [meridian_frontend]"]
    N288["AppContext.tsx [meridian_frontend/src]"]
    N289["main.tsx [meridian_frontend/src]"]
    N290["Mascot.tsx [meridian_frontend/src]"]
    N291["Mascot3DCharacter.tsx [meridian_frontend/src]"]
    N292["MobileApp.tsx [meridian_frontend/src]"]
    N293["AgentStatusStream.tsx [meridian_frontend/src/components]"]
    N294["CommandPalette.tsx [meridian_frontend/src/components]"]
    N295["DevAutomationPanel.tsx [meridian_frontend/src/components]"]
    N296["DeveloperSuitePanel.tsx [meridian_frontend/src/components]"]
    N297["LocalModelManager.tsx [meridian_frontend/src/components]"]
    N298["MemoryConsolidationView.tsx [meridian_frontend/src/components]"]
    N299["NavRail.tsx [meridian_frontend/src/components]"]
    N300["PerceptionHUD.tsx [meridian_frontend/src/components]"]
    N301["ProactiveGuardBanner.tsx [meridian_frontend/src/components]"]
    N302["ProfileHeader.tsx [meridian_frontend/src/components]"]
    N303["RightDrawer.tsx [meridian_frontend/src/components]"]
    N304["ServerConnectionModal.tsx [meridian_frontend/src/components]"]
    N305["Shell.tsx [meridian_frontend/src/components]"]
    N306["StatusBar.tsx [meridian_frontend/src/components]"]
    N307["DropdownNav.tsx [meridian_frontend/src/components/mobile]"]
    N308["LiveThoughtCarousel.tsx [meridian_frontend/src/components/mobile]"]
    N309["VoiceOrbHUD.tsx [meridian_frontend/src/components/mobile]"]
    N310["AmbientParticles.tsx [meridian_frontend/src/components/ui]"]
    N311["DataBadge.tsx [meridian_frontend/src/components/ui]"]
    N312["GlowCard.tsx [meridian_frontend/src/components/ui]"]
    N313["HoloButton.tsx [meridian_frontend/src/components/ui]"]
    N314["ProgressArc.tsx [meridian_frontend/src/components/ui]"]
    N315["TerminalLine.tsx [meridian_frontend/src/components/ui]"]
    N316["ToastContext.tsx [meridian_frontend/src/components/ui]"]
    N317["useMemoryOptimizer.ts [meridian_frontend/src/hooks]"]
    N318["oauthService.ts [meridian_frontend/src/services]"]
    N319["streamingAudioPlayer.ts [meridian_frontend/src/services]"]
    N320["BackendSetup.tsx [meridian_frontend/src/startup]"]
    N321["BootSequence.tsx [meridian_frontend/src/startup]"]
    N322["OnboardingWizard.tsx [meridian_frontend/src/startup]"]
    N323["SetupWizard.tsx [meridian_frontend/src/startup]"]
    N324["Clipboard.tsx [meridian_frontend/src/views]"]
    N325["Jobs.tsx [meridian_frontend/src/views]"]
    N326["MemoryEditor.tsx [meridian_frontend/src/views]"]
    N327["Productivity.tsx [meridian_frontend/src/views]"]
    N328["Settings.tsx [meridian_frontend/src/views]"]
    N329["SwarmDebate.tsx [meridian_frontend/src/views]"]
    N330["Timeline.tsx [meridian_frontend/src/views]"]
    N331["WorkflowBuilder.tsx [meridian_frontend/src/views]"]
    N332["AiModelsTab.tsx [meridian_frontend/src/views/settings]"]
    N333["IntegrationsTab.tsx [meridian_frontend/src/views/settings]"]
    N334["MascotTab.tsx [meridian_frontend/src/views/settings]"]
    N335["PasswordInput.tsx [meridian_frontend/src/views/settings]"]
    N336["SpendAirGapTab.tsx [meridian_frontend/src/views/settings]"]
    N337["SystemGuardTab.tsx [meridian_frontend/src/views/settings]"]
    N338["VoiceTab.tsx [meridian_frontend/src/views/settings]"]
    N339["config.py [meridian_frontend/src-tauri/api/_internal/cv2]"]
    N340["load_config_py3.py [meridian_frontend/src-tauri/api/_internal/cv2]"]
    N341["__init__.py [meridian_frontend/src-tauri/api/_internal/cv2]"]
    N342["__init__.py [meridian_frontend/src-tauri/api/_internal/cv2/data]"]
    N343["__init__.py [meridian_frontend/src-tauri/api/_internal/cv2/mat_wrapper]"]
    N344["version.py [meridian_frontend/src-tauri/api/_internal/cv2/misc]"]
    N345["__init__.py [meridian_frontend/src-tauri/api/_internal/cv2/typing]"]
    N346["__init__.py [meridian_frontend/src-tauri/api/_internal/cv2/utils]"]
    N347["applications.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N348["background.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N349["cli.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N350["concurrency.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N351["datastructures.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N352["encoders.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N353["exceptions.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N354["exception_handlers.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N355["logger.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N356["params.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N357["param_functions.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N358["requests.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N359["responses.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N360["routing.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N361["sse.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N362["staticfiles.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N363["templating.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N364["testclient.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N365["types.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N366["utils.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N367["websockets.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N368["__init__.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N369["__main__.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N370["models.py [meridian_frontend/src-tauri/api/_internal/fastapi/dependencies]"]
    N371["utils.py [meridian_frontend/src-tauri/api/_internal/fastapi/dependencies]"]
    N372["asyncexitstack.py [meridian_frontend/src-tauri/api/_internal/fastapi/middleware]"]
    N373["cors.py [meridian_frontend/src-tauri/api/_internal/fastapi/middleware]"]
    N374["gzip.py [meridian_frontend/src-tauri/api/_internal/fastapi/middleware]"]
    N375["httpsredirect.py [meridian_frontend/src-tauri/api/_internal/fastapi/middleware]"]
    N376["trustedhost.py [meridian_frontend/src-tauri/api/_internal/fastapi/middleware]"]
    N377["wsgi.py [meridian_frontend/src-tauri/api/_internal/fastapi/middleware]"]
    N378["__init__.py [meridian_frontend/src-tauri/api/_internal/fastapi/middleware]"]
    N379["docs.py [meridian_frontend/src-tauri/api/_internal/fastapi/openapi]"]
    N380["models.py [meridian_frontend/src-tauri/api/_internal/fastapi/openapi]"]
    N381["utils.py [meridian_frontend/src-tauri/api/_internal/fastapi/openapi]"]
    N382["api_key.py [meridian_frontend/src-tauri/api/_internal/fastapi/security]"]
    N383["base.py [meridian_frontend/src-tauri/api/_internal/fastapi/security]"]
    N384["http.py [meridian_frontend/src-tauri/api/_internal/fastapi/security]"]
    N385["oauth2.py [meridian_frontend/src-tauri/api/_internal/fastapi/security]"]
    N386["open_id_connect_url.py [meridian_frontend/src-tauri/api/_internal/fastapi/security]"]
    N387["shared.py [meridian_frontend/src-tauri/api/_internal/fastapi/_compat]"]
    N388["v2.py [meridian_frontend/src-tauri/api/_internal/fastapi/_compat]"]
    N389["coreBundle.js [meridian_frontend/src-tauri/api/_internal/playwright/driver/package/lib]"]
    N390["utilsBundle.js [meridian_frontend/src-tauri/api/_internal/playwright/driver/package/lib]"]
    N391["structs.d.ts [meridian_frontend/src-tauri/api/_internal/playwright/driver/package/types]"]
    N392["types.d.ts [meridian_frontend/src-tauri/api/_internal/playwright/driver/package/types]"]
    N393["aliases.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N394["alias_generators.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N395["annotated_handlers.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N396["color.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N397["config.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N398["dataclasses.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N399["errors.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N400["fields.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N401["functional_serializers.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N402["functional_validators.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N403["json_schema.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N404["main.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N405["mypy.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N406["networks.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N407["root_model.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N408["types.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N409["type_adapter.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N410["validate_call_decorator.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N411["version.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N412["warnings.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N413["_migration.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N414["__init__.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N415["class_validators.py [meridian_frontend/src-tauri/api/_internal/pydantic/deprecated]"]
    N416["config.py [meridian_frontend/src-tauri/api/_internal/pydantic/deprecated]"]
    N417["copy_internals.py [meridian_frontend/src-tauri/api/_internal/pydantic/deprecated]"]
    N418["decorator.py [meridian_frontend/src-tauri/api/_internal/pydantic/deprecated]"]
    N419["json.py [meridian_frontend/src-tauri/api/_internal/pydantic/deprecated]"]
    N420["parse.py [meridian_frontend/src-tauri/api/_internal/pydantic/deprecated]"]
    N421["tools.py [meridian_frontend/src-tauri/api/_internal/pydantic/deprecated]"]
    N422["arguments_schema.py [meridian_frontend/src-tauri/api/_internal/pydantic/experimental]"]
    N423["missing_sentinel.py [meridian_frontend/src-tauri/api/_internal/pydantic/experimental]"]
    N424["pipeline.py [meridian_frontend/src-tauri/api/_internal/pydantic/experimental]"]
    N425["_loader.py [meridian_frontend/src-tauri/api/_internal/pydantic/plugin]"]
    N426["_schema_validator.py [meridian_frontend/src-tauri/api/_internal/pydantic/plugin]"]
    N427["__init__.py [meridian_frontend/src-tauri/api/_internal/pydantic/plugin]"]
    N428["annotated_types.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N429["class_validators.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N430["color.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N431["config.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N432["dataclasses.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N433["datetime_parse.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N434["decorator.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N435["env_settings.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N436["errors.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N437["error_wrappers.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N438["fields.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N439["generics.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N440["json.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N441["main.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N442["mypy.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N443["networks.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N444["parse.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N445["schema.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N446["tools.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N447["types.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N448["typing.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N449["utils.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N450["validators.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N451["version.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N452["_hypothesis_plugin.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N453["__init__.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N454["_config.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N455["_core_metadata.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N456["_core_utils.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N457["_dataclasses.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N458["_decorators.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N459["_decorators_v1.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N460["_discriminated_union.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N461["_docs_extraction.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N462["_fields.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N463["_forward_ref.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N464["_generate_schema.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N465["_generics.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N466["_git.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N467["_import_utils.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N468["_internal_dataclass.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N469["_known_annotated_metadata.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N470["_mock_val_ser.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N471["_model_construction.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N472["_namespace_utils.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N473["_repr.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N474["_schema_gather.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N475["_schema_generation_shared.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N476["_serializers.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N477["_signature.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N478["_typing_extra.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N479["_utils.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N480["_validate_call.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N481["_validators.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N482["applications.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N483["authentication.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N484["background.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N485["concurrency.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N486["config.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N487["convertors.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N488["datastructures.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N489["endpoints.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N490["exceptions.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N491["formparsers.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N492["requests.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N493["responses.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N494["routing.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N495["schemas.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N496["staticfiles.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N497["status.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N498["templating.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N499["testclient.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N500["types.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N501["websockets.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N502["_exception_handler.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N503["_utils.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N504["authentication.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N505["base.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N506["cors.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N507["errors.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N508["exceptions.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N509["gzip.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N510["httpsredirect.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N511["sessions.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N512["trustedhost.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N513["wsgi.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N514["__init__.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N515["config.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N516["importer.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N517["logging.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N518["main.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N519["server.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N520["workers.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N521["_compat.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N522["_subprocess.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N523["_types.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N524["__init__.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N525["__main__.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N526["off.py [meridian_frontend/src-tauri/api/_internal/uvicorn/lifespan]"]
    N527["on.py [meridian_frontend/src-tauri/api/_internal/uvicorn/lifespan]"]
    N528["asyncio.py [meridian_frontend/src-tauri/api/_internal/uvicorn/loops]"]
    N529["auto.py [meridian_frontend/src-tauri/api/_internal/uvicorn/loops]"]
    N530["uvloop.py [meridian_frontend/src-tauri/api/_internal/uvicorn/loops]"]
    N531["asgi2.py [meridian_frontend/src-tauri/api/_internal/uvicorn/middleware]"]
    N532["message_logger.py [meridian_frontend/src-tauri/api/_internal/uvicorn/middleware]"]
    N533["proxy_headers.py [meridian_frontend/src-tauri/api/_internal/uvicorn/middleware]"]
    N534["wsgi.py [meridian_frontend/src-tauri/api/_internal/uvicorn/middleware]"]
    N535["utils.py [meridian_frontend/src-tauri/api/_internal/uvicorn/protocols]"]
    N536["auto.py [meridian_frontend/src-tauri/api/_internal/uvicorn/protocols/http]"]
    N537["flow_control.py [meridian_frontend/src-tauri/api/_internal/uvicorn/protocols/http]"]
    N538["h11_impl.py [meridian_frontend/src-tauri/api/_internal/uvicorn/protocols/http]"]
    N539["httptools_impl.py [meridian_frontend/src-tauri/api/_internal/uvicorn/protocols/http]"]
    N540["auto.py [meridian_frontend/src-tauri/api/_internal/uvicorn/protocols/websockets]"]
    N541["websockets_impl.py [meridian_frontend/src-tauri/api/_internal/uvicorn/protocols/websockets]"]
    N542["websockets_sansio_impl.py [meridian_frontend/src-tauri/api/_internal/uvicorn/protocols/websockets]"]
    N543["wsproto_impl.py [meridian_frontend/src-tauri/api/_internal/uvicorn/protocols/websockets]"]
    N544["basereload.py [meridian_frontend/src-tauri/api/_internal/uvicorn/supervisors]"]
    N545["multiprocess.py [meridian_frontend/src-tauri/api/_internal/uvicorn/supervisors]"]
    N546["statreload.py [meridian_frontend/src-tauri/api/_internal/uvicorn/supervisors]"]
    N547["watchfilesreload.py [meridian_frontend/src-tauri/api/_internal/uvicorn/supervisors]"]
    N548["__init__.py [meridian_frontend/src-tauri/api/_internal/uvicorn/supervisors]"]
    N549["auth.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N550["cli.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N551["client.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N552["connection.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N553["datastructures.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N554["exceptions.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N555["frames.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N556["headers.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N557["http11.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N558["imports.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N559["protocol.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N560["proxy.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N561["server.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N562["streams.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N563["typing.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N564["uri.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N565["utils.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N566["version.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N567["__init__.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N568["client.py [meridian_frontend/src-tauri/api/_internal/websockets/asyncio]"]
    N569["connection.py [meridian_frontend/src-tauri/api/_internal/websockets/asyncio]"]
    N570["messages.py [meridian_frontend/src-tauri/api/_internal/websockets/asyncio]"]
    N571["router.py [meridian_frontend/src-tauri/api/_internal/websockets/asyncio]"]
    N572["server.py [meridian_frontend/src-tauri/api/_internal/websockets/asyncio]"]
    N573["base.py [meridian_frontend/src-tauri/api/_internal/websockets/extensions]"]
    N574["permessage_deflate.py [meridian_frontend/src-tauri/api/_internal/websockets/extensions]"]
    N575["auth.py [meridian_frontend/src-tauri/api/_internal/websockets/legacy]"]
    N576["client.py [meridian_frontend/src-tauri/api/_internal/websockets/legacy]"]
    N577["exceptions.py [meridian_frontend/src-tauri/api/_internal/websockets/legacy]"]
    N578["framing.py [meridian_frontend/src-tauri/api/_internal/websockets/legacy]"]
    N579["handshake.py [meridian_frontend/src-tauri/api/_internal/websockets/legacy]"]
    N580["http.py [meridian_frontend/src-tauri/api/_internal/websockets/legacy]"]
    N581["protocol.py [meridian_frontend/src-tauri/api/_internal/websockets/legacy]"]
    N582["server.py [meridian_frontend/src-tauri/api/_internal/websockets/legacy]"]
    N583["__init__.py [meridian_frontend/src-tauri/api/_internal/websockets/legacy]"]
    N584["client.py [meridian_frontend/src-tauri/api/_internal/websockets/sync]"]
    N585["connection.py [meridian_frontend/src-tauri/api/_internal/websockets/sync]"]
    N586["messages.py [meridian_frontend/src-tauri/api/_internal/websockets/sync]"]
    N587["router.py [meridian_frontend/src-tauri/api/_internal/websockets/sync]"]
    N588["server.py [meridian_frontend/src-tauri/api/_internal/websockets/sync]"]
    N589["utils.py [meridian_frontend/src-tauri/api/_internal/websockets/sync]"]
    N590["client.py [meridian_frontend/src-tauri/api/_internal/websockets/trio]"]
    N591["connection.py [meridian_frontend/src-tauri/api/_internal/websockets/trio]"]
    N592["messages.py [meridian_frontend/src-tauri/api/_internal/websockets/trio]"]
    N593["router.py [meridian_frontend/src-tauri/api/_internal/websockets/trio]"]
    N594["server.py [meridian_frontend/src-tauri/api/_internal/websockets/trio]"]
    N595["utils.py [meridian_frontend/src-tauri/api/_internal/websockets/trio]"]
    N596["build_apk.py [meridian_mobile]"]
    N597["flutter_lldb_helper.py [meridian_mobile/ios/Flutter/ephemeral]"]
    N598["get_system_platform_info.py [plugins]"]

    N1 --> N419
    N1 --> N440
    N1 --> N448
    N1 --> N563
    N2 --> N419
    N2 --> N440
    N2 --> N448
    N2 --> N563
    N3 --> N419
    N3 --> N440
    N4 --> N528
    N4 --> N419
    N4 --> N440
    N4 --> N13
    N8 --> N419
    N8 --> N440
    N8 --> N448
    N8 --> N563
    N9 --> N398
    N9 --> N432
    N12 --> N9
    N12 --> N49
    N12 --> N339
    N12 --> N397
    N12 --> N416
    N12 --> N431
    N12 --> N486
    N12 --> N515
    N12 --> N11
    N12 --> N10
    N13 --> N419
    N13 --> N440
    N13 --> N517
    N13 --> N528
    N13 --> N448
    N13 --> N563
    N13 --> N14
    N14 --> N419
    N14 --> N440
    N14 --> N448
    N14 --> N563
    N15 --> N419
    N15 --> N440
    N15 --> N528
    N15 --> N517
    N15 --> N448
    N15 --> N563
    N18 --> N419
    N18 --> N440
    N18 --> N448
    N18 --> N563
    N18 --> N14
    N19 --> N419
    N19 --> N440
    N19 --> N528
    N19 --> N448
    N19 --> N563
    N19 --> N14
    N20 --> N419
    N20 --> N440
    N20 --> N517
    N20 --> N448
    N20 --> N563
    N20 --> N14
    N21 --> N419
    N21 --> N440
    N21 --> N448
    N21 --> N563
    N22 --> N419
    N22 --> N440
    N22 --> N448
    N22 --> N563
    N22 --> N14
    N23 --> N448
    N23 --> N563
    N24 --> N448
    N24 --> N563
    N24 --> N14
    N25 --> N448
    N25 --> N563
    N25 --> N14
    N26 --> N419
    N26 --> N440
    N26 --> N448
    N26 --> N563
    N26 --> N14
    N27 --> N419
    N27 --> N440
    N27 --> N517
    N27 --> N528
    N27 --> N448
    N27 --> N563
    N27 --> N14
    N28 --> N419
    N28 --> N440
    N28 --> N448
    N28 --> N563
    N28 --> N14
    N28 --> N528
    N29 --> N448
    N29 --> N563
    N30 --> N517
    N30 --> N448
    N30 --> N563
    N31 --> N419
    N31 --> N440
    N31 --> N448
    N31 --> N563
    N31 --> N14
    N33 --> N419
    N33 --> N440
    N33 --> N517
    N33 --> N448
    N33 --> N563
    N33 --> N14
    N34 --> N528
    N34 --> N517
    N34 --> N448
    N34 --> N563
    N35 --> N517
    N35 --> N448
    N35 --> N563
    N36 --> N419
    N36 --> N440
    N36 --> N517
    N36 --> N448
    N36 --> N563
    N37 --> N419
    N37 --> N440
    N37 --> N517
    N38 --> N448
    N38 --> N563
    N38 --> N419
    N38 --> N440
    N39 --> N517
    N39 --> N448
    N39 --> N563
    N40 --> N517
    N40 --> N448
    N40 --> N563
    N41 --> N517
    N41 --> N448
    N41 --> N563
    N41 --> N419
    N41 --> N440
    N42 --> N528
    N42 --> N448
    N42 --> N563
    N43 --> N517
    N43 --> N448
    N43 --> N563
    N44 --> N528
    N44 --> N448
    N44 --> N563
    N45 --> N448
    N45 --> N563
    N45 --> N14
    N46 --> N448
    N46 --> N563
    N47 --> N419
    N47 --> N440
    N47 --> N517
    N47 --> N448
    N47 --> N563
    N48 --> N517
    N48 --> N448
    N48 --> N563
    N50 --> N528
    N50 --> N448
    N50 --> N563
    N50 --> N14
    N51 --> N419
    N51 --> N440
    N51 --> N517
    N51 --> N448
    N51 --> N563
    N51 --> N528
    N51 --> N14
    N52 --> N517
    N52 --> N448
    N52 --> N563
    N53 --> N528
    N53 --> N517
    N53 --> N448
    N53 --> N563
    N54 --> N528
    N54 --> N448
    N54 --> N563
    N54 --> N14
    N55 --> N448
    N55 --> N563
    N57 --> N419
    N57 --> N440
    N57 --> N517
    N57 --> N448
    N57 --> N563
    N57 --> N14
    N58 --> N517
    N58 --> N448
    N58 --> N563
    N59 --> N517
    N59 --> N448
    N59 --> N563
    N60 --> N517
    N60 --> N448
    N60 --> N563
    N61 --> N517
    N61 --> N448
    N61 --> N563
    N62 --> N448
    N62 --> N563
    N62 --> N14
    N63 --> N517
    N63 --> N448
    N63 --> N563
    N64 --> N517
    N64 --> N448
    N64 --> N563
    N65 --> N448
    N65 --> N563
    N66 --> N419
    N66 --> N440
    N66 --> N448
    N66 --> N563
    N67 --> N419
    N67 --> N440
    N67 --> N448
    N67 --> N563
    N68 --> N517
    N68 --> N448
    N68 --> N563
    N68 --> N412
    N68 --> N419
    N68 --> N440
    N70 --> N517
    N70 --> N448
    N70 --> N563
    N70 --> N14
    N71 --> N528
    N71 --> N517
    N71 --> N448
    N71 --> N563
    N71 --> N14
    N72 --> N448
    N72 --> N563
    N72 --> N14
    N73 --> N419
    N73 --> N440
    N73 --> N517
    N73 --> N528
    N73 --> N448
    N73 --> N563
    N73 --> N14
    N74 --> N517
    N74 --> N528
    N74 --> N448
    N74 --> N563
    N74 --> N14
    N74 --> N419
    N74 --> N440
    N75 --> N419
    N75 --> N440
    N75 --> N517
    N75 --> N448
    N75 --> N563
    N76 --> N517
    N76 --> N419
    N76 --> N440
    N77 --> N419
    N77 --> N440
    N77 --> N528
    N77 --> N448
    N77 --> N563
    N77 --> N14
    N78 --> N419
    N78 --> N440
    N78 --> N528
    N78 --> N448
    N78 --> N563
    N78 --> N14
    N79 --> N419
    N79 --> N440
    N79 --> N448
    N79 --> N563
    N79 --> N14
    N80 --> N419
    N80 --> N440
    N80 --> N528
    N80 --> N448
    N80 --> N563
    N80 --> N14
    N81 --> N419
    N81 --> N440
    N81 --> N528
    N81 --> N448
    N81 --> N563
    N81 --> N14
    N82 --> N419
    N82 --> N440
    N82 --> N528
    N82 --> N448
    N82 --> N563
    N82 --> N14
    N83 --> N419
    N83 --> N440
    N83 --> N528
    N83 --> N448
    N83 --> N563
    N84 --> N517
    N84 --> N448
    N84 --> N563
    N85 --> N419
    N85 --> N440
    N85 --> N528
    N85 --> N517
    N85 --> N448
    N85 --> N563
    N86 --> N528
    N86 --> N419
    N86 --> N440
    N86 --> N517
    N86 --> N448
    N86 --> N563
    N87 --> N419
    N87 --> N440
    N87 --> N448
    N87 --> N563
    N88 --> N517
    N88 --> N528
    N88 --> N419
    N88 --> N440
    N88 --> N448
    N88 --> N563
    N88 --> N14
    N89 --> N419
    N89 --> N440
    N89 --> N448
    N89 --> N563
    N89 --> N14
    N90 --> N419
    N90 --> N440
    N90 --> N517
    N90 --> N448
    N90 --> N563
    N90 --> N14
    N90 --> N528
    N91 --> N448
    N91 --> N563
    N91 --> N14
    N91 --> N419
    N91 --> N440
    N92 --> N448
    N92 --> N563
    N93 --> N419
    N93 --> N440
    N93 --> N448
    N93 --> N563
    N94 --> N517
    N94 --> N528
    N94 --> N448
    N94 --> N563
    N94 --> N419
    N94 --> N440
    N95 --> N419
    N95 --> N440
    N95 --> N448
    N95 --> N563
    N95 --> N14
    N97 --> N448
    N97 --> N563
    N98 --> N448
    N98 --> N563
    N99 --> N517
    N99 --> N448
    N99 --> N563
    N100 --> N517
    N100 --> N448
    N100 --> N563
    N101 --> N517
    N101 --> N448
    N101 --> N563
    N101 --> N14
    N102 --> N448
    N102 --> N563
    N103 --> N517
    N103 --> N448
    N103 --> N563
    N104 --> N517
    N104 --> N448
    N104 --> N563
    N105 --> N517
    N105 --> N448
    N105 --> N563
    N106 --> N517
    N106 --> N448
    N106 --> N563
    N107 --> N517
    N107 --> N448
    N107 --> N563
    N108 --> N419
    N108 --> N440
    N108 --> N448
    N108 --> N563
    N109 --> N448
    N109 --> N563
    N110 --> N448
    N110 --> N563
    N111 --> N517
    N111 --> N448
    N111 --> N563
    N112 --> N528
    N112 --> N412
    N112 --> N14
    N112 --> N419
    N112 --> N440
    N113 --> N528
    N113 --> N517
    N113 --> N448
    N113 --> N563
    N114 --> N517
    N114 --> N448
    N114 --> N563
    N115 --> N517
    N115 --> N448
    N115 --> N563
    N116 --> N517
    N116 --> N448
    N116 --> N563
    N117 --> N517
    N117 --> N448
    N117 --> N563
    N118 --> N517
    N118 --> N448
    N118 --> N563
    N118 --> N14
    N119 --> N419
    N119 --> N440
    N119 --> N528
    N119 --> N448
    N119 --> N563
    N119 --> N14
    N120 --> N528
    N120 --> N419
    N120 --> N440
    N120 --> N448
    N120 --> N563
    N120 --> N14
    N121 --> N517
    N121 --> N448
    N121 --> N563
    N122 --> N448
    N122 --> N563
    N122 --> N528
    N122 --> N14
    N123 --> N448
    N123 --> N563
    N124 --> N517
    N124 --> N448
    N124 --> N563
    N125 --> N448
    N125 --> N563
    N126 --> N517
    N126 --> N448
    N126 --> N563
    N127 --> N419
    N127 --> N440
    N127 --> N448
    N127 --> N563
    N128 --> N517
    N128 --> N448
    N128 --> N563
    N128 --> N14
    N129 --> N517
    N129 --> N448
    N129 --> N563
    N130 --> N517
    N130 --> N448
    N130 --> N563
    N131 --> N517
    N131 --> N448
    N131 --> N563
    N132 --> N517
    N132 --> N448
    N132 --> N563
    N133 --> N419
    N133 --> N440
    N133 --> N448
    N133 --> N563
    N134 --> N517
    N134 --> N448
    N134 --> N563
    N135 --> N448
    N135 --> N563
    N135 --> N14
    N135 --> N13
    N136 --> N528
    N136 --> N448
    N136 --> N563
    N137 --> N448
    N137 --> N563
    N138 --> N517
    N138 --> N448
    N138 --> N563
    N138 --> N14
    N140 --> N448
    N140 --> N563
    N141 --> N419
    N141 --> N440
    N141 --> N448
    N141 --> N563
    N142 --> N517
    N142 --> N448
    N142 --> N563
    N143 --> N419
    N143 --> N440
    N143 --> N517
    N143 --> N448
    N143 --> N563
    N144 --> N419
    N144 --> N440
    N144 --> N448
    N144 --> N563
    N144 --> N528
    N144 --> N14
    N145 --> N448
    N145 --> N563
    N146 --> N448
    N146 --> N563
    N146 --> N14
    N147 --> N448
    N147 --> N563
    N147 --> N14
    N148 --> N517
    N148 --> N448
    N148 --> N563
    N148 --> N14
    N149 --> N448
    N149 --> N563
    N149 --> N14
    N150 --> N448
    N150 --> N563
    N150 --> N14
    N151 --> N448
    N151 --> N563
    N152 --> N528
    N152 --> N448
    N152 --> N563
    N153 --> N448
    N153 --> N563
    N154 --> N448
    N154 --> N563
    N155 --> N448
    N155 --> N563
    N156 --> N448
    N156 --> N563
    N157 --> N517
    N157 --> N448
    N157 --> N563
    N158 --> N419
    N158 --> N440
    N158 --> N448
    N158 --> N563
    N159 --> N419
    N159 --> N440
    N159 --> N448
    N159 --> N563
    N159 --> N14
    N160 --> N419
    N160 --> N440
    N160 --> N358
    N160 --> N492
    N160 --> N448
    N160 --> N563
    N161 --> N448
    N161 --> N563
    N162 --> N448
    N162 --> N563
    N163 --> N419
    N163 --> N440
    N163 --> N448
    N163 --> N563
    N164 --> N448
    N164 --> N563
    N165 --> N448
    N165 --> N563
    N166 --> N419
    N166 --> N440
    N166 --> N448
    N166 --> N563
    N167 --> N448
    N167 --> N563
    N167 --> N14
    N168 --> N517
    N168 --> N448
    N168 --> N563
    N169 --> N419
    N169 --> N440
    N169 --> N448
    N169 --> N563
    N170 --> N448
    N170 --> N563
    N171 --> N517
    N171 --> N448
    N171 --> N563
    N172 --> N14
    N173 --> N419
    N173 --> N440
    N173 --> N448
    N173 --> N563
    N173 --> N398
    N173 --> N432
    N173 --> N9
    N173 --> N49
    N173 --> N339
    N173 --> N397
    N173 --> N416
    N173 --> N431
    N173 --> N486
    N173 --> N515
    N173 --> N11
    N173 --> N10
    N174 --> N448
    N174 --> N563
    N175 --> N448
    N175 --> N563
    N176 --> N419
    N176 --> N440
    N176 --> N528
    N176 --> N517
    N176 --> N448
    N176 --> N563
    N176 --> N14
    N177 --> N517
    N177 --> N448
    N177 --> N563
    N178 --> N419
    N178 --> N440
    N178 --> N14
    N179 --> N528
    N179 --> N448
    N179 --> N563
    N179 --> N14
    N179 --> N419
    N179 --> N440
    N180 --> N448
    N180 --> N563
    N180 --> N14
    N182 --> N419
    N182 --> N440
    N182 --> N448
    N182 --> N563
    N183 --> N448
    N183 --> N563
    N183 --> N14
    N184 --> N448
    N184 --> N563
    N185 --> N448
    N185 --> N563
    N185 --> N14
    N186 --> N14
    N189 --> N448
    N189 --> N563
    N190 --> N419
    N190 --> N440
    N190 --> N448
    N190 --> N563
    N191 --> N448
    N191 --> N563
    N192 --> N448
    N192 --> N563
    N192 --> N419
    N192 --> N440
    N193 --> N517
    N193 --> N448
    N193 --> N563
    N195 --> N448
    N195 --> N563
    N196 --> N448
    N196 --> N563
    N196 --> N14
    N197 --> N419
    N197 --> N440
    N197 --> N448
    N197 --> N563
    N197 --> N14
    N198 --> N448
    N198 --> N563
    N198 --> N14
    N199 --> N448
    N199 --> N563
    N200 --> N419
    N200 --> N440
    N200 --> N517
    N200 --> N448
    N200 --> N563
    N200 --> N14
    N201 --> N517
    N201 --> N448
    N201 --> N563
    N202 --> N517
    N202 --> N448
    N202 --> N563
    N203 --> N528
    N203 --> N517
    N203 --> N448
    N203 --> N563
    N204 --> N448
    N204 --> N563
    N205 --> N517
    N205 --> N448
    N205 --> N563
    N206 --> N517
    N206 --> N14
    N207 --> N517
    N207 --> N448
    N207 --> N563
    N207 --> N14
    N208 --> N448
    N208 --> N563
    N209 --> N448
    N209 --> N563
    N210 --> N517
    N210 --> N14
    N214 --> N419
    N214 --> N440
    N216 --> N528
    N216 --> N13
    N218 --> N14
    N219 --> N13
    N224 --> N14
    N225 --> N13
    N229 --> N14
    N231 --> N14
    N232 --> N528
    N238 --> N14
    N239 --> N14
    N240 --> N13
    N242 --> N419
    N242 --> N440
    N242 --> N14
    N244 --> N419
    N244 --> N440
    N244 --> N14
    N244 --> N528
    N245 --> N528
    N245 --> N13
    N251 --> N528
    N252 --> N517
    N252 --> N419
    N252 --> N440
    N253 --> N419
    N253 --> N440
    N254 --> N528
    N255 --> N419
    N255 --> N440
    N255 --> N13
    N255 --> N528
    N256 --> N14
    N258 --> N528
    N258 --> N13
    N260 --> N14
    N261 --> N528
    N262 --> N419
    N262 --> N440
    N263 --> N528
    N263 --> N13
    N264 --> N419
    N264 --> N440
    N265 --> N419
    N265 --> N440
    N266 --> N13
    N266 --> N448
    N266 --> N563
    N266 --> N528
    N269 --> N13
    N270 --> N419
    N270 --> N440
    N271 --> N517
    N272 --> N14
    N273 --> N13
    N274 --> N419
    N274 --> N440
    N274 --> N15
    N275 --> N528
    N276 --> N528
    N277 --> N419
    N277 --> N440
    N278 --> N528
    N282 --> N13
    N283 --> N13
    N284 --> N13
    N288 --> N365
    N288 --> N392
    N288 --> N408
    N288 --> N447
    N288 --> N500
    N288 --> N9
    N288 --> N49
    N288 --> N339
    N288 --> N397
    N288 --> N416
    N288 --> N431
    N288 --> N486
    N288 --> N515
    N289 --> N551
    N289 --> N568
    N289 --> N576
    N289 --> N584
    N289 --> N590
    N289 --> N290
    N289 --> N321
    N289 --> N323
    N289 --> N305
    N289 --> N288
    N289 --> N9
    N289 --> N49
    N289 --> N339
    N289 --> N397
    N289 --> N416
    N289 --> N431
    N289 --> N486
    N289 --> N515
    N289 --> N322
    N289 --> N320
    N290 --> N291
    N290 --> N9
    N290 --> N49
    N290 --> N339
    N290 --> N397
    N290 --> N416
    N290 --> N431
    N290 --> N486
    N290 --> N515
    N290 --> N288
    N290 --> N319
    N292 --> N307
    N292 --> N309
    N292 --> N308
    N293 --> N9
    N293 --> N49
    N293 --> N339
    N293 --> N397
    N293 --> N416
    N293 --> N431
    N293 --> N486
    N293 --> N515
    N295 --> N9
    N295 --> N49
    N295 --> N339
    N295 --> N397
    N295 --> N416
    N295 --> N431
    N295 --> N486
    N295 --> N515
    N296 --> N9
    N296 --> N49
    N296 --> N339
    N296 --> N397
    N296 --> N416
    N296 --> N431
    N296 --> N486
    N296 --> N515
    N297 --> N316
    N297 --> N9
    N297 --> N49
    N297 --> N339
    N297 --> N397
    N297 --> N416
    N297 --> N431
    N297 --> N486
    N297 --> N515
    N298 --> N9
    N298 --> N49
    N298 --> N339
    N298 --> N397
    N298 --> N416
    N298 --> N431
    N298 --> N486
    N298 --> N515
    N299 --> N288
    N299 --> N290
    N301 --> N9
    N301 --> N49
    N301 --> N339
    N301 --> N397
    N301 --> N416
    N301 --> N431
    N301 --> N486
    N301 --> N515
    N303 --> N288
    N303 --> N314
    N303 --> N311
    N304 --> N9
    N304 --> N49
    N304 --> N339
    N304 --> N397
    N304 --> N416
    N304 --> N431
    N304 --> N486
    N304 --> N515
    N305 --> N288
    N305 --> N299
    N305 --> N306
    N305 --> N303
    N305 --> N294
    N305 --> N316
    N305 --> N330
    N305 --> N325
    N305 --> N324
    N305 --> N327
    N305 --> N310
    N305 --> N301
    N306 --> N288
    N306 --> N9
    N306 --> N49
    N306 --> N339
    N306 --> N397
    N306 --> N416
    N306 --> N431
    N306 --> N486
    N306 --> N515
    N306 --> N311
    N310 --> N317
    N318 --> N9
    N318 --> N49
    N318 --> N339
    N318 --> N397
    N318 --> N416
    N318 --> N431
    N318 --> N486
    N318 --> N515
    N319 --> N9
    N319 --> N49
    N319 --> N339
    N319 --> N397
    N319 --> N416
    N319 --> N431
    N319 --> N486
    N319 --> N515
    N320 --> N9
    N320 --> N49
    N320 --> N339
    N320 --> N397
    N320 --> N416
    N320 --> N431
    N320 --> N486
    N320 --> N515
    N321 --> N9
    N321 --> N49
    N321 --> N339
    N321 --> N397
    N321 --> N416
    N321 --> N431
    N321 --> N486
    N321 --> N515
    N321 --> N290
    N322 --> N9
    N322 --> N49
    N322 --> N339
    N322 --> N397
    N322 --> N416
    N322 --> N431
    N322 --> N486
    N322 --> N515
    N323 --> N313
    N323 --> N9
    N323 --> N49
    N323 --> N339
    N323 --> N397
    N323 --> N416
    N323 --> N431
    N323 --> N486
    N323 --> N515
    N324 --> N365
    N324 --> N392
    N324 --> N408
    N324 --> N447
    N324 --> N500
    N324 --> N288
    N324 --> N313
    N324 --> N9
    N324 --> N49
    N324 --> N339
    N324 --> N397
    N324 --> N416
    N324 --> N431
    N324 --> N486
    N324 --> N515
    N325 --> N365
    N325 --> N392
    N325 --> N408
    N325 --> N447
    N325 --> N500
    N325 --> N313
    N325 --> N312
    N325 --> N9
    N325 --> N49
    N325 --> N339
    N325 --> N397
    N325 --> N416
    N325 --> N431
    N325 --> N486
    N325 --> N515
    N326 --> N9
    N326 --> N49
    N326 --> N339
    N326 --> N397
    N326 --> N416
    N326 --> N431
    N326 --> N486
    N326 --> N515
    N327 --> N365
    N327 --> N392
    N327 --> N408
    N327 --> N447
    N327 --> N500
    N327 --> N314
    N327 --> N313
    N327 --> N312
    N327 --> N9
    N327 --> N49
    N327 --> N339
    N327 --> N397
    N327 --> N416
    N327 --> N431
    N327 --> N486
    N327 --> N515
    N327 --> N297
    N327 --> N298
    N327 --> N295
    N327 --> N293
    N327 --> N296
    N328 --> N9
    N328 --> N49
    N328 --> N339
    N328 --> N397
    N328 --> N416
    N328 --> N431
    N328 --> N486
    N328 --> N515
    N328 --> N365
    N328 --> N392
    N328 --> N408
    N328 --> N447
    N328 --> N500
    N328 --> N288
    N328 --> N317
    N328 --> N314
    N328 --> N313
    N328 --> N312
    N328 --> N334
    N328 --> N338
    N328 --> N333
    N328 --> N332
    N328 --> N337
    N328 --> N336
    N328 --> N335
    N329 --> N315
    N329 --> N313
    N329 --> N9
    N329 --> N49
    N329 --> N339
    N329 --> N397
    N329 --> N416
    N329 --> N431
    N329 --> N486
    N329 --> N515
    N330 --> N365
    N330 --> N392
    N330 --> N408
    N330 --> N447
    N330 --> N500
    N330 --> N313
    N330 --> N312
    N330 --> N9
    N330 --> N49
    N330 --> N339
    N330 --> N397
    N330 --> N416
    N330 --> N431
    N330 --> N486
    N330 --> N515
    N330 --> N319
    N331 --> N9
    N331 --> N49
    N331 --> N339
    N331 --> N397
    N331 --> N416
    N331 --> N431
    N331 --> N486
    N331 --> N515
    N332 --> N312
    N332 --> N313
    N332 --> N335
    N333 --> N312
    N333 --> N313
    N333 --> N335
    N333 --> N9
    N333 --> N49
    N333 --> N339
    N333 --> N397
    N333 --> N416
    N333 --> N431
    N333 --> N486
    N333 --> N515
    N334 --> N312
    N336 --> N312
    N336 --> N313
    N337 --> N312
    N337 --> N313
    N338 --> N312
    N338 --> N313
    N343 --> N448
    N343 --> N563
    N345 --> N448
    N345 --> N563
    N347 --> N448
    N347 --> N563
    N348 --> N448
    N348 --> N563
    N350 --> N448
    N350 --> N563
    N351 --> N448
    N351 --> N563
    N352 --> N398
    N352 --> N432
    N352 --> N365
    N352 --> N392
    N352 --> N408
    N352 --> N447
    N352 --> N500
    N352 --> N448
    N352 --> N563
    N353 --> N448
    N353 --> N563
    N355 --> N517
    N356 --> N412
    N356 --> N398
    N356 --> N432
    N356 --> N448
    N356 --> N563
    N357 --> N448
    N357 --> N563
    N359 --> N448
    N359 --> N563
    N360 --> N419
    N360 --> N440
    N360 --> N365
    N360 --> N392
    N360 --> N408
    N360 --> N447
    N360 --> N500
    N360 --> N398
    N360 --> N432
    N360 --> N448
    N360 --> N563
    N361 --> N448
    N361 --> N563
    N365 --> N392
    N365 --> N408
    N365 --> N447
    N365 --> N500
    N365 --> N448
    N365 --> N563
    N366 --> N412
    N366 --> N448
    N366 --> N563
    N370 --> N398
    N370 --> N432
    N370 --> N448
    N370 --> N563
    N370 --> N528
    N371 --> N398
    N371 --> N432
    N371 --> N448
    N371 --> N563
    N379 --> N419
    N379 --> N440
    N379 --> N448
    N379 --> N563
    N380 --> N448
    N380 --> N563
    N381 --> N384
    N381 --> N580
    N381 --> N412
    N381 --> N448
    N381 --> N563
    N382 --> N448
    N382 --> N563
    N384 --> N448
    N384 --> N563
    N385 --> N448
    N385 --> N563
    N386 --> N448
    N386 --> N563
    N387 --> N365
    N387 --> N392
    N387 --> N408
    N387 --> N447
    N387 --> N500
    N387 --> N448
    N387 --> N563
    N387 --> N412
    N387 --> N398
    N387 --> N432
    N388 --> N412
    N388 --> N398
    N388 --> N432
    N388 --> N448
    N388 --> N563
    N391 --> N365
    N391 --> N392
    N391 --> N408
    N391 --> N447
    N391 --> N500
    N392 --> N559
    N392 --> N581
    N392 --> N391
    N393 --> N398
    N393 --> N432
    N393 --> N448
    N393 --> N563
    N395 --> N448
    N395 --> N563
    N396 --> N448
    N396 --> N563
    N397 --> N412
    N397 --> N448
    N397 --> N563
    N398 --> N432
    N398 --> N365
    N398 --> N392
    N398 --> N408
    N398 --> N447
    N398 --> N500
    N398 --> N448
    N398 --> N563
    N398 --> N412
    N399 --> N448
    N399 --> N563
    N400 --> N398
    N400 --> N432
    N400 --> N448
    N400 --> N563
    N400 --> N412
    N400 --> N428
    N401 --> N398
    N401 --> N432
    N401 --> N448
    N401 --> N563
    N402 --> N398
    N402 --> N432
    N402 --> N412
    N402 --> N448
    N402 --> N563
    N403 --> N398
    N403 --> N432
    N403 --> N412
    N403 --> N448
    N403 --> N563
    N404 --> N365
    N404 --> N392
    N404 --> N408
    N404 --> N447
    N404 --> N500
    N404 --> N412
    N404 --> N448
    N404 --> N563
    N404 --> N419
    N404 --> N440
    N405 --> N448
    N405 --> N563
    N405 --> N442
    N405 --> N412
    N406 --> N398
    N406 --> N432
    N406 --> N448
    N406 --> N563
    N407 --> N448
    N407 --> N563
    N408 --> N398
    N408 --> N432
    N408 --> N365
    N408 --> N392
    N408 --> N447
    N408 --> N500
    N408 --> N448
    N408 --> N563
    N408 --> N428
    N408 --> N419
    N408 --> N440
    N409 --> N365
    N409 --> N392
    N409 --> N408
    N409 --> N447
    N409 --> N500
    N409 --> N398
    N409 --> N432
    N409 --> N448
    N409 --> N563
    N410 --> N365
    N410 --> N392
    N410 --> N408
    N410 --> N447
    N410 --> N500
    N410 --> N448
    N410 --> N563
    N413 --> N448
    N413 --> N563
    N413 --> N412
    N414 --> N448
    N414 --> N563
    N414 --> N412
    N415 --> N365
    N415 --> N392
    N415 --> N408
    N415 --> N447
    N415 --> N500
    N415 --> N448
    N415 --> N563
    N415 --> N412
    N416 --> N412
    N416 --> N448
    N416 --> N563
    N417 --> N448
    N417 --> N563
    N418 --> N412
    N418 --> N448
    N418 --> N563
    N419 --> N412
    N419 --> N365
    N419 --> N392
    N419 --> N408
    N419 --> N447
    N419 --> N500
    N419 --> N448
    N419 --> N563
    N419 --> N398
    N419 --> N432
    N420 --> N419
    N420 --> N440
    N420 --> N412
    N420 --> N448
    N420 --> N563
    N421 --> N419
    N421 --> N440
    N421 --> N412
    N421 --> N448
    N421 --> N563
    N422 --> N448
    N422 --> N563
    N424 --> N398
    N424 --> N432
    N424 --> N448
    N424 --> N563
    N424 --> N428
    N424 --> N365
    N424 --> N392
    N424 --> N408
    N424 --> N447
    N424 --> N500
    N425 --> N412
    N425 --> N448
    N425 --> N563
    N426 --> N448
    N426 --> N563
    N427 --> N448
    N427 --> N563
    N428 --> N448
    N428 --> N563
    N429 --> N412
    N429 --> N365
    N429 --> N392
    N429 --> N408
    N429 --> N447
    N429 --> N500
    N429 --> N448
    N429 --> N563
    N430 --> N448
    N430 --> N563
    N431 --> N419
    N431 --> N440
    N431 --> N448
    N431 --> N563
    N432 --> N398
    N432 --> N448
    N432 --> N563
    N433 --> N448
    N433 --> N563
    N434 --> N448
    N434 --> N563
    N435 --> N412
    N435 --> N448
    N435 --> N563
    N436 --> N448
    N436 --> N563
    N437 --> N419
    N437 --> N440
    N437 --> N448
    N437 --> N563
    N438 --> N448
    N438 --> N563
    N439 --> N365
    N439 --> N392
    N439 --> N408
    N439 --> N447
    N439 --> N500
    N439 --> N448
    N439 --> N563
    N440 --> N365
    N440 --> N392
    N440 --> N408
    N440 --> N447
    N440 --> N500
    N440 --> N448
    N440 --> N563
    N440 --> N398
    N440 --> N432
    N441 --> N412
    N441 --> N365
    N441 --> N392
    N441 --> N408
    N441 --> N447
    N441 --> N500
    N441 --> N448
    N441 --> N563
    N442 --> N448
    N442 --> N563
    N442 --> N405
    N442 --> N412
    N443 --> N448
    N443 --> N563
    N444 --> N419
    N444 --> N440
    N444 --> N448
    N444 --> N563
    N445 --> N412
    N445 --> N398
    N445 --> N432
    N445 --> N448
    N445 --> N563
    N446 --> N419
    N446 --> N440
    N446 --> N448
    N446 --> N563
    N447 --> N412
    N447 --> N365
    N447 --> N392
    N447 --> N408
    N447 --> N500
    N447 --> N448
    N447 --> N563
    N448 --> N563
    N448 --> N365
    N448 --> N392
    N448 --> N408
    N448 --> N447
    N448 --> N500
    N449 --> N412
    N449 --> N365
    N449 --> N392
    N449 --> N408
    N449 --> N447
    N449 --> N500
    N449 --> N448
    N449 --> N563
    N450 --> N448
    N450 --> N563
    N450 --> N412
    N452 --> N419
    N452 --> N440
    N452 --> N448
    N452 --> N563
    N454 --> N412
    N454 --> N448
    N454 --> N563
    N455 --> N448
    N455 --> N563
    N455 --> N412
    N456 --> N448
    N456 --> N563
    N457 --> N398
    N457 --> N432
    N457 --> N412
    N457 --> N448
    N457 --> N563
    N458 --> N365
    N458 --> N392
    N458 --> N408
    N458 --> N447
    N458 --> N500
    N458 --> N398
    N458 --> N432
    N458 --> N448
    N458 --> N563
    N459 --> N448
    N459 --> N563
    N460 --> N448
    N460 --> N563
    N461 --> N448
    N461 --> N563
    N462 --> N398
    N462 --> N432
    N462 --> N412
    N462 --> N448
    N462 --> N563
    N462 --> N428
    N463 --> N398
    N463 --> N432
    N463 --> N448
    N463 --> N563
    N464 --> N398
    N464 --> N432
    N464 --> N448
    N464 --> N563
    N464 --> N412
    N464 --> N365
    N464 --> N392
    N464 --> N408
    N464 --> N447
    N464 --> N500
    N465 --> N365
    N465 --> N392
    N465 --> N408
    N465 --> N447
    N465 --> N500
    N465 --> N448
    N465 --> N563
    N467 --> N448
    N467 --> N563
    N469 --> N448
    N469 --> N563
    N469 --> N428
    N470 --> N448
    N470 --> N563
    N471 --> N448
    N471 --> N563
    N471 --> N412
    N471 --> N365
    N471 --> N392
    N471 --> N408
    N471 --> N447
    N471 --> N500
    N472 --> N448
    N472 --> N563
    N473 --> N365
    N473 --> N392
    N473 --> N408
    N473 --> N447
    N473 --> N500
    N473 --> N448
    N473 --> N563
    N474 --> N398
    N474 --> N432
    N474 --> N448
    N474 --> N563
    N475 --> N448
    N475 --> N563
    N476 --> N448
    N476 --> N563
    N477 --> N398
    N477 --> N432
    N477 --> N448
    N477 --> N563
    N478 --> N365
    N478 --> N392
    N478 --> N408
    N478 --> N447
    N478 --> N500
    N478 --> N448
    N478 --> N563
    N479 --> N398
    N479 --> N432
    N479 --> N412
    N479 --> N365
    N479 --> N392
    N479 --> N408
    N479 --> N447
    N479 --> N500
    N479 --> N448
    N479 --> N563
    N480 --> N448
    N480 --> N563
    N481 --> N448
    N481 --> N563
    N482 --> N448
    N482 --> N563
    N483 --> N448
    N483 --> N563
    N484 --> N448
    N484 --> N563
    N485 --> N412
    N485 --> N448
    N485 --> N563
    N486 --> N412
    N486 --> N448
    N486 --> N563
    N487 --> N448
    N487 --> N563
    N488 --> N448
    N488 --> N563
    N489 --> N419
    N489 --> N440
    N489 --> N448
    N489 --> N563
    N490 --> N384
    N490 --> N580
    N491 --> N398
    N491 --> N432
    N491 --> N448
    N491 --> N563
    N492 --> N419
    N492 --> N440
    N492 --> N384
    N492 --> N580
    N492 --> N448
    N492 --> N563
    N493 --> N384
    N493 --> N580
    N493 --> N419
    N493 --> N440
    N493 --> N448
    N493 --> N563
    N494 --> N365
    N494 --> N392
    N494 --> N408
    N494 --> N447
    N494 --> N500
    N494 --> N412
    N494 --> N448
    N494 --> N563
    N495 --> N448
    N495 --> N563
    N496 --> N448
    N496 --> N563
    N497 --> N412
    N498 --> N448
    N498 --> N563
    N499 --> N419
    N499 --> N440
    N499 --> N412
    N499 --> N365
    N499 --> N392
    N499 --> N408
    N499 --> N447
    N499 --> N500
    N499 --> N448
    N499 --> N563
    N500 --> N448
    N500 --> N563
    N501 --> N419
    N501 --> N440
    N501 --> N448
    N501 --> N563
    N502 --> N448
    N502 --> N563
    N503 --> N448
    N503 --> N563
    N503 --> N528
    N505 --> N448
    N505 --> N563
    N508 --> N448
    N508 --> N563
    N509 --> N374
    N509 --> N448
    N509 --> N563
    N511 --> N419
    N511 --> N440
    N511 --> N448
    N511 --> N563
    N513 --> N412
    N513 --> N448
    N513 --> N563
    N514 --> N448
    N514 --> N563
    N515 --> N528
    N515 --> N419
    N515 --> N440
    N515 --> N517
    N515 --> N448
    N515 --> N563
    N516 --> N448
    N516 --> N563
    N517 --> N384
    N517 --> N580
    N517 --> N448
    N517 --> N563
    N518 --> N528
    N518 --> N517
    N518 --> N412
    N518 --> N448
    N518 --> N563
    N519 --> N528
    N519 --> N517
    N519 --> N365
    N519 --> N392
    N519 --> N408
    N519 --> N447
    N519 --> N500
    N519 --> N448
    N519 --> N563
    N520 --> N528
    N520 --> N517
    N520 --> N412
    N520 --> N448
    N520 --> N563
    N521 --> N528
    N521 --> N448
    N521 --> N563
    N523 --> N365
    N523 --> N392
    N523 --> N408
    N523 --> N447
    N523 --> N500
    N523 --> N448
    N523 --> N563
    N526 --> N448
    N526 --> N563
    N527 --> N528
    N527 --> N517
    N527 --> N448
    N527 --> N563
    N529 --> N528
    N529 --> N530
    N530 --> N528
    N532 --> N517
    N532 --> N448
    N532 --> N563
    N534 --> N528
    N534 --> N412
    N535 --> N528
    N536 --> N528
    N537 --> N528
    N538 --> N528
    N538 --> N384
    N538 --> N580
    N538 --> N517
    N538 --> N448
    N538 --> N563
    N539 --> N528
    N539 --> N384
    N539 --> N580
    N539 --> N517
    N539 --> N448
    N539 --> N563
    N540 --> N528
    N540 --> N367
    N540 --> N501
    N541 --> N528
    N541 --> N384
    N541 --> N580
    N541 --> N517
    N541 --> N448
    N541 --> N563
    N541 --> N367
    N541 --> N501
    N542 --> N528
    N542 --> N517
    N542 --> N384
    N542 --> N580
    N542 --> N448
    N542 --> N563
    N542 --> N367
    N542 --> N501
    N543 --> N528
    N543 --> N517
    N543 --> N448
    N543 --> N563
    N544 --> N517
    N544 --> N365
    N544 --> N392
    N544 --> N408
    N544 --> N447
    N544 --> N500
    N545 --> N517
    N545 --> N448
    N545 --> N563
    N546 --> N517
    N548 --> N448
    N548 --> N563
    N549 --> N412
    N550 --> N528
    N550 --> N448
    N550 --> N563
    N551 --> N412
    N551 --> N448
    N551 --> N563
    N552 --> N412
    N553 --> N448
    N553 --> N563
    N554 --> N412
    N555 --> N398
    N555 --> N432
    N555 --> N448
    N555 --> N563
    N556 --> N448
    N556 --> N563
    N557 --> N398
    N557 --> N432
    N557 --> N412
    N557 --> N448
    N557 --> N563
    N558 --> N412
    N558 --> N448
    N558 --> N563
    N559 --> N517
    N560 --> N398
    N560 --> N432
    N561 --> N384
    N561 --> N580
    N561 --> N412
    N561 --> N448
    N561 --> N563
    N563 --> N384
    N563 --> N580
    N563 --> N517
    N563 --> N448
    N564 --> N398
    N564 --> N432
    N567 --> N448
    N567 --> N563
    N568 --> N528
    N568 --> N517
    N568 --> N365
    N568 --> N392
    N568 --> N408
    N568 --> N447
    N568 --> N500
    N568 --> N448
    N568 --> N563
    N568 --> N367
    N568 --> N501
    N569 --> N528
    N569 --> N517
    N569 --> N365
    N569 --> N392
    N569 --> N408
    N569 --> N447
    N569 --> N500
    N569 --> N448
    N569 --> N563
    N570 --> N528
    N570 --> N448
    N570 --> N563
    N571 --> N384
    N571 --> N580
    N571 --> N448
    N571 --> N563
    N571 --> N367
    N571 --> N501
    N572 --> N528
    N572 --> N384
    N572 --> N580
    N572 --> N517
    N572 --> N365
    N572 --> N392
    N572 --> N408
    N572 --> N447
    N572 --> N500
    N572 --> N448
    N572 --> N563
    N572 --> N367
    N572 --> N501
    N574 --> N448
    N574 --> N563
    N575 --> N384
    N575 --> N580
    N575 --> N448
    N575 --> N563
    N576 --> N528
    N576 --> N517
    N576 --> N412
    N576 --> N365
    N576 --> N392
    N576 --> N408
    N576 --> N447
    N576 --> N500
    N576 --> N448
    N576 --> N563
    N577 --> N384
    N577 --> N580
    N578 --> N448
    N578 --> N563
    N580 --> N528
    N581 --> N528
    N581 --> N517
    N581 --> N412
    N581 --> N448
    N581 --> N563
    N582 --> N528
    N582 --> N384
    N582 --> N580
    N582 --> N517
    N582 --> N412
    N582 --> N365
    N582 --> N392
    N582 --> N408
    N582 --> N447
    N582 --> N500
    N582 --> N448
    N582 --> N563
    N583 --> N412
    N584 --> N517
    N584 --> N412
    N584 --> N365
    N584 --> N392
    N584 --> N408
    N584 --> N447
    N584 --> N500
    N584 --> N448
    N584 --> N563
    N584 --> N367
    N584 --> N501
    N585 --> N517
    N585 --> N365
    N585 --> N392
    N585 --> N408
    N585 --> N447
    N585 --> N500
    N585 --> N448
    N585 --> N563
    N586 --> N448
    N586 --> N563
    N587 --> N384
    N587 --> N580
    N587 --> N448
    N587 --> N563
    N587 --> N367
    N587 --> N501
    N588 --> N384
    N588 --> N580
    N588 --> N517
    N588 --> N412
    N588 --> N365
    N588 --> N392
    N588 --> N408
    N588 --> N447
    N588 --> N500
    N588 --> N448
    N588 --> N563
    N588 --> N367
    N588 --> N501
    N590 --> N517
    N590 --> N365
    N590 --> N392
    N590 --> N408
    N590 --> N447
    N590 --> N500
    N590 --> N448
    N590 --> N563
    N590 --> N367
    N590 --> N501
    N591 --> N517
    N591 --> N365
    N591 --> N392
    N591 --> N408
    N591 --> N447
    N591 --> N500
    N591 --> N448
    N591 --> N563
    N592 --> N448
    N592 --> N563
    N593 --> N384
    N593 --> N580
    N593 --> N448
    N593 --> N563
    N593 --> N367
    N593 --> N501
    N594 --> N384
    N594 --> N580
    N594 --> N517
    N594 --> N365
    N594 --> N392
    N594 --> N408
    N594 --> N447
    N594 --> N500
    N594 --> N448
    N594 --> N563
    N594 --> N367
    N594 --> N501
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
  - Imports: `base64`
  - Imports: `collections`
  - Imports: `cryptography`
  - Imports: `datetime`
  - Imports: `docx`
  - Imports: `fastembed`
  - Imports: `hashlib`
  - Imports: `httpx`
  - Imports: `json`
  - Imports: `numpy`
  - Imports: `ollama`
  - Imports: `os`
  - Imports: `pymongo`
  - Imports: `pypdf`
  - Imports: `random`
  - Imports: `re`
  - Imports: `sqlite3`
  - Imports: `src`
  - Imports: `threading`
  - Imports: `time`
  - Imports: `turbovec`
  - Imports: `typing`
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