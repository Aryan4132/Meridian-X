# Workspace Architecture & Component Map
Generated automatically by Meridian-X.

## Component Dependency Graph
```mermaid
graph TD
    N1["build_mobile.py []"]
    N2["build_standalone.py []"]
    N3["bump_version.py []"]
    N4["cleanup.py []"]
    N5["create_shortcut.py []"]
    N6["main.py []"]
    N7["setup_db.py []"]
    N8["setup_startup.py []"]
    N9["verify_system.py []"]
    N10["analyze_music_cues.py [.agents/skills/brag/scripts]"]
    N11["config.py [generated_repos/attention_is_all_you_need__transformer_]"]
    N12["dataset.py [generated_repos/attention_is_all_you_need__transformer_]"]
    N13["model.py [generated_repos/attention_is_all_you_need__transformer_]"]
    N14["trainer.py [generated_repos/attention_is_all_you_need__transformer_]"]
    N15["api.py [meridian_backend]"]
    N16["database.py [meridian_backend]"]
    N17["mobile_bridge_service.py [meridian_backend]"]
    N18["tests_run.py [meridian_backend]"]
    N19["ProfileHeader.tsx [meridian_backend/meridian_frontend/src/components]"]
    N20["__init__.py [meridian_backend/src]"]
    N21["automation.py [meridian_backend/src/api]"]
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
    N34["workspace.py [meridian_backend/src/api]"]
    N35["__init__.py [meridian_backend/src/api]"]
    N36["action_journal.py [meridian_backend/src/core]"]
    N37["agent_status_stream.py [meridian_backend/src/core]"]
    N38["ar_bridge.py [meridian_backend/src/core]"]
    N39["audit_logger.py [meridian_backend/src/core]"]
    N40["auth.py [meridian_backend/src/core]"]
    N41["behavior_monitor.py [meridian_backend/src/core]"]
    N42["boilerplate_genie.py [meridian_backend/src/core]"]
    N43["breach_sentinel.py [meridian_backend/src/core]"]
    N44["bus.py [meridian_backend/src/core]"]
    N45["camera_sentinel.py [meridian_backend/src/core]"]
    N46["checkpoints.py [meridian_backend/src/core]"]
    N47["clipboard.py [meridian_backend/src/core]"]
    N48["code_graph.py [meridian_backend/src/core]"]
    N49["cognitive_graph.py [meridian_backend/src/core]"]
    N50["commit_whisperer.py [meridian_backend/src/core]"]
    N51["config.py [meridian_backend/src/core]"]
    N52["confirmations.py [meridian_backend/src/core]"]
    N53["consensus_engine.py [meridian_backend/src/core]"]
    N54["deep_project_context.py [meridian_backend/src/core]"]
    N55["dev_automation.py [meridian_backend/src/core]"]
    N56["discord_bridge.py [meridian_backend/src/core]"]
    N57["discord_utils.py [meridian_backend/src/core]"]
    N58["doc_generator.py [meridian_backend/src/core]"]
    N59["doc_indexer.py [meridian_backend/src/core]"]
    N60["elevated_runner.py [meridian_backend/src/core]"]
    N61["emergency_lockdown.py [meridian_backend/src/core]"]
    N62["experiment_runner.py [meridian_backend/src/core]"]
    N63["explain_code_engine.py [meridian_backend/src/core]"]
    N64["exporter.py [meridian_backend/src/core]"]
    N65["fim_sentinel.py [meridian_backend/src/core]"]
    N66["gaze_tracker.py [meridian_backend/src/core]"]
    N67["governor.py [meridian_backend/src/core]"]
    N68["graph_rag.py [meridian_backend/src/core]"]
    N69["graph_sync.py [meridian_backend/src/core]"]
    N70["hardware_detector.py [meridian_backend/src/core]"]
    N71["history_manager.py [meridian_backend/src/core]"]
    N72["llm_auth.py [meridian_backend/src/core]"]
    N73["llm_client.py [meridian_backend/src/core]"]
    N74["llm_clients.py [meridian_backend/src/core]"]
    N75["llm_provider.py [meridian_backend/src/core]"]
    N76["local_model_manager.py [meridian_backend/src/core]"]
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
    N141["auto_reviewer.py [meridian_backend/src/tools]"]
    N142["bill_radar.py [meridian_backend/src/tools]"]
    N143["bookmark_manager.py [meridian_backend/src/tools]"]
    N144["browser_agent.py [meridian_backend/src/tools]"]
    N145["browser_use_agent.py [meridian_backend/src/tools]"]
    N146["cam_guard.py [meridian_backend/src/tools]"]
    N147["chrome_manager.py [meridian_backend/src/tools]"]
    N148["clipboard.py [meridian_backend/src/tools]"]
    N149["communication.py [meridian_backend/src/tools]"]
    N150["db_query.py [meridian_backend/src/tools]"]
    N151["desktop.py [meridian_backend/src/tools]"]
    N152["detonation_sandbox.py [meridian_backend/src/tools]"]
    N153["developer.py [meridian_backend/src/tools]"]
    N154["dns_shield.py [meridian_backend/src/tools]"]
    N155["documents.py [meridian_backend/src/tools]"]
    N156["documents_office.py [meridian_backend/src/tools]"]
    N157["documents_slides.py [meridian_backend/src/tools]"]
    N158["dynamic_manager.py [meridian_backend/src/tools]"]
    N159["expiry_sentinel.py [meridian_backend/src/tools]"]
    N160["exporter.py [meridian_backend/src/tools]"]
    N161["external_connectors.py [meridian_backend/src/tools]"]
    N162["filesystem.py [meridian_backend/src/tools]"]
    N163["file_janitor.py [meridian_backend/src/tools]"]
    N164["finance_sentinel.py [meridian_backend/src/tools]"]
    N165["geo_location.py [meridian_backend/src/tools]"]
    N166["health_ingest.py [meridian_backend/src/tools]"]
    N167["household.py [meridian_backend/src/tools]"]
    N168["knowledge.py [meridian_backend/src/tools]"]
    N169["learning_queue.py [meridian_backend/src/tools]"]
    N170["mcp_marketplace.py [meridian_backend/src/tools]"]
    N171["network_guardian.py [meridian_backend/src/tools]"]
    N172["networth_tracker.py [meridian_backend/src/tools]"]
    N173["ollama_manager.py [meridian_backend/src/tools]"]
    N174["papercoder.py [meridian_backend/src/tools]"]
    N175["password_auditor.py [meridian_backend/src/tools]"]
    N176["phishing_guard.py [meridian_backend/src/tools]"]
    N177["phone_agent.py [meridian_backend/src/tools]"]
    N178["price_watcher.py [meridian_backend/src/tools]"]
    N179["recording.py [meridian_backend/src/tools]"]
    N180["registry.py [meridian_backend/src/tools]"]
    N181["review.py [meridian_backend/src/tools]"]
    N182["scheduler.py [meridian_backend/src/tools]"]
    N183["screenshot_memory.py [meridian_backend/src/tools]"]
    N184["search_hub.py [meridian_backend/src/tools]"]
    N185["security_auditor.py [meridian_backend/src/tools]"]
    N186["shell.py [meridian_backend/src/tools]"]
    N187["system.py [meridian_backend/src/tools]"]
    N188["system_windows.py [meridian_backend/src/tools]"]
    N189["task_scheduler.py [meridian_backend/src/tools]"]
    N190["totp_generator.py [meridian_backend/src/tools]"]
    N191["travel_butler.py [meridian_backend/src/tools]"]
    N192["usb_watchdog.py [meridian_backend/src/tools]"]
    N193["vault.py [meridian_backend/src/tools]"]
    N194["video_editor.py [meridian_backend/src/tools]"]
    N195["voice.py [meridian_backend/src/tools]"]
    N196["watcher.py [meridian_backend/src/tools]"]
    N197["web.py [meridian_backend/src/tools]"]
    N198["web_browser.py [meridian_backend/src/tools]"]
    N199["web_scraper.py [meridian_backend/src/tools]"]
    N200["wellness.py [meridian_backend/src/tools]"]
    N201["whatsapp_manager.py [meridian_backend/src/tools]"]
    N202["wifi_assessor.py [meridian_backend/src/tools]"]
    N203["workspace_layout.py [meridian_backend/src/tools]"]
    N204["ambient_listener.py [meridian_backend/src/voice]"]
    N205["duplex.py [meridian_backend/src/voice]"]
    N206["polyglot.py [meridian_backend/src/voice]"]
    N207["stt.py [meridian_backend/src/voice]"]
    N208["tts.py [meridian_backend/src/voice]"]
    N209["voice_biometrics.py [meridian_backend/src/voice]"]
    N210["wakeword.py [meridian_backend/src/voice]"]
    N211["conftest.py [meridian_backend/tests]"]
    N212["run_tests.py [meridian_backend/tests]"]
    N213["test_advanced_proactive.py [meridian_backend/tests]"]
    N214["test_auto_bug_fixer.py [meridian_backend/tests]"]
    N215["test_backend_improvements.py [meridian_backend/tests]"]
    N216["test_backlog_features.py [meridian_backend/tests]"]
    N217["test_backlog_sprint.py [meridian_backend/tests]"]
    N218["test_bridges.py [meridian_backend/tests]"]
    N219["test_browser_agent.py [meridian_backend/tests]"]
    N220["test_browser_fallback.py [meridian_backend/tests]"]
    N221["test_browser_use.py [meridian_backend/tests]"]
    N222["test_butler_media.py [meridian_backend/tests]"]
    N223["test_chat_abort.py [meridian_backend/tests]"]
    N224["test_cognitive_graph.py [meridian_backend/tests]"]
    N225["test_config.py [meridian_backend/tests]"]
    N226["test_consensus_gate.py [meridian_backend/tests]"]
    N227["test_context_budget.py [meridian_backend/tests]"]
    N228["test_custom_password_auth.py [meridian_backend/tests]"]
    N229["test_database.py [meridian_backend/tests]"]
    N230["test_day10_features.py [meridian_backend/tests]"]
    N231["test_day11_features.py [meridian_backend/tests]"]
    N232["test_day12_features.py [meridian_backend/tests]"]
    N233["test_day13_features.py [meridian_backend/tests]"]
    N234["test_day14_day15_features.py [meridian_backend/tests]"]
    N235["test_day16_17_18_features.py [meridian_backend/tests]"]
    N236["test_day3_features.py [meridian_backend/tests]"]
    N237["test_day4_features.py [meridian_backend/tests]"]
    N238["test_day5_features.py [meridian_backend/tests]"]
    N239["test_day6_features.py [meridian_backend/tests]"]
    N240["test_day7_features.py [meridian_backend/tests]"]
    N241["test_day8_features.py [meridian_backend/tests]"]
    N242["test_day9_features.py [meridian_backend/tests]"]
    N243["test_dev_intelligence_suite.py [meridian_backend/tests]"]
    N244["test_document_tools.py [meridian_backend/tests]"]
    N245["test_full_proactive_suite.py [meridian_backend/tests]"]
    N246["test_geo_location.py [meridian_backend/tests]"]
    N247["test_jarvis_perception.py [meridian_backend/tests]"]
    N248["test_known_errors_remediation.py [meridian_backend/tests]"]
    N249["test_llm_provider.py [meridian_backend/tests]"]
    N250["test_logging.py [meridian_backend/tests]"]
    N251["test_loop_parser.py [meridian_backend/tests]"]
    N252["test_loop_submodules.py [meridian_backend/tests]"]
    N253["test_mobile_websocket.py [meridian_backend/tests]"]
    N254["test_model_source.py [meridian_backend/tests]"]
    N255["test_multi_os.py [meridian_backend/tests]"]
    N256["test_new_features.py [meridian_backend/tests]"]
    N257["test_oauth.py [meridian_backend/tests]"]
    N258["test_p2p.py [meridian_backend/tests]"]
    N259["test_proactive.py [meridian_backend/tests]"]
    N260["test_proactive_mode.py [meridian_backend/tests]"]
    N261["test_proactive_notifications.py [meridian_backend/tests]"]
    N262["test_security_features.py [meridian_backend/tests]"]
    N263["test_skill_packs.py [meridian_backend/tests]"]
    N264["test_sprint2_features.py [meridian_backend/tests]"]
    N265["test_standalone_bridge.py [meridian_backend/tests]"]
    N266["test_stream_resiliency.py [meridian_backend/tests]"]
    N267["test_swarm.py [meridian_backend/tests]"]
    N268["test_tools.py [meridian_backend/tests]"]
    N269["test_tool_regression.py [meridian_backend/tests]"]
    N270["test_vault.py [meridian_backend/tests]"]
    N271["test_video_editor.py [meridian_backend/tests]"]
    N272["test_voice_speed.py [meridian_backend/tests]"]
    N273["test_wakeword_continuous.py [meridian_backend/tests]"]
    N274["test_wakeword_onnx.py [meridian_backend/tests]"]
    N275["test_web_guards.py [meridian_backend/tests]"]
    N276["test_workflow.py [meridian_backend/tests]"]
    N277["vite.config.ts [meridian_frontend]"]
    N278["AppContext.tsx [meridian_frontend/src]"]
    N279["main.tsx [meridian_frontend/src]"]
    N280["Mascot.tsx [meridian_frontend/src]"]
    N281["Mascot3DCharacter.tsx [meridian_frontend/src]"]
    N282["MobileApp.tsx [meridian_frontend/src]"]
    N283["AgentStatusStream.tsx [meridian_frontend/src/components]"]
    N284["CommandPalette.tsx [meridian_frontend/src/components]"]
    N285["DevAutomationPanel.tsx [meridian_frontend/src/components]"]
    N286["DeveloperSuitePanel.tsx [meridian_frontend/src/components]"]
    N287["LocalModelManager.tsx [meridian_frontend/src/components]"]
    N288["MemoryConsolidationView.tsx [meridian_frontend/src/components]"]
    N289["NavRail.tsx [meridian_frontend/src/components]"]
    N290["PerceptionHUD.tsx [meridian_frontend/src/components]"]
    N291["ProactiveGuardBanner.tsx [meridian_frontend/src/components]"]
    N292["ProfileHeader.tsx [meridian_frontend/src/components]"]
    N293["RightDrawer.tsx [meridian_frontend/src/components]"]
    N294["ServerConnectionModal.tsx [meridian_frontend/src/components]"]
    N295["Shell.tsx [meridian_frontend/src/components]"]
    N296["StatusBar.tsx [meridian_frontend/src/components]"]
    N297["DropdownNav.tsx [meridian_frontend/src/components/mobile]"]
    N298["LiveThoughtCarousel.tsx [meridian_frontend/src/components/mobile]"]
    N299["VoiceOrbHUD.tsx [meridian_frontend/src/components/mobile]"]
    N300["AmbientParticles.tsx [meridian_frontend/src/components/ui]"]
    N301["DataBadge.tsx [meridian_frontend/src/components/ui]"]
    N302["GlowCard.tsx [meridian_frontend/src/components/ui]"]
    N303["HoloButton.tsx [meridian_frontend/src/components/ui]"]
    N304["ProgressArc.tsx [meridian_frontend/src/components/ui]"]
    N305["TerminalLine.tsx [meridian_frontend/src/components/ui]"]
    N306["ToastContext.tsx [meridian_frontend/src/components/ui]"]
    N307["useMemoryOptimizer.ts [meridian_frontend/src/hooks]"]
    N308["oauthService.ts [meridian_frontend/src/services]"]
    N309["streamingAudioPlayer.ts [meridian_frontend/src/services]"]
    N310["BackendSetup.tsx [meridian_frontend/src/startup]"]
    N311["BootSequence.tsx [meridian_frontend/src/startup]"]
    N312["OnboardingWizard.tsx [meridian_frontend/src/startup]"]
    N313["SetupWizard.tsx [meridian_frontend/src/startup]"]
    N314["Clipboard.tsx [meridian_frontend/src/views]"]
    N315["Jobs.tsx [meridian_frontend/src/views]"]
    N316["MemoryEditor.tsx [meridian_frontend/src/views]"]
    N317["Productivity.tsx [meridian_frontend/src/views]"]
    N318["Settings.tsx [meridian_frontend/src/views]"]
    N319["SwarmDebate.tsx [meridian_frontend/src/views]"]
    N320["Timeline.tsx [meridian_frontend/src/views]"]
    N321["WorkflowBuilder.tsx [meridian_frontend/src/views]"]
    N322["config.py [meridian_frontend/src-tauri/api/_internal/cv2]"]
    N323["load_config_py3.py [meridian_frontend/src-tauri/api/_internal/cv2]"]
    N324["__init__.py [meridian_frontend/src-tauri/api/_internal/cv2]"]
    N325["__init__.py [meridian_frontend/src-tauri/api/_internal/cv2/data]"]
    N326["__init__.py [meridian_frontend/src-tauri/api/_internal/cv2/mat_wrapper]"]
    N327["version.py [meridian_frontend/src-tauri/api/_internal/cv2/misc]"]
    N328["__init__.py [meridian_frontend/src-tauri/api/_internal/cv2/typing]"]
    N329["__init__.py [meridian_frontend/src-tauri/api/_internal/cv2/utils]"]
    N330["applications.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N331["background.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N332["cli.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N333["concurrency.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N334["datastructures.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N335["encoders.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N336["exceptions.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N337["exception_handlers.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N338["logger.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N339["params.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N340["param_functions.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N341["requests.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N342["responses.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N343["routing.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N344["sse.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N345["staticfiles.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N346["templating.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N347["testclient.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N348["types.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N349["utils.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N350["websockets.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N351["__init__.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N352["__main__.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N353["models.py [meridian_frontend/src-tauri/api/_internal/fastapi/dependencies]"]
    N354["utils.py [meridian_frontend/src-tauri/api/_internal/fastapi/dependencies]"]
    N355["asyncexitstack.py [meridian_frontend/src-tauri/api/_internal/fastapi/middleware]"]
    N356["cors.py [meridian_frontend/src-tauri/api/_internal/fastapi/middleware]"]
    N357["gzip.py [meridian_frontend/src-tauri/api/_internal/fastapi/middleware]"]
    N358["httpsredirect.py [meridian_frontend/src-tauri/api/_internal/fastapi/middleware]"]
    N359["trustedhost.py [meridian_frontend/src-tauri/api/_internal/fastapi/middleware]"]
    N360["wsgi.py [meridian_frontend/src-tauri/api/_internal/fastapi/middleware]"]
    N361["__init__.py [meridian_frontend/src-tauri/api/_internal/fastapi/middleware]"]
    N362["docs.py [meridian_frontend/src-tauri/api/_internal/fastapi/openapi]"]
    N363["models.py [meridian_frontend/src-tauri/api/_internal/fastapi/openapi]"]
    N364["utils.py [meridian_frontend/src-tauri/api/_internal/fastapi/openapi]"]
    N365["api_key.py [meridian_frontend/src-tauri/api/_internal/fastapi/security]"]
    N366["base.py [meridian_frontend/src-tauri/api/_internal/fastapi/security]"]
    N367["http.py [meridian_frontend/src-tauri/api/_internal/fastapi/security]"]
    N368["oauth2.py [meridian_frontend/src-tauri/api/_internal/fastapi/security]"]
    N369["open_id_connect_url.py [meridian_frontend/src-tauri/api/_internal/fastapi/security]"]
    N370["shared.py [meridian_frontend/src-tauri/api/_internal/fastapi/_compat]"]
    N371["v2.py [meridian_frontend/src-tauri/api/_internal/fastapi/_compat]"]
    N372["coreBundle.js [meridian_frontend/src-tauri/api/_internal/playwright/driver/package/lib]"]
    N373["utilsBundle.js [meridian_frontend/src-tauri/api/_internal/playwright/driver/package/lib]"]
    N374["structs.d.ts [meridian_frontend/src-tauri/api/_internal/playwright/driver/package/types]"]
    N375["types.d.ts [meridian_frontend/src-tauri/api/_internal/playwright/driver/package/types]"]
    N376["aliases.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N377["alias_generators.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N378["annotated_handlers.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N379["color.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N380["config.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N381["dataclasses.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N382["errors.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N383["fields.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N384["functional_serializers.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N385["functional_validators.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N386["json_schema.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N387["main.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N388["mypy.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N389["networks.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N390["root_model.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N391["types.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N392["type_adapter.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N393["validate_call_decorator.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N394["version.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N395["warnings.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N396["_migration.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N397["__init__.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N398["class_validators.py [meridian_frontend/src-tauri/api/_internal/pydantic/deprecated]"]
    N399["config.py [meridian_frontend/src-tauri/api/_internal/pydantic/deprecated]"]
    N400["copy_internals.py [meridian_frontend/src-tauri/api/_internal/pydantic/deprecated]"]
    N401["decorator.py [meridian_frontend/src-tauri/api/_internal/pydantic/deprecated]"]
    N402["json.py [meridian_frontend/src-tauri/api/_internal/pydantic/deprecated]"]
    N403["parse.py [meridian_frontend/src-tauri/api/_internal/pydantic/deprecated]"]
    N404["tools.py [meridian_frontend/src-tauri/api/_internal/pydantic/deprecated]"]
    N405["arguments_schema.py [meridian_frontend/src-tauri/api/_internal/pydantic/experimental]"]
    N406["missing_sentinel.py [meridian_frontend/src-tauri/api/_internal/pydantic/experimental]"]
    N407["pipeline.py [meridian_frontend/src-tauri/api/_internal/pydantic/experimental]"]
    N408["_loader.py [meridian_frontend/src-tauri/api/_internal/pydantic/plugin]"]
    N409["_schema_validator.py [meridian_frontend/src-tauri/api/_internal/pydantic/plugin]"]
    N410["__init__.py [meridian_frontend/src-tauri/api/_internal/pydantic/plugin]"]
    N411["annotated_types.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N412["class_validators.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N413["color.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N414["config.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N415["dataclasses.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N416["datetime_parse.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N417["decorator.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N418["env_settings.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N419["errors.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N420["error_wrappers.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N421["fields.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N422["generics.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N423["json.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N424["main.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N425["mypy.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N426["networks.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N427["parse.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N428["schema.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N429["tools.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N430["types.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N431["typing.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N432["utils.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N433["validators.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N434["version.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N435["_hypothesis_plugin.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N436["__init__.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N437["_config.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N438["_core_metadata.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N439["_core_utils.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N440["_dataclasses.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N441["_decorators.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N442["_decorators_v1.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N443["_discriminated_union.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N444["_docs_extraction.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N445["_fields.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N446["_forward_ref.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N447["_generate_schema.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N448["_generics.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N449["_git.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N450["_import_utils.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N451["_internal_dataclass.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N452["_known_annotated_metadata.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N453["_mock_val_ser.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N454["_model_construction.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N455["_namespace_utils.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N456["_repr.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N457["_schema_gather.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N458["_schema_generation_shared.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N459["_serializers.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N460["_signature.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N461["_typing_extra.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N462["_utils.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N463["_validate_call.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N464["_validators.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N465["applications.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N466["authentication.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N467["background.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N468["concurrency.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N469["config.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N470["convertors.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N471["datastructures.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N472["endpoints.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N473["exceptions.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N474["formparsers.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N475["requests.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N476["responses.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N477["routing.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N478["schemas.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N479["staticfiles.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N480["status.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N481["templating.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N482["testclient.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N483["types.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N484["websockets.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N485["_exception_handler.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N486["_utils.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N487["authentication.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N488["base.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N489["cors.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N490["errors.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N491["exceptions.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N492["gzip.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N493["httpsredirect.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N494["sessions.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N495["trustedhost.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N496["wsgi.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N497["__init__.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N498["config.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N499["importer.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N500["logging.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N501["main.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N502["server.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N503["workers.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N504["_compat.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N505["_subprocess.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N506["_types.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N507["__init__.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N508["__main__.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N509["off.py [meridian_frontend/src-tauri/api/_internal/uvicorn/lifespan]"]
    N510["on.py [meridian_frontend/src-tauri/api/_internal/uvicorn/lifespan]"]
    N511["asyncio.py [meridian_frontend/src-tauri/api/_internal/uvicorn/loops]"]
    N512["auto.py [meridian_frontend/src-tauri/api/_internal/uvicorn/loops]"]
    N513["uvloop.py [meridian_frontend/src-tauri/api/_internal/uvicorn/loops]"]
    N514["asgi2.py [meridian_frontend/src-tauri/api/_internal/uvicorn/middleware]"]
    N515["message_logger.py [meridian_frontend/src-tauri/api/_internal/uvicorn/middleware]"]
    N516["proxy_headers.py [meridian_frontend/src-tauri/api/_internal/uvicorn/middleware]"]
    N517["wsgi.py [meridian_frontend/src-tauri/api/_internal/uvicorn/middleware]"]
    N518["utils.py [meridian_frontend/src-tauri/api/_internal/uvicorn/protocols]"]
    N519["auto.py [meridian_frontend/src-tauri/api/_internal/uvicorn/protocols/http]"]
    N520["flow_control.py [meridian_frontend/src-tauri/api/_internal/uvicorn/protocols/http]"]
    N521["h11_impl.py [meridian_frontend/src-tauri/api/_internal/uvicorn/protocols/http]"]
    N522["httptools_impl.py [meridian_frontend/src-tauri/api/_internal/uvicorn/protocols/http]"]
    N523["auto.py [meridian_frontend/src-tauri/api/_internal/uvicorn/protocols/websockets]"]
    N524["websockets_impl.py [meridian_frontend/src-tauri/api/_internal/uvicorn/protocols/websockets]"]
    N525["websockets_sansio_impl.py [meridian_frontend/src-tauri/api/_internal/uvicorn/protocols/websockets]"]
    N526["wsproto_impl.py [meridian_frontend/src-tauri/api/_internal/uvicorn/protocols/websockets]"]
    N527["basereload.py [meridian_frontend/src-tauri/api/_internal/uvicorn/supervisors]"]
    N528["multiprocess.py [meridian_frontend/src-tauri/api/_internal/uvicorn/supervisors]"]
    N529["statreload.py [meridian_frontend/src-tauri/api/_internal/uvicorn/supervisors]"]
    N530["watchfilesreload.py [meridian_frontend/src-tauri/api/_internal/uvicorn/supervisors]"]
    N531["__init__.py [meridian_frontend/src-tauri/api/_internal/uvicorn/supervisors]"]
    N532["auth.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N533["cli.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N534["client.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N535["connection.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N536["datastructures.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N537["exceptions.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N538["frames.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N539["headers.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N540["http11.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N541["imports.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N542["protocol.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N543["proxy.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N544["server.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N545["streams.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N546["typing.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N547["uri.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N548["utils.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N549["version.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N550["__init__.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N551["client.py [meridian_frontend/src-tauri/api/_internal/websockets/asyncio]"]
    N552["connection.py [meridian_frontend/src-tauri/api/_internal/websockets/asyncio]"]
    N553["messages.py [meridian_frontend/src-tauri/api/_internal/websockets/asyncio]"]
    N554["router.py [meridian_frontend/src-tauri/api/_internal/websockets/asyncio]"]
    N555["server.py [meridian_frontend/src-tauri/api/_internal/websockets/asyncio]"]
    N556["base.py [meridian_frontend/src-tauri/api/_internal/websockets/extensions]"]
    N557["permessage_deflate.py [meridian_frontend/src-tauri/api/_internal/websockets/extensions]"]
    N558["auth.py [meridian_frontend/src-tauri/api/_internal/websockets/legacy]"]
    N559["client.py [meridian_frontend/src-tauri/api/_internal/websockets/legacy]"]
    N560["exceptions.py [meridian_frontend/src-tauri/api/_internal/websockets/legacy]"]
    N561["framing.py [meridian_frontend/src-tauri/api/_internal/websockets/legacy]"]
    N562["handshake.py [meridian_frontend/src-tauri/api/_internal/websockets/legacy]"]
    N563["http.py [meridian_frontend/src-tauri/api/_internal/websockets/legacy]"]
    N564["protocol.py [meridian_frontend/src-tauri/api/_internal/websockets/legacy]"]
    N565["server.py [meridian_frontend/src-tauri/api/_internal/websockets/legacy]"]
    N566["__init__.py [meridian_frontend/src-tauri/api/_internal/websockets/legacy]"]
    N567["client.py [meridian_frontend/src-tauri/api/_internal/websockets/sync]"]
    N568["connection.py [meridian_frontend/src-tauri/api/_internal/websockets/sync]"]
    N569["messages.py [meridian_frontend/src-tauri/api/_internal/websockets/sync]"]
    N570["router.py [meridian_frontend/src-tauri/api/_internal/websockets/sync]"]
    N571["server.py [meridian_frontend/src-tauri/api/_internal/websockets/sync]"]
    N572["utils.py [meridian_frontend/src-tauri/api/_internal/websockets/sync]"]
    N573["client.py [meridian_frontend/src-tauri/api/_internal/websockets/trio]"]
    N574["connection.py [meridian_frontend/src-tauri/api/_internal/websockets/trio]"]
    N575["messages.py [meridian_frontend/src-tauri/api/_internal/websockets/trio]"]
    N576["router.py [meridian_frontend/src-tauri/api/_internal/websockets/trio]"]
    N577["server.py [meridian_frontend/src-tauri/api/_internal/websockets/trio]"]
    N578["utils.py [meridian_frontend/src-tauri/api/_internal/websockets/trio]"]
    N579["build_apk.py [meridian_mobile]"]
    N580["flutter_lldb_helper.py [meridian_mobile/ios/Flutter/ephemeral]"]
    N581["get_system_platform_info.py [plugins]"]

    N1 --> N402
    N1 --> N423
    N1 --> N431
    N1 --> N546
    N2 --> N402
    N2 --> N423
    N2 --> N431
    N2 --> N546
    N3 --> N402
    N3 --> N423
    N6 --> N511
    N6 --> N402
    N6 --> N423
    N6 --> N15
    N10 --> N402
    N10 --> N423
    N10 --> N431
    N10 --> N546
    N11 --> N381
    N11 --> N415
    N14 --> N11
    N14 --> N51
    N14 --> N322
    N14 --> N380
    N14 --> N399
    N14 --> N414
    N14 --> N469
    N14 --> N498
    N14 --> N13
    N14 --> N12
    N15 --> N402
    N15 --> N423
    N15 --> N500
    N15 --> N511
    N15 --> N431
    N15 --> N546
    N15 --> N16
    N16 --> N402
    N16 --> N423
    N16 --> N431
    N16 --> N546
    N17 --> N402
    N17 --> N423
    N17 --> N511
    N17 --> N500
    N17 --> N431
    N17 --> N546
    N21 --> N402
    N21 --> N423
    N21 --> N431
    N21 --> N546
    N21 --> N16
    N22 --> N402
    N22 --> N423
    N22 --> N511
    N22 --> N431
    N22 --> N546
    N22 --> N16
    N23 --> N402
    N23 --> N423
    N23 --> N500
    N23 --> N431
    N23 --> N546
    N23 --> N16
    N24 --> N402
    N24 --> N423
    N24 --> N431
    N24 --> N546
    N25 --> N402
    N25 --> N423
    N25 --> N431
    N25 --> N546
    N25 --> N16
    N26 --> N431
    N26 --> N546
    N27 --> N431
    N27 --> N546
    N27 --> N16
    N28 --> N431
    N28 --> N546
    N28 --> N16
    N29 --> N402
    N29 --> N423
    N29 --> N431
    N29 --> N546
    N29 --> N16
    N30 --> N402
    N30 --> N423
    N30 --> N431
    N30 --> N546
    N30 --> N16
    N31 --> N431
    N31 --> N546
    N31 --> N16
    N31 --> N511
    N32 --> N431
    N32 --> N546
    N33 --> N431
    N33 --> N546
    N34 --> N402
    N34 --> N423
    N34 --> N431
    N34 --> N546
    N34 --> N16
    N36 --> N402
    N36 --> N423
    N36 --> N500
    N36 --> N431
    N36 --> N546
    N36 --> N16
    N37 --> N511
    N37 --> N500
    N37 --> N431
    N37 --> N546
    N38 --> N500
    N38 --> N431
    N38 --> N546
    N39 --> N402
    N39 --> N423
    N39 --> N500
    N40 --> N431
    N40 --> N546
    N40 --> N402
    N40 --> N423
    N41 --> N500
    N41 --> N431
    N41 --> N546
    N42 --> N500
    N42 --> N431
    N42 --> N546
    N43 --> N500
    N43 --> N431
    N43 --> N546
    N43 --> N402
    N43 --> N423
    N44 --> N511
    N44 --> N431
    N44 --> N546
    N45 --> N500
    N45 --> N431
    N45 --> N546
    N46 --> N511
    N46 --> N431
    N46 --> N546
    N47 --> N431
    N47 --> N546
    N47 --> N16
    N48 --> N431
    N48 --> N546
    N49 --> N402
    N49 --> N423
    N49 --> N500
    N49 --> N431
    N49 --> N546
    N50 --> N500
    N50 --> N431
    N50 --> N546
    N52 --> N511
    N52 --> N431
    N52 --> N546
    N52 --> N16
    N53 --> N402
    N53 --> N423
    N53 --> N500
    N53 --> N431
    N53 --> N546
    N53 --> N511
    N53 --> N16
    N54 --> N500
    N54 --> N431
    N54 --> N546
    N55 --> N511
    N55 --> N500
    N55 --> N431
    N55 --> N546
    N56 --> N511
    N56 --> N431
    N56 --> N546
    N56 --> N16
    N57 --> N431
    N57 --> N546
    N59 --> N402
    N59 --> N423
    N59 --> N500
    N59 --> N431
    N59 --> N546
    N59 --> N16
    N60 --> N500
    N60 --> N431
    N60 --> N546
    N61 --> N500
    N61 --> N431
    N61 --> N546
    N62 --> N500
    N62 --> N431
    N62 --> N546
    N63 --> N500
    N63 --> N431
    N63 --> N546
    N64 --> N431
    N64 --> N546
    N64 --> N16
    N65 --> N500
    N65 --> N431
    N65 --> N546
    N66 --> N500
    N66 --> N431
    N66 --> N546
    N67 --> N431
    N67 --> N546
    N68 --> N402
    N68 --> N423
    N68 --> N431
    N68 --> N546
    N69 --> N402
    N69 --> N423
    N69 --> N431
    N69 --> N546
    N70 --> N500
    N70 --> N431
    N70 --> N546
    N70 --> N395
    N70 --> N402
    N70 --> N423
    N72 --> N500
    N72 --> N431
    N72 --> N546
    N72 --> N16
    N73 --> N511
    N73 --> N500
    N73 --> N431
    N73 --> N546
    N73 --> N16
    N74 --> N431
    N74 --> N546
    N74 --> N16
    N75 --> N402
    N75 --> N423
    N75 --> N500
    N75 --> N511
    N75 --> N431
    N75 --> N546
    N75 --> N16
    N76 --> N500
    N76 --> N511
    N76 --> N431
    N76 --> N546
    N76 --> N16
    N76 --> N402
    N76 --> N423
    N77 --> N500
    N77 --> N402
    N77 --> N423
    N78 --> N402
    N78 --> N423
    N78 --> N511
    N78 --> N431
    N78 --> N546
    N78 --> N16
    N79 --> N402
    N79 --> N423
    N79 --> N511
    N79 --> N431
    N79 --> N546
    N79 --> N16
    N80 --> N402
    N80 --> N423
    N80 --> N431
    N80 --> N546
    N80 --> N16
    N81 --> N402
    N81 --> N423
    N81 --> N511
    N81 --> N431
    N81 --> N546
    N81 --> N16
    N82 --> N402
    N82 --> N423
    N82 --> N511
    N82 --> N431
    N82 --> N546
    N82 --> N16
    N83 --> N402
    N83 --> N423
    N83 --> N511
    N83 --> N431
    N83 --> N546
    N83 --> N16
    N84 --> N402
    N84 --> N423
    N84 --> N511
    N84 --> N431
    N84 --> N546
    N85 --> N500
    N85 --> N431
    N85 --> N546
    N86 --> N402
    N86 --> N423
    N86 --> N511
    N86 --> N500
    N86 --> N431
    N86 --> N546
    N87 --> N511
    N87 --> N402
    N87 --> N423
    N87 --> N500
    N87 --> N431
    N87 --> N546
    N88 --> N402
    N88 --> N423
    N88 --> N431
    N88 --> N546
    N89 --> N500
    N89 --> N511
    N89 --> N402
    N89 --> N423
    N89 --> N431
    N89 --> N546
    N89 --> N16
    N90 --> N402
    N90 --> N423
    N90 --> N431
    N90 --> N546
    N90 --> N16
    N91 --> N402
    N91 --> N423
    N91 --> N500
    N91 --> N431
    N91 --> N546
    N91 --> N16
    N91 --> N511
    N92 --> N431
    N92 --> N546
    N92 --> N16
    N92 --> N402
    N92 --> N423
    N93 --> N431
    N93 --> N546
    N94 --> N402
    N94 --> N423
    N94 --> N431
    N94 --> N546
    N95 --> N500
    N95 --> N511
    N95 --> N431
    N95 --> N546
    N95 --> N402
    N95 --> N423
    N96 --> N402
    N96 --> N423
    N96 --> N431
    N96 --> N546
    N96 --> N16
    N98 --> N431
    N98 --> N546
    N99 --> N431
    N99 --> N546
    N100 --> N500
    N100 --> N431
    N100 --> N546
    N101 --> N500
    N101 --> N431
    N101 --> N546
    N102 --> N500
    N102 --> N431
    N102 --> N546
    N102 --> N16
    N103 --> N431
    N103 --> N546
    N104 --> N500
    N104 --> N431
    N104 --> N546
    N105 --> N500
    N105 --> N431
    N105 --> N546
    N106 --> N500
    N106 --> N431
    N106 --> N546
    N107 --> N500
    N107 --> N431
    N107 --> N546
    N108 --> N500
    N108 --> N431
    N108 --> N546
    N109 --> N402
    N109 --> N423
    N109 --> N431
    N109 --> N546
    N110 --> N431
    N110 --> N546
    N111 --> N431
    N111 --> N546
    N112 --> N500
    N112 --> N431
    N112 --> N546
    N113 --> N511
    N113 --> N395
    N113 --> N16
    N113 --> N402
    N113 --> N423
    N114 --> N511
    N114 --> N500
    N114 --> N431
    N114 --> N546
    N115 --> N500
    N115 --> N431
    N115 --> N546
    N116 --> N500
    N116 --> N431
    N116 --> N546
    N117 --> N500
    N117 --> N431
    N117 --> N546
    N118 --> N500
    N118 --> N431
    N118 --> N546
    N119 --> N500
    N119 --> N431
    N119 --> N546
    N119 --> N16
    N120 --> N402
    N120 --> N423
    N120 --> N511
    N120 --> N431
    N120 --> N546
    N120 --> N16
    N121 --> N511
    N121 --> N402
    N121 --> N423
    N121 --> N431
    N121 --> N546
    N121 --> N16
    N122 --> N500
    N122 --> N431
    N122 --> N546
    N123 --> N431
    N123 --> N546
    N123 --> N511
    N123 --> N16
    N124 --> N431
    N124 --> N546
    N125 --> N500
    N125 --> N431
    N125 --> N546
    N126 --> N431
    N126 --> N546
    N127 --> N500
    N127 --> N431
    N127 --> N546
    N128 --> N402
    N128 --> N423
    N128 --> N431
    N128 --> N546
    N129 --> N500
    N129 --> N431
    N129 --> N546
    N129 --> N16
    N130 --> N500
    N130 --> N431
    N130 --> N546
    N131 --> N500
    N131 --> N431
    N131 --> N546
    N132 --> N500
    N132 --> N431
    N132 --> N546
    N133 --> N500
    N133 --> N431
    N133 --> N546
    N134 --> N402
    N134 --> N423
    N134 --> N431
    N134 --> N546
    N135 --> N500
    N135 --> N431
    N135 --> N546
    N136 --> N431
    N136 --> N546
    N136 --> N16
    N136 --> N15
    N137 --> N511
    N137 --> N431
    N137 --> N546
    N138 --> N431
    N138 --> N546
    N139 --> N431
    N139 --> N546
    N139 --> N16
    N141 --> N431
    N141 --> N546
    N142 --> N402
    N142 --> N423
    N142 --> N431
    N142 --> N546
    N143 --> N500
    N143 --> N431
    N143 --> N546
    N144 --> N402
    N144 --> N423
    N144 --> N431
    N144 --> N546
    N145 --> N402
    N145 --> N423
    N145 --> N431
    N145 --> N546
    N145 --> N511
    N145 --> N16
    N146 --> N431
    N146 --> N546
    N147 --> N431
    N147 --> N546
    N147 --> N16
    N148 --> N431
    N148 --> N546
    N148 --> N16
    N149 --> N500
    N149 --> N431
    N149 --> N546
    N149 --> N16
    N150 --> N431
    N150 --> N546
    N150 --> N16
    N151 --> N431
    N151 --> N546
    N151 --> N16
    N152 --> N431
    N152 --> N546
    N153 --> N511
    N153 --> N431
    N153 --> N546
    N154 --> N431
    N154 --> N546
    N155 --> N431
    N155 --> N546
    N156 --> N431
    N156 --> N546
    N157 --> N431
    N157 --> N546
    N158 --> N500
    N158 --> N431
    N158 --> N546
    N159 --> N402
    N159 --> N423
    N159 --> N431
    N159 --> N546
    N160 --> N402
    N160 --> N423
    N160 --> N431
    N160 --> N546
    N160 --> N16
    N161 --> N402
    N161 --> N423
    N161 --> N341
    N161 --> N475
    N161 --> N431
    N161 --> N546
    N162 --> N431
    N162 --> N546
    N163 --> N431
    N163 --> N546
    N164 --> N402
    N164 --> N423
    N164 --> N431
    N164 --> N546
    N165 --> N431
    N165 --> N546
    N166 --> N431
    N166 --> N546
    N167 --> N402
    N167 --> N423
    N167 --> N431
    N167 --> N546
    N168 --> N431
    N168 --> N546
    N168 --> N16
    N169 --> N500
    N169 --> N431
    N169 --> N546
    N170 --> N402
    N170 --> N423
    N170 --> N431
    N170 --> N546
    N171 --> N431
    N171 --> N546
    N172 --> N500
    N172 --> N431
    N172 --> N546
    N173 --> N16
    N174 --> N402
    N174 --> N423
    N174 --> N431
    N174 --> N546
    N174 --> N381
    N174 --> N415
    N174 --> N11
    N174 --> N51
    N174 --> N322
    N174 --> N380
    N174 --> N399
    N174 --> N414
    N174 --> N469
    N174 --> N498
    N174 --> N13
    N174 --> N12
    N175 --> N431
    N175 --> N546
    N176 --> N431
    N176 --> N546
    N177 --> N402
    N177 --> N423
    N177 --> N511
    N177 --> N500
    N177 --> N431
    N177 --> N546
    N177 --> N16
    N178 --> N500
    N178 --> N431
    N178 --> N546
    N179 --> N402
    N179 --> N423
    N179 --> N16
    N180 --> N511
    N180 --> N431
    N180 --> N546
    N180 --> N16
    N180 --> N402
    N180 --> N423
    N181 --> N431
    N181 --> N546
    N181 --> N16
    N183 --> N402
    N183 --> N423
    N183 --> N431
    N183 --> N546
    N184 --> N431
    N184 --> N546
    N184 --> N16
    N185 --> N431
    N185 --> N546
    N186 --> N431
    N186 --> N546
    N186 --> N16
    N187 --> N16
    N190 --> N431
    N190 --> N546
    N191 --> N402
    N191 --> N423
    N191 --> N431
    N191 --> N546
    N192 --> N431
    N192 --> N546
    N193 --> N431
    N193 --> N546
    N193 --> N402
    N193 --> N423
    N194 --> N500
    N194 --> N431
    N194 --> N546
    N196 --> N431
    N196 --> N546
    N197 --> N431
    N197 --> N546
    N197 --> N16
    N198 --> N402
    N198 --> N423
    N198 --> N431
    N198 --> N546
    N198 --> N16
    N199 --> N431
    N199 --> N546
    N199 --> N16
    N200 --> N431
    N200 --> N546
    N201 --> N402
    N201 --> N423
    N201 --> N500
    N201 --> N431
    N201 --> N546
    N201 --> N16
    N202 --> N500
    N202 --> N431
    N202 --> N546
    N203 --> N500
    N203 --> N431
    N203 --> N546
    N204 --> N511
    N204 --> N500
    N204 --> N431
    N204 --> N546
    N205 --> N511
    N205 --> N431
    N205 --> N546
    N206 --> N500
    N206 --> N431
    N206 --> N546
    N207 --> N500
    N207 --> N431
    N207 --> N546
    N207 --> N16
    N208 --> N500
    N208 --> N431
    N208 --> N546
    N208 --> N16
    N209 --> N431
    N209 --> N546
    N210 --> N500
    N210 --> N16
    N214 --> N511
    N214 --> N15
    N216 --> N16
    N217 --> N15
    N222 --> N16
    N223 --> N15
    N227 --> N16
    N229 --> N16
    N230 --> N511
    N236 --> N16
    N237 --> N16
    N238 --> N15
    N240 --> N402
    N240 --> N423
    N240 --> N16
    N242 --> N402
    N242 --> N423
    N242 --> N16
    N242 --> N511
    N243 --> N511
    N243 --> N15
    N249 --> N511
    N250 --> N500
    N250 --> N402
    N250 --> N423
    N251 --> N402
    N251 --> N423
    N252 --> N511
    N253 --> N402
    N253 --> N423
    N253 --> N15
    N253 --> N511
    N254 --> N16
    N256 --> N511
    N256 --> N15
    N258 --> N16
    N259 --> N511
    N260 --> N402
    N260 --> N423
    N261 --> N511
    N261 --> N15
    N262 --> N15
    N262 --> N431
    N262 --> N546
    N262 --> N511
    N264 --> N15
    N265 --> N402
    N265 --> N423
    N265 --> N17
    N266 --> N511
    N267 --> N511
    N268 --> N402
    N268 --> N423
    N272 --> N15
    N273 --> N15
    N274 --> N15
    N278 --> N348
    N278 --> N375
    N278 --> N391
    N278 --> N430
    N278 --> N483
    N278 --> N11
    N278 --> N51
    N278 --> N322
    N278 --> N380
    N278 --> N399
    N278 --> N414
    N278 --> N469
    N278 --> N498
    N279 --> N534
    N279 --> N551
    N279 --> N559
    N279 --> N567
    N279 --> N573
    N279 --> N280
    N279 --> N311
    N279 --> N313
    N279 --> N295
    N279 --> N278
    N279 --> N11
    N279 --> N51
    N279 --> N322
    N279 --> N380
    N279 --> N399
    N279 --> N414
    N279 --> N469
    N279 --> N498
    N279 --> N312
    N279 --> N310
    N280 --> N281
    N280 --> N11
    N280 --> N51
    N280 --> N322
    N280 --> N380
    N280 --> N399
    N280 --> N414
    N280 --> N469
    N280 --> N498
    N280 --> N278
    N280 --> N309
    N282 --> N297
    N282 --> N299
    N282 --> N298
    N283 --> N11
    N283 --> N51
    N283 --> N322
    N283 --> N380
    N283 --> N399
    N283 --> N414
    N283 --> N469
    N283 --> N498
    N285 --> N11
    N285 --> N51
    N285 --> N322
    N285 --> N380
    N285 --> N399
    N285 --> N414
    N285 --> N469
    N285 --> N498
    N286 --> N11
    N286 --> N51
    N286 --> N322
    N286 --> N380
    N286 --> N399
    N286 --> N414
    N286 --> N469
    N286 --> N498
    N287 --> N306
    N287 --> N11
    N287 --> N51
    N287 --> N322
    N287 --> N380
    N287 --> N399
    N287 --> N414
    N287 --> N469
    N287 --> N498
    N288 --> N11
    N288 --> N51
    N288 --> N322
    N288 --> N380
    N288 --> N399
    N288 --> N414
    N288 --> N469
    N288 --> N498
    N289 --> N278
    N289 --> N280
    N291 --> N11
    N291 --> N51
    N291 --> N322
    N291 --> N380
    N291 --> N399
    N291 --> N414
    N291 --> N469
    N291 --> N498
    N293 --> N278
    N293 --> N304
    N293 --> N301
    N294 --> N11
    N294 --> N51
    N294 --> N322
    N294 --> N380
    N294 --> N399
    N294 --> N414
    N294 --> N469
    N294 --> N498
    N295 --> N278
    N295 --> N289
    N295 --> N296
    N295 --> N293
    N295 --> N284
    N295 --> N306
    N295 --> N320
    N295 --> N315
    N295 --> N314
    N295 --> N317
    N295 --> N318
    N295 --> N300
    N295 --> N291
    N296 --> N278
    N296 --> N11
    N296 --> N51
    N296 --> N322
    N296 --> N380
    N296 --> N399
    N296 --> N414
    N296 --> N469
    N296 --> N498
    N296 --> N301
    N300 --> N307
    N308 --> N11
    N308 --> N51
    N308 --> N322
    N308 --> N380
    N308 --> N399
    N308 --> N414
    N308 --> N469
    N308 --> N498
    N309 --> N11
    N309 --> N51
    N309 --> N322
    N309 --> N380
    N309 --> N399
    N309 --> N414
    N309 --> N469
    N309 --> N498
    N310 --> N11
    N310 --> N51
    N310 --> N322
    N310 --> N380
    N310 --> N399
    N310 --> N414
    N310 --> N469
    N310 --> N498
    N311 --> N11
    N311 --> N51
    N311 --> N322
    N311 --> N380
    N311 --> N399
    N311 --> N414
    N311 --> N469
    N311 --> N498
    N311 --> N280
    N312 --> N11
    N312 --> N51
    N312 --> N322
    N312 --> N380
    N312 --> N399
    N312 --> N414
    N312 --> N469
    N312 --> N498
    N313 --> N303
    N313 --> N11
    N313 --> N51
    N313 --> N322
    N313 --> N380
    N313 --> N399
    N313 --> N414
    N313 --> N469
    N313 --> N498
    N314 --> N348
    N314 --> N375
    N314 --> N391
    N314 --> N430
    N314 --> N483
    N314 --> N278
    N314 --> N303
    N314 --> N11
    N314 --> N51
    N314 --> N322
    N314 --> N380
    N314 --> N399
    N314 --> N414
    N314 --> N469
    N314 --> N498
    N315 --> N348
    N315 --> N375
    N315 --> N391
    N315 --> N430
    N315 --> N483
    N315 --> N303
    N315 --> N302
    N315 --> N11
    N315 --> N51
    N315 --> N322
    N315 --> N380
    N315 --> N399
    N315 --> N414
    N315 --> N469
    N315 --> N498
    N316 --> N11
    N316 --> N51
    N316 --> N322
    N316 --> N380
    N316 --> N399
    N316 --> N414
    N316 --> N469
    N316 --> N498
    N317 --> N348
    N317 --> N375
    N317 --> N391
    N317 --> N430
    N317 --> N483
    N317 --> N304
    N317 --> N303
    N317 --> N302
    N317 --> N11
    N317 --> N51
    N317 --> N322
    N317 --> N380
    N317 --> N399
    N317 --> N414
    N317 --> N469
    N317 --> N498
    N317 --> N287
    N317 --> N288
    N317 --> N285
    N317 --> N283
    N317 --> N286
    N318 --> N11
    N318 --> N51
    N318 --> N322
    N318 --> N380
    N318 --> N399
    N318 --> N414
    N318 --> N469
    N318 --> N498
    N318 --> N348
    N318 --> N375
    N318 --> N391
    N318 --> N430
    N318 --> N483
    N318 --> N278
    N318 --> N307
    N318 --> N304
    N318 --> N303
    N318 --> N302
    N319 --> N305
    N319 --> N303
    N319 --> N11
    N319 --> N51
    N319 --> N322
    N319 --> N380
    N319 --> N399
    N319 --> N414
    N319 --> N469
    N319 --> N498
    N320 --> N348
    N320 --> N375
    N320 --> N391
    N320 --> N430
    N320 --> N483
    N320 --> N303
    N320 --> N302
    N320 --> N11
    N320 --> N51
    N320 --> N322
    N320 --> N380
    N320 --> N399
    N320 --> N414
    N320 --> N469
    N320 --> N498
    N320 --> N309
    N321 --> N11
    N321 --> N51
    N321 --> N322
    N321 --> N380
    N321 --> N399
    N321 --> N414
    N321 --> N469
    N321 --> N498
    N326 --> N431
    N326 --> N546
    N328 --> N431
    N328 --> N546
    N330 --> N431
    N330 --> N546
    N331 --> N431
    N331 --> N546
    N333 --> N431
    N333 --> N546
    N334 --> N431
    N334 --> N546
    N335 --> N381
    N335 --> N415
    N335 --> N348
    N335 --> N375
    N335 --> N391
    N335 --> N430
    N335 --> N483
    N335 --> N431
    N335 --> N546
    N336 --> N431
    N336 --> N546
    N338 --> N500
    N339 --> N395
    N339 --> N381
    N339 --> N415
    N339 --> N431
    N339 --> N546
    N340 --> N431
    N340 --> N546
    N342 --> N431
    N342 --> N546
    N343 --> N402
    N343 --> N423
    N343 --> N348
    N343 --> N375
    N343 --> N391
    N343 --> N430
    N343 --> N483
    N343 --> N381
    N343 --> N415
    N343 --> N431
    N343 --> N546
    N344 --> N431
    N344 --> N546
    N348 --> N375
    N348 --> N391
    N348 --> N430
    N348 --> N483
    N348 --> N431
    N348 --> N546
    N349 --> N395
    N349 --> N431
    N349 --> N546
    N353 --> N381
    N353 --> N415
    N353 --> N431
    N353 --> N546
    N353 --> N511
    N354 --> N381
    N354 --> N415
    N354 --> N431
    N354 --> N546
    N362 --> N402
    N362 --> N423
    N362 --> N431
    N362 --> N546
    N363 --> N431
    N363 --> N546
    N364 --> N367
    N364 --> N563
    N364 --> N395
    N364 --> N431
    N364 --> N546
    N365 --> N431
    N365 --> N546
    N367 --> N431
    N367 --> N546
    N368 --> N431
    N368 --> N546
    N369 --> N431
    N369 --> N546
    N370 --> N348
    N370 --> N375
    N370 --> N391
    N370 --> N430
    N370 --> N483
    N370 --> N431
    N370 --> N546
    N370 --> N395
    N370 --> N381
    N370 --> N415
    N371 --> N395
    N371 --> N381
    N371 --> N415
    N371 --> N431
    N371 --> N546
    N374 --> N348
    N374 --> N375
    N374 --> N391
    N374 --> N430
    N374 --> N483
    N375 --> N542
    N375 --> N564
    N375 --> N374
    N376 --> N381
    N376 --> N415
    N376 --> N431
    N376 --> N546
    N378 --> N431
    N378 --> N546
    N379 --> N431
    N379 --> N546
    N380 --> N395
    N380 --> N431
    N380 --> N546
    N381 --> N415
    N381 --> N348
    N381 --> N375
    N381 --> N391
    N381 --> N430
    N381 --> N483
    N381 --> N431
    N381 --> N546
    N381 --> N395
    N382 --> N431
    N382 --> N546
    N383 --> N381
    N383 --> N415
    N383 --> N431
    N383 --> N546
    N383 --> N395
    N383 --> N411
    N384 --> N381
    N384 --> N415
    N384 --> N431
    N384 --> N546
    N385 --> N381
    N385 --> N415
    N385 --> N395
    N385 --> N431
    N385 --> N546
    N386 --> N381
    N386 --> N415
    N386 --> N395
    N386 --> N431
    N386 --> N546
    N387 --> N348
    N387 --> N375
    N387 --> N391
    N387 --> N430
    N387 --> N483
    N387 --> N395
    N387 --> N431
    N387 --> N546
    N387 --> N402
    N387 --> N423
    N388 --> N431
    N388 --> N546
    N388 --> N425
    N388 --> N395
    N389 --> N381
    N389 --> N415
    N389 --> N431
    N389 --> N546
    N390 --> N431
    N390 --> N546
    N391 --> N381
    N391 --> N415
    N391 --> N348
    N391 --> N375
    N391 --> N430
    N391 --> N483
    N391 --> N431
    N391 --> N546
    N391 --> N411
    N391 --> N402
    N391 --> N423
    N392 --> N348
    N392 --> N375
    N392 --> N391
    N392 --> N430
    N392 --> N483
    N392 --> N381
    N392 --> N415
    N392 --> N431
    N392 --> N546
    N393 --> N348
    N393 --> N375
    N393 --> N391
    N393 --> N430
    N393 --> N483
    N393 --> N431
    N393 --> N546
    N396 --> N431
    N396 --> N546
    N396 --> N395
    N397 --> N431
    N397 --> N546
    N397 --> N395
    N398 --> N348
    N398 --> N375
    N398 --> N391
    N398 --> N430
    N398 --> N483
    N398 --> N431
    N398 --> N546
    N398 --> N395
    N399 --> N395
    N399 --> N431
    N399 --> N546
    N400 --> N431
    N400 --> N546
    N401 --> N395
    N401 --> N431
    N401 --> N546
    N402 --> N395
    N402 --> N348
    N402 --> N375
    N402 --> N391
    N402 --> N430
    N402 --> N483
    N402 --> N431
    N402 --> N546
    N402 --> N381
    N402 --> N415
    N403 --> N402
    N403 --> N423
    N403 --> N395
    N403 --> N431
    N403 --> N546
    N404 --> N402
    N404 --> N423
    N404 --> N395
    N404 --> N431
    N404 --> N546
    N405 --> N431
    N405 --> N546
    N407 --> N381
    N407 --> N415
    N407 --> N431
    N407 --> N546
    N407 --> N411
    N407 --> N348
    N407 --> N375
    N407 --> N391
    N407 --> N430
    N407 --> N483
    N408 --> N395
    N408 --> N431
    N408 --> N546
    N409 --> N431
    N409 --> N546
    N410 --> N431
    N410 --> N546
    N411 --> N431
    N411 --> N546
    N412 --> N395
    N412 --> N348
    N412 --> N375
    N412 --> N391
    N412 --> N430
    N412 --> N483
    N412 --> N431
    N412 --> N546
    N413 --> N431
    N413 --> N546
    N414 --> N402
    N414 --> N423
    N414 --> N431
    N414 --> N546
    N415 --> N381
    N415 --> N431
    N415 --> N546
    N416 --> N431
    N416 --> N546
    N417 --> N431
    N417 --> N546
    N418 --> N395
    N418 --> N431
    N418 --> N546
    N419 --> N431
    N419 --> N546
    N420 --> N402
    N420 --> N423
    N420 --> N431
    N420 --> N546
    N421 --> N431
    N421 --> N546
    N422 --> N348
    N422 --> N375
    N422 --> N391
    N422 --> N430
    N422 --> N483
    N422 --> N431
    N422 --> N546
    N423 --> N348
    N423 --> N375
    N423 --> N391
    N423 --> N430
    N423 --> N483
    N423 --> N431
    N423 --> N546
    N423 --> N381
    N423 --> N415
    N424 --> N395
    N424 --> N348
    N424 --> N375
    N424 --> N391
    N424 --> N430
    N424 --> N483
    N424 --> N431
    N424 --> N546
    N425 --> N431
    N425 --> N546
    N425 --> N388
    N425 --> N395
    N426 --> N431
    N426 --> N546
    N427 --> N402
    N427 --> N423
    N427 --> N431
    N427 --> N546
    N428 --> N395
    N428 --> N381
    N428 --> N415
    N428 --> N431
    N428 --> N546
    N429 --> N402
    N429 --> N423
    N429 --> N431
    N429 --> N546
    N430 --> N395
    N430 --> N348
    N430 --> N375
    N430 --> N391
    N430 --> N483
    N430 --> N431
    N430 --> N546
    N431 --> N546
    N431 --> N348
    N431 --> N375
    N431 --> N391
    N431 --> N430
    N431 --> N483
    N432 --> N395
    N432 --> N348
    N432 --> N375
    N432 --> N391
    N432 --> N430
    N432 --> N483
    N432 --> N431
    N432 --> N546
    N433 --> N431
    N433 --> N546
    N433 --> N395
    N435 --> N402
    N435 --> N423
    N435 --> N431
    N435 --> N546
    N437 --> N395
    N437 --> N431
    N437 --> N546
    N438 --> N431
    N438 --> N546
    N438 --> N395
    N439 --> N431
    N439 --> N546
    N440 --> N381
    N440 --> N415
    N440 --> N395
    N440 --> N431
    N440 --> N546
    N441 --> N348
    N441 --> N375
    N441 --> N391
    N441 --> N430
    N441 --> N483
    N441 --> N381
    N441 --> N415
    N441 --> N431
    N441 --> N546
    N442 --> N431
    N442 --> N546
    N443 --> N431
    N443 --> N546
    N444 --> N431
    N444 --> N546
    N445 --> N381
    N445 --> N415
    N445 --> N395
    N445 --> N431
    N445 --> N546
    N445 --> N411
    N446 --> N381
    N446 --> N415
    N446 --> N431
    N446 --> N546
    N447 --> N381
    N447 --> N415
    N447 --> N431
    N447 --> N546
    N447 --> N395
    N447 --> N348
    N447 --> N375
    N447 --> N391
    N447 --> N430
    N447 --> N483
    N448 --> N348
    N448 --> N375
    N448 --> N391
    N448 --> N430
    N448 --> N483
    N448 --> N431
    N448 --> N546
    N450 --> N431
    N450 --> N546
    N452 --> N431
    N452 --> N546
    N452 --> N411
    N453 --> N431
    N453 --> N546
    N454 --> N431
    N454 --> N546
    N454 --> N395
    N454 --> N348
    N454 --> N375
    N454 --> N391
    N454 --> N430
    N454 --> N483
    N455 --> N431
    N455 --> N546
    N456 --> N348
    N456 --> N375
    N456 --> N391
    N456 --> N430
    N456 --> N483
    N456 --> N431
    N456 --> N546
    N457 --> N381
    N457 --> N415
    N457 --> N431
    N457 --> N546
    N458 --> N431
    N458 --> N546
    N459 --> N431
    N459 --> N546
    N460 --> N381
    N460 --> N415
    N460 --> N431
    N460 --> N546
    N461 --> N348
    N461 --> N375
    N461 --> N391
    N461 --> N430
    N461 --> N483
    N461 --> N431
    N461 --> N546
    N462 --> N381
    N462 --> N415
    N462 --> N395
    N462 --> N348
    N462 --> N375
    N462 --> N391
    N462 --> N430
    N462 --> N483
    N462 --> N431
    N462 --> N546
    N463 --> N431
    N463 --> N546
    N464 --> N431
    N464 --> N546
    N465 --> N431
    N465 --> N546
    N466 --> N431
    N466 --> N546
    N467 --> N431
    N467 --> N546
    N468 --> N395
    N468 --> N431
    N468 --> N546
    N469 --> N395
    N469 --> N431
    N469 --> N546
    N470 --> N431
    N470 --> N546
    N471 --> N431
    N471 --> N546
    N472 --> N402
    N472 --> N423
    N472 --> N431
    N472 --> N546
    N473 --> N367
    N473 --> N563
    N474 --> N381
    N474 --> N415
    N474 --> N431
    N474 --> N546
    N475 --> N402
    N475 --> N423
    N475 --> N367
    N475 --> N563
    N475 --> N431
    N475 --> N546
    N476 --> N367
    N476 --> N563
    N476 --> N402
    N476 --> N423
    N476 --> N431
    N476 --> N546
    N477 --> N348
    N477 --> N375
    N477 --> N391
    N477 --> N430
    N477 --> N483
    N477 --> N395
    N477 --> N431
    N477 --> N546
    N478 --> N431
    N478 --> N546
    N479 --> N431
    N479 --> N546
    N480 --> N395
    N481 --> N431
    N481 --> N546
    N482 --> N402
    N482 --> N423
    N482 --> N395
    N482 --> N348
    N482 --> N375
    N482 --> N391
    N482 --> N430
    N482 --> N483
    N482 --> N431
    N482 --> N546
    N483 --> N431
    N483 --> N546
    N484 --> N402
    N484 --> N423
    N484 --> N431
    N484 --> N546
    N485 --> N431
    N485 --> N546
    N486 --> N431
    N486 --> N546
    N486 --> N511
    N488 --> N431
    N488 --> N546
    N491 --> N431
    N491 --> N546
    N492 --> N357
    N492 --> N431
    N492 --> N546
    N494 --> N402
    N494 --> N423
    N494 --> N431
    N494 --> N546
    N496 --> N395
    N496 --> N431
    N496 --> N546
    N497 --> N431
    N497 --> N546
    N498 --> N511
    N498 --> N402
    N498 --> N423
    N498 --> N500
    N498 --> N431
    N498 --> N546
    N499 --> N431
    N499 --> N546
    N500 --> N367
    N500 --> N563
    N500 --> N431
    N500 --> N546
    N501 --> N511
    N501 --> N500
    N501 --> N395
    N501 --> N431
    N501 --> N546
    N502 --> N511
    N502 --> N500
    N502 --> N348
    N502 --> N375
    N502 --> N391
    N502 --> N430
    N502 --> N483
    N502 --> N431
    N502 --> N546
    N503 --> N511
    N503 --> N500
    N503 --> N395
    N503 --> N431
    N503 --> N546
    N504 --> N511
    N504 --> N431
    N504 --> N546
    N506 --> N348
    N506 --> N375
    N506 --> N391
    N506 --> N430
    N506 --> N483
    N506 --> N431
    N506 --> N546
    N509 --> N431
    N509 --> N546
    N510 --> N511
    N510 --> N500
    N510 --> N431
    N510 --> N546
    N512 --> N511
    N512 --> N513
    N513 --> N511
    N515 --> N500
    N515 --> N431
    N515 --> N546
    N517 --> N511
    N517 --> N395
    N518 --> N511
    N519 --> N511
    N520 --> N511
    N521 --> N511
    N521 --> N367
    N521 --> N563
    N521 --> N500
    N521 --> N431
    N521 --> N546
    N522 --> N511
    N522 --> N367
    N522 --> N563
    N522 --> N500
    N522 --> N431
    N522 --> N546
    N523 --> N511
    N523 --> N350
    N523 --> N484
    N524 --> N511
    N524 --> N367
    N524 --> N563
    N524 --> N500
    N524 --> N431
    N524 --> N546
    N524 --> N350
    N524 --> N484
    N525 --> N511
    N525 --> N500
    N525 --> N367
    N525 --> N563
    N525 --> N431
    N525 --> N546
    N525 --> N350
    N525 --> N484
    N526 --> N511
    N526 --> N500
    N526 --> N431
    N526 --> N546
    N527 --> N500
    N527 --> N348
    N527 --> N375
    N527 --> N391
    N527 --> N430
    N527 --> N483
    N528 --> N500
    N528 --> N431
    N528 --> N546
    N529 --> N500
    N531 --> N431
    N531 --> N546
    N532 --> N395
    N533 --> N511
    N533 --> N431
    N533 --> N546
    N534 --> N395
    N534 --> N431
    N534 --> N546
    N535 --> N395
    N536 --> N431
    N536 --> N546
    N537 --> N395
    N538 --> N381
    N538 --> N415
    N538 --> N431
    N538 --> N546
    N539 --> N431
    N539 --> N546
    N540 --> N381
    N540 --> N415
    N540 --> N395
    N540 --> N431
    N540 --> N546
    N541 --> N395
    N541 --> N431
    N541 --> N546
    N542 --> N500
    N543 --> N381
    N543 --> N415
    N544 --> N367
    N544 --> N563
    N544 --> N395
    N544 --> N431
    N544 --> N546
    N546 --> N367
    N546 --> N563
    N546 --> N500
    N546 --> N431
    N547 --> N381
    N547 --> N415
    N550 --> N431
    N550 --> N546
    N551 --> N511
    N551 --> N500
    N551 --> N348
    N551 --> N375
    N551 --> N391
    N551 --> N430
    N551 --> N483
    N551 --> N431
    N551 --> N546
    N551 --> N350
    N551 --> N484
    N552 --> N511
    N552 --> N500
    N552 --> N348
    N552 --> N375
    N552 --> N391
    N552 --> N430
    N552 --> N483
    N552 --> N431
    N552 --> N546
    N553 --> N511
    N553 --> N431
    N553 --> N546
    N554 --> N367
    N554 --> N563
    N554 --> N431
    N554 --> N546
    N554 --> N350
    N554 --> N484
    N555 --> N511
    N555 --> N367
    N555 --> N563
    N555 --> N500
    N555 --> N348
    N555 --> N375
    N555 --> N391
    N555 --> N430
    N555 --> N483
    N555 --> N431
    N555 --> N546
    N555 --> N350
    N555 --> N484
    N557 --> N431
    N557 --> N546
    N558 --> N367
    N558 --> N563
    N558 --> N431
    N558 --> N546
    N559 --> N511
    N559 --> N500
    N559 --> N395
    N559 --> N348
    N559 --> N375
    N559 --> N391
    N559 --> N430
    N559 --> N483
    N559 --> N431
    N559 --> N546
    N560 --> N367
    N560 --> N563
    N561 --> N431
    N561 --> N546
    N563 --> N511
    N564 --> N511
    N564 --> N500
    N564 --> N395
    N564 --> N431
    N564 --> N546
    N565 --> N511
    N565 --> N367
    N565 --> N563
    N565 --> N500
    N565 --> N395
    N565 --> N348
    N565 --> N375
    N565 --> N391
    N565 --> N430
    N565 --> N483
    N565 --> N431
    N565 --> N546
    N566 --> N395
    N567 --> N500
    N567 --> N395
    N567 --> N348
    N567 --> N375
    N567 --> N391
    N567 --> N430
    N567 --> N483
    N567 --> N431
    N567 --> N546
    N567 --> N350
    N567 --> N484
    N568 --> N500
    N568 --> N348
    N568 --> N375
    N568 --> N391
    N568 --> N430
    N568 --> N483
    N568 --> N431
    N568 --> N546
    N569 --> N431
    N569 --> N546
    N570 --> N367
    N570 --> N563
    N570 --> N431
    N570 --> N546
    N570 --> N350
    N570 --> N484
    N571 --> N367
    N571 --> N563
    N571 --> N500
    N571 --> N395
    N571 --> N348
    N571 --> N375
    N571 --> N391
    N571 --> N430
    N571 --> N483
    N571 --> N431
    N571 --> N546
    N571 --> N350
    N571 --> N484
    N573 --> N500
    N573 --> N348
    N573 --> N375
    N573 --> N391
    N573 --> N430
    N573 --> N483
    N573 --> N431
    N573 --> N546
    N573 --> N350
    N573 --> N484
    N574 --> N500
    N574 --> N348
    N574 --> N375
    N574 --> N391
    N574 --> N430
    N574 --> N483
    N574 --> N431
    N574 --> N546
    N575 --> N431
    N575 --> N546
    N576 --> N367
    N576 --> N563
    N576 --> N431
    N576 --> N546
    N576 --> N350
    N576 --> N484
    N577 --> N367
    N577 --> N563
    N577 --> N500
    N577 --> N348
    N577 --> N375
    N577 --> N391
    N577 --> N430
    N577 --> N483
    N577 --> N431
    N577 --> N546
    N577 --> N350
    N577 --> N484
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
- **cleanup.py**
  - Imports: `os`
  - Imports: `shutil`
  - Imports: `sys`
- **create_shortcut.py**
  - Imports: `os`
  - Imports: `subprocess`
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
  - Imports: `database`
  - Imports: `fastapi`
  - Imports: `json`
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
  - Imports: `typing`
- **meridian_backend/src/tools/bookmark_manager.py**
  - Imports: `logging`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/tools/browser_agent.py**
  - Imports: `json`
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
  - Imports: `logging`
  - Imports: `src`
  - Imports: `struct`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/voice/duplex.py**
  - Imports: `asyncio`
  - Imports: `src`
  - Imports: `time`
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
  - Imports: `tempfile`
  - Imports: `threading`
  - Imports: `time`
  - Imports: `torch`
  - Imports: `typing`
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
- **meridian_backend/tests/test_skill_packs.py**
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
  - Imports: `Settings`
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
  - Imports: `AppContext`
  - Imports: `GlowCard`
  - Imports: `HoloButton`
  - Imports: `ProgressArc`
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