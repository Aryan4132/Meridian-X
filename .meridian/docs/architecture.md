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
    N215["test_auto_bug_fixer.py [meridian_backend/tests]"]
    N216["test_backend_improvements.py [meridian_backend/tests]"]
    N217["test_backlog_features.py [meridian_backend/tests]"]
    N218["test_backlog_sprint.py [meridian_backend/tests]"]
    N219["test_bridges.py [meridian_backend/tests]"]
    N220["test_browser_agent.py [meridian_backend/tests]"]
    N221["test_browser_fallback.py [meridian_backend/tests]"]
    N222["test_browser_use.py [meridian_backend/tests]"]
    N223["test_butler_media.py [meridian_backend/tests]"]
    N224["test_chat_abort.py [meridian_backend/tests]"]
    N225["test_cognitive_graph.py [meridian_backend/tests]"]
    N226["test_config.py [meridian_backend/tests]"]
    N227["test_consensus_gate.py [meridian_backend/tests]"]
    N228["test_context_budget.py [meridian_backend/tests]"]
    N229["test_custom_password_auth.py [meridian_backend/tests]"]
    N230["test_database.py [meridian_backend/tests]"]
    N231["test_day10_features.py [meridian_backend/tests]"]
    N232["test_day11_features.py [meridian_backend/tests]"]
    N233["test_day12_features.py [meridian_backend/tests]"]
    N234["test_day13_features.py [meridian_backend/tests]"]
    N235["test_day14_day15_features.py [meridian_backend/tests]"]
    N236["test_day16_17_18_features.py [meridian_backend/tests]"]
    N237["test_day3_features.py [meridian_backend/tests]"]
    N238["test_day4_features.py [meridian_backend/tests]"]
    N239["test_day5_features.py [meridian_backend/tests]"]
    N240["test_day6_features.py [meridian_backend/tests]"]
    N241["test_day7_features.py [meridian_backend/tests]"]
    N242["test_day8_features.py [meridian_backend/tests]"]
    N243["test_day9_features.py [meridian_backend/tests]"]
    N244["test_dev_intelligence_suite.py [meridian_backend/tests]"]
    N245["test_document_tools.py [meridian_backend/tests]"]
    N246["test_full_proactive_suite.py [meridian_backend/tests]"]
    N247["test_geo_location.py [meridian_backend/tests]"]
    N248["test_jarvis_perception.py [meridian_backend/tests]"]
    N249["test_known_errors_remediation.py [meridian_backend/tests]"]
    N250["test_llm_provider.py [meridian_backend/tests]"]
    N251["test_logging.py [meridian_backend/tests]"]
    N252["test_loop_parser.py [meridian_backend/tests]"]
    N253["test_loop_submodules.py [meridian_backend/tests]"]
    N254["test_mobile_websocket.py [meridian_backend/tests]"]
    N255["test_model_source.py [meridian_backend/tests]"]
    N256["test_multi_os.py [meridian_backend/tests]"]
    N257["test_new_features.py [meridian_backend/tests]"]
    N258["test_oauth.py [meridian_backend/tests]"]
    N259["test_p2p.py [meridian_backend/tests]"]
    N260["test_proactive.py [meridian_backend/tests]"]
    N261["test_proactive_mode.py [meridian_backend/tests]"]
    N262["test_proactive_notifications.py [meridian_backend/tests]"]
    N263["test_security_features.py [meridian_backend/tests]"]
    N264["test_silero_vad.py [meridian_backend/tests]"]
    N265["test_skill_packs.py [meridian_backend/tests]"]
    N266["test_sprint24_hardening.py [meridian_backend/tests]"]
    N267["test_sprint25_hardening.py [meridian_backend/tests]"]
    N268["test_sprint27_hardening.py [meridian_backend/tests]"]
    N269["test_sprint28_hardening.py [meridian_backend/tests]"]
    N270["test_sprint2_features.py [meridian_backend/tests]"]
    N271["test_standalone_bridge.py [meridian_backend/tests]"]
    N272["test_stream_resiliency.py [meridian_backend/tests]"]
    N273["test_swarm.py [meridian_backend/tests]"]
    N274["test_tools.py [meridian_backend/tests]"]
    N275["test_tool_modernization.py [meridian_backend/tests]"]
    N276["test_tool_regression.py [meridian_backend/tests]"]
    N277["test_vault.py [meridian_backend/tests]"]
    N278["test_video_editor.py [meridian_backend/tests]"]
    N279["test_voice_speed.py [meridian_backend/tests]"]
    N280["test_wakeword_continuous.py [meridian_backend/tests]"]
    N281["test_wakeword_onnx.py [meridian_backend/tests]"]
    N282["test_web_guards.py [meridian_backend/tests]"]
    N283["test_workflow.py [meridian_backend/tests]"]
    N284["vite.config.ts [meridian_frontend]"]
    N285["AppContext.tsx [meridian_frontend/src]"]
    N286["main.tsx [meridian_frontend/src]"]
    N287["Mascot.tsx [meridian_frontend/src]"]
    N288["Mascot3DCharacter.tsx [meridian_frontend/src]"]
    N289["MobileApp.tsx [meridian_frontend/src]"]
    N290["AgentStatusStream.tsx [meridian_frontend/src/components]"]
    N291["CommandPalette.tsx [meridian_frontend/src/components]"]
    N292["DevAutomationPanel.tsx [meridian_frontend/src/components]"]
    N293["DeveloperSuitePanel.tsx [meridian_frontend/src/components]"]
    N294["LocalModelManager.tsx [meridian_frontend/src/components]"]
    N295["MemoryConsolidationView.tsx [meridian_frontend/src/components]"]
    N296["NavRail.tsx [meridian_frontend/src/components]"]
    N297["PerceptionHUD.tsx [meridian_frontend/src/components]"]
    N298["ProactiveGuardBanner.tsx [meridian_frontend/src/components]"]
    N299["ProfileHeader.tsx [meridian_frontend/src/components]"]
    N300["RightDrawer.tsx [meridian_frontend/src/components]"]
    N301["ServerConnectionModal.tsx [meridian_frontend/src/components]"]
    N302["Shell.tsx [meridian_frontend/src/components]"]
    N303["StatusBar.tsx [meridian_frontend/src/components]"]
    N304["DropdownNav.tsx [meridian_frontend/src/components/mobile]"]
    N305["LiveThoughtCarousel.tsx [meridian_frontend/src/components/mobile]"]
    N306["VoiceOrbHUD.tsx [meridian_frontend/src/components/mobile]"]
    N307["AmbientParticles.tsx [meridian_frontend/src/components/ui]"]
    N308["DataBadge.tsx [meridian_frontend/src/components/ui]"]
    N309["GlowCard.tsx [meridian_frontend/src/components/ui]"]
    N310["HoloButton.tsx [meridian_frontend/src/components/ui]"]
    N311["ProgressArc.tsx [meridian_frontend/src/components/ui]"]
    N312["TerminalLine.tsx [meridian_frontend/src/components/ui]"]
    N313["ToastContext.tsx [meridian_frontend/src/components/ui]"]
    N314["useMemoryOptimizer.ts [meridian_frontend/src/hooks]"]
    N315["oauthService.ts [meridian_frontend/src/services]"]
    N316["streamingAudioPlayer.ts [meridian_frontend/src/services]"]
    N317["BackendSetup.tsx [meridian_frontend/src/startup]"]
    N318["BootSequence.tsx [meridian_frontend/src/startup]"]
    N319["OnboardingWizard.tsx [meridian_frontend/src/startup]"]
    N320["SetupWizard.tsx [meridian_frontend/src/startup]"]
    N321["Clipboard.tsx [meridian_frontend/src/views]"]
    N322["Jobs.tsx [meridian_frontend/src/views]"]
    N323["MemoryEditor.tsx [meridian_frontend/src/views]"]
    N324["Productivity.tsx [meridian_frontend/src/views]"]
    N325["Settings.tsx [meridian_frontend/src/views]"]
    N326["SwarmDebate.tsx [meridian_frontend/src/views]"]
    N327["Timeline.tsx [meridian_frontend/src/views]"]
    N328["WorkflowBuilder.tsx [meridian_frontend/src/views]"]
    N329["AiModelsTab.tsx [meridian_frontend/src/views/settings]"]
    N330["IntegrationsTab.tsx [meridian_frontend/src/views/settings]"]
    N331["MascotTab.tsx [meridian_frontend/src/views/settings]"]
    N332["PasswordInput.tsx [meridian_frontend/src/views/settings]"]
    N333["SpendAirGapTab.tsx [meridian_frontend/src/views/settings]"]
    N334["SystemGuardTab.tsx [meridian_frontend/src/views/settings]"]
    N335["VoiceTab.tsx [meridian_frontend/src/views/settings]"]
    N336["config.py [meridian_frontend/src-tauri/api/_internal/cv2]"]
    N337["load_config_py3.py [meridian_frontend/src-tauri/api/_internal/cv2]"]
    N338["__init__.py [meridian_frontend/src-tauri/api/_internal/cv2]"]
    N339["__init__.py [meridian_frontend/src-tauri/api/_internal/cv2/data]"]
    N340["__init__.py [meridian_frontend/src-tauri/api/_internal/cv2/mat_wrapper]"]
    N341["version.py [meridian_frontend/src-tauri/api/_internal/cv2/misc]"]
    N342["__init__.py [meridian_frontend/src-tauri/api/_internal/cv2/typing]"]
    N343["__init__.py [meridian_frontend/src-tauri/api/_internal/cv2/utils]"]
    N344["applications.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N345["background.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N346["cli.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N347["concurrency.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N348["datastructures.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N349["encoders.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N350["exceptions.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N351["exception_handlers.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N352["logger.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N353["params.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N354["param_functions.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N355["requests.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N356["responses.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N357["routing.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N358["sse.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N359["staticfiles.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N360["templating.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N361["testclient.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N362["types.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N363["utils.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N364["websockets.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N365["__init__.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N366["__main__.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N367["models.py [meridian_frontend/src-tauri/api/_internal/fastapi/dependencies]"]
    N368["utils.py [meridian_frontend/src-tauri/api/_internal/fastapi/dependencies]"]
    N369["asyncexitstack.py [meridian_frontend/src-tauri/api/_internal/fastapi/middleware]"]
    N370["cors.py [meridian_frontend/src-tauri/api/_internal/fastapi/middleware]"]
    N371["gzip.py [meridian_frontend/src-tauri/api/_internal/fastapi/middleware]"]
    N372["httpsredirect.py [meridian_frontend/src-tauri/api/_internal/fastapi/middleware]"]
    N373["trustedhost.py [meridian_frontend/src-tauri/api/_internal/fastapi/middleware]"]
    N374["wsgi.py [meridian_frontend/src-tauri/api/_internal/fastapi/middleware]"]
    N375["__init__.py [meridian_frontend/src-tauri/api/_internal/fastapi/middleware]"]
    N376["docs.py [meridian_frontend/src-tauri/api/_internal/fastapi/openapi]"]
    N377["models.py [meridian_frontend/src-tauri/api/_internal/fastapi/openapi]"]
    N378["utils.py [meridian_frontend/src-tauri/api/_internal/fastapi/openapi]"]
    N379["api_key.py [meridian_frontend/src-tauri/api/_internal/fastapi/security]"]
    N380["base.py [meridian_frontend/src-tauri/api/_internal/fastapi/security]"]
    N381["http.py [meridian_frontend/src-tauri/api/_internal/fastapi/security]"]
    N382["oauth2.py [meridian_frontend/src-tauri/api/_internal/fastapi/security]"]
    N383["open_id_connect_url.py [meridian_frontend/src-tauri/api/_internal/fastapi/security]"]
    N384["shared.py [meridian_frontend/src-tauri/api/_internal/fastapi/_compat]"]
    N385["v2.py [meridian_frontend/src-tauri/api/_internal/fastapi/_compat]"]
    N386["coreBundle.js [meridian_frontend/src-tauri/api/_internal/playwright/driver/package/lib]"]
    N387["utilsBundle.js [meridian_frontend/src-tauri/api/_internal/playwright/driver/package/lib]"]
    N388["structs.d.ts [meridian_frontend/src-tauri/api/_internal/playwright/driver/package/types]"]
    N389["types.d.ts [meridian_frontend/src-tauri/api/_internal/playwright/driver/package/types]"]
    N390["aliases.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N391["alias_generators.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N392["annotated_handlers.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N393["color.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N394["config.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N395["dataclasses.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N396["errors.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N397["fields.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N398["functional_serializers.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N399["functional_validators.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N400["json_schema.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N401["main.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N402["mypy.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N403["networks.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N404["root_model.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N405["types.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N406["type_adapter.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N407["validate_call_decorator.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N408["version.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N409["warnings.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N410["_migration.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N411["__init__.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N412["class_validators.py [meridian_frontend/src-tauri/api/_internal/pydantic/deprecated]"]
    N413["config.py [meridian_frontend/src-tauri/api/_internal/pydantic/deprecated]"]
    N414["copy_internals.py [meridian_frontend/src-tauri/api/_internal/pydantic/deprecated]"]
    N415["decorator.py [meridian_frontend/src-tauri/api/_internal/pydantic/deprecated]"]
    N416["json.py [meridian_frontend/src-tauri/api/_internal/pydantic/deprecated]"]
    N417["parse.py [meridian_frontend/src-tauri/api/_internal/pydantic/deprecated]"]
    N418["tools.py [meridian_frontend/src-tauri/api/_internal/pydantic/deprecated]"]
    N419["arguments_schema.py [meridian_frontend/src-tauri/api/_internal/pydantic/experimental]"]
    N420["missing_sentinel.py [meridian_frontend/src-tauri/api/_internal/pydantic/experimental]"]
    N421["pipeline.py [meridian_frontend/src-tauri/api/_internal/pydantic/experimental]"]
    N422["_loader.py [meridian_frontend/src-tauri/api/_internal/pydantic/plugin]"]
    N423["_schema_validator.py [meridian_frontend/src-tauri/api/_internal/pydantic/plugin]"]
    N424["__init__.py [meridian_frontend/src-tauri/api/_internal/pydantic/plugin]"]
    N425["annotated_types.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N426["class_validators.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N427["color.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N428["config.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N429["dataclasses.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N430["datetime_parse.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N431["decorator.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N432["env_settings.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N433["errors.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N434["error_wrappers.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N435["fields.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N436["generics.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N437["json.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N438["main.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N439["mypy.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N440["networks.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N441["parse.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N442["schema.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N443["tools.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N444["types.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N445["typing.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N446["utils.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N447["validators.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N448["version.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N449["_hypothesis_plugin.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N450["__init__.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N451["_config.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N452["_core_metadata.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N453["_core_utils.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N454["_dataclasses.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N455["_decorators.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N456["_decorators_v1.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N457["_discriminated_union.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N458["_docs_extraction.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N459["_fields.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N460["_forward_ref.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N461["_generate_schema.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N462["_generics.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N463["_git.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N464["_import_utils.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N465["_internal_dataclass.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N466["_known_annotated_metadata.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N467["_mock_val_ser.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N468["_model_construction.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N469["_namespace_utils.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N470["_repr.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N471["_schema_gather.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N472["_schema_generation_shared.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N473["_serializers.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N474["_signature.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N475["_typing_extra.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N476["_utils.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N477["_validate_call.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N478["_validators.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N479["applications.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N480["authentication.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N481["background.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N482["concurrency.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N483["config.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N484["convertors.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N485["datastructures.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N486["endpoints.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N487["exceptions.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N488["formparsers.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N489["requests.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N490["responses.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N491["routing.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N492["schemas.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N493["staticfiles.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N494["status.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N495["templating.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N496["testclient.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N497["types.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N498["websockets.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N499["_exception_handler.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N500["_utils.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N501["authentication.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N502["base.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N503["cors.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N504["errors.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N505["exceptions.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N506["gzip.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N507["httpsredirect.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N508["sessions.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N509["trustedhost.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N510["wsgi.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N511["__init__.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N512["config.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N513["importer.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N514["logging.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N515["main.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N516["server.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N517["workers.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N518["_compat.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N519["_subprocess.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N520["_types.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N521["__init__.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N522["__main__.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N523["off.py [meridian_frontend/src-tauri/api/_internal/uvicorn/lifespan]"]
    N524["on.py [meridian_frontend/src-tauri/api/_internal/uvicorn/lifespan]"]
    N525["asyncio.py [meridian_frontend/src-tauri/api/_internal/uvicorn/loops]"]
    N526["auto.py [meridian_frontend/src-tauri/api/_internal/uvicorn/loops]"]
    N527["uvloop.py [meridian_frontend/src-tauri/api/_internal/uvicorn/loops]"]
    N528["asgi2.py [meridian_frontend/src-tauri/api/_internal/uvicorn/middleware]"]
    N529["message_logger.py [meridian_frontend/src-tauri/api/_internal/uvicorn/middleware]"]
    N530["proxy_headers.py [meridian_frontend/src-tauri/api/_internal/uvicorn/middleware]"]
    N531["wsgi.py [meridian_frontend/src-tauri/api/_internal/uvicorn/middleware]"]
    N532["utils.py [meridian_frontend/src-tauri/api/_internal/uvicorn/protocols]"]
    N533["auto.py [meridian_frontend/src-tauri/api/_internal/uvicorn/protocols/http]"]
    N534["flow_control.py [meridian_frontend/src-tauri/api/_internal/uvicorn/protocols/http]"]
    N535["h11_impl.py [meridian_frontend/src-tauri/api/_internal/uvicorn/protocols/http]"]
    N536["httptools_impl.py [meridian_frontend/src-tauri/api/_internal/uvicorn/protocols/http]"]
    N537["auto.py [meridian_frontend/src-tauri/api/_internal/uvicorn/protocols/websockets]"]
    N538["websockets_impl.py [meridian_frontend/src-tauri/api/_internal/uvicorn/protocols/websockets]"]
    N539["websockets_sansio_impl.py [meridian_frontend/src-tauri/api/_internal/uvicorn/protocols/websockets]"]
    N540["wsproto_impl.py [meridian_frontend/src-tauri/api/_internal/uvicorn/protocols/websockets]"]
    N541["basereload.py [meridian_frontend/src-tauri/api/_internal/uvicorn/supervisors]"]
    N542["multiprocess.py [meridian_frontend/src-tauri/api/_internal/uvicorn/supervisors]"]
    N543["statreload.py [meridian_frontend/src-tauri/api/_internal/uvicorn/supervisors]"]
    N544["watchfilesreload.py [meridian_frontend/src-tauri/api/_internal/uvicorn/supervisors]"]
    N545["__init__.py [meridian_frontend/src-tauri/api/_internal/uvicorn/supervisors]"]
    N546["auth.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N547["cli.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N548["client.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N549["connection.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N550["datastructures.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N551["exceptions.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N552["frames.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N553["headers.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N554["http11.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N555["imports.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N556["protocol.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N557["proxy.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N558["server.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N559["streams.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N560["typing.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N561["uri.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N562["utils.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N563["version.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N564["__init__.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N565["client.py [meridian_frontend/src-tauri/api/_internal/websockets/asyncio]"]
    N566["connection.py [meridian_frontend/src-tauri/api/_internal/websockets/asyncio]"]
    N567["messages.py [meridian_frontend/src-tauri/api/_internal/websockets/asyncio]"]
    N568["router.py [meridian_frontend/src-tauri/api/_internal/websockets/asyncio]"]
    N569["server.py [meridian_frontend/src-tauri/api/_internal/websockets/asyncio]"]
    N570["base.py [meridian_frontend/src-tauri/api/_internal/websockets/extensions]"]
    N571["permessage_deflate.py [meridian_frontend/src-tauri/api/_internal/websockets/extensions]"]
    N572["auth.py [meridian_frontend/src-tauri/api/_internal/websockets/legacy]"]
    N573["client.py [meridian_frontend/src-tauri/api/_internal/websockets/legacy]"]
    N574["exceptions.py [meridian_frontend/src-tauri/api/_internal/websockets/legacy]"]
    N575["framing.py [meridian_frontend/src-tauri/api/_internal/websockets/legacy]"]
    N576["handshake.py [meridian_frontend/src-tauri/api/_internal/websockets/legacy]"]
    N577["http.py [meridian_frontend/src-tauri/api/_internal/websockets/legacy]"]
    N578["protocol.py [meridian_frontend/src-tauri/api/_internal/websockets/legacy]"]
    N579["server.py [meridian_frontend/src-tauri/api/_internal/websockets/legacy]"]
    N580["__init__.py [meridian_frontend/src-tauri/api/_internal/websockets/legacy]"]
    N581["client.py [meridian_frontend/src-tauri/api/_internal/websockets/sync]"]
    N582["connection.py [meridian_frontend/src-tauri/api/_internal/websockets/sync]"]
    N583["messages.py [meridian_frontend/src-tauri/api/_internal/websockets/sync]"]
    N584["router.py [meridian_frontend/src-tauri/api/_internal/websockets/sync]"]
    N585["server.py [meridian_frontend/src-tauri/api/_internal/websockets/sync]"]
    N586["utils.py [meridian_frontend/src-tauri/api/_internal/websockets/sync]"]
    N587["client.py [meridian_frontend/src-tauri/api/_internal/websockets/trio]"]
    N588["connection.py [meridian_frontend/src-tauri/api/_internal/websockets/trio]"]
    N589["messages.py [meridian_frontend/src-tauri/api/_internal/websockets/trio]"]
    N590["router.py [meridian_frontend/src-tauri/api/_internal/websockets/trio]"]
    N591["server.py [meridian_frontend/src-tauri/api/_internal/websockets/trio]"]
    N592["utils.py [meridian_frontend/src-tauri/api/_internal/websockets/trio]"]
    N593["build_apk.py [meridian_mobile]"]
    N594["flutter_lldb_helper.py [meridian_mobile/ios/Flutter/ephemeral]"]
    N595["get_system_platform_info.py [plugins]"]

    N1 --> N416
    N1 --> N437
    N1 --> N445
    N1 --> N560
    N2 --> N416
    N2 --> N437
    N2 --> N445
    N2 --> N560
    N3 --> N416
    N3 --> N437
    N4 --> N525
    N4 --> N416
    N4 --> N437
    N4 --> N13
    N8 --> N416
    N8 --> N437
    N8 --> N445
    N8 --> N560
    N9 --> N395
    N9 --> N429
    N12 --> N9
    N12 --> N49
    N12 --> N336
    N12 --> N394
    N12 --> N413
    N12 --> N428
    N12 --> N483
    N12 --> N512
    N12 --> N11
    N12 --> N10
    N13 --> N416
    N13 --> N437
    N13 --> N514
    N13 --> N525
    N13 --> N445
    N13 --> N560
    N13 --> N14
    N14 --> N416
    N14 --> N437
    N14 --> N445
    N14 --> N560
    N15 --> N416
    N15 --> N437
    N15 --> N525
    N15 --> N514
    N15 --> N445
    N15 --> N560
    N18 --> N416
    N18 --> N437
    N18 --> N445
    N18 --> N560
    N18 --> N14
    N19 --> N416
    N19 --> N437
    N19 --> N525
    N19 --> N445
    N19 --> N560
    N19 --> N14
    N20 --> N416
    N20 --> N437
    N20 --> N514
    N20 --> N445
    N20 --> N560
    N20 --> N14
    N21 --> N416
    N21 --> N437
    N21 --> N445
    N21 --> N560
    N22 --> N416
    N22 --> N437
    N22 --> N445
    N22 --> N560
    N22 --> N14
    N23 --> N445
    N23 --> N560
    N24 --> N445
    N24 --> N560
    N24 --> N14
    N25 --> N445
    N25 --> N560
    N25 --> N14
    N26 --> N416
    N26 --> N437
    N26 --> N445
    N26 --> N560
    N26 --> N14
    N27 --> N416
    N27 --> N437
    N27 --> N514
    N27 --> N525
    N27 --> N445
    N27 --> N560
    N27 --> N14
    N28 --> N445
    N28 --> N560
    N28 --> N14
    N28 --> N525
    N29 --> N445
    N29 --> N560
    N30 --> N514
    N30 --> N445
    N30 --> N560
    N31 --> N416
    N31 --> N437
    N31 --> N445
    N31 --> N560
    N31 --> N14
    N33 --> N416
    N33 --> N437
    N33 --> N514
    N33 --> N445
    N33 --> N560
    N33 --> N14
    N34 --> N525
    N34 --> N514
    N34 --> N445
    N34 --> N560
    N35 --> N514
    N35 --> N445
    N35 --> N560
    N36 --> N416
    N36 --> N437
    N36 --> N514
    N36 --> N445
    N36 --> N560
    N37 --> N416
    N37 --> N437
    N37 --> N514
    N38 --> N445
    N38 --> N560
    N38 --> N416
    N38 --> N437
    N39 --> N514
    N39 --> N445
    N39 --> N560
    N40 --> N514
    N40 --> N445
    N40 --> N560
    N41 --> N514
    N41 --> N445
    N41 --> N560
    N41 --> N416
    N41 --> N437
    N42 --> N525
    N42 --> N445
    N42 --> N560
    N43 --> N514
    N43 --> N445
    N43 --> N560
    N44 --> N525
    N44 --> N445
    N44 --> N560
    N45 --> N445
    N45 --> N560
    N45 --> N14
    N46 --> N445
    N46 --> N560
    N47 --> N416
    N47 --> N437
    N47 --> N514
    N47 --> N445
    N47 --> N560
    N48 --> N514
    N48 --> N445
    N48 --> N560
    N50 --> N525
    N50 --> N445
    N50 --> N560
    N50 --> N14
    N51 --> N416
    N51 --> N437
    N51 --> N514
    N51 --> N445
    N51 --> N560
    N51 --> N525
    N51 --> N14
    N52 --> N514
    N52 --> N445
    N52 --> N560
    N53 --> N525
    N53 --> N514
    N53 --> N445
    N53 --> N560
    N54 --> N525
    N54 --> N445
    N54 --> N560
    N54 --> N14
    N55 --> N445
    N55 --> N560
    N57 --> N416
    N57 --> N437
    N57 --> N514
    N57 --> N445
    N57 --> N560
    N57 --> N14
    N58 --> N514
    N58 --> N445
    N58 --> N560
    N59 --> N514
    N59 --> N445
    N59 --> N560
    N60 --> N514
    N60 --> N445
    N60 --> N560
    N61 --> N514
    N61 --> N445
    N61 --> N560
    N62 --> N445
    N62 --> N560
    N62 --> N14
    N63 --> N514
    N63 --> N445
    N63 --> N560
    N64 --> N514
    N64 --> N445
    N64 --> N560
    N65 --> N445
    N65 --> N560
    N66 --> N416
    N66 --> N437
    N66 --> N445
    N66 --> N560
    N67 --> N416
    N67 --> N437
    N67 --> N445
    N67 --> N560
    N68 --> N514
    N68 --> N445
    N68 --> N560
    N68 --> N409
    N68 --> N416
    N68 --> N437
    N70 --> N514
    N70 --> N445
    N70 --> N560
    N70 --> N14
    N71 --> N525
    N71 --> N514
    N71 --> N445
    N71 --> N560
    N71 --> N14
    N72 --> N445
    N72 --> N560
    N72 --> N14
    N73 --> N416
    N73 --> N437
    N73 --> N514
    N73 --> N525
    N73 --> N445
    N73 --> N560
    N73 --> N14
    N74 --> N514
    N74 --> N525
    N74 --> N445
    N74 --> N560
    N74 --> N14
    N74 --> N416
    N74 --> N437
    N75 --> N416
    N75 --> N437
    N75 --> N514
    N75 --> N445
    N75 --> N560
    N76 --> N514
    N76 --> N416
    N76 --> N437
    N77 --> N416
    N77 --> N437
    N77 --> N525
    N77 --> N445
    N77 --> N560
    N77 --> N14
    N78 --> N416
    N78 --> N437
    N78 --> N525
    N78 --> N445
    N78 --> N560
    N78 --> N14
    N79 --> N416
    N79 --> N437
    N79 --> N445
    N79 --> N560
    N79 --> N14
    N80 --> N416
    N80 --> N437
    N80 --> N525
    N80 --> N445
    N80 --> N560
    N80 --> N14
    N81 --> N416
    N81 --> N437
    N81 --> N525
    N81 --> N445
    N81 --> N560
    N81 --> N14
    N82 --> N416
    N82 --> N437
    N82 --> N525
    N82 --> N445
    N82 --> N560
    N82 --> N14
    N83 --> N416
    N83 --> N437
    N83 --> N525
    N83 --> N445
    N83 --> N560
    N84 --> N514
    N84 --> N445
    N84 --> N560
    N85 --> N416
    N85 --> N437
    N85 --> N525
    N85 --> N514
    N85 --> N445
    N85 --> N560
    N86 --> N525
    N86 --> N416
    N86 --> N437
    N86 --> N514
    N86 --> N445
    N86 --> N560
    N87 --> N416
    N87 --> N437
    N87 --> N445
    N87 --> N560
    N88 --> N514
    N88 --> N525
    N88 --> N416
    N88 --> N437
    N88 --> N445
    N88 --> N560
    N88 --> N14
    N89 --> N416
    N89 --> N437
    N89 --> N445
    N89 --> N560
    N89 --> N14
    N90 --> N416
    N90 --> N437
    N90 --> N514
    N90 --> N445
    N90 --> N560
    N90 --> N14
    N90 --> N525
    N91 --> N445
    N91 --> N560
    N91 --> N14
    N91 --> N416
    N91 --> N437
    N92 --> N445
    N92 --> N560
    N93 --> N416
    N93 --> N437
    N93 --> N445
    N93 --> N560
    N94 --> N514
    N94 --> N525
    N94 --> N445
    N94 --> N560
    N94 --> N416
    N94 --> N437
    N95 --> N416
    N95 --> N437
    N95 --> N445
    N95 --> N560
    N95 --> N14
    N97 --> N445
    N97 --> N560
    N98 --> N445
    N98 --> N560
    N99 --> N514
    N99 --> N445
    N99 --> N560
    N100 --> N514
    N100 --> N445
    N100 --> N560
    N101 --> N514
    N101 --> N445
    N101 --> N560
    N101 --> N14
    N102 --> N445
    N102 --> N560
    N103 --> N514
    N103 --> N445
    N103 --> N560
    N104 --> N514
    N104 --> N445
    N104 --> N560
    N105 --> N514
    N105 --> N445
    N105 --> N560
    N106 --> N514
    N106 --> N445
    N106 --> N560
    N107 --> N514
    N107 --> N445
    N107 --> N560
    N108 --> N416
    N108 --> N437
    N108 --> N445
    N108 --> N560
    N109 --> N445
    N109 --> N560
    N110 --> N445
    N110 --> N560
    N111 --> N514
    N111 --> N445
    N111 --> N560
    N112 --> N525
    N112 --> N409
    N112 --> N14
    N112 --> N416
    N112 --> N437
    N113 --> N525
    N113 --> N514
    N113 --> N445
    N113 --> N560
    N114 --> N514
    N114 --> N445
    N114 --> N560
    N115 --> N514
    N115 --> N445
    N115 --> N560
    N116 --> N514
    N116 --> N445
    N116 --> N560
    N117 --> N514
    N117 --> N445
    N117 --> N560
    N118 --> N514
    N118 --> N445
    N118 --> N560
    N118 --> N14
    N119 --> N416
    N119 --> N437
    N119 --> N525
    N119 --> N445
    N119 --> N560
    N119 --> N14
    N120 --> N525
    N120 --> N416
    N120 --> N437
    N120 --> N445
    N120 --> N560
    N120 --> N14
    N121 --> N514
    N121 --> N445
    N121 --> N560
    N122 --> N445
    N122 --> N560
    N122 --> N525
    N122 --> N14
    N123 --> N445
    N123 --> N560
    N124 --> N514
    N124 --> N445
    N124 --> N560
    N125 --> N445
    N125 --> N560
    N126 --> N514
    N126 --> N445
    N126 --> N560
    N127 --> N416
    N127 --> N437
    N127 --> N445
    N127 --> N560
    N128 --> N514
    N128 --> N445
    N128 --> N560
    N128 --> N14
    N129 --> N514
    N129 --> N445
    N129 --> N560
    N130 --> N514
    N130 --> N445
    N130 --> N560
    N131 --> N514
    N131 --> N445
    N131 --> N560
    N132 --> N514
    N132 --> N445
    N132 --> N560
    N133 --> N416
    N133 --> N437
    N133 --> N445
    N133 --> N560
    N134 --> N514
    N134 --> N445
    N134 --> N560
    N135 --> N445
    N135 --> N560
    N135 --> N14
    N135 --> N13
    N136 --> N525
    N136 --> N445
    N136 --> N560
    N137 --> N445
    N137 --> N560
    N138 --> N445
    N138 --> N560
    N138 --> N14
    N140 --> N445
    N140 --> N560
    N141 --> N416
    N141 --> N437
    N141 --> N445
    N141 --> N560
    N142 --> N514
    N142 --> N445
    N142 --> N560
    N143 --> N416
    N143 --> N437
    N143 --> N514
    N143 --> N445
    N143 --> N560
    N144 --> N416
    N144 --> N437
    N144 --> N445
    N144 --> N560
    N144 --> N525
    N144 --> N14
    N145 --> N445
    N145 --> N560
    N146 --> N445
    N146 --> N560
    N146 --> N14
    N147 --> N445
    N147 --> N560
    N147 --> N14
    N148 --> N514
    N148 --> N445
    N148 --> N560
    N148 --> N14
    N149 --> N445
    N149 --> N560
    N149 --> N14
    N150 --> N445
    N150 --> N560
    N150 --> N14
    N151 --> N445
    N151 --> N560
    N152 --> N525
    N152 --> N445
    N152 --> N560
    N153 --> N445
    N153 --> N560
    N154 --> N445
    N154 --> N560
    N155 --> N445
    N155 --> N560
    N156 --> N445
    N156 --> N560
    N157 --> N514
    N157 --> N445
    N157 --> N560
    N158 --> N416
    N158 --> N437
    N158 --> N445
    N158 --> N560
    N159 --> N416
    N159 --> N437
    N159 --> N445
    N159 --> N560
    N159 --> N14
    N160 --> N416
    N160 --> N437
    N160 --> N355
    N160 --> N489
    N160 --> N445
    N160 --> N560
    N161 --> N445
    N161 --> N560
    N162 --> N445
    N162 --> N560
    N163 --> N416
    N163 --> N437
    N163 --> N445
    N163 --> N560
    N164 --> N445
    N164 --> N560
    N165 --> N445
    N165 --> N560
    N166 --> N416
    N166 --> N437
    N166 --> N445
    N166 --> N560
    N167 --> N445
    N167 --> N560
    N167 --> N14
    N168 --> N514
    N168 --> N445
    N168 --> N560
    N169 --> N416
    N169 --> N437
    N169 --> N445
    N169 --> N560
    N170 --> N445
    N170 --> N560
    N171 --> N514
    N171 --> N445
    N171 --> N560
    N172 --> N14
    N173 --> N416
    N173 --> N437
    N173 --> N445
    N173 --> N560
    N173 --> N395
    N173 --> N429
    N173 --> N9
    N173 --> N49
    N173 --> N336
    N173 --> N394
    N173 --> N413
    N173 --> N428
    N173 --> N483
    N173 --> N512
    N173 --> N11
    N173 --> N10
    N174 --> N445
    N174 --> N560
    N175 --> N445
    N175 --> N560
    N176 --> N416
    N176 --> N437
    N176 --> N525
    N176 --> N514
    N176 --> N445
    N176 --> N560
    N176 --> N14
    N177 --> N514
    N177 --> N445
    N177 --> N560
    N178 --> N416
    N178 --> N437
    N178 --> N14
    N179 --> N525
    N179 --> N445
    N179 --> N560
    N179 --> N14
    N179 --> N416
    N179 --> N437
    N180 --> N445
    N180 --> N560
    N180 --> N14
    N182 --> N416
    N182 --> N437
    N182 --> N445
    N182 --> N560
    N183 --> N445
    N183 --> N560
    N183 --> N14
    N184 --> N445
    N184 --> N560
    N185 --> N445
    N185 --> N560
    N185 --> N14
    N186 --> N14
    N189 --> N445
    N189 --> N560
    N190 --> N416
    N190 --> N437
    N190 --> N445
    N190 --> N560
    N191 --> N445
    N191 --> N560
    N192 --> N445
    N192 --> N560
    N192 --> N416
    N192 --> N437
    N193 --> N514
    N193 --> N445
    N193 --> N560
    N195 --> N445
    N195 --> N560
    N196 --> N445
    N196 --> N560
    N196 --> N14
    N197 --> N416
    N197 --> N437
    N197 --> N445
    N197 --> N560
    N197 --> N14
    N198 --> N445
    N198 --> N560
    N198 --> N14
    N199 --> N445
    N199 --> N560
    N200 --> N416
    N200 --> N437
    N200 --> N514
    N200 --> N445
    N200 --> N560
    N200 --> N14
    N201 --> N514
    N201 --> N445
    N201 --> N560
    N202 --> N514
    N202 --> N445
    N202 --> N560
    N203 --> N525
    N203 --> N514
    N203 --> N445
    N203 --> N560
    N204 --> N445
    N204 --> N560
    N205 --> N514
    N205 --> N445
    N205 --> N560
    N206 --> N514
    N206 --> N14
    N207 --> N514
    N207 --> N445
    N207 --> N560
    N207 --> N14
    N208 --> N445
    N208 --> N560
    N209 --> N445
    N209 --> N560
    N210 --> N514
    N210 --> N14
    N214 --> N416
    N214 --> N437
    N215 --> N525
    N215 --> N13
    N217 --> N14
    N218 --> N13
    N223 --> N14
    N224 --> N13
    N228 --> N14
    N230 --> N14
    N231 --> N525
    N237 --> N14
    N238 --> N14
    N239 --> N13
    N241 --> N416
    N241 --> N437
    N241 --> N14
    N243 --> N416
    N243 --> N437
    N243 --> N14
    N243 --> N525
    N244 --> N525
    N244 --> N13
    N250 --> N525
    N251 --> N514
    N251 --> N416
    N251 --> N437
    N252 --> N416
    N252 --> N437
    N253 --> N525
    N254 --> N416
    N254 --> N437
    N254 --> N13
    N254 --> N525
    N255 --> N14
    N257 --> N525
    N257 --> N13
    N259 --> N14
    N260 --> N525
    N261 --> N416
    N261 --> N437
    N262 --> N525
    N262 --> N13
    N263 --> N13
    N263 --> N445
    N263 --> N560
    N263 --> N525
    N266 --> N13
    N267 --> N416
    N267 --> N437
    N268 --> N514
    N269 --> N14
    N270 --> N13
    N271 --> N416
    N271 --> N437
    N271 --> N15
    N272 --> N525
    N273 --> N525
    N274 --> N416
    N274 --> N437
    N275 --> N525
    N279 --> N13
    N280 --> N13
    N281 --> N13
    N285 --> N362
    N285 --> N389
    N285 --> N405
    N285 --> N444
    N285 --> N497
    N285 --> N9
    N285 --> N49
    N285 --> N336
    N285 --> N394
    N285 --> N413
    N285 --> N428
    N285 --> N483
    N285 --> N512
    N286 --> N548
    N286 --> N565
    N286 --> N573
    N286 --> N581
    N286 --> N587
    N286 --> N287
    N286 --> N318
    N286 --> N320
    N286 --> N302
    N286 --> N285
    N286 --> N9
    N286 --> N49
    N286 --> N336
    N286 --> N394
    N286 --> N413
    N286 --> N428
    N286 --> N483
    N286 --> N512
    N286 --> N319
    N286 --> N317
    N287 --> N288
    N287 --> N9
    N287 --> N49
    N287 --> N336
    N287 --> N394
    N287 --> N413
    N287 --> N428
    N287 --> N483
    N287 --> N512
    N287 --> N285
    N287 --> N316
    N289 --> N304
    N289 --> N306
    N289 --> N305
    N290 --> N9
    N290 --> N49
    N290 --> N336
    N290 --> N394
    N290 --> N413
    N290 --> N428
    N290 --> N483
    N290 --> N512
    N292 --> N9
    N292 --> N49
    N292 --> N336
    N292 --> N394
    N292 --> N413
    N292 --> N428
    N292 --> N483
    N292 --> N512
    N293 --> N9
    N293 --> N49
    N293 --> N336
    N293 --> N394
    N293 --> N413
    N293 --> N428
    N293 --> N483
    N293 --> N512
    N294 --> N313
    N294 --> N9
    N294 --> N49
    N294 --> N336
    N294 --> N394
    N294 --> N413
    N294 --> N428
    N294 --> N483
    N294 --> N512
    N295 --> N9
    N295 --> N49
    N295 --> N336
    N295 --> N394
    N295 --> N413
    N295 --> N428
    N295 --> N483
    N295 --> N512
    N296 --> N285
    N296 --> N287
    N298 --> N9
    N298 --> N49
    N298 --> N336
    N298 --> N394
    N298 --> N413
    N298 --> N428
    N298 --> N483
    N298 --> N512
    N300 --> N285
    N300 --> N311
    N300 --> N308
    N301 --> N9
    N301 --> N49
    N301 --> N336
    N301 --> N394
    N301 --> N413
    N301 --> N428
    N301 --> N483
    N301 --> N512
    N302 --> N285
    N302 --> N296
    N302 --> N303
    N302 --> N300
    N302 --> N291
    N302 --> N313
    N302 --> N327
    N302 --> N322
    N302 --> N321
    N302 --> N324
    N302 --> N307
    N302 --> N298
    N303 --> N285
    N303 --> N9
    N303 --> N49
    N303 --> N336
    N303 --> N394
    N303 --> N413
    N303 --> N428
    N303 --> N483
    N303 --> N512
    N303 --> N308
    N307 --> N314
    N315 --> N9
    N315 --> N49
    N315 --> N336
    N315 --> N394
    N315 --> N413
    N315 --> N428
    N315 --> N483
    N315 --> N512
    N316 --> N9
    N316 --> N49
    N316 --> N336
    N316 --> N394
    N316 --> N413
    N316 --> N428
    N316 --> N483
    N316 --> N512
    N317 --> N9
    N317 --> N49
    N317 --> N336
    N317 --> N394
    N317 --> N413
    N317 --> N428
    N317 --> N483
    N317 --> N512
    N318 --> N9
    N318 --> N49
    N318 --> N336
    N318 --> N394
    N318 --> N413
    N318 --> N428
    N318 --> N483
    N318 --> N512
    N318 --> N287
    N319 --> N9
    N319 --> N49
    N319 --> N336
    N319 --> N394
    N319 --> N413
    N319 --> N428
    N319 --> N483
    N319 --> N512
    N320 --> N310
    N320 --> N9
    N320 --> N49
    N320 --> N336
    N320 --> N394
    N320 --> N413
    N320 --> N428
    N320 --> N483
    N320 --> N512
    N321 --> N362
    N321 --> N389
    N321 --> N405
    N321 --> N444
    N321 --> N497
    N321 --> N285
    N321 --> N310
    N321 --> N9
    N321 --> N49
    N321 --> N336
    N321 --> N394
    N321 --> N413
    N321 --> N428
    N321 --> N483
    N321 --> N512
    N322 --> N362
    N322 --> N389
    N322 --> N405
    N322 --> N444
    N322 --> N497
    N322 --> N310
    N322 --> N309
    N322 --> N9
    N322 --> N49
    N322 --> N336
    N322 --> N394
    N322 --> N413
    N322 --> N428
    N322 --> N483
    N322 --> N512
    N323 --> N9
    N323 --> N49
    N323 --> N336
    N323 --> N394
    N323 --> N413
    N323 --> N428
    N323 --> N483
    N323 --> N512
    N324 --> N362
    N324 --> N389
    N324 --> N405
    N324 --> N444
    N324 --> N497
    N324 --> N311
    N324 --> N310
    N324 --> N309
    N324 --> N9
    N324 --> N49
    N324 --> N336
    N324 --> N394
    N324 --> N413
    N324 --> N428
    N324 --> N483
    N324 --> N512
    N324 --> N294
    N324 --> N295
    N324 --> N292
    N324 --> N290
    N324 --> N293
    N325 --> N9
    N325 --> N49
    N325 --> N336
    N325 --> N394
    N325 --> N413
    N325 --> N428
    N325 --> N483
    N325 --> N512
    N325 --> N362
    N325 --> N389
    N325 --> N405
    N325 --> N444
    N325 --> N497
    N325 --> N285
    N325 --> N314
    N325 --> N311
    N325 --> N310
    N325 --> N309
    N325 --> N331
    N325 --> N335
    N325 --> N330
    N325 --> N329
    N325 --> N334
    N325 --> N333
    N325 --> N332
    N326 --> N312
    N326 --> N310
    N326 --> N9
    N326 --> N49
    N326 --> N336
    N326 --> N394
    N326 --> N413
    N326 --> N428
    N326 --> N483
    N326 --> N512
    N327 --> N362
    N327 --> N389
    N327 --> N405
    N327 --> N444
    N327 --> N497
    N327 --> N310
    N327 --> N309
    N327 --> N9
    N327 --> N49
    N327 --> N336
    N327 --> N394
    N327 --> N413
    N327 --> N428
    N327 --> N483
    N327 --> N512
    N327 --> N316
    N328 --> N9
    N328 --> N49
    N328 --> N336
    N328 --> N394
    N328 --> N413
    N328 --> N428
    N328 --> N483
    N328 --> N512
    N329 --> N309
    N329 --> N310
    N329 --> N332
    N330 --> N309
    N330 --> N310
    N330 --> N332
    N330 --> N9
    N330 --> N49
    N330 --> N336
    N330 --> N394
    N330 --> N413
    N330 --> N428
    N330 --> N483
    N330 --> N512
    N331 --> N309
    N333 --> N309
    N333 --> N310
    N334 --> N309
    N334 --> N310
    N335 --> N309
    N335 --> N310
    N340 --> N445
    N340 --> N560
    N342 --> N445
    N342 --> N560
    N344 --> N445
    N344 --> N560
    N345 --> N445
    N345 --> N560
    N347 --> N445
    N347 --> N560
    N348 --> N445
    N348 --> N560
    N349 --> N395
    N349 --> N429
    N349 --> N362
    N349 --> N389
    N349 --> N405
    N349 --> N444
    N349 --> N497
    N349 --> N445
    N349 --> N560
    N350 --> N445
    N350 --> N560
    N352 --> N514
    N353 --> N409
    N353 --> N395
    N353 --> N429
    N353 --> N445
    N353 --> N560
    N354 --> N445
    N354 --> N560
    N356 --> N445
    N356 --> N560
    N357 --> N416
    N357 --> N437
    N357 --> N362
    N357 --> N389
    N357 --> N405
    N357 --> N444
    N357 --> N497
    N357 --> N395
    N357 --> N429
    N357 --> N445
    N357 --> N560
    N358 --> N445
    N358 --> N560
    N362 --> N389
    N362 --> N405
    N362 --> N444
    N362 --> N497
    N362 --> N445
    N362 --> N560
    N363 --> N409
    N363 --> N445
    N363 --> N560
    N367 --> N395
    N367 --> N429
    N367 --> N445
    N367 --> N560
    N367 --> N525
    N368 --> N395
    N368 --> N429
    N368 --> N445
    N368 --> N560
    N376 --> N416
    N376 --> N437
    N376 --> N445
    N376 --> N560
    N377 --> N445
    N377 --> N560
    N378 --> N381
    N378 --> N577
    N378 --> N409
    N378 --> N445
    N378 --> N560
    N379 --> N445
    N379 --> N560
    N381 --> N445
    N381 --> N560
    N382 --> N445
    N382 --> N560
    N383 --> N445
    N383 --> N560
    N384 --> N362
    N384 --> N389
    N384 --> N405
    N384 --> N444
    N384 --> N497
    N384 --> N445
    N384 --> N560
    N384 --> N409
    N384 --> N395
    N384 --> N429
    N385 --> N409
    N385 --> N395
    N385 --> N429
    N385 --> N445
    N385 --> N560
    N388 --> N362
    N388 --> N389
    N388 --> N405
    N388 --> N444
    N388 --> N497
    N389 --> N556
    N389 --> N578
    N389 --> N388
    N390 --> N395
    N390 --> N429
    N390 --> N445
    N390 --> N560
    N392 --> N445
    N392 --> N560
    N393 --> N445
    N393 --> N560
    N394 --> N409
    N394 --> N445
    N394 --> N560
    N395 --> N429
    N395 --> N362
    N395 --> N389
    N395 --> N405
    N395 --> N444
    N395 --> N497
    N395 --> N445
    N395 --> N560
    N395 --> N409
    N396 --> N445
    N396 --> N560
    N397 --> N395
    N397 --> N429
    N397 --> N445
    N397 --> N560
    N397 --> N409
    N397 --> N425
    N398 --> N395
    N398 --> N429
    N398 --> N445
    N398 --> N560
    N399 --> N395
    N399 --> N429
    N399 --> N409
    N399 --> N445
    N399 --> N560
    N400 --> N395
    N400 --> N429
    N400 --> N409
    N400 --> N445
    N400 --> N560
    N401 --> N362
    N401 --> N389
    N401 --> N405
    N401 --> N444
    N401 --> N497
    N401 --> N409
    N401 --> N445
    N401 --> N560
    N401 --> N416
    N401 --> N437
    N402 --> N445
    N402 --> N560
    N402 --> N439
    N402 --> N409
    N403 --> N395
    N403 --> N429
    N403 --> N445
    N403 --> N560
    N404 --> N445
    N404 --> N560
    N405 --> N395
    N405 --> N429
    N405 --> N362
    N405 --> N389
    N405 --> N444
    N405 --> N497
    N405 --> N445
    N405 --> N560
    N405 --> N425
    N405 --> N416
    N405 --> N437
    N406 --> N362
    N406 --> N389
    N406 --> N405
    N406 --> N444
    N406 --> N497
    N406 --> N395
    N406 --> N429
    N406 --> N445
    N406 --> N560
    N407 --> N362
    N407 --> N389
    N407 --> N405
    N407 --> N444
    N407 --> N497
    N407 --> N445
    N407 --> N560
    N410 --> N445
    N410 --> N560
    N410 --> N409
    N411 --> N445
    N411 --> N560
    N411 --> N409
    N412 --> N362
    N412 --> N389
    N412 --> N405
    N412 --> N444
    N412 --> N497
    N412 --> N445
    N412 --> N560
    N412 --> N409
    N413 --> N409
    N413 --> N445
    N413 --> N560
    N414 --> N445
    N414 --> N560
    N415 --> N409
    N415 --> N445
    N415 --> N560
    N416 --> N409
    N416 --> N362
    N416 --> N389
    N416 --> N405
    N416 --> N444
    N416 --> N497
    N416 --> N445
    N416 --> N560
    N416 --> N395
    N416 --> N429
    N417 --> N416
    N417 --> N437
    N417 --> N409
    N417 --> N445
    N417 --> N560
    N418 --> N416
    N418 --> N437
    N418 --> N409
    N418 --> N445
    N418 --> N560
    N419 --> N445
    N419 --> N560
    N421 --> N395
    N421 --> N429
    N421 --> N445
    N421 --> N560
    N421 --> N425
    N421 --> N362
    N421 --> N389
    N421 --> N405
    N421 --> N444
    N421 --> N497
    N422 --> N409
    N422 --> N445
    N422 --> N560
    N423 --> N445
    N423 --> N560
    N424 --> N445
    N424 --> N560
    N425 --> N445
    N425 --> N560
    N426 --> N409
    N426 --> N362
    N426 --> N389
    N426 --> N405
    N426 --> N444
    N426 --> N497
    N426 --> N445
    N426 --> N560
    N427 --> N445
    N427 --> N560
    N428 --> N416
    N428 --> N437
    N428 --> N445
    N428 --> N560
    N429 --> N395
    N429 --> N445
    N429 --> N560
    N430 --> N445
    N430 --> N560
    N431 --> N445
    N431 --> N560
    N432 --> N409
    N432 --> N445
    N432 --> N560
    N433 --> N445
    N433 --> N560
    N434 --> N416
    N434 --> N437
    N434 --> N445
    N434 --> N560
    N435 --> N445
    N435 --> N560
    N436 --> N362
    N436 --> N389
    N436 --> N405
    N436 --> N444
    N436 --> N497
    N436 --> N445
    N436 --> N560
    N437 --> N362
    N437 --> N389
    N437 --> N405
    N437 --> N444
    N437 --> N497
    N437 --> N445
    N437 --> N560
    N437 --> N395
    N437 --> N429
    N438 --> N409
    N438 --> N362
    N438 --> N389
    N438 --> N405
    N438 --> N444
    N438 --> N497
    N438 --> N445
    N438 --> N560
    N439 --> N445
    N439 --> N560
    N439 --> N402
    N439 --> N409
    N440 --> N445
    N440 --> N560
    N441 --> N416
    N441 --> N437
    N441 --> N445
    N441 --> N560
    N442 --> N409
    N442 --> N395
    N442 --> N429
    N442 --> N445
    N442 --> N560
    N443 --> N416
    N443 --> N437
    N443 --> N445
    N443 --> N560
    N444 --> N409
    N444 --> N362
    N444 --> N389
    N444 --> N405
    N444 --> N497
    N444 --> N445
    N444 --> N560
    N445 --> N560
    N445 --> N362
    N445 --> N389
    N445 --> N405
    N445 --> N444
    N445 --> N497
    N446 --> N409
    N446 --> N362
    N446 --> N389
    N446 --> N405
    N446 --> N444
    N446 --> N497
    N446 --> N445
    N446 --> N560
    N447 --> N445
    N447 --> N560
    N447 --> N409
    N449 --> N416
    N449 --> N437
    N449 --> N445
    N449 --> N560
    N451 --> N409
    N451 --> N445
    N451 --> N560
    N452 --> N445
    N452 --> N560
    N452 --> N409
    N453 --> N445
    N453 --> N560
    N454 --> N395
    N454 --> N429
    N454 --> N409
    N454 --> N445
    N454 --> N560
    N455 --> N362
    N455 --> N389
    N455 --> N405
    N455 --> N444
    N455 --> N497
    N455 --> N395
    N455 --> N429
    N455 --> N445
    N455 --> N560
    N456 --> N445
    N456 --> N560
    N457 --> N445
    N457 --> N560
    N458 --> N445
    N458 --> N560
    N459 --> N395
    N459 --> N429
    N459 --> N409
    N459 --> N445
    N459 --> N560
    N459 --> N425
    N460 --> N395
    N460 --> N429
    N460 --> N445
    N460 --> N560
    N461 --> N395
    N461 --> N429
    N461 --> N445
    N461 --> N560
    N461 --> N409
    N461 --> N362
    N461 --> N389
    N461 --> N405
    N461 --> N444
    N461 --> N497
    N462 --> N362
    N462 --> N389
    N462 --> N405
    N462 --> N444
    N462 --> N497
    N462 --> N445
    N462 --> N560
    N464 --> N445
    N464 --> N560
    N466 --> N445
    N466 --> N560
    N466 --> N425
    N467 --> N445
    N467 --> N560
    N468 --> N445
    N468 --> N560
    N468 --> N409
    N468 --> N362
    N468 --> N389
    N468 --> N405
    N468 --> N444
    N468 --> N497
    N469 --> N445
    N469 --> N560
    N470 --> N362
    N470 --> N389
    N470 --> N405
    N470 --> N444
    N470 --> N497
    N470 --> N445
    N470 --> N560
    N471 --> N395
    N471 --> N429
    N471 --> N445
    N471 --> N560
    N472 --> N445
    N472 --> N560
    N473 --> N445
    N473 --> N560
    N474 --> N395
    N474 --> N429
    N474 --> N445
    N474 --> N560
    N475 --> N362
    N475 --> N389
    N475 --> N405
    N475 --> N444
    N475 --> N497
    N475 --> N445
    N475 --> N560
    N476 --> N395
    N476 --> N429
    N476 --> N409
    N476 --> N362
    N476 --> N389
    N476 --> N405
    N476 --> N444
    N476 --> N497
    N476 --> N445
    N476 --> N560
    N477 --> N445
    N477 --> N560
    N478 --> N445
    N478 --> N560
    N479 --> N445
    N479 --> N560
    N480 --> N445
    N480 --> N560
    N481 --> N445
    N481 --> N560
    N482 --> N409
    N482 --> N445
    N482 --> N560
    N483 --> N409
    N483 --> N445
    N483 --> N560
    N484 --> N445
    N484 --> N560
    N485 --> N445
    N485 --> N560
    N486 --> N416
    N486 --> N437
    N486 --> N445
    N486 --> N560
    N487 --> N381
    N487 --> N577
    N488 --> N395
    N488 --> N429
    N488 --> N445
    N488 --> N560
    N489 --> N416
    N489 --> N437
    N489 --> N381
    N489 --> N577
    N489 --> N445
    N489 --> N560
    N490 --> N381
    N490 --> N577
    N490 --> N416
    N490 --> N437
    N490 --> N445
    N490 --> N560
    N491 --> N362
    N491 --> N389
    N491 --> N405
    N491 --> N444
    N491 --> N497
    N491 --> N409
    N491 --> N445
    N491 --> N560
    N492 --> N445
    N492 --> N560
    N493 --> N445
    N493 --> N560
    N494 --> N409
    N495 --> N445
    N495 --> N560
    N496 --> N416
    N496 --> N437
    N496 --> N409
    N496 --> N362
    N496 --> N389
    N496 --> N405
    N496 --> N444
    N496 --> N497
    N496 --> N445
    N496 --> N560
    N497 --> N445
    N497 --> N560
    N498 --> N416
    N498 --> N437
    N498 --> N445
    N498 --> N560
    N499 --> N445
    N499 --> N560
    N500 --> N445
    N500 --> N560
    N500 --> N525
    N502 --> N445
    N502 --> N560
    N505 --> N445
    N505 --> N560
    N506 --> N371
    N506 --> N445
    N506 --> N560
    N508 --> N416
    N508 --> N437
    N508 --> N445
    N508 --> N560
    N510 --> N409
    N510 --> N445
    N510 --> N560
    N511 --> N445
    N511 --> N560
    N512 --> N525
    N512 --> N416
    N512 --> N437
    N512 --> N514
    N512 --> N445
    N512 --> N560
    N513 --> N445
    N513 --> N560
    N514 --> N381
    N514 --> N577
    N514 --> N445
    N514 --> N560
    N515 --> N525
    N515 --> N514
    N515 --> N409
    N515 --> N445
    N515 --> N560
    N516 --> N525
    N516 --> N514
    N516 --> N362
    N516 --> N389
    N516 --> N405
    N516 --> N444
    N516 --> N497
    N516 --> N445
    N516 --> N560
    N517 --> N525
    N517 --> N514
    N517 --> N409
    N517 --> N445
    N517 --> N560
    N518 --> N525
    N518 --> N445
    N518 --> N560
    N520 --> N362
    N520 --> N389
    N520 --> N405
    N520 --> N444
    N520 --> N497
    N520 --> N445
    N520 --> N560
    N523 --> N445
    N523 --> N560
    N524 --> N525
    N524 --> N514
    N524 --> N445
    N524 --> N560
    N526 --> N525
    N526 --> N527
    N527 --> N525
    N529 --> N514
    N529 --> N445
    N529 --> N560
    N531 --> N525
    N531 --> N409
    N532 --> N525
    N533 --> N525
    N534 --> N525
    N535 --> N525
    N535 --> N381
    N535 --> N577
    N535 --> N514
    N535 --> N445
    N535 --> N560
    N536 --> N525
    N536 --> N381
    N536 --> N577
    N536 --> N514
    N536 --> N445
    N536 --> N560
    N537 --> N525
    N537 --> N364
    N537 --> N498
    N538 --> N525
    N538 --> N381
    N538 --> N577
    N538 --> N514
    N538 --> N445
    N538 --> N560
    N538 --> N364
    N538 --> N498
    N539 --> N525
    N539 --> N514
    N539 --> N381
    N539 --> N577
    N539 --> N445
    N539 --> N560
    N539 --> N364
    N539 --> N498
    N540 --> N525
    N540 --> N514
    N540 --> N445
    N540 --> N560
    N541 --> N514
    N541 --> N362
    N541 --> N389
    N541 --> N405
    N541 --> N444
    N541 --> N497
    N542 --> N514
    N542 --> N445
    N542 --> N560
    N543 --> N514
    N545 --> N445
    N545 --> N560
    N546 --> N409
    N547 --> N525
    N547 --> N445
    N547 --> N560
    N548 --> N409
    N548 --> N445
    N548 --> N560
    N549 --> N409
    N550 --> N445
    N550 --> N560
    N551 --> N409
    N552 --> N395
    N552 --> N429
    N552 --> N445
    N552 --> N560
    N553 --> N445
    N553 --> N560
    N554 --> N395
    N554 --> N429
    N554 --> N409
    N554 --> N445
    N554 --> N560
    N555 --> N409
    N555 --> N445
    N555 --> N560
    N556 --> N514
    N557 --> N395
    N557 --> N429
    N558 --> N381
    N558 --> N577
    N558 --> N409
    N558 --> N445
    N558 --> N560
    N560 --> N381
    N560 --> N577
    N560 --> N514
    N560 --> N445
    N561 --> N395
    N561 --> N429
    N564 --> N445
    N564 --> N560
    N565 --> N525
    N565 --> N514
    N565 --> N362
    N565 --> N389
    N565 --> N405
    N565 --> N444
    N565 --> N497
    N565 --> N445
    N565 --> N560
    N565 --> N364
    N565 --> N498
    N566 --> N525
    N566 --> N514
    N566 --> N362
    N566 --> N389
    N566 --> N405
    N566 --> N444
    N566 --> N497
    N566 --> N445
    N566 --> N560
    N567 --> N525
    N567 --> N445
    N567 --> N560
    N568 --> N381
    N568 --> N577
    N568 --> N445
    N568 --> N560
    N568 --> N364
    N568 --> N498
    N569 --> N525
    N569 --> N381
    N569 --> N577
    N569 --> N514
    N569 --> N362
    N569 --> N389
    N569 --> N405
    N569 --> N444
    N569 --> N497
    N569 --> N445
    N569 --> N560
    N569 --> N364
    N569 --> N498
    N571 --> N445
    N571 --> N560
    N572 --> N381
    N572 --> N577
    N572 --> N445
    N572 --> N560
    N573 --> N525
    N573 --> N514
    N573 --> N409
    N573 --> N362
    N573 --> N389
    N573 --> N405
    N573 --> N444
    N573 --> N497
    N573 --> N445
    N573 --> N560
    N574 --> N381
    N574 --> N577
    N575 --> N445
    N575 --> N560
    N577 --> N525
    N578 --> N525
    N578 --> N514
    N578 --> N409
    N578 --> N445
    N578 --> N560
    N579 --> N525
    N579 --> N381
    N579 --> N577
    N579 --> N514
    N579 --> N409
    N579 --> N362
    N579 --> N389
    N579 --> N405
    N579 --> N444
    N579 --> N497
    N579 --> N445
    N579 --> N560
    N580 --> N409
    N581 --> N514
    N581 --> N409
    N581 --> N362
    N581 --> N389
    N581 --> N405
    N581 --> N444
    N581 --> N497
    N581 --> N445
    N581 --> N560
    N581 --> N364
    N581 --> N498
    N582 --> N514
    N582 --> N362
    N582 --> N389
    N582 --> N405
    N582 --> N444
    N582 --> N497
    N582 --> N445
    N582 --> N560
    N583 --> N445
    N583 --> N560
    N584 --> N381
    N584 --> N577
    N584 --> N445
    N584 --> N560
    N584 --> N364
    N584 --> N498
    N585 --> N381
    N585 --> N577
    N585 --> N514
    N585 --> N409
    N585 --> N362
    N585 --> N389
    N585 --> N405
    N585 --> N444
    N585 --> N497
    N585 --> N445
    N585 --> N560
    N585 --> N364
    N585 --> N498
    N587 --> N514
    N587 --> N362
    N587 --> N389
    N587 --> N405
    N587 --> N444
    N587 --> N497
    N587 --> N445
    N587 --> N560
    N587 --> N364
    N587 --> N498
    N588 --> N514
    N588 --> N362
    N588 --> N389
    N588 --> N405
    N588 --> N444
    N588 --> N497
    N588 --> N445
    N588 --> N560
    N589 --> N445
    N589 --> N560
    N590 --> N381
    N590 --> N577
    N590 --> N445
    N590 --> N560
    N590 --> N364
    N590 --> N498
    N591 --> N381
    N591 --> N577
    N591 --> N514
    N591 --> N362
    N591 --> N389
    N591 --> N405
    N591 --> N444
    N591 --> N497
    N591 --> N445
    N591 --> N560
    N591 --> N364
    N591 --> N498
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