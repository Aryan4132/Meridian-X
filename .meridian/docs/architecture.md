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
    N10["config.py [generated_repos/attention_is_all_you_need__transformer_]"]
    N11["dataset.py [generated_repos/attention_is_all_you_need__transformer_]"]
    N12["model.py [generated_repos/attention_is_all_you_need__transformer_]"]
    N13["trainer.py [generated_repos/attention_is_all_you_need__transformer_]"]
    N14["api.py [meridian_backend]"]
    N15["database.py [meridian_backend]"]
    N16["mobile_bridge_service.py [meridian_backend]"]
    N17["tests_run.py [meridian_backend]"]
    N18["__init__.py [meridian_backend/src]"]
    N19["action_journal.py [meridian_backend/src/core]"]
    N20["agent_status_stream.py [meridian_backend/src/core]"]
    N21["ar_bridge.py [meridian_backend/src/core]"]
    N22["audit_logger.py [meridian_backend/src/core]"]
    N23["auth.py [meridian_backend/src/core]"]
    N24["behavior_monitor.py [meridian_backend/src/core]"]
    N25["boilerplate_genie.py [meridian_backend/src/core]"]
    N26["breach_sentinel.py [meridian_backend/src/core]"]
    N27["bus.py [meridian_backend/src/core]"]
    N28["camera_sentinel.py [meridian_backend/src/core]"]
    N29["clipboard.py [meridian_backend/src/core]"]
    N30["code_graph.py [meridian_backend/src/core]"]
    N31["cognitive_graph.py [meridian_backend/src/core]"]
    N32["commit_whisperer.py [meridian_backend/src/core]"]
    N33["config.py [meridian_backend/src/core]"]
    N34["consensus_engine.py [meridian_backend/src/core]"]
    N35["deep_project_context.py [meridian_backend/src/core]"]
    N36["dev_automation.py [meridian_backend/src/core]"]
    N37["discord_bridge.py [meridian_backend/src/core]"]
    N38["doc_generator.py [meridian_backend/src/core]"]
    N39["doc_indexer.py [meridian_backend/src/core]"]
    N40["elevated_runner.py [meridian_backend/src/core]"]
    N41["emergency_lockdown.py [meridian_backend/src/core]"]
    N42["experiment_runner.py [meridian_backend/src/core]"]
    N43["explain_code_engine.py [meridian_backend/src/core]"]
    N44["exporter.py [meridian_backend/src/core]"]
    N45["fim_sentinel.py [meridian_backend/src/core]"]
    N46["gaze_tracker.py [meridian_backend/src/core]"]
    N47["governor.py [meridian_backend/src/core]"]
    N48["graph_rag.py [meridian_backend/src/core]"]
    N49["graph_sync.py [meridian_backend/src/core]"]
    N50["hardware_detector.py [meridian_backend/src/core]"]
    N51["history_manager.py [meridian_backend/src/core]"]
    N52["llm_provider.py [meridian_backend/src/core]"]
    N53["local_model_manager.py [meridian_backend/src/core]"]
    N54["logging_config.py [meridian_backend/src/core]"]
    N55["loop.py [meridian_backend/src/core]"]
    N56["loop_dispatcher.py [meridian_backend/src/core]"]
    N57["loop_parser.py [meridian_backend/src/core]"]
    N58["loop_stream.py [meridian_backend/src/core]"]
    N59["lsp_client.py [meridian_backend/src/core]"]
    N60["malware_scanner.py [meridian_backend/src/core]"]
    N61["mcp_client.py [meridian_backend/src/core]"]
    N62["mcp_executor.py [meridian_backend/src/core]"]
    N63["memory_backup.py [meridian_backend/src/core]"]
    N64["memory_consolidation.py [meridian_backend/src/core]"]
    N65["memory_editor.py [meridian_backend/src/core]"]
    N66["mobile_bridge.py [meridian_backend/src/core]"]
    N67["mode.py [meridian_backend/src/core]"]
    N68["neural_rag.py [meridian_backend/src/core]"]
    N69["oauth_manager.py [meridian_backend/src/core]"]
    N70["ollama_manager.py [meridian_backend/src/core]"]
    N71["p2p.py [meridian_backend/src/core]"]
    N72["perception.py [meridian_backend/src/core]"]
    N73["persistence_sentinel.py [meridian_backend/src/core]"]
    N74["personal_crm.py [meridian_backend/src/core]"]
    N75["plugins.py [meridian_backend/src/core]"]
    N76["polyglot.py [meridian_backend/src/core]"]
    N77["predictive_engine.py [meridian_backend/src/core]"]
    N78["presence_briefing.py [meridian_backend/src/core]"]
    N79["proactive.py [meridian_backend/src/core]"]
    N80["proactive_system_guard.py [meridian_backend/src/core]"]
    N81["prompt_injection.py [meridian_backend/src/core]"]
    N82["prompt_templates.py [meridian_backend/src/core]"]
    N83["rag_optimizer.py [meridian_backend/src/core]"]
    N84["response_models.py [meridian_backend/src/core]"]
    N85["sandbox_runner.py [meridian_backend/src/core]"]
    N86["scheduler.py [meridian_backend/src/core]"]
    N87["screen_sense.py [meridian_backend/src/core]"]
    N88["security_middleware.py [meridian_backend/src/core]"]
    N89["self_evolving_tooling.py [meridian_backend/src/core]"]
    N90["silent_workflow_guardian.py [meridian_backend/src/core]"]
    N91["sos_protocol.py [meridian_backend/src/core]"]
    N92["speculative.py [meridian_backend/src/core]"]
    N93["swarm.py [meridian_backend/src/core]"]
    N94["system_defense.py [meridian_backend/src/core]"]
    N95["telegram_bridge.py [meridian_backend/src/core]"]
    N96["temporal_memory.py [meridian_backend/src/core]"]
    N97["tool_regression_sentinel.py [meridian_backend/src/core]"]
    N98["triggers.py [meridian_backend/src/core]"]
    N99["updater.py [meridian_backend/src/core]"]
    N100["vault.py [meridian_backend/src/core]"]
    N101["vision.py [meridian_backend/src/core]"]
    N102["vision_face.py [meridian_backend/src/core]"]
    N103["vision_gesture.py [meridian_backend/src/core]"]
    N104["watcher.py [meridian_backend/src/core]"]
    N105["what_broke_detective.py [meridian_backend/src/core]"]
    N106["workflow_engine.py [meridian_backend/src/core]"]
    N107["workspace_orchestrator.py [meridian_backend/src/core]"]
    N108["auto_reviewer.py [meridian_backend/src/tools]"]
    N109["bill_radar.py [meridian_backend/src/tools]"]
    N110["bookmark_manager.py [meridian_backend/src/tools]"]
    N111["browser_agent.py [meridian_backend/src/tools]"]
    N112["browser_use_agent.py [meridian_backend/src/tools]"]
    N113["cam_guard.py [meridian_backend/src/tools]"]
    N114["chrome_manager.py [meridian_backend/src/tools]"]
    N115["clipboard.py [meridian_backend/src/tools]"]
    N116["communication.py [meridian_backend/src/tools]"]
    N117["db_query.py [meridian_backend/src/tools]"]
    N118["desktop.py [meridian_backend/src/tools]"]
    N119["detonation_sandbox.py [meridian_backend/src/tools]"]
    N120["developer.py [meridian_backend/src/tools]"]
    N121["dns_shield.py [meridian_backend/src/tools]"]
    N122["documents.py [meridian_backend/src/tools]"]
    N123["dynamic_manager.py [meridian_backend/src/tools]"]
    N124["expiry_sentinel.py [meridian_backend/src/tools]"]
    N125["exporter.py [meridian_backend/src/tools]"]
    N126["external_connectors.py [meridian_backend/src/tools]"]
    N127["filesystem.py [meridian_backend/src/tools]"]
    N128["file_janitor.py [meridian_backend/src/tools]"]
    N129["finance_sentinel.py [meridian_backend/src/tools]"]
    N130["geo_location.py [meridian_backend/src/tools]"]
    N131["health_ingest.py [meridian_backend/src/tools]"]
    N132["household.py [meridian_backend/src/tools]"]
    N133["knowledge.py [meridian_backend/src/tools]"]
    N134["learning_queue.py [meridian_backend/src/tools]"]
    N135["mcp_marketplace.py [meridian_backend/src/tools]"]
    N136["network_guardian.py [meridian_backend/src/tools]"]
    N137["networth_tracker.py [meridian_backend/src/tools]"]
    N138["ollama_manager.py [meridian_backend/src/tools]"]
    N139["papercoder.py [meridian_backend/src/tools]"]
    N140["password_auditor.py [meridian_backend/src/tools]"]
    N141["phishing_guard.py [meridian_backend/src/tools]"]
    N142["phone_agent.py [meridian_backend/src/tools]"]
    N143["price_watcher.py [meridian_backend/src/tools]"]
    N144["recording.py [meridian_backend/src/tools]"]
    N145["registry.py [meridian_backend/src/tools]"]
    N146["review.py [meridian_backend/src/tools]"]
    N147["scheduler.py [meridian_backend/src/tools]"]
    N148["screenshot_memory.py [meridian_backend/src/tools]"]
    N149["search_hub.py [meridian_backend/src/tools]"]
    N150["security_auditor.py [meridian_backend/src/tools]"]
    N151["shell.py [meridian_backend/src/tools]"]
    N152["system.py [meridian_backend/src/tools]"]
    N153["task_scheduler.py [meridian_backend/src/tools]"]
    N154["totp_generator.py [meridian_backend/src/tools]"]
    N155["travel_butler.py [meridian_backend/src/tools]"]
    N156["usb_watchdog.py [meridian_backend/src/tools]"]
    N157["vault.py [meridian_backend/src/tools]"]
    N158["video_editor.py [meridian_backend/src/tools]"]
    N159["voice.py [meridian_backend/src/tools]"]
    N160["watcher.py [meridian_backend/src/tools]"]
    N161["web.py [meridian_backend/src/tools]"]
    N162["web_browser.py [meridian_backend/src/tools]"]
    N163["wellness.py [meridian_backend/src/tools]"]
    N164["whatsapp_manager.py [meridian_backend/src/tools]"]
    N165["wifi_assessor.py [meridian_backend/src/tools]"]
    N166["workspace_layout.py [meridian_backend/src/tools]"]
    N167["ambient_listener.py [meridian_backend/src/voice]"]
    N168["duplex.py [meridian_backend/src/voice]"]
    N169["polyglot.py [meridian_backend/src/voice]"]
    N170["stt.py [meridian_backend/src/voice]"]
    N171["tts.py [meridian_backend/src/voice]"]
    N172["voice_biometrics.py [meridian_backend/src/voice]"]
    N173["wakeword.py [meridian_backend/src/voice]"]
    N174["conftest.py [meridian_backend/tests]"]
    N175["run_tests.py [meridian_backend/tests]"]
    N176["test_advanced_proactive.py [meridian_backend/tests]"]
    N177["test_auto_bug_fixer.py [meridian_backend/tests]"]
    N178["test_backend_improvements.py [meridian_backend/tests]"]
    N179["test_backlog_features.py [meridian_backend/tests]"]
    N180["test_backlog_sprint.py [meridian_backend/tests]"]
    N181["test_bridges.py [meridian_backend/tests]"]
    N182["test_browser_agent.py [meridian_backend/tests]"]
    N183["test_browser_fallback.py [meridian_backend/tests]"]
    N184["test_browser_use.py [meridian_backend/tests]"]
    N185["test_butler_media.py [meridian_backend/tests]"]
    N186["test_chat_abort.py [meridian_backend/tests]"]
    N187["test_cognitive_graph.py [meridian_backend/tests]"]
    N188["test_config.py [meridian_backend/tests]"]
    N189["test_context_budget.py [meridian_backend/tests]"]
    N190["test_custom_password_auth.py [meridian_backend/tests]"]
    N191["test_database.py [meridian_backend/tests]"]
    N192["test_day10_features.py [meridian_backend/tests]"]
    N193["test_day11_features.py [meridian_backend/tests]"]
    N194["test_day12_features.py [meridian_backend/tests]"]
    N195["test_day13_features.py [meridian_backend/tests]"]
    N196["test_day14_day15_features.py [meridian_backend/tests]"]
    N197["test_day16_17_18_features.py [meridian_backend/tests]"]
    N198["test_day3_features.py [meridian_backend/tests]"]
    N199["test_day4_features.py [meridian_backend/tests]"]
    N200["test_day5_features.py [meridian_backend/tests]"]
    N201["test_day6_features.py [meridian_backend/tests]"]
    N202["test_day7_features.py [meridian_backend/tests]"]
    N203["test_day8_features.py [meridian_backend/tests]"]
    N204["test_day9_features.py [meridian_backend/tests]"]
    N205["test_dev_intelligence_suite.py [meridian_backend/tests]"]
    N206["test_document_tools.py [meridian_backend/tests]"]
    N207["test_full_proactive_suite.py [meridian_backend/tests]"]
    N208["test_geo_location.py [meridian_backend/tests]"]
    N209["test_jarvis_perception.py [meridian_backend/tests]"]
    N210["test_known_errors_remediation.py [meridian_backend/tests]"]
    N211["test_llm_provider.py [meridian_backend/tests]"]
    N212["test_logging.py [meridian_backend/tests]"]
    N213["test_loop_parser.py [meridian_backend/tests]"]
    N214["test_loop_submodules.py [meridian_backend/tests]"]
    N215["test_mobile_websocket.py [meridian_backend/tests]"]
    N216["test_model_source.py [meridian_backend/tests]"]
    N217["test_multi_os.py [meridian_backend/tests]"]
    N218["test_new_features.py [meridian_backend/tests]"]
    N219["test_oauth.py [meridian_backend/tests]"]
    N220["test_p2p.py [meridian_backend/tests]"]
    N221["test_proactive.py [meridian_backend/tests]"]
    N222["test_proactive_mode.py [meridian_backend/tests]"]
    N223["test_proactive_notifications.py [meridian_backend/tests]"]
    N224["test_security_features.py [meridian_backend/tests]"]
    N225["test_sprint2_features.py [meridian_backend/tests]"]
    N226["test_standalone_bridge.py [meridian_backend/tests]"]
    N227["test_stream_resiliency.py [meridian_backend/tests]"]
    N228["test_swarm.py [meridian_backend/tests]"]
    N229["test_tools.py [meridian_backend/tests]"]
    N230["test_tool_regression.py [meridian_backend/tests]"]
    N231["test_vault.py [meridian_backend/tests]"]
    N232["test_video_editor.py [meridian_backend/tests]"]
    N233["test_voice_speed.py [meridian_backend/tests]"]
    N234["test_wakeword_continuous.py [meridian_backend/tests]"]
    N235["test_wakeword_onnx.py [meridian_backend/tests]"]
    N236["test_workflow.py [meridian_backend/tests]"]
    N237["vite.config.ts [meridian_frontend]"]
    N238["AppContext.tsx [meridian_frontend/src]"]
    N239["main.tsx [meridian_frontend/src]"]
    N240["Mascot.tsx [meridian_frontend/src]"]
    N241["Mascot3DCharacter.tsx [meridian_frontend/src]"]
    N242["MobileApp.tsx [meridian_frontend/src]"]
    N243["AgentStatusStream.tsx [meridian_frontend/src/components]"]
    N244["CommandPalette.tsx [meridian_frontend/src/components]"]
    N245["DevAutomationPanel.tsx [meridian_frontend/src/components]"]
    N246["DeveloperSuitePanel.tsx [meridian_frontend/src/components]"]
    N247["LocalModelManager.tsx [meridian_frontend/src/components]"]
    N248["MemoryConsolidationView.tsx [meridian_frontend/src/components]"]
    N249["NavRail.tsx [meridian_frontend/src/components]"]
    N250["PerceptionHUD.tsx [meridian_frontend/src/components]"]
    N251["ProactiveGuardBanner.tsx [meridian_frontend/src/components]"]
    N252["ProfileHeader.tsx [meridian_frontend/src/components]"]
    N253["RightDrawer.tsx [meridian_frontend/src/components]"]
    N254["ServerConnectionModal.tsx [meridian_frontend/src/components]"]
    N255["Shell.tsx [meridian_frontend/src/components]"]
    N256["StatusBar.tsx [meridian_frontend/src/components]"]
    N257["DropdownNav.tsx [meridian_frontend/src/components/mobile]"]
    N258["LiveThoughtCarousel.tsx [meridian_frontend/src/components/mobile]"]
    N259["VoiceOrbHUD.tsx [meridian_frontend/src/components/mobile]"]
    N260["AmbientParticles.tsx [meridian_frontend/src/components/ui]"]
    N261["DataBadge.tsx [meridian_frontend/src/components/ui]"]
    N262["GlowCard.tsx [meridian_frontend/src/components/ui]"]
    N263["HoloButton.tsx [meridian_frontend/src/components/ui]"]
    N264["ProgressArc.tsx [meridian_frontend/src/components/ui]"]
    N265["TerminalLine.tsx [meridian_frontend/src/components/ui]"]
    N266["ToastContext.tsx [meridian_frontend/src/components/ui]"]
    N267["useMemoryOptimizer.ts [meridian_frontend/src/hooks]"]
    N268["oauthService.ts [meridian_frontend/src/services]"]
    N269["streamingAudioPlayer.ts [meridian_frontend/src/services]"]
    N270["BackendSetup.tsx [meridian_frontend/src/startup]"]
    N271["BootSequence.tsx [meridian_frontend/src/startup]"]
    N272["OnboardingWizard.tsx [meridian_frontend/src/startup]"]
    N273["SetupWizard.tsx [meridian_frontend/src/startup]"]
    N274["Clipboard.tsx [meridian_frontend/src/views]"]
    N275["Jobs.tsx [meridian_frontend/src/views]"]
    N276["MemoryEditor.tsx [meridian_frontend/src/views]"]
    N277["Productivity.tsx [meridian_frontend/src/views]"]
    N278["Settings.tsx [meridian_frontend/src/views]"]
    N279["SwarmDebate.tsx [meridian_frontend/src/views]"]
    N280["Timeline.tsx [meridian_frontend/src/views]"]
    N281["WorkflowBuilder.tsx [meridian_frontend/src/views]"]
    N282["config.py [meridian_frontend/src-tauri/api/_internal/cv2]"]
    N283["load_config_py3.py [meridian_frontend/src-tauri/api/_internal/cv2]"]
    N284["__init__.py [meridian_frontend/src-tauri/api/_internal/cv2]"]
    N285["__init__.py [meridian_frontend/src-tauri/api/_internal/cv2/data]"]
    N286["__init__.py [meridian_frontend/src-tauri/api/_internal/cv2/mat_wrapper]"]
    N287["version.py [meridian_frontend/src-tauri/api/_internal/cv2/misc]"]
    N288["__init__.py [meridian_frontend/src-tauri/api/_internal/cv2/typing]"]
    N289["__init__.py [meridian_frontend/src-tauri/api/_internal/cv2/utils]"]
    N290["applications.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N291["background.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N292["cli.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N293["concurrency.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N294["datastructures.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N295["encoders.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N296["exceptions.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N297["exception_handlers.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N298["logger.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N299["params.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N300["param_functions.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N301["requests.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N302["responses.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N303["routing.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N304["sse.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N305["staticfiles.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N306["templating.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N307["testclient.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N308["types.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N309["utils.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N310["websockets.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N311["__init__.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N312["__main__.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N313["models.py [meridian_frontend/src-tauri/api/_internal/fastapi/dependencies]"]
    N314["utils.py [meridian_frontend/src-tauri/api/_internal/fastapi/dependencies]"]
    N315["asyncexitstack.py [meridian_frontend/src-tauri/api/_internal/fastapi/middleware]"]
    N316["cors.py [meridian_frontend/src-tauri/api/_internal/fastapi/middleware]"]
    N317["gzip.py [meridian_frontend/src-tauri/api/_internal/fastapi/middleware]"]
    N318["httpsredirect.py [meridian_frontend/src-tauri/api/_internal/fastapi/middleware]"]
    N319["trustedhost.py [meridian_frontend/src-tauri/api/_internal/fastapi/middleware]"]
    N320["wsgi.py [meridian_frontend/src-tauri/api/_internal/fastapi/middleware]"]
    N321["__init__.py [meridian_frontend/src-tauri/api/_internal/fastapi/middleware]"]
    N322["docs.py [meridian_frontend/src-tauri/api/_internal/fastapi/openapi]"]
    N323["models.py [meridian_frontend/src-tauri/api/_internal/fastapi/openapi]"]
    N324["utils.py [meridian_frontend/src-tauri/api/_internal/fastapi/openapi]"]
    N325["api_key.py [meridian_frontend/src-tauri/api/_internal/fastapi/security]"]
    N326["base.py [meridian_frontend/src-tauri/api/_internal/fastapi/security]"]
    N327["http.py [meridian_frontend/src-tauri/api/_internal/fastapi/security]"]
    N328["oauth2.py [meridian_frontend/src-tauri/api/_internal/fastapi/security]"]
    N329["open_id_connect_url.py [meridian_frontend/src-tauri/api/_internal/fastapi/security]"]
    N330["shared.py [meridian_frontend/src-tauri/api/_internal/fastapi/_compat]"]
    N331["v2.py [meridian_frontend/src-tauri/api/_internal/fastapi/_compat]"]
    N332["coreBundle.js [meridian_frontend/src-tauri/api/_internal/playwright/driver/package/lib]"]
    N333["utilsBundle.js [meridian_frontend/src-tauri/api/_internal/playwright/driver/package/lib]"]
    N334["structs.d.ts [meridian_frontend/src-tauri/api/_internal/playwright/driver/package/types]"]
    N335["types.d.ts [meridian_frontend/src-tauri/api/_internal/playwright/driver/package/types]"]
    N336["aliases.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N337["alias_generators.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N338["annotated_handlers.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N339["color.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N340["config.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N341["dataclasses.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N342["errors.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N343["fields.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N344["functional_serializers.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N345["functional_validators.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N346["json_schema.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N347["main.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N348["mypy.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N349["networks.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N350["root_model.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N351["types.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N352["type_adapter.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N353["validate_call_decorator.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N354["version.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N355["warnings.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N356["_migration.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N357["__init__.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N358["class_validators.py [meridian_frontend/src-tauri/api/_internal/pydantic/deprecated]"]
    N359["config.py [meridian_frontend/src-tauri/api/_internal/pydantic/deprecated]"]
    N360["copy_internals.py [meridian_frontend/src-tauri/api/_internal/pydantic/deprecated]"]
    N361["decorator.py [meridian_frontend/src-tauri/api/_internal/pydantic/deprecated]"]
    N362["json.py [meridian_frontend/src-tauri/api/_internal/pydantic/deprecated]"]
    N363["parse.py [meridian_frontend/src-tauri/api/_internal/pydantic/deprecated]"]
    N364["tools.py [meridian_frontend/src-tauri/api/_internal/pydantic/deprecated]"]
    N365["arguments_schema.py [meridian_frontend/src-tauri/api/_internal/pydantic/experimental]"]
    N366["missing_sentinel.py [meridian_frontend/src-tauri/api/_internal/pydantic/experimental]"]
    N367["pipeline.py [meridian_frontend/src-tauri/api/_internal/pydantic/experimental]"]
    N368["_loader.py [meridian_frontend/src-tauri/api/_internal/pydantic/plugin]"]
    N369["_schema_validator.py [meridian_frontend/src-tauri/api/_internal/pydantic/plugin]"]
    N370["__init__.py [meridian_frontend/src-tauri/api/_internal/pydantic/plugin]"]
    N371["annotated_types.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N372["class_validators.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N373["color.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N374["config.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N375["dataclasses.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N376["datetime_parse.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N377["decorator.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N378["env_settings.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N379["errors.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N380["error_wrappers.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N381["fields.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N382["generics.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N383["json.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N384["main.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N385["mypy.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N386["networks.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N387["parse.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N388["schema.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N389["tools.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N390["types.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N391["typing.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N392["utils.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N393["validators.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N394["version.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N395["_hypothesis_plugin.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N396["__init__.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N397["_config.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N398["_core_metadata.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N399["_core_utils.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N400["_dataclasses.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N401["_decorators.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N402["_decorators_v1.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N403["_discriminated_union.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N404["_docs_extraction.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N405["_fields.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N406["_forward_ref.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N407["_generate_schema.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N408["_generics.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N409["_git.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N410["_import_utils.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N411["_internal_dataclass.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N412["_known_annotated_metadata.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N413["_mock_val_ser.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N414["_model_construction.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N415["_namespace_utils.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N416["_repr.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N417["_schema_gather.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N418["_schema_generation_shared.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N419["_serializers.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N420["_signature.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N421["_typing_extra.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N422["_utils.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N423["_validate_call.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N424["_validators.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N425["applications.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N426["authentication.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N427["background.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N428["concurrency.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N429["config.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N430["convertors.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N431["datastructures.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N432["endpoints.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N433["exceptions.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N434["formparsers.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N435["requests.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N436["responses.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N437["routing.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N438["schemas.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N439["staticfiles.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N440["status.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N441["templating.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N442["testclient.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N443["types.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N444["websockets.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N445["_exception_handler.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N446["_utils.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N447["authentication.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N448["base.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N449["cors.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N450["errors.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N451["exceptions.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N452["gzip.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N453["httpsredirect.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N454["sessions.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N455["trustedhost.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N456["wsgi.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N457["__init__.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N458["config.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N459["importer.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N460["logging.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N461["main.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N462["server.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N463["workers.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N464["_compat.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N465["_subprocess.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N466["_types.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N467["__init__.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N468["__main__.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N469["off.py [meridian_frontend/src-tauri/api/_internal/uvicorn/lifespan]"]
    N470["on.py [meridian_frontend/src-tauri/api/_internal/uvicorn/lifespan]"]
    N471["asyncio.py [meridian_frontend/src-tauri/api/_internal/uvicorn/loops]"]
    N472["auto.py [meridian_frontend/src-tauri/api/_internal/uvicorn/loops]"]
    N473["uvloop.py [meridian_frontend/src-tauri/api/_internal/uvicorn/loops]"]
    N474["asgi2.py [meridian_frontend/src-tauri/api/_internal/uvicorn/middleware]"]
    N475["message_logger.py [meridian_frontend/src-tauri/api/_internal/uvicorn/middleware]"]
    N476["proxy_headers.py [meridian_frontend/src-tauri/api/_internal/uvicorn/middleware]"]
    N477["wsgi.py [meridian_frontend/src-tauri/api/_internal/uvicorn/middleware]"]
    N478["utils.py [meridian_frontend/src-tauri/api/_internal/uvicorn/protocols]"]
    N479["auto.py [meridian_frontend/src-tauri/api/_internal/uvicorn/protocols/http]"]
    N480["flow_control.py [meridian_frontend/src-tauri/api/_internal/uvicorn/protocols/http]"]
    N481["h11_impl.py [meridian_frontend/src-tauri/api/_internal/uvicorn/protocols/http]"]
    N482["httptools_impl.py [meridian_frontend/src-tauri/api/_internal/uvicorn/protocols/http]"]
    N483["auto.py [meridian_frontend/src-tauri/api/_internal/uvicorn/protocols/websockets]"]
    N484["websockets_impl.py [meridian_frontend/src-tauri/api/_internal/uvicorn/protocols/websockets]"]
    N485["websockets_sansio_impl.py [meridian_frontend/src-tauri/api/_internal/uvicorn/protocols/websockets]"]
    N486["wsproto_impl.py [meridian_frontend/src-tauri/api/_internal/uvicorn/protocols/websockets]"]
    N487["basereload.py [meridian_frontend/src-tauri/api/_internal/uvicorn/supervisors]"]
    N488["multiprocess.py [meridian_frontend/src-tauri/api/_internal/uvicorn/supervisors]"]
    N489["statreload.py [meridian_frontend/src-tauri/api/_internal/uvicorn/supervisors]"]
    N490["watchfilesreload.py [meridian_frontend/src-tauri/api/_internal/uvicorn/supervisors]"]
    N491["__init__.py [meridian_frontend/src-tauri/api/_internal/uvicorn/supervisors]"]
    N492["auth.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N493["cli.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N494["client.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N495["connection.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N496["datastructures.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N497["exceptions.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N498["frames.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N499["headers.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N500["http11.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N501["imports.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N502["protocol.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N503["proxy.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N504["server.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N505["streams.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N506["typing.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N507["uri.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N508["utils.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N509["version.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N510["__init__.py [meridian_frontend/src-tauri/api/_internal/websockets]"]
    N511["client.py [meridian_frontend/src-tauri/api/_internal/websockets/asyncio]"]
    N512["connection.py [meridian_frontend/src-tauri/api/_internal/websockets/asyncio]"]
    N513["messages.py [meridian_frontend/src-tauri/api/_internal/websockets/asyncio]"]
    N514["router.py [meridian_frontend/src-tauri/api/_internal/websockets/asyncio]"]
    N515["server.py [meridian_frontend/src-tauri/api/_internal/websockets/asyncio]"]
    N516["base.py [meridian_frontend/src-tauri/api/_internal/websockets/extensions]"]
    N517["permessage_deflate.py [meridian_frontend/src-tauri/api/_internal/websockets/extensions]"]
    N518["auth.py [meridian_frontend/src-tauri/api/_internal/websockets/legacy]"]
    N519["client.py [meridian_frontend/src-tauri/api/_internal/websockets/legacy]"]
    N520["exceptions.py [meridian_frontend/src-tauri/api/_internal/websockets/legacy]"]
    N521["framing.py [meridian_frontend/src-tauri/api/_internal/websockets/legacy]"]
    N522["handshake.py [meridian_frontend/src-tauri/api/_internal/websockets/legacy]"]
    N523["http.py [meridian_frontend/src-tauri/api/_internal/websockets/legacy]"]
    N524["protocol.py [meridian_frontend/src-tauri/api/_internal/websockets/legacy]"]
    N525["server.py [meridian_frontend/src-tauri/api/_internal/websockets/legacy]"]
    N526["__init__.py [meridian_frontend/src-tauri/api/_internal/websockets/legacy]"]
    N527["client.py [meridian_frontend/src-tauri/api/_internal/websockets/sync]"]
    N528["connection.py [meridian_frontend/src-tauri/api/_internal/websockets/sync]"]
    N529["messages.py [meridian_frontend/src-tauri/api/_internal/websockets/sync]"]
    N530["router.py [meridian_frontend/src-tauri/api/_internal/websockets/sync]"]
    N531["server.py [meridian_frontend/src-tauri/api/_internal/websockets/sync]"]
    N532["utils.py [meridian_frontend/src-tauri/api/_internal/websockets/sync]"]
    N533["client.py [meridian_frontend/src-tauri/api/_internal/websockets/trio]"]
    N534["connection.py [meridian_frontend/src-tauri/api/_internal/websockets/trio]"]
    N535["messages.py [meridian_frontend/src-tauri/api/_internal/websockets/trio]"]
    N536["router.py [meridian_frontend/src-tauri/api/_internal/websockets/trio]"]
    N537["server.py [meridian_frontend/src-tauri/api/_internal/websockets/trio]"]
    N538["utils.py [meridian_frontend/src-tauri/api/_internal/websockets/trio]"]
    N539["build_apk.py [meridian_mobile]"]
    N540["flutter_lldb_helper.py [meridian_mobile/ios/Flutter/ephemeral]"]
    N541["get_system_platform_info.py [plugins]"]
    N542["ProfileHeader.tsx [src/components]"]

    N1 --> N362
    N1 --> N383
    N1 --> N391
    N1 --> N506
    N2 --> N362
    N2 --> N383
    N2 --> N391
    N2 --> N506
    N3 --> N362
    N3 --> N383
    N6 --> N471
    N6 --> N362
    N6 --> N383
    N6 --> N14
    N10 --> N341
    N10 --> N375
    N13 --> N10
    N13 --> N33
    N13 --> N282
    N13 --> N340
    N13 --> N359
    N13 --> N374
    N13 --> N429
    N13 --> N458
    N13 --> N12
    N13 --> N11
    N14 --> N471
    N14 --> N460
    N14 --> N362
    N14 --> N383
    N14 --> N391
    N14 --> N506
    N14 --> N15
    N15 --> N362
    N15 --> N383
    N15 --> N391
    N15 --> N506
    N16 --> N362
    N16 --> N383
    N16 --> N471
    N16 --> N460
    N16 --> N391
    N16 --> N506
    N19 --> N362
    N19 --> N383
    N19 --> N460
    N19 --> N391
    N19 --> N506
    N19 --> N15
    N20 --> N471
    N20 --> N460
    N20 --> N391
    N20 --> N506
    N21 --> N460
    N21 --> N391
    N21 --> N506
    N22 --> N362
    N22 --> N383
    N22 --> N460
    N23 --> N391
    N23 --> N506
    N23 --> N362
    N23 --> N383
    N24 --> N460
    N24 --> N391
    N24 --> N506
    N25 --> N460
    N25 --> N391
    N25 --> N506
    N26 --> N460
    N26 --> N391
    N26 --> N506
    N26 --> N362
    N26 --> N383
    N27 --> N471
    N27 --> N391
    N27 --> N506
    N28 --> N460
    N28 --> N391
    N28 --> N506
    N29 --> N391
    N29 --> N506
    N29 --> N15
    N30 --> N391
    N30 --> N506
    N31 --> N362
    N31 --> N383
    N31 --> N460
    N31 --> N391
    N31 --> N506
    N32 --> N460
    N32 --> N391
    N32 --> N506
    N34 --> N362
    N34 --> N383
    N34 --> N460
    N34 --> N391
    N34 --> N506
    N35 --> N460
    N35 --> N391
    N35 --> N506
    N36 --> N471
    N36 --> N460
    N36 --> N391
    N36 --> N506
    N37 --> N471
    N37 --> N391
    N37 --> N506
    N37 --> N15
    N39 --> N362
    N39 --> N383
    N39 --> N391
    N39 --> N506
    N39 --> N15
    N39 --> N460
    N40 --> N460
    N40 --> N391
    N40 --> N506
    N41 --> N460
    N41 --> N391
    N41 --> N506
    N42 --> N460
    N42 --> N391
    N42 --> N506
    N43 --> N460
    N43 --> N391
    N43 --> N506
    N44 --> N391
    N44 --> N506
    N44 --> N15
    N45 --> N460
    N45 --> N391
    N45 --> N506
    N46 --> N460
    N46 --> N391
    N46 --> N506
    N47 --> N391
    N47 --> N506
    N48 --> N362
    N48 --> N383
    N48 --> N391
    N48 --> N506
    N49 --> N362
    N49 --> N383
    N49 --> N391
    N49 --> N506
    N50 --> N460
    N50 --> N391
    N50 --> N506
    N50 --> N362
    N50 --> N383
    N52 --> N362
    N52 --> N383
    N52 --> N460
    N52 --> N471
    N52 --> N391
    N52 --> N506
    N52 --> N15
    N53 --> N460
    N53 --> N471
    N53 --> N391
    N53 --> N506
    N53 --> N15
    N53 --> N362
    N53 --> N383
    N54 --> N460
    N54 --> N362
    N54 --> N383
    N55 --> N362
    N55 --> N383
    N55 --> N471
    N55 --> N391
    N55 --> N506
    N55 --> N15
    N56 --> N471
    N56 --> N391
    N56 --> N506
    N57 --> N362
    N57 --> N383
    N57 --> N471
    N57 --> N391
    N57 --> N506
    N57 --> N15
    N58 --> N362
    N58 --> N383
    N58 --> N471
    N58 --> N391
    N58 --> N506
    N58 --> N15
    N59 --> N362
    N59 --> N383
    N59 --> N471
    N59 --> N391
    N59 --> N506
    N60 --> N460
    N60 --> N391
    N60 --> N506
    N61 --> N362
    N61 --> N383
    N61 --> N471
    N61 --> N460
    N61 --> N391
    N61 --> N506
    N62 --> N471
    N62 --> N362
    N62 --> N383
    N62 --> N460
    N62 --> N391
    N62 --> N506
    N63 --> N362
    N63 --> N383
    N63 --> N391
    N63 --> N506
    N64 --> N460
    N64 --> N471
    N64 --> N362
    N64 --> N383
    N64 --> N391
    N64 --> N506
    N64 --> N15
    N65 --> N362
    N65 --> N383
    N65 --> N391
    N65 --> N506
    N65 --> N15
    N66 --> N362
    N66 --> N383
    N66 --> N460
    N66 --> N391
    N66 --> N506
    N66 --> N15
    N66 --> N471
    N67 --> N391
    N67 --> N506
    N67 --> N15
    N67 --> N362
    N67 --> N383
    N68 --> N391
    N68 --> N506
    N69 --> N362
    N69 --> N383
    N69 --> N391
    N69 --> N506
    N70 --> N460
    N70 --> N471
    N70 --> N391
    N70 --> N506
    N70 --> N362
    N70 --> N383
    N71 --> N362
    N71 --> N383
    N71 --> N391
    N71 --> N506
    N71 --> N15
    N72 --> N460
    N72 --> N391
    N72 --> N506
    N73 --> N460
    N73 --> N391
    N73 --> N506
    N74 --> N460
    N74 --> N391
    N74 --> N506
    N74 --> N15
    N75 --> N391
    N75 --> N506
    N76 --> N460
    N76 --> N391
    N76 --> N506
    N77 --> N460
    N77 --> N391
    N77 --> N506
    N78 --> N460
    N78 --> N391
    N78 --> N506
    N79 --> N471
    N79 --> N391
    N79 --> N506
    N79 --> N15
    N79 --> N14
    N80 --> N460
    N80 --> N391
    N80 --> N506
    N81 --> N460
    N81 --> N391
    N81 --> N506
    N82 --> N362
    N82 --> N383
    N82 --> N391
    N82 --> N506
    N83 --> N391
    N83 --> N506
    N84 --> N391
    N84 --> N506
    N85 --> N460
    N85 --> N391
    N85 --> N506
    N86 --> N471
    N86 --> N15
    N86 --> N362
    N86 --> N383
    N87 --> N471
    N87 --> N460
    N87 --> N391
    N87 --> N506
    N88 --> N460
    N88 --> N391
    N88 --> N506
    N89 --> N460
    N89 --> N391
    N89 --> N506
    N90 --> N460
    N90 --> N391
    N90 --> N506
    N91 --> N460
    N91 --> N391
    N91 --> N506
    N91 --> N15
    N92 --> N362
    N92 --> N383
    N92 --> N471
    N92 --> N391
    N92 --> N506
    N92 --> N15
    N93 --> N471
    N93 --> N362
    N93 --> N383
    N93 --> N391
    N93 --> N506
    N93 --> N15
    N94 --> N460
    N94 --> N391
    N94 --> N506
    N95 --> N391
    N95 --> N506
    N95 --> N471
    N95 --> N15
    N96 --> N391
    N96 --> N506
    N97 --> N460
    N97 --> N391
    N97 --> N506
    N98 --> N391
    N98 --> N506
    N99 --> N460
    N99 --> N391
    N99 --> N506
    N100 --> N362
    N100 --> N383
    N100 --> N391
    N100 --> N506
    N101 --> N460
    N101 --> N391
    N101 --> N506
    N101 --> N15
    N102 --> N460
    N102 --> N391
    N102 --> N506
    N103 --> N460
    N103 --> N391
    N103 --> N506
    N104 --> N460
    N104 --> N391
    N104 --> N506
    N105 --> N460
    N105 --> N391
    N105 --> N506
    N106 --> N362
    N106 --> N383
    N106 --> N391
    N106 --> N506
    N107 --> N460
    N107 --> N391
    N107 --> N506
    N108 --> N391
    N108 --> N506
    N109 --> N362
    N109 --> N383
    N109 --> N391
    N109 --> N506
    N110 --> N460
    N110 --> N391
    N110 --> N506
    N111 --> N362
    N111 --> N383
    N111 --> N391
    N111 --> N506
    N112 --> N362
    N112 --> N383
    N112 --> N391
    N112 --> N506
    N112 --> N471
    N112 --> N15
    N113 --> N391
    N113 --> N506
    N114 --> N391
    N114 --> N506
    N114 --> N15
    N115 --> N391
    N115 --> N506
    N115 --> N15
    N116 --> N460
    N116 --> N391
    N116 --> N506
    N116 --> N15
    N117 --> N391
    N117 --> N506
    N117 --> N15
    N118 --> N391
    N118 --> N506
    N118 --> N15
    N119 --> N391
    N119 --> N506
    N120 --> N471
    N120 --> N391
    N120 --> N506
    N121 --> N391
    N121 --> N506
    N122 --> N391
    N122 --> N506
    N123 --> N460
    N123 --> N391
    N123 --> N506
    N124 --> N362
    N124 --> N383
    N124 --> N391
    N124 --> N506
    N125 --> N362
    N125 --> N383
    N125 --> N391
    N125 --> N506
    N125 --> N15
    N126 --> N362
    N126 --> N383
    N126 --> N301
    N126 --> N435
    N126 --> N391
    N126 --> N506
    N127 --> N391
    N127 --> N506
    N128 --> N391
    N128 --> N506
    N129 --> N362
    N129 --> N383
    N129 --> N391
    N129 --> N506
    N130 --> N391
    N130 --> N506
    N131 --> N391
    N131 --> N506
    N132 --> N362
    N132 --> N383
    N132 --> N391
    N132 --> N506
    N133 --> N391
    N133 --> N506
    N133 --> N15
    N134 --> N460
    N134 --> N391
    N134 --> N506
    N135 --> N362
    N135 --> N383
    N135 --> N391
    N135 --> N506
    N136 --> N391
    N136 --> N506
    N137 --> N460
    N137 --> N391
    N137 --> N506
    N138 --> N15
    N139 --> N362
    N139 --> N383
    N139 --> N391
    N139 --> N506
    N139 --> N341
    N139 --> N375
    N139 --> N10
    N139 --> N33
    N139 --> N282
    N139 --> N340
    N139 --> N359
    N139 --> N374
    N139 --> N429
    N139 --> N458
    N139 --> N12
    N139 --> N11
    N140 --> N391
    N140 --> N506
    N141 --> N391
    N141 --> N506
    N142 --> N362
    N142 --> N383
    N142 --> N471
    N142 --> N460
    N142 --> N391
    N142 --> N506
    N142 --> N15
    N143 --> N460
    N143 --> N391
    N143 --> N506
    N144 --> N362
    N144 --> N383
    N144 --> N15
    N145 --> N471
    N145 --> N391
    N145 --> N506
    N145 --> N15
    N145 --> N362
    N145 --> N383
    N146 --> N391
    N146 --> N506
    N146 --> N15
    N148 --> N362
    N148 --> N383
    N148 --> N391
    N148 --> N506
    N149 --> N391
    N149 --> N506
    N149 --> N15
    N150 --> N391
    N150 --> N506
    N151 --> N391
    N151 --> N506
    N151 --> N15
    N152 --> N15
    N154 --> N391
    N154 --> N506
    N155 --> N362
    N155 --> N383
    N155 --> N391
    N155 --> N506
    N156 --> N391
    N156 --> N506
    N157 --> N391
    N157 --> N506
    N157 --> N362
    N157 --> N383
    N158 --> N460
    N158 --> N391
    N158 --> N506
    N160 --> N391
    N160 --> N506
    N161 --> N391
    N161 --> N506
    N161 --> N15
    N162 --> N362
    N162 --> N383
    N162 --> N391
    N162 --> N506
    N162 --> N15
    N163 --> N391
    N163 --> N506
    N164 --> N362
    N164 --> N383
    N164 --> N460
    N164 --> N391
    N164 --> N506
    N164 --> N15
    N165 --> N460
    N165 --> N391
    N165 --> N506
    N166 --> N460
    N166 --> N391
    N166 --> N506
    N167 --> N471
    N167 --> N460
    N167 --> N391
    N167 --> N506
    N168 --> N471
    N168 --> N391
    N168 --> N506
    N169 --> N460
    N169 --> N391
    N169 --> N506
    N170 --> N391
    N170 --> N506
    N170 --> N15
    N171 --> N460
    N171 --> N391
    N171 --> N506
    N171 --> N15
    N172 --> N391
    N172 --> N506
    N173 --> N460
    N173 --> N15
    N177 --> N471
    N177 --> N14
    N179 --> N15
    N180 --> N14
    N185 --> N15
    N186 --> N14
    N189 --> N15
    N191 --> N15
    N192 --> N471
    N198 --> N15
    N199 --> N15
    N200 --> N14
    N202 --> N362
    N202 --> N383
    N202 --> N15
    N204 --> N362
    N204 --> N383
    N204 --> N15
    N204 --> N471
    N205 --> N471
    N205 --> N14
    N211 --> N471
    N212 --> N460
    N212 --> N362
    N212 --> N383
    N213 --> N362
    N213 --> N383
    N214 --> N471
    N215 --> N362
    N215 --> N383
    N215 --> N14
    N215 --> N471
    N216 --> N15
    N218 --> N471
    N218 --> N14
    N220 --> N15
    N221 --> N471
    N222 --> N362
    N222 --> N383
    N223 --> N471
    N223 --> N14
    N224 --> N14
    N224 --> N391
    N224 --> N506
    N224 --> N471
    N225 --> N14
    N226 --> N362
    N226 --> N383
    N226 --> N16
    N227 --> N471
    N228 --> N471
    N229 --> N362
    N229 --> N383
    N233 --> N14
    N234 --> N14
    N235 --> N14
    N238 --> N308
    N238 --> N335
    N238 --> N351
    N238 --> N390
    N238 --> N443
    N238 --> N10
    N238 --> N33
    N238 --> N282
    N238 --> N340
    N238 --> N359
    N238 --> N374
    N238 --> N429
    N238 --> N458
    N239 --> N494
    N239 --> N511
    N239 --> N519
    N239 --> N527
    N239 --> N533
    N239 --> N240
    N239 --> N271
    N239 --> N273
    N239 --> N255
    N239 --> N238
    N239 --> N10
    N239 --> N33
    N239 --> N282
    N239 --> N340
    N239 --> N359
    N239 --> N374
    N239 --> N429
    N239 --> N458
    N239 --> N272
    N239 --> N270
    N240 --> N241
    N240 --> N10
    N240 --> N33
    N240 --> N282
    N240 --> N340
    N240 --> N359
    N240 --> N374
    N240 --> N429
    N240 --> N458
    N240 --> N238
    N240 --> N269
    N242 --> N257
    N242 --> N259
    N242 --> N258
    N243 --> N10
    N243 --> N33
    N243 --> N282
    N243 --> N340
    N243 --> N359
    N243 --> N374
    N243 --> N429
    N243 --> N458
    N245 --> N10
    N245 --> N33
    N245 --> N282
    N245 --> N340
    N245 --> N359
    N245 --> N374
    N245 --> N429
    N245 --> N458
    N246 --> N10
    N246 --> N33
    N246 --> N282
    N246 --> N340
    N246 --> N359
    N246 --> N374
    N246 --> N429
    N246 --> N458
    N247 --> N266
    N247 --> N10
    N247 --> N33
    N247 --> N282
    N247 --> N340
    N247 --> N359
    N247 --> N374
    N247 --> N429
    N247 --> N458
    N248 --> N10
    N248 --> N33
    N248 --> N282
    N248 --> N340
    N248 --> N359
    N248 --> N374
    N248 --> N429
    N248 --> N458
    N249 --> N238
    N249 --> N240
    N251 --> N10
    N251 --> N33
    N251 --> N282
    N251 --> N340
    N251 --> N359
    N251 --> N374
    N251 --> N429
    N251 --> N458
    N253 --> N238
    N253 --> N264
    N253 --> N261
    N254 --> N10
    N254 --> N33
    N254 --> N282
    N254 --> N340
    N254 --> N359
    N254 --> N374
    N254 --> N429
    N254 --> N458
    N255 --> N238
    N255 --> N249
    N255 --> N256
    N255 --> N253
    N255 --> N244
    N255 --> N266
    N255 --> N280
    N255 --> N275
    N255 --> N274
    N255 --> N277
    N255 --> N279
    N255 --> N281
    N255 --> N276
    N255 --> N278
    N255 --> N260
    N255 --> N251
    N256 --> N238
    N256 --> N10
    N256 --> N33
    N256 --> N282
    N256 --> N340
    N256 --> N359
    N256 --> N374
    N256 --> N429
    N256 --> N458
    N256 --> N261
    N260 --> N267
    N268 --> N10
    N268 --> N33
    N268 --> N282
    N268 --> N340
    N268 --> N359
    N268 --> N374
    N268 --> N429
    N268 --> N458
    N269 --> N10
    N269 --> N33
    N269 --> N282
    N269 --> N340
    N269 --> N359
    N269 --> N374
    N269 --> N429
    N269 --> N458
    N270 --> N10
    N270 --> N33
    N270 --> N282
    N270 --> N340
    N270 --> N359
    N270 --> N374
    N270 --> N429
    N270 --> N458
    N271 --> N10
    N271 --> N33
    N271 --> N282
    N271 --> N340
    N271 --> N359
    N271 --> N374
    N271 --> N429
    N271 --> N458
    N271 --> N240
    N272 --> N10
    N272 --> N33
    N272 --> N282
    N272 --> N340
    N272 --> N359
    N272 --> N374
    N272 --> N429
    N272 --> N458
    N273 --> N263
    N273 --> N10
    N273 --> N33
    N273 --> N282
    N273 --> N340
    N273 --> N359
    N273 --> N374
    N273 --> N429
    N273 --> N458
    N274 --> N308
    N274 --> N335
    N274 --> N351
    N274 --> N390
    N274 --> N443
    N274 --> N238
    N274 --> N263
    N274 --> N10
    N274 --> N33
    N274 --> N282
    N274 --> N340
    N274 --> N359
    N274 --> N374
    N274 --> N429
    N274 --> N458
    N275 --> N308
    N275 --> N335
    N275 --> N351
    N275 --> N390
    N275 --> N443
    N275 --> N263
    N275 --> N262
    N275 --> N10
    N275 --> N33
    N275 --> N282
    N275 --> N340
    N275 --> N359
    N275 --> N374
    N275 --> N429
    N275 --> N458
    N276 --> N10
    N276 --> N33
    N276 --> N282
    N276 --> N340
    N276 --> N359
    N276 --> N374
    N276 --> N429
    N276 --> N458
    N277 --> N308
    N277 --> N335
    N277 --> N351
    N277 --> N390
    N277 --> N443
    N277 --> N264
    N277 --> N263
    N277 --> N262
    N277 --> N10
    N277 --> N33
    N277 --> N282
    N277 --> N340
    N277 --> N359
    N277 --> N374
    N277 --> N429
    N277 --> N458
    N277 --> N247
    N277 --> N248
    N277 --> N245
    N277 --> N243
    N277 --> N246
    N278 --> N10
    N278 --> N33
    N278 --> N282
    N278 --> N340
    N278 --> N359
    N278 --> N374
    N278 --> N429
    N278 --> N458
    N278 --> N308
    N278 --> N335
    N278 --> N351
    N278 --> N390
    N278 --> N443
    N278 --> N238
    N278 --> N267
    N278 --> N264
    N278 --> N263
    N278 --> N262
    N279 --> N265
    N279 --> N263
    N279 --> N10
    N279 --> N33
    N279 --> N282
    N279 --> N340
    N279 --> N359
    N279 --> N374
    N279 --> N429
    N279 --> N458
    N280 --> N308
    N280 --> N335
    N280 --> N351
    N280 --> N390
    N280 --> N443
    N280 --> N263
    N280 --> N262
    N280 --> N10
    N280 --> N33
    N280 --> N282
    N280 --> N340
    N280 --> N359
    N280 --> N374
    N280 --> N429
    N280 --> N458
    N280 --> N269
    N281 --> N10
    N281 --> N33
    N281 --> N282
    N281 --> N340
    N281 --> N359
    N281 --> N374
    N281 --> N429
    N281 --> N458
    N286 --> N391
    N286 --> N506
    N288 --> N391
    N288 --> N506
    N290 --> N391
    N290 --> N506
    N291 --> N391
    N291 --> N506
    N293 --> N391
    N293 --> N506
    N294 --> N391
    N294 --> N506
    N295 --> N341
    N295 --> N375
    N295 --> N308
    N295 --> N335
    N295 --> N351
    N295 --> N390
    N295 --> N443
    N295 --> N391
    N295 --> N506
    N296 --> N391
    N296 --> N506
    N298 --> N460
    N299 --> N355
    N299 --> N341
    N299 --> N375
    N299 --> N391
    N299 --> N506
    N300 --> N391
    N300 --> N506
    N302 --> N391
    N302 --> N506
    N303 --> N362
    N303 --> N383
    N303 --> N308
    N303 --> N335
    N303 --> N351
    N303 --> N390
    N303 --> N443
    N303 --> N341
    N303 --> N375
    N303 --> N391
    N303 --> N506
    N304 --> N391
    N304 --> N506
    N308 --> N335
    N308 --> N351
    N308 --> N390
    N308 --> N443
    N308 --> N391
    N308 --> N506
    N309 --> N355
    N309 --> N391
    N309 --> N506
    N313 --> N341
    N313 --> N375
    N313 --> N391
    N313 --> N506
    N313 --> N471
    N314 --> N341
    N314 --> N375
    N314 --> N391
    N314 --> N506
    N322 --> N362
    N322 --> N383
    N322 --> N391
    N322 --> N506
    N323 --> N391
    N323 --> N506
    N324 --> N327
    N324 --> N523
    N324 --> N355
    N324 --> N391
    N324 --> N506
    N325 --> N391
    N325 --> N506
    N327 --> N391
    N327 --> N506
    N328 --> N391
    N328 --> N506
    N329 --> N391
    N329 --> N506
    N330 --> N308
    N330 --> N335
    N330 --> N351
    N330 --> N390
    N330 --> N443
    N330 --> N391
    N330 --> N506
    N330 --> N355
    N330 --> N341
    N330 --> N375
    N331 --> N355
    N331 --> N341
    N331 --> N375
    N331 --> N391
    N331 --> N506
    N334 --> N308
    N334 --> N335
    N334 --> N351
    N334 --> N390
    N334 --> N443
    N335 --> N502
    N335 --> N524
    N335 --> N334
    N336 --> N341
    N336 --> N375
    N336 --> N391
    N336 --> N506
    N338 --> N391
    N338 --> N506
    N339 --> N391
    N339 --> N506
    N340 --> N355
    N340 --> N391
    N340 --> N506
    N341 --> N375
    N341 --> N308
    N341 --> N335
    N341 --> N351
    N341 --> N390
    N341 --> N443
    N341 --> N391
    N341 --> N506
    N341 --> N355
    N342 --> N391
    N342 --> N506
    N343 --> N341
    N343 --> N375
    N343 --> N391
    N343 --> N506
    N343 --> N355
    N343 --> N371
    N344 --> N341
    N344 --> N375
    N344 --> N391
    N344 --> N506
    N345 --> N341
    N345 --> N375
    N345 --> N355
    N345 --> N391
    N345 --> N506
    N346 --> N341
    N346 --> N375
    N346 --> N355
    N346 --> N391
    N346 --> N506
    N347 --> N308
    N347 --> N335
    N347 --> N351
    N347 --> N390
    N347 --> N443
    N347 --> N355
    N347 --> N391
    N347 --> N506
    N347 --> N362
    N347 --> N383
    N348 --> N391
    N348 --> N506
    N348 --> N385
    N348 --> N355
    N349 --> N341
    N349 --> N375
    N349 --> N391
    N349 --> N506
    N350 --> N391
    N350 --> N506
    N351 --> N341
    N351 --> N375
    N351 --> N308
    N351 --> N335
    N351 --> N390
    N351 --> N443
    N351 --> N391
    N351 --> N506
    N351 --> N371
    N351 --> N362
    N351 --> N383
    N352 --> N308
    N352 --> N335
    N352 --> N351
    N352 --> N390
    N352 --> N443
    N352 --> N341
    N352 --> N375
    N352 --> N391
    N352 --> N506
    N353 --> N308
    N353 --> N335
    N353 --> N351
    N353 --> N390
    N353 --> N443
    N353 --> N391
    N353 --> N506
    N356 --> N391
    N356 --> N506
    N356 --> N355
    N357 --> N391
    N357 --> N506
    N357 --> N355
    N358 --> N308
    N358 --> N335
    N358 --> N351
    N358 --> N390
    N358 --> N443
    N358 --> N391
    N358 --> N506
    N358 --> N355
    N359 --> N355
    N359 --> N391
    N359 --> N506
    N360 --> N391
    N360 --> N506
    N361 --> N355
    N361 --> N391
    N361 --> N506
    N362 --> N355
    N362 --> N308
    N362 --> N335
    N362 --> N351
    N362 --> N390
    N362 --> N443
    N362 --> N391
    N362 --> N506
    N362 --> N341
    N362 --> N375
    N363 --> N362
    N363 --> N383
    N363 --> N355
    N363 --> N391
    N363 --> N506
    N364 --> N362
    N364 --> N383
    N364 --> N355
    N364 --> N391
    N364 --> N506
    N365 --> N391
    N365 --> N506
    N367 --> N341
    N367 --> N375
    N367 --> N391
    N367 --> N506
    N367 --> N371
    N367 --> N308
    N367 --> N335
    N367 --> N351
    N367 --> N390
    N367 --> N443
    N368 --> N355
    N368 --> N391
    N368 --> N506
    N369 --> N391
    N369 --> N506
    N370 --> N391
    N370 --> N506
    N371 --> N391
    N371 --> N506
    N372 --> N355
    N372 --> N308
    N372 --> N335
    N372 --> N351
    N372 --> N390
    N372 --> N443
    N372 --> N391
    N372 --> N506
    N373 --> N391
    N373 --> N506
    N374 --> N362
    N374 --> N383
    N374 --> N391
    N374 --> N506
    N375 --> N341
    N375 --> N391
    N375 --> N506
    N376 --> N391
    N376 --> N506
    N377 --> N391
    N377 --> N506
    N378 --> N355
    N378 --> N391
    N378 --> N506
    N379 --> N391
    N379 --> N506
    N380 --> N362
    N380 --> N383
    N380 --> N391
    N380 --> N506
    N381 --> N391
    N381 --> N506
    N382 --> N308
    N382 --> N335
    N382 --> N351
    N382 --> N390
    N382 --> N443
    N382 --> N391
    N382 --> N506
    N383 --> N308
    N383 --> N335
    N383 --> N351
    N383 --> N390
    N383 --> N443
    N383 --> N391
    N383 --> N506
    N383 --> N341
    N383 --> N375
    N384 --> N355
    N384 --> N308
    N384 --> N335
    N384 --> N351
    N384 --> N390
    N384 --> N443
    N384 --> N391
    N384 --> N506
    N385 --> N391
    N385 --> N506
    N385 --> N348
    N385 --> N355
    N386 --> N391
    N386 --> N506
    N387 --> N362
    N387 --> N383
    N387 --> N391
    N387 --> N506
    N388 --> N355
    N388 --> N341
    N388 --> N375
    N388 --> N391
    N388 --> N506
    N389 --> N362
    N389 --> N383
    N389 --> N391
    N389 --> N506
    N390 --> N355
    N390 --> N308
    N390 --> N335
    N390 --> N351
    N390 --> N443
    N390 --> N391
    N390 --> N506
    N391 --> N506
    N391 --> N308
    N391 --> N335
    N391 --> N351
    N391 --> N390
    N391 --> N443
    N392 --> N355
    N392 --> N308
    N392 --> N335
    N392 --> N351
    N392 --> N390
    N392 --> N443
    N392 --> N391
    N392 --> N506
    N393 --> N391
    N393 --> N506
    N393 --> N355
    N395 --> N362
    N395 --> N383
    N395 --> N391
    N395 --> N506
    N397 --> N355
    N397 --> N391
    N397 --> N506
    N398 --> N391
    N398 --> N506
    N398 --> N355
    N399 --> N391
    N399 --> N506
    N400 --> N341
    N400 --> N375
    N400 --> N355
    N400 --> N391
    N400 --> N506
    N401 --> N308
    N401 --> N335
    N401 --> N351
    N401 --> N390
    N401 --> N443
    N401 --> N341
    N401 --> N375
    N401 --> N391
    N401 --> N506
    N402 --> N391
    N402 --> N506
    N403 --> N391
    N403 --> N506
    N404 --> N391
    N404 --> N506
    N405 --> N341
    N405 --> N375
    N405 --> N355
    N405 --> N391
    N405 --> N506
    N405 --> N371
    N406 --> N341
    N406 --> N375
    N406 --> N391
    N406 --> N506
    N407 --> N341
    N407 --> N375
    N407 --> N391
    N407 --> N506
    N407 --> N355
    N407 --> N308
    N407 --> N335
    N407 --> N351
    N407 --> N390
    N407 --> N443
    N408 --> N308
    N408 --> N335
    N408 --> N351
    N408 --> N390
    N408 --> N443
    N408 --> N391
    N408 --> N506
    N410 --> N391
    N410 --> N506
    N412 --> N391
    N412 --> N506
    N412 --> N371
    N413 --> N391
    N413 --> N506
    N414 --> N391
    N414 --> N506
    N414 --> N355
    N414 --> N308
    N414 --> N335
    N414 --> N351
    N414 --> N390
    N414 --> N443
    N415 --> N391
    N415 --> N506
    N416 --> N308
    N416 --> N335
    N416 --> N351
    N416 --> N390
    N416 --> N443
    N416 --> N391
    N416 --> N506
    N417 --> N341
    N417 --> N375
    N417 --> N391
    N417 --> N506
    N418 --> N391
    N418 --> N506
    N419 --> N391
    N419 --> N506
    N420 --> N341
    N420 --> N375
    N420 --> N391
    N420 --> N506
    N421 --> N308
    N421 --> N335
    N421 --> N351
    N421 --> N390
    N421 --> N443
    N421 --> N391
    N421 --> N506
    N422 --> N341
    N422 --> N375
    N422 --> N355
    N422 --> N308
    N422 --> N335
    N422 --> N351
    N422 --> N390
    N422 --> N443
    N422 --> N391
    N422 --> N506
    N423 --> N391
    N423 --> N506
    N424 --> N391
    N424 --> N506
    N425 --> N391
    N425 --> N506
    N426 --> N391
    N426 --> N506
    N427 --> N391
    N427 --> N506
    N428 --> N355
    N428 --> N391
    N428 --> N506
    N429 --> N355
    N429 --> N391
    N429 --> N506
    N430 --> N391
    N430 --> N506
    N431 --> N391
    N431 --> N506
    N432 --> N362
    N432 --> N383
    N432 --> N391
    N432 --> N506
    N433 --> N327
    N433 --> N523
    N434 --> N341
    N434 --> N375
    N434 --> N391
    N434 --> N506
    N435 --> N362
    N435 --> N383
    N435 --> N327
    N435 --> N523
    N435 --> N391
    N435 --> N506
    N436 --> N327
    N436 --> N523
    N436 --> N362
    N436 --> N383
    N436 --> N391
    N436 --> N506
    N437 --> N308
    N437 --> N335
    N437 --> N351
    N437 --> N390
    N437 --> N443
    N437 --> N355
    N437 --> N391
    N437 --> N506
    N438 --> N391
    N438 --> N506
    N439 --> N391
    N439 --> N506
    N440 --> N355
    N441 --> N391
    N441 --> N506
    N442 --> N362
    N442 --> N383
    N442 --> N355
    N442 --> N308
    N442 --> N335
    N442 --> N351
    N442 --> N390
    N442 --> N443
    N442 --> N391
    N442 --> N506
    N443 --> N391
    N443 --> N506
    N444 --> N362
    N444 --> N383
    N444 --> N391
    N444 --> N506
    N445 --> N391
    N445 --> N506
    N446 --> N391
    N446 --> N506
    N446 --> N471
    N448 --> N391
    N448 --> N506
    N451 --> N391
    N451 --> N506
    N452 --> N317
    N452 --> N391
    N452 --> N506
    N454 --> N362
    N454 --> N383
    N454 --> N391
    N454 --> N506
    N456 --> N355
    N456 --> N391
    N456 --> N506
    N457 --> N391
    N457 --> N506
    N458 --> N471
    N458 --> N362
    N458 --> N383
    N458 --> N460
    N458 --> N391
    N458 --> N506
    N459 --> N391
    N459 --> N506
    N460 --> N327
    N460 --> N523
    N460 --> N391
    N460 --> N506
    N461 --> N471
    N461 --> N460
    N461 --> N355
    N461 --> N391
    N461 --> N506
    N462 --> N471
    N462 --> N460
    N462 --> N308
    N462 --> N335
    N462 --> N351
    N462 --> N390
    N462 --> N443
    N462 --> N391
    N462 --> N506
    N463 --> N471
    N463 --> N460
    N463 --> N355
    N463 --> N391
    N463 --> N506
    N464 --> N471
    N464 --> N391
    N464 --> N506
    N466 --> N308
    N466 --> N335
    N466 --> N351
    N466 --> N390
    N466 --> N443
    N466 --> N391
    N466 --> N506
    N469 --> N391
    N469 --> N506
    N470 --> N471
    N470 --> N460
    N470 --> N391
    N470 --> N506
    N472 --> N471
    N472 --> N473
    N473 --> N471
    N475 --> N460
    N475 --> N391
    N475 --> N506
    N477 --> N471
    N477 --> N355
    N478 --> N471
    N479 --> N471
    N480 --> N471
    N481 --> N471
    N481 --> N327
    N481 --> N523
    N481 --> N460
    N481 --> N391
    N481 --> N506
    N482 --> N471
    N482 --> N327
    N482 --> N523
    N482 --> N460
    N482 --> N391
    N482 --> N506
    N483 --> N471
    N483 --> N310
    N483 --> N444
    N484 --> N471
    N484 --> N327
    N484 --> N523
    N484 --> N460
    N484 --> N391
    N484 --> N506
    N484 --> N310
    N484 --> N444
    N485 --> N471
    N485 --> N460
    N485 --> N327
    N485 --> N523
    N485 --> N391
    N485 --> N506
    N485 --> N310
    N485 --> N444
    N486 --> N471
    N486 --> N460
    N486 --> N391
    N486 --> N506
    N487 --> N460
    N487 --> N308
    N487 --> N335
    N487 --> N351
    N487 --> N390
    N487 --> N443
    N488 --> N460
    N488 --> N391
    N488 --> N506
    N489 --> N460
    N491 --> N391
    N491 --> N506
    N492 --> N355
    N493 --> N471
    N493 --> N391
    N493 --> N506
    N494 --> N355
    N494 --> N391
    N494 --> N506
    N495 --> N355
    N496 --> N391
    N496 --> N506
    N497 --> N355
    N498 --> N341
    N498 --> N375
    N498 --> N391
    N498 --> N506
    N499 --> N391
    N499 --> N506
    N500 --> N341
    N500 --> N375
    N500 --> N355
    N500 --> N391
    N500 --> N506
    N501 --> N355
    N501 --> N391
    N501 --> N506
    N502 --> N460
    N503 --> N341
    N503 --> N375
    N504 --> N327
    N504 --> N523
    N504 --> N355
    N504 --> N391
    N504 --> N506
    N506 --> N327
    N506 --> N523
    N506 --> N460
    N506 --> N391
    N507 --> N341
    N507 --> N375
    N510 --> N391
    N510 --> N506
    N511 --> N471
    N511 --> N460
    N511 --> N308
    N511 --> N335
    N511 --> N351
    N511 --> N390
    N511 --> N443
    N511 --> N391
    N511 --> N506
    N511 --> N310
    N511 --> N444
    N512 --> N471
    N512 --> N460
    N512 --> N308
    N512 --> N335
    N512 --> N351
    N512 --> N390
    N512 --> N443
    N512 --> N391
    N512 --> N506
    N513 --> N471
    N513 --> N391
    N513 --> N506
    N514 --> N327
    N514 --> N523
    N514 --> N391
    N514 --> N506
    N514 --> N310
    N514 --> N444
    N515 --> N471
    N515 --> N327
    N515 --> N523
    N515 --> N460
    N515 --> N308
    N515 --> N335
    N515 --> N351
    N515 --> N390
    N515 --> N443
    N515 --> N391
    N515 --> N506
    N515 --> N310
    N515 --> N444
    N517 --> N391
    N517 --> N506
    N518 --> N327
    N518 --> N523
    N518 --> N391
    N518 --> N506
    N519 --> N471
    N519 --> N460
    N519 --> N355
    N519 --> N308
    N519 --> N335
    N519 --> N351
    N519 --> N390
    N519 --> N443
    N519 --> N391
    N519 --> N506
    N520 --> N327
    N520 --> N523
    N521 --> N391
    N521 --> N506
    N523 --> N471
    N524 --> N471
    N524 --> N460
    N524 --> N355
    N524 --> N391
    N524 --> N506
    N525 --> N471
    N525 --> N327
    N525 --> N523
    N525 --> N460
    N525 --> N355
    N525 --> N308
    N525 --> N335
    N525 --> N351
    N525 --> N390
    N525 --> N443
    N525 --> N391
    N525 --> N506
    N526 --> N355
    N527 --> N460
    N527 --> N355
    N527 --> N308
    N527 --> N335
    N527 --> N351
    N527 --> N390
    N527 --> N443
    N527 --> N391
    N527 --> N506
    N527 --> N310
    N527 --> N444
    N528 --> N460
    N528 --> N308
    N528 --> N335
    N528 --> N351
    N528 --> N390
    N528 --> N443
    N528 --> N391
    N528 --> N506
    N529 --> N391
    N529 --> N506
    N530 --> N327
    N530 --> N523
    N530 --> N391
    N530 --> N506
    N530 --> N310
    N530 --> N444
    N531 --> N327
    N531 --> N523
    N531 --> N460
    N531 --> N355
    N531 --> N308
    N531 --> N335
    N531 --> N351
    N531 --> N390
    N531 --> N443
    N531 --> N391
    N531 --> N506
    N531 --> N310
    N531 --> N444
    N533 --> N460
    N533 --> N308
    N533 --> N335
    N533 --> N351
    N533 --> N390
    N533 --> N443
    N533 --> N391
    N533 --> N506
    N533 --> N310
    N533 --> N444
    N534 --> N460
    N534 --> N308
    N534 --> N335
    N534 --> N351
    N534 --> N390
    N534 --> N443
    N534 --> N391
    N534 --> N506
    N535 --> N391
    N535 --> N506
    N536 --> N327
    N536 --> N523
    N536 --> N391
    N536 --> N506
    N536 --> N310
    N536 --> N444
    N537 --> N327
    N537 --> N523
    N537 --> N460
    N537 --> N308
    N537 --> N335
    N537 --> N351
    N537 --> N390
    N537 --> N443
    N537 --> N391
    N537 --> N506
    N537 --> N310
    N537 --> N444
```

## Detailed File Index
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
  - Imports: `ast`
  - Imports: `asyncio`
  - Imports: `base64`
  - Imports: `contextlib`
  - Imports: `contextvars`
  - Imports: `database`
  - Imports: `fastapi`
  - Imports: `hashlib`
  - Imports: `hmac`
  - Imports: `httpx`
  - Imports: `io`
  - Imports: `json`
  - Imports: `logging`
  - Imports: `numpy`
  - Imports: `ollama`
  - Imports: `os`
  - Imports: `platform`
  - Imports: `prometheus_client`
  - Imports: `psutil`
  - Imports: `pydantic`
  - Imports: `random`
  - Imports: `re`
  - Imports: `secrets`
  - Imports: `shutil`
  - Imports: `signal`
  - Imports: `slowapi`
  - Imports: `socket`
  - Imports: `soundfile`
  - Imports: `src`
  - Imports: `subprocess`
  - Imports: `sys`
  - Imports: `tempfile`
  - Imports: `threading`
  - Imports: `time`
  - Imports: `trustme`
  - Imports: `typing`
  - Imports: `urllib`
  - Imports: `uuid`
  - Imports: `uvicorn`
  - Imports: `webbrowser`
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
- **meridian_backend/src/core/consensus_engine.py**
  - Imports: `datetime`
  - Imports: `json`
  - Imports: `logging`
  - Imports: `re`
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
  - Imports: `os`
  - Imports: `platform`
  - Imports: `psutil`
  - Imports: `pynvml`
  - Imports: `subprocess`
  - Imports: `sys`
  - Imports: `typing`
- **meridian_backend/src/core/history_manager.py**
  - Imports: `os`
  - Imports: `subprocess`
- **meridian_backend/src/core/llm_provider.py**
  - Imports: `asyncio`
  - Imports: `concurrent`
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
  - Imports: `anthropic`
  - Imports: `ast`
  - Imports: `asyncio`
  - Imports: `database`
  - Imports: `inspect`
  - Imports: `json`
  - Imports: `ollama`
  - Imports: `openai`
  - Imports: `os`
  - Imports: `psutil`
  - Imports: `random`
  - Imports: `re`
  - Imports: `src`
  - Imports: `subprocess`
  - Imports: `threading`
  - Imports: `time`
  - Imports: `typing`
  - Imports: `uuid`
- **meridian_backend/src/core/loop_dispatcher.py**
  - Imports: `asyncio`
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
- **meridian_backend/src/core/loop_stream.py**
  - Imports: `asyncio`
  - Imports: `database`
  - Imports: `json`
  - Imports: `src`
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
  - Imports: `base64`
  - Imports: `cryptography`
  - Imports: `database`
  - Imports: `hashlib`
  - Imports: `hmac`
  - Imports: `json`
  - Imports: `os`
  - Imports: `secrets`
  - Imports: `socket`
  - Imports: `src`
  - Imports: `threading`
  - Imports: `time`
  - Imports: `typing`
  - Imports: `zeroconf`
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
- **meridian_backend/src/core/proactive.py**
  - Imports: `api`
  - Imports: `asyncio`
  - Imports: `ctypes`
  - Imports: `database`
  - Imports: `datetime`
  - Imports: `ollama`
  - Imports: `os`
  - Imports: `platform`
  - Imports: `psutil`
  - Imports: `random`
  - Imports: `re`
  - Imports: `socket`
  - Imports: `src`
  - Imports: `subprocess`
  - Imports: `threading`
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
  - Imports: `os`
  - Imports: `psutil`
  - Imports: `pynvml`
  - Imports: `src`
  - Imports: `time`
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
  - Imports: `docx`
  - Imports: `importlib`
  - Imports: `openpyxl`
  - Imports: `os`
  - Imports: `pptx`
  - Imports: `pypdf`
  - Imports: `re`
  - Imports: `reportlab`
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
  - Imports: `Quartz`
  - Imports: `database`
  - Imports: `ewmh`
  - Imports: `os`
  - Imports: `platform`
  - Imports: `psutil`
  - Imports: `pyautogui`
  - Imports: `pygetwindow`
  - Imports: `pyperclip`
  - Imports: `src`
  - Imports: `subprocess`
  - Imports: `sys`
  - Imports: `time`
  - Imports: `webbrowser`
  - Imports: `winreg`
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
  - Imports: `ipaddress`
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
  - Imports: `MemoryEditor`
  - Imports: `NavRail`
  - Imports: `ProactiveGuardBanner`
  - Imports: `Productivity`
  - Imports: `RightDrawer`
  - Imports: `Settings`
  - Imports: `StatusBar`
  - Imports: `SwarmDebate`
  - Imports: `Timeline`
  - Imports: `ToastContext`
  - Imports: `WorkflowBuilder`
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
- **src/components/ProfileHeader.tsx**
  - Imports: `react`
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