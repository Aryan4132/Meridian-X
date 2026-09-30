# Workspace Architecture & Component Map
Generated automatically by Meridian-X.

## Component Dependency Graph
```mermaid
graph TD
    N1["build_standalone.py []"]
    N2["bump_version.py []"]
    N3["cleanup.py []"]
    N4["create_shortcut.py []"]
    N5["main.py []"]
    N6["setup_db.py []"]
    N7["setup_startup.py []"]
    N8["verify_system.py []"]
    N9["config.py [generated_repos/attention_is_all_you_need__transformer_]"]
    N10["dataset.py [generated_repos/attention_is_all_you_need__transformer_]"]
    N11["model.py [generated_repos/attention_is_all_you_need__transformer_]"]
    N12["trainer.py [generated_repos/attention_is_all_you_need__transformer_]"]
    N13["api.py [meridian_backend]"]
    N14["database.py [meridian_backend]"]
    N15["tests_run.py [meridian_backend]"]
    N16["action_journal.py [meridian_backend/src/core]"]
    N17["ar_bridge.py [meridian_backend/src/core]"]
    N18["audit_logger.py [meridian_backend/src/core]"]
    N19["auth.py [meridian_backend/src/core]"]
    N20["behavior_monitor.py [meridian_backend/src/core]"]
    N21["breach_sentinel.py [meridian_backend/src/core]"]
    N22["bus.py [meridian_backend/src/core]"]
    N23["camera_sentinel.py [meridian_backend/src/core]"]
    N24["clipboard.py [meridian_backend/src/core]"]
    N25["code_graph.py [meridian_backend/src/core]"]
    N26["config.py [meridian_backend/src/core]"]
    N27["discord_bridge.py [meridian_backend/src/core]"]
    N28["doc_generator.py [meridian_backend/src/core]"]
    N29["doc_indexer.py [meridian_backend/src/core]"]
    N30["elevated_runner.py [meridian_backend/src/core]"]
    N31["emergency_lockdown.py [meridian_backend/src/core]"]
    N32["exporter.py [meridian_backend/src/core]"]
    N33["fim_sentinel.py [meridian_backend/src/core]"]
    N34["gaze_tracker.py [meridian_backend/src/core]"]
    N35["governor.py [meridian_backend/src/core]"]
    N36["graph_rag.py [meridian_backend/src/core]"]
    N37["graph_sync.py [meridian_backend/src/core]"]
    N38["hardware_detector.py [meridian_backend/src/core]"]
    N39["history_manager.py [meridian_backend/src/core]"]
    N40["llm_provider.py [meridian_backend/src/core]"]
    N41["logging_config.py [meridian_backend/src/core]"]
    N42["loop.py [meridian_backend/src/core]"]
    N43["loop_dispatcher.py [meridian_backend/src/core]"]
    N44["loop_parser.py [meridian_backend/src/core]"]
    N45["loop_stream.py [meridian_backend/src/core]"]
    N46["lsp_client.py [meridian_backend/src/core]"]
    N47["malware_scanner.py [meridian_backend/src/core]"]
    N48["mcp_client.py [meridian_backend/src/core]"]
    N49["mcp_executor.py [meridian_backend/src/core]"]
    N50["memory_backup.py [meridian_backend/src/core]"]
    N51["memory_editor.py [meridian_backend/src/core]"]
    N52["mobile_bridge.py [meridian_backend/src/core]"]
    N53["mode.py [meridian_backend/src/core]"]
    N54["neural_rag.py [meridian_backend/src/core]"]
    N55["oauth_manager.py [meridian_backend/src/core]"]
    N56["ollama_manager.py [meridian_backend/src/core]"]
    N57["p2p.py [meridian_backend/src/core]"]
    N58["perception.py [meridian_backend/src/core]"]
    N59["persistence_sentinel.py [meridian_backend/src/core]"]
    N60["personal_crm.py [meridian_backend/src/core]"]
    N61["plugins.py [meridian_backend/src/core]"]
    N62["predictive_engine.py [meridian_backend/src/core]"]
    N63["presence_briefing.py [meridian_backend/src/core]"]
    N64["proactive.py [meridian_backend/src/core]"]
    N65["prompt_injection.py [meridian_backend/src/core]"]
    N66["prompt_templates.py [meridian_backend/src/core]"]
    N67["rag_optimizer.py [meridian_backend/src/core]"]
    N68["sandbox_runner.py [meridian_backend/src/core]"]
    N69["scheduler.py [meridian_backend/src/core]"]
    N70["screen_sense.py [meridian_backend/src/core]"]
    N71["security_middleware.py [meridian_backend/src/core]"]
    N72["sos_protocol.py [meridian_backend/src/core]"]
    N73["speculative.py [meridian_backend/src/core]"]
    N74["swarm.py [meridian_backend/src/core]"]
    N75["system_defense.py [meridian_backend/src/core]"]
    N76["telegram_bridge.py [meridian_backend/src/core]"]
    N77["temporal_memory.py [meridian_backend/src/core]"]
    N78["triggers.py [meridian_backend/src/core]"]
    N79["updater.py [meridian_backend/src/core]"]
    N80["vault.py [meridian_backend/src/core]"]
    N81["vision.py [meridian_backend/src/core]"]
    N82["vision_face.py [meridian_backend/src/core]"]
    N83["watcher.py [meridian_backend/src/core]"]
    N84["workflow_engine.py [meridian_backend/src/core]"]
    N85["auto_reviewer.py [meridian_backend/src/tools]"]
    N86["bill_radar.py [meridian_backend/src/tools]"]
    N87["browser_agent.py [meridian_backend/src/tools]"]
    N88["cam_guard.py [meridian_backend/src/tools]"]
    N89["chrome_manager.py [meridian_backend/src/tools]"]
    N90["clipboard.py [meridian_backend/src/tools]"]
    N91["communication.py [meridian_backend/src/tools]"]
    N92["db_query.py [meridian_backend/src/tools]"]
    N93["desktop.py [meridian_backend/src/tools]"]
    N94["detonation_sandbox.py [meridian_backend/src/tools]"]
    N95["developer.py [meridian_backend/src/tools]"]
    N96["dns_shield.py [meridian_backend/src/tools]"]
    N97["documents.py [meridian_backend/src/tools]"]
    N98["dynamic_manager.py [meridian_backend/src/tools]"]
    N99["expiry_sentinel.py [meridian_backend/src/tools]"]
    N100["exporter.py [meridian_backend/src/tools]"]
    N101["external_connectors.py [meridian_backend/src/tools]"]
    N102["filesystem.py [meridian_backend/src/tools]"]
    N103["file_janitor.py [meridian_backend/src/tools]"]
    N104["finance_sentinel.py [meridian_backend/src/tools]"]
    N105["geo_location.py [meridian_backend/src/tools]"]
    N106["health_ingest.py [meridian_backend/src/tools]"]
    N107["household.py [meridian_backend/src/tools]"]
    N108["knowledge.py [meridian_backend/src/tools]"]
    N109["mcp_marketplace.py [meridian_backend/src/tools]"]
    N110["media_player.py [meridian_backend/src/tools]"]
    N111["network_guardian.py [meridian_backend/src/tools]"]
    N112["ollama_manager.py [meridian_backend/src/tools]"]
    N113["papercoder.py [meridian_backend/src/tools]"]
    N114["password_auditor.py [meridian_backend/src/tools]"]
    N115["phishing_guard.py [meridian_backend/src/tools]"]
    N116["phone_agent.py [meridian_backend/src/tools]"]
    N117["recording.py [meridian_backend/src/tools]"]
    N118["registry.py [meridian_backend/src/tools]"]
    N119["review.py [meridian_backend/src/tools]"]
    N120["scheduler.py [meridian_backend/src/tools]"]
    N121["screenshot_memory.py [meridian_backend/src/tools]"]
    N122["search_hub.py [meridian_backend/src/tools]"]
    N123["security_auditor.py [meridian_backend/src/tools]"]
    N124["shell.py [meridian_backend/src/tools]"]
    N125["system.py [meridian_backend/src/tools]"]
    N126["task_scheduler.py [meridian_backend/src/tools]"]
    N127["totp_generator.py [meridian_backend/src/tools]"]
    N128["travel_butler.py [meridian_backend/src/tools]"]
    N129["usb_watchdog.py [meridian_backend/src/tools]"]
    N130["vault.py [meridian_backend/src/tools]"]
    N131["video_editor.py [meridian_backend/src/tools]"]
    N132["voice.py [meridian_backend/src/tools]"]
    N133["watcher.py [meridian_backend/src/tools]"]
    N134["web.py [meridian_backend/src/tools]"]
    N135["web_browser.py [meridian_backend/src/tools]"]
    N136["wellness.py [meridian_backend/src/tools]"]
    N137["whatsapp_manager.py [meridian_backend/src/tools]"]
    N138["ambient_listener.py [meridian_backend/src/voice]"]
    N139["duplex.py [meridian_backend/src/voice]"]
    N140["polyglot.py [meridian_backend/src/voice]"]
    N141["stt.py [meridian_backend/src/voice]"]
    N142["tts.py [meridian_backend/src/voice]"]
    N143["voice_biometrics.py [meridian_backend/src/voice]"]
    N144["wakeword.py [meridian_backend/src/voice]"]
    N145["conftest.py [meridian_backend/tests]"]
    N146["run_tests.py [meridian_backend/tests]"]
    N147["test_auto_bug_fixer.py [meridian_backend/tests]"]
    N148["test_backlog_features.py [meridian_backend/tests]"]
    N149["test_backlog_sprint.py [meridian_backend/tests]"]
    N150["test_bridges.py [meridian_backend/tests]"]
    N151["test_browser_agent.py [meridian_backend/tests]"]
    N152["test_butler_media.py [meridian_backend/tests]"]
    N153["test_config.py [meridian_backend/tests]"]
    N154["test_context_budget.py [meridian_backend/tests]"]
    N155["test_database.py [meridian_backend/tests]"]
    N156["test_day10_features.py [meridian_backend/tests]"]
    N157["test_day11_features.py [meridian_backend/tests]"]
    N158["test_day12_features.py [meridian_backend/tests]"]
    N159["test_day13_features.py [meridian_backend/tests]"]
    N160["test_day14_day15_features.py [meridian_backend/tests]"]
    N161["test_day3_features.py [meridian_backend/tests]"]
    N162["test_day4_features.py [meridian_backend/tests]"]
    N163["test_day5_features.py [meridian_backend/tests]"]
    N164["test_day6_features.py [meridian_backend/tests]"]
    N165["test_day7_features.py [meridian_backend/tests]"]
    N166["test_day8_features.py [meridian_backend/tests]"]
    N167["test_day9_features.py [meridian_backend/tests]"]
    N168["test_document_tools.py [meridian_backend/tests]"]
    N169["test_geo_location.py [meridian_backend/tests]"]
    N170["test_jarvis_perception.py [meridian_backend/tests]"]
    N171["test_known_errors_remediation.py [meridian_backend/tests]"]
    N172["test_llm_provider.py [meridian_backend/tests]"]
    N173["test_logging.py [meridian_backend/tests]"]
    N174["test_loop_parser.py [meridian_backend/tests]"]
    N175["test_loop_submodules.py [meridian_backend/tests]"]
    N176["test_mobile_websocket.py [meridian_backend/tests]"]
    N177["test_model_source.py [meridian_backend/tests]"]
    N178["test_multi_os.py [meridian_backend/tests]"]
    N179["test_oauth.py [meridian_backend/tests]"]
    N180["test_p2p.py [meridian_backend/tests]"]
    N181["test_proactive.py [meridian_backend/tests]"]
    N182["test_proactive_notifications.py [meridian_backend/tests]"]
    N183["test_security_features.py [meridian_backend/tests]"]
    N184["test_sprint2_features.py [meridian_backend/tests]"]
    N185["test_stream_resiliency.py [meridian_backend/tests]"]
    N186["test_swarm.py [meridian_backend/tests]"]
    N187["test_tools.py [meridian_backend/tests]"]
    N188["test_tool_regression.py [meridian_backend/tests]"]
    N189["test_vault.py [meridian_backend/tests]"]
    N190["test_video_editor.py [meridian_backend/tests]"]
    N191["test_voice_speed.py [meridian_backend/tests]"]
    N192["test_wakeword_continuous.py [meridian_backend/tests]"]
    N193["test_wakeword_onnx.py [meridian_backend/tests]"]
    N194["test_workflow.py [meridian_backend/tests]"]
    N195["vite.config.ts [meridian_frontend]"]
    N196["AppContext.tsx [meridian_frontend/src]"]
    N197["main.tsx [meridian_frontend/src]"]
    N198["Mascot.tsx [meridian_frontend/src]"]
    N199["Mascot3DCharacter.tsx [meridian_frontend/src]"]
    N200["MobileApp.tsx [meridian_frontend/src]"]
    N201["CommandPalette.tsx [meridian_frontend/src/components]"]
    N202["NavRail.tsx [meridian_frontend/src/components]"]
    N203["RightDrawer.tsx [meridian_frontend/src/components]"]
    N204["ServerConnectionModal.tsx [meridian_frontend/src/components]"]
    N205["Shell.tsx [meridian_frontend/src/components]"]
    N206["StatusBar.tsx [meridian_frontend/src/components]"]
    N207["DropdownNav.tsx [meridian_frontend/src/components/mobile]"]
    N208["LiveThoughtCarousel.tsx [meridian_frontend/src/components/mobile]"]
    N209["QRScannerModal.tsx [meridian_frontend/src/components/mobile]"]
    N210["VoiceOrbHUD.tsx [meridian_frontend/src/components/mobile]"]
    N211["AmbientParticles.tsx [meridian_frontend/src/components/ui]"]
    N212["DataBadge.tsx [meridian_frontend/src/components/ui]"]
    N213["GlowCard.tsx [meridian_frontend/src/components/ui]"]
    N214["HoloButton.tsx [meridian_frontend/src/components/ui]"]
    N215["ProgressArc.tsx [meridian_frontend/src/components/ui]"]
    N216["TerminalLine.tsx [meridian_frontend/src/components/ui]"]
    N217["useMemoryOptimizer.ts [meridian_frontend/src/hooks]"]
    N218["oauthService.ts [meridian_frontend/src/services]"]
    N219["BackendSetup.tsx [meridian_frontend/src/startup]"]
    N220["BootSequence.tsx [meridian_frontend/src/startup]"]
    N221["OnboardingWizard.tsx [meridian_frontend/src/startup]"]
    N222["SetupWizard.tsx [meridian_frontend/src/startup]"]
    N223["Clipboard.tsx [meridian_frontend/src/views]"]
    N224["Jobs.tsx [meridian_frontend/src/views]"]
    N225["MemoryEditor.tsx [meridian_frontend/src/views]"]
    N226["Productivity.tsx [meridian_frontend/src/views]"]
    N227["Settings.tsx [meridian_frontend/src/views]"]
    N228["SwarmDebate.tsx [meridian_frontend/src/views]"]
    N229["Timeline.tsx [meridian_frontend/src/views]"]
    N230["WorkflowBuilder.tsx [meridian_frontend/src/views]"]
    N231["config.py [meridian_frontend/src-tauri/api/_internal/cv2]"]
    N232["load_config_py3.py [meridian_frontend/src-tauri/api/_internal/cv2]"]
    N233["__init__.py [meridian_frontend/src-tauri/api/_internal/cv2]"]
    N234["__init__.py [meridian_frontend/src-tauri/api/_internal/cv2/data]"]
    N235["__init__.py [meridian_frontend/src-tauri/api/_internal/cv2/mat_wrapper]"]
    N236["version.py [meridian_frontend/src-tauri/api/_internal/cv2/misc]"]
    N237["__init__.py [meridian_frontend/src-tauri/api/_internal/cv2/typing]"]
    N238["__init__.py [meridian_frontend/src-tauri/api/_internal/cv2/utils]"]
    N239["applications.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N240["background.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N241["cli.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N242["concurrency.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N243["datastructures.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N244["encoders.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N245["exceptions.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N246["exception_handlers.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N247["logger.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N248["params.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N249["param_functions.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N250["requests.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N251["responses.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N252["routing.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N253["sse.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N254["staticfiles.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N255["templating.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N256["testclient.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N257["types.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N258["utils.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N259["websockets.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N260["__init__.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N261["__main__.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N262["models.py [meridian_frontend/src-tauri/api/_internal/fastapi/dependencies]"]
    N263["utils.py [meridian_frontend/src-tauri/api/_internal/fastapi/dependencies]"]
    N264["asyncexitstack.py [meridian_frontend/src-tauri/api/_internal/fastapi/middleware]"]
    N265["cors.py [meridian_frontend/src-tauri/api/_internal/fastapi/middleware]"]
    N266["gzip.py [meridian_frontend/src-tauri/api/_internal/fastapi/middleware]"]
    N267["httpsredirect.py [meridian_frontend/src-tauri/api/_internal/fastapi/middleware]"]
    N268["trustedhost.py [meridian_frontend/src-tauri/api/_internal/fastapi/middleware]"]
    N269["wsgi.py [meridian_frontend/src-tauri/api/_internal/fastapi/middleware]"]
    N270["__init__.py [meridian_frontend/src-tauri/api/_internal/fastapi/middleware]"]
    N271["docs.py [meridian_frontend/src-tauri/api/_internal/fastapi/openapi]"]
    N272["models.py [meridian_frontend/src-tauri/api/_internal/fastapi/openapi]"]
    N273["utils.py [meridian_frontend/src-tauri/api/_internal/fastapi/openapi]"]
    N274["api_key.py [meridian_frontend/src-tauri/api/_internal/fastapi/security]"]
    N275["base.py [meridian_frontend/src-tauri/api/_internal/fastapi/security]"]
    N276["http.py [meridian_frontend/src-tauri/api/_internal/fastapi/security]"]
    N277["oauth2.py [meridian_frontend/src-tauri/api/_internal/fastapi/security]"]
    N278["open_id_connect_url.py [meridian_frontend/src-tauri/api/_internal/fastapi/security]"]
    N279["shared.py [meridian_frontend/src-tauri/api/_internal/fastapi/_compat]"]
    N280["v2.py [meridian_frontend/src-tauri/api/_internal/fastapi/_compat]"]
    N281["coreBundle.js [meridian_frontend/src-tauri/api/_internal/playwright/driver/package/lib]"]
    N282["utilsBundle.js [meridian_frontend/src-tauri/api/_internal/playwright/driver/package/lib]"]
    N283["structs.d.ts [meridian_frontend/src-tauri/api/_internal/playwright/driver/package/types]"]
    N284["types.d.ts [meridian_frontend/src-tauri/api/_internal/playwright/driver/package/types]"]
    N285["aliases.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N286["alias_generators.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N287["annotated_handlers.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N288["color.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N289["config.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N290["dataclasses.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N291["errors.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N292["fields.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N293["functional_serializers.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N294["functional_validators.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N295["json_schema.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N296["main.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N297["mypy.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N298["networks.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N299["root_model.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N300["types.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N301["type_adapter.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N302["validate_call_decorator.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N303["version.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N304["warnings.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N305["_migration.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N306["__init__.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N307["class_validators.py [meridian_frontend/src-tauri/api/_internal/pydantic/deprecated]"]
    N308["config.py [meridian_frontend/src-tauri/api/_internal/pydantic/deprecated]"]
    N309["copy_internals.py [meridian_frontend/src-tauri/api/_internal/pydantic/deprecated]"]
    N310["decorator.py [meridian_frontend/src-tauri/api/_internal/pydantic/deprecated]"]
    N311["json.py [meridian_frontend/src-tauri/api/_internal/pydantic/deprecated]"]
    N312["parse.py [meridian_frontend/src-tauri/api/_internal/pydantic/deprecated]"]
    N313["tools.py [meridian_frontend/src-tauri/api/_internal/pydantic/deprecated]"]
    N314["arguments_schema.py [meridian_frontend/src-tauri/api/_internal/pydantic/experimental]"]
    N315["missing_sentinel.py [meridian_frontend/src-tauri/api/_internal/pydantic/experimental]"]
    N316["pipeline.py [meridian_frontend/src-tauri/api/_internal/pydantic/experimental]"]
    N317["_loader.py [meridian_frontend/src-tauri/api/_internal/pydantic/plugin]"]
    N318["_schema_validator.py [meridian_frontend/src-tauri/api/_internal/pydantic/plugin]"]
    N319["__init__.py [meridian_frontend/src-tauri/api/_internal/pydantic/plugin]"]
    N320["annotated_types.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N321["class_validators.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N322["color.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N323["config.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N324["dataclasses.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N325["datetime_parse.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N326["decorator.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N327["env_settings.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N328["errors.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N329["error_wrappers.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N330["fields.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N331["generics.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N332["json.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N333["main.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N334["mypy.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N335["networks.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N336["parse.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N337["schema.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N338["tools.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N339["types.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N340["typing.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N341["utils.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N342["validators.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N343["version.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N344["_hypothesis_plugin.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N345["__init__.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N346["_config.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N347["_core_metadata.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N348["_core_utils.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N349["_dataclasses.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N350["_decorators.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N351["_decorators_v1.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N352["_discriminated_union.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N353["_docs_extraction.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N354["_fields.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N355["_forward_ref.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N356["_generate_schema.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N357["_generics.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N358["_git.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N359["_import_utils.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N360["_internal_dataclass.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N361["_known_annotated_metadata.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N362["_mock_val_ser.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N363["_model_construction.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N364["_namespace_utils.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N365["_repr.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N366["_schema_gather.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N367["_schema_generation_shared.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N368["_serializers.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N369["_signature.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N370["_typing_extra.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N371["_utils.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N372["_validate_call.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N373["_validators.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N374["applications.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N375["authentication.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N376["background.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N377["concurrency.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N378["config.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N379["convertors.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N380["datastructures.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N381["endpoints.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N382["exceptions.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N383["formparsers.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N384["requests.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N385["responses.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N386["routing.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N387["schemas.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N388["staticfiles.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N389["status.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N390["templating.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N391["testclient.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N392["types.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N393["websockets.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N394["_exception_handler.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N395["_utils.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N396["authentication.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N397["base.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N398["cors.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N399["errors.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N400["exceptions.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N401["gzip.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N402["httpsredirect.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N403["sessions.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N404["trustedhost.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N405["wsgi.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N406["__init__.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N407["config.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N408["importer.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N409["logging.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N410["main.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N411["server.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N412["workers.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N413["_compat.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N414["_subprocess.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N415["_types.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N416["__init__.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N417["__main__.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N418["off.py [meridian_frontend/src-tauri/api/_internal/uvicorn/lifespan]"]
    N419["on.py [meridian_frontend/src-tauri/api/_internal/uvicorn/lifespan]"]
    N420["asyncio.py [meridian_frontend/src-tauri/api/_internal/uvicorn/loops]"]
    N421["auto.py [meridian_frontend/src-tauri/api/_internal/uvicorn/loops]"]
    N422["uvloop.py [meridian_frontend/src-tauri/api/_internal/uvicorn/loops]"]
    N423["asgi2.py [meridian_frontend/src-tauri/api/_internal/uvicorn/middleware]"]
    N424["message_logger.py [meridian_frontend/src-tauri/api/_internal/uvicorn/middleware]"]
    N425["proxy_headers.py [meridian_frontend/src-tauri/api/_internal/uvicorn/middleware]"]
    N426["wsgi.py [meridian_frontend/src-tauri/api/_internal/uvicorn/middleware]"]
    N427["utils.py [meridian_frontend/src-tauri/api/_internal/uvicorn/protocols]"]
    N428["auto.py [meridian_frontend/src-tauri/api/_internal/uvicorn/protocols/http]"]
    N429["flow_control.py [meridian_frontend/src-tauri/api/_internal/uvicorn/protocols/http]"]
    N430["h11_impl.py [meridian_frontend/src-tauri/api/_internal/uvicorn/protocols/http]"]
    N431["httptools_impl.py [meridian_frontend/src-tauri/api/_internal/uvicorn/protocols/http]"]
    N432["auto.py [meridian_frontend/src-tauri/api/_internal/uvicorn/protocols/websockets]"]
    N433["websockets_impl.py [meridian_frontend/src-tauri/api/_internal/uvicorn/protocols/websockets]"]
    N434["websockets_sansio_impl.py [meridian_frontend/src-tauri/api/_internal/uvicorn/protocols/websockets]"]
    N435["wsproto_impl.py [meridian_frontend/src-tauri/api/_internal/uvicorn/protocols/websockets]"]
    N436["basereload.py [meridian_frontend/src-tauri/api/_internal/uvicorn/supervisors]"]
    N437["multiprocess.py [meridian_frontend/src-tauri/api/_internal/uvicorn/supervisors]"]
    N438["statreload.py [meridian_frontend/src-tauri/api/_internal/uvicorn/supervisors]"]
    N439["watchfilesreload.py [meridian_frontend/src-tauri/api/_internal/uvicorn/supervisors]"]
    N440["__init__.py [meridian_frontend/src-tauri/api/_internal/uvicorn/supervisors]"]
    N441["build_apk.py [meridian_mobile]"]
    N442["vite.config.ts [meridian_mobile]"]
    N443["App.tsx [meridian_mobile/src]"]
    N444["main.tsx [meridian_mobile/src]"]
    N445["MobileApp.tsx [meridian_mobile/src]"]
    N446["DropdownNav.tsx [meridian_mobile/src/components]"]
    N447["DropdownNav.tsx [meridian_mobile/src/components/mobile]"]
    N448["LiveThoughtCarousel.tsx [meridian_mobile/src/components/mobile]"]
    N449["QRScannerModal.tsx [meridian_mobile/src/components/mobile]"]
    N450["ServerConnectionModal.tsx [meridian_mobile/src/components/mobile]"]
    N451["VoiceOrbHUD.tsx [meridian_mobile/src/components/mobile]"]
    N452["get_system_platform_info.py [plugins]"]

    N1 --> N311
    N1 --> N332
    N1 --> N340
    N2 --> N311
    N2 --> N332
    N5 --> N420
    N5 --> N311
    N5 --> N332
    N5 --> N13
    N9 --> N290
    N9 --> N324
    N12 --> N9
    N12 --> N26
    N12 --> N231
    N12 --> N289
    N12 --> N308
    N12 --> N323
    N12 --> N378
    N12 --> N407
    N12 --> N11
    N12 --> N10
    N13 --> N420
    N13 --> N409
    N13 --> N311
    N13 --> N332
    N13 --> N340
    N13 --> N14
    N14 --> N311
    N14 --> N332
    N14 --> N340
    N16 --> N311
    N16 --> N332
    N16 --> N409
    N16 --> N340
    N16 --> N14
    N17 --> N340
    N18 --> N311
    N18 --> N332
    N18 --> N409
    N19 --> N340
    N20 --> N409
    N20 --> N340
    N21 --> N409
    N21 --> N340
    N22 --> N420
    N22 --> N340
    N23 --> N340
    N24 --> N340
    N24 --> N14
    N25 --> N340
    N27 --> N420
    N27 --> N340
    N27 --> N14
    N29 --> N311
    N29 --> N332
    N29 --> N340
    N29 --> N14
    N30 --> N409
    N30 --> N340
    N31 --> N409
    N31 --> N340
    N32 --> N340
    N32 --> N14
    N33 --> N409
    N33 --> N340
    N34 --> N340
    N35 --> N340
    N36 --> N311
    N36 --> N332
    N36 --> N340
    N37 --> N311
    N37 --> N332
    N37 --> N340
    N38 --> N409
    N38 --> N340
    N40 --> N311
    N40 --> N332
    N40 --> N409
    N40 --> N420
    N40 --> N340
    N40 --> N14
    N41 --> N409
    N41 --> N311
    N41 --> N332
    N42 --> N311
    N42 --> N332
    N42 --> N420
    N42 --> N340
    N42 --> N14
    N43 --> N420
    N43 --> N340
    N44 --> N311
    N44 --> N332
    N44 --> N420
    N44 --> N340
    N44 --> N14
    N45 --> N311
    N45 --> N332
    N45 --> N420
    N45 --> N340
    N45 --> N14
    N46 --> N311
    N46 --> N332
    N46 --> N420
    N46 --> N340
    N47 --> N409
    N47 --> N340
    N48 --> N311
    N48 --> N332
    N48 --> N420
    N48 --> N409
    N48 --> N340
    N49 --> N420
    N49 --> N311
    N49 --> N332
    N49 --> N409
    N49 --> N340
    N50 --> N311
    N50 --> N332
    N50 --> N340
    N51 --> N311
    N51 --> N332
    N51 --> N340
    N51 --> N14
    N52 --> N311
    N52 --> N332
    N52 --> N420
    N52 --> N409
    N52 --> N340
    N53 --> N340
    N53 --> N311
    N53 --> N332
    N53 --> N14
    N54 --> N340
    N55 --> N311
    N55 --> N332
    N55 --> N340
    N56 --> N409
    N56 --> N420
    N56 --> N340
    N56 --> N311
    N56 --> N332
    N57 --> N311
    N57 --> N332
    N57 --> N340
    N57 --> N14
    N58 --> N409
    N58 --> N340
    N59 --> N409
    N59 --> N340
    N60 --> N409
    N60 --> N340
    N60 --> N14
    N61 --> N340
    N62 --> N409
    N62 --> N340
    N63 --> N340
    N64 --> N420
    N64 --> N340
    N64 --> N14
    N64 --> N13
    N65 --> N409
    N65 --> N340
    N66 --> N311
    N66 --> N332
    N66 --> N340
    N67 --> N340
    N68 --> N409
    N68 --> N340
    N69 --> N420
    N69 --> N14
    N69 --> N311
    N69 --> N332
    N70 --> N420
    N70 --> N409
    N70 --> N340
    N71 --> N409
    N71 --> N340
    N72 --> N409
    N72 --> N340
    N72 --> N14
    N73 --> N311
    N73 --> N332
    N73 --> N420
    N73 --> N340
    N73 --> N14
    N74 --> N420
    N74 --> N311
    N74 --> N332
    N74 --> N340
    N74 --> N14
    N75 --> N409
    N75 --> N340
    N76 --> N340
    N76 --> N420
    N76 --> N14
    N77 --> N340
    N78 --> N340
    N79 --> N409
    N79 --> N340
    N80 --> N311
    N80 --> N332
    N80 --> N340
    N81 --> N409
    N81 --> N340
    N81 --> N14
    N82 --> N409
    N82 --> N340
    N83 --> N409
    N83 --> N340
    N84 --> N311
    N84 --> N332
    N84 --> N340
    N85 --> N340
    N86 --> N311
    N86 --> N332
    N86 --> N340
    N87 --> N311
    N87 --> N332
    N87 --> N340
    N88 --> N340
    N89 --> N340
    N89 --> N14
    N90 --> N340
    N90 --> N14
    N91 --> N409
    N91 --> N340
    N91 --> N14
    N92 --> N340
    N92 --> N14
    N93 --> N340
    N93 --> N14
    N94 --> N340
    N95 --> N420
    N95 --> N340
    N96 --> N340
    N97 --> N340
    N98 --> N409
    N98 --> N340
    N99 --> N311
    N99 --> N332
    N99 --> N340
    N100 --> N311
    N100 --> N332
    N100 --> N340
    N100 --> N14
    N101 --> N311
    N101 --> N332
    N101 --> N250
    N101 --> N384
    N101 --> N340
    N102 --> N340
    N103 --> N340
    N104 --> N311
    N104 --> N332
    N104 --> N340
    N105 --> N340
    N106 --> N311
    N106 --> N332
    N106 --> N340
    N107 --> N311
    N107 --> N332
    N107 --> N340
    N108 --> N340
    N108 --> N14
    N109 --> N311
    N109 --> N332
    N109 --> N340
    N110 --> N340
    N110 --> N14
    N111 --> N340
    N112 --> N14
    N113 --> N311
    N113 --> N332
    N113 --> N340
    N113 --> N290
    N113 --> N324
    N113 --> N9
    N113 --> N26
    N113 --> N231
    N113 --> N289
    N113 --> N308
    N113 --> N323
    N113 --> N378
    N113 --> N407
    N113 --> N11
    N113 --> N10
    N114 --> N340
    N115 --> N340
    N116 --> N311
    N116 --> N332
    N116 --> N420
    N116 --> N409
    N116 --> N340
    N116 --> N14
    N117 --> N311
    N117 --> N332
    N117 --> N340
    N117 --> N14
    N118 --> N420
    N118 --> N340
    N118 --> N14
    N118 --> N311
    N118 --> N332
    N119 --> N340
    N119 --> N14
    N121 --> N311
    N121 --> N332
    N121 --> N340
    N122 --> N311
    N122 --> N332
    N122 --> N340
    N123 --> N340
    N124 --> N340
    N124 --> N14
    N127 --> N340
    N128 --> N311
    N128 --> N332
    N128 --> N340
    N129 --> N340
    N130 --> N340
    N130 --> N311
    N130 --> N332
    N131 --> N409
    N131 --> N340
    N133 --> N340
    N134 --> N340
    N134 --> N14
    N135 --> N311
    N135 --> N332
    N135 --> N340
    N135 --> N14
    N136 --> N340
    N137 --> N311
    N137 --> N332
    N137 --> N409
    N137 --> N340
    N137 --> N14
    N138 --> N420
    N138 --> N409
    N138 --> N340
    N139 --> N420
    N139 --> N340
    N140 --> N409
    N140 --> N340
    N141 --> N340
    N141 --> N14
    N142 --> N409
    N142 --> N340
    N142 --> N14
    N143 --> N340
    N144 --> N14
    N147 --> N420
    N147 --> N13
    N148 --> N14
    N149 --> N13
    N152 --> N14
    N154 --> N14
    N155 --> N14
    N156 --> N420
    N161 --> N14
    N162 --> N14
    N163 --> N13
    N165 --> N311
    N165 --> N332
    N165 --> N14
    N167 --> N311
    N167 --> N332
    N167 --> N14
    N167 --> N420
    N172 --> N420
    N173 --> N409
    N173 --> N311
    N173 --> N332
    N174 --> N311
    N174 --> N332
    N175 --> N420
    N176 --> N311
    N176 --> N332
    N176 --> N13
    N176 --> N420
    N177 --> N14
    N180 --> N14
    N181 --> N420
    N182 --> N420
    N182 --> N13
    N183 --> N13
    N183 --> N420
    N184 --> N13
    N185 --> N420
    N186 --> N420
    N187 --> N311
    N187 --> N332
    N191 --> N132
    N192 --> N13
    N193 --> N13
    N195 --> N442
    N196 --> N257
    N196 --> N284
    N196 --> N300
    N196 --> N339
    N196 --> N392
    N196 --> N9
    N196 --> N26
    N196 --> N231
    N196 --> N289
    N196 --> N308
    N196 --> N323
    N196 --> N378
    N196 --> N407
    N197 --> N198
    N197 --> N220
    N197 --> N222
    N197 --> N205
    N197 --> N196
    N197 --> N9
    N197 --> N26
    N197 --> N231
    N197 --> N289
    N197 --> N308
    N197 --> N323
    N197 --> N378
    N197 --> N407
    N197 --> N221
    N197 --> N219
    N198 --> N199
    N198 --> N9
    N198 --> N26
    N198 --> N231
    N198 --> N289
    N198 --> N308
    N198 --> N323
    N198 --> N378
    N198 --> N407
    N200 --> N207
    N200 --> N446
    N200 --> N447
    N200 --> N210
    N200 --> N451
    N200 --> N208
    N200 --> N448
    N200 --> N209
    N200 --> N449
    N202 --> N196
    N202 --> N198
    N203 --> N196
    N203 --> N215
    N203 --> N212
    N204 --> N9
    N204 --> N26
    N204 --> N231
    N204 --> N289
    N204 --> N308
    N204 --> N323
    N204 --> N378
    N204 --> N407
    N205 --> N196
    N205 --> N202
    N205 --> N206
    N205 --> N203
    N205 --> N229
    N205 --> N224
    N205 --> N223
    N205 --> N226
    N205 --> N228
    N205 --> N230
    N205 --> N225
    N205 --> N227
    N205 --> N211
    N206 --> N196
    N206 --> N9
    N206 --> N26
    N206 --> N231
    N206 --> N289
    N206 --> N308
    N206 --> N323
    N206 --> N378
    N206 --> N407
    N206 --> N212
    N211 --> N217
    N218 --> N9
    N218 --> N26
    N218 --> N231
    N218 --> N289
    N218 --> N308
    N218 --> N323
    N218 --> N378
    N218 --> N407
    N219 --> N9
    N219 --> N26
    N219 --> N231
    N219 --> N289
    N219 --> N308
    N219 --> N323
    N219 --> N378
    N219 --> N407
    N220 --> N9
    N220 --> N26
    N220 --> N231
    N220 --> N289
    N220 --> N308
    N220 --> N323
    N220 --> N378
    N220 --> N407
    N220 --> N198
    N221 --> N9
    N221 --> N26
    N221 --> N231
    N221 --> N289
    N221 --> N308
    N221 --> N323
    N221 --> N378
    N221 --> N407
    N222 --> N214
    N222 --> N9
    N222 --> N26
    N222 --> N231
    N222 --> N289
    N222 --> N308
    N222 --> N323
    N222 --> N378
    N222 --> N407
    N223 --> N257
    N223 --> N284
    N223 --> N300
    N223 --> N339
    N223 --> N392
    N223 --> N196
    N223 --> N214
    N223 --> N9
    N223 --> N26
    N223 --> N231
    N223 --> N289
    N223 --> N308
    N223 --> N323
    N223 --> N378
    N223 --> N407
    N224 --> N257
    N224 --> N284
    N224 --> N300
    N224 --> N339
    N224 --> N392
    N224 --> N214
    N224 --> N213
    N224 --> N9
    N224 --> N26
    N224 --> N231
    N224 --> N289
    N224 --> N308
    N224 --> N323
    N224 --> N378
    N224 --> N407
    N225 --> N9
    N225 --> N26
    N225 --> N231
    N225 --> N289
    N225 --> N308
    N225 --> N323
    N225 --> N378
    N225 --> N407
    N226 --> N257
    N226 --> N284
    N226 --> N300
    N226 --> N339
    N226 --> N392
    N226 --> N215
    N226 --> N214
    N226 --> N213
    N226 --> N9
    N226 --> N26
    N226 --> N231
    N226 --> N289
    N226 --> N308
    N226 --> N323
    N226 --> N378
    N226 --> N407
    N227 --> N9
    N227 --> N26
    N227 --> N231
    N227 --> N289
    N227 --> N308
    N227 --> N323
    N227 --> N378
    N227 --> N407
    N227 --> N257
    N227 --> N284
    N227 --> N300
    N227 --> N339
    N227 --> N392
    N227 --> N196
    N227 --> N217
    N227 --> N215
    N227 --> N214
    N227 --> N213
    N228 --> N216
    N228 --> N214
    N228 --> N9
    N228 --> N26
    N228 --> N231
    N228 --> N289
    N228 --> N308
    N228 --> N323
    N228 --> N378
    N228 --> N407
    N229 --> N257
    N229 --> N284
    N229 --> N300
    N229 --> N339
    N229 --> N392
    N229 --> N214
    N229 --> N213
    N229 --> N9
    N229 --> N26
    N229 --> N231
    N229 --> N289
    N229 --> N308
    N229 --> N323
    N229 --> N378
    N229 --> N407
    N230 --> N9
    N230 --> N26
    N230 --> N231
    N230 --> N289
    N230 --> N308
    N230 --> N323
    N230 --> N378
    N230 --> N407
    N235 --> N340
    N237 --> N340
    N239 --> N340
    N240 --> N340
    N242 --> N340
    N243 --> N340
    N244 --> N290
    N244 --> N324
    N244 --> N257
    N244 --> N284
    N244 --> N300
    N244 --> N339
    N244 --> N392
    N244 --> N340
    N245 --> N340
    N247 --> N409
    N248 --> N304
    N248 --> N290
    N248 --> N324
    N248 --> N340
    N249 --> N340
    N251 --> N340
    N252 --> N311
    N252 --> N332
    N252 --> N257
    N252 --> N284
    N252 --> N300
    N252 --> N339
    N252 --> N392
    N252 --> N290
    N252 --> N324
    N252 --> N340
    N253 --> N340
    N257 --> N284
    N257 --> N300
    N257 --> N339
    N257 --> N392
    N257 --> N340
    N258 --> N304
    N258 --> N340
    N262 --> N290
    N262 --> N324
    N262 --> N340
    N262 --> N420
    N263 --> N290
    N263 --> N324
    N263 --> N340
    N271 --> N311
    N271 --> N332
    N271 --> N340
    N272 --> N340
    N273 --> N276
    N273 --> N304
    N273 --> N340
    N274 --> N340
    N276 --> N340
    N277 --> N340
    N278 --> N340
    N279 --> N257
    N279 --> N284
    N279 --> N300
    N279 --> N339
    N279 --> N392
    N279 --> N340
    N279 --> N304
    N279 --> N290
    N279 --> N324
    N280 --> N304
    N280 --> N290
    N280 --> N324
    N280 --> N340
    N283 --> N257
    N283 --> N284
    N283 --> N300
    N283 --> N339
    N283 --> N392
    N284 --> N283
    N285 --> N290
    N285 --> N324
    N285 --> N340
    N287 --> N340
    N288 --> N340
    N289 --> N304
    N289 --> N340
    N290 --> N324
    N290 --> N257
    N290 --> N284
    N290 --> N300
    N290 --> N339
    N290 --> N392
    N290 --> N340
    N290 --> N304
    N291 --> N340
    N292 --> N290
    N292 --> N324
    N292 --> N340
    N292 --> N304
    N292 --> N320
    N293 --> N290
    N293 --> N324
    N293 --> N340
    N294 --> N290
    N294 --> N324
    N294 --> N304
    N294 --> N340
    N295 --> N290
    N295 --> N324
    N295 --> N304
    N295 --> N340
    N296 --> N257
    N296 --> N284
    N296 --> N300
    N296 --> N339
    N296 --> N392
    N296 --> N304
    N296 --> N340
    N296 --> N311
    N296 --> N332
    N297 --> N340
    N297 --> N334
    N297 --> N304
    N298 --> N290
    N298 --> N324
    N298 --> N340
    N299 --> N340
    N300 --> N290
    N300 --> N324
    N300 --> N257
    N300 --> N284
    N300 --> N339
    N300 --> N392
    N300 --> N340
    N300 --> N320
    N300 --> N311
    N300 --> N332
    N301 --> N257
    N301 --> N284
    N301 --> N300
    N301 --> N339
    N301 --> N392
    N301 --> N290
    N301 --> N324
    N301 --> N340
    N302 --> N257
    N302 --> N284
    N302 --> N300
    N302 --> N339
    N302 --> N392
    N302 --> N340
    N305 --> N340
    N305 --> N304
    N306 --> N340
    N306 --> N304
    N307 --> N257
    N307 --> N284
    N307 --> N300
    N307 --> N339
    N307 --> N392
    N307 --> N340
    N307 --> N304
    N308 --> N304
    N308 --> N340
    N309 --> N340
    N310 --> N304
    N310 --> N340
    N311 --> N304
    N311 --> N257
    N311 --> N284
    N311 --> N300
    N311 --> N339
    N311 --> N392
    N311 --> N340
    N311 --> N290
    N311 --> N324
    N312 --> N311
    N312 --> N332
    N312 --> N304
    N312 --> N340
    N313 --> N311
    N313 --> N332
    N313 --> N304
    N313 --> N340
    N314 --> N340
    N316 --> N290
    N316 --> N324
    N316 --> N340
    N316 --> N320
    N316 --> N257
    N316 --> N284
    N316 --> N300
    N316 --> N339
    N316 --> N392
    N317 --> N304
    N317 --> N340
    N318 --> N340
    N319 --> N340
    N320 --> N340
    N321 --> N304
    N321 --> N257
    N321 --> N284
    N321 --> N300
    N321 --> N339
    N321 --> N392
    N321 --> N340
    N322 --> N340
    N323 --> N311
    N323 --> N332
    N323 --> N340
    N324 --> N290
    N324 --> N340
    N325 --> N340
    N326 --> N340
    N327 --> N304
    N327 --> N340
    N328 --> N340
    N329 --> N311
    N329 --> N332
    N329 --> N340
    N330 --> N340
    N331 --> N257
    N331 --> N284
    N331 --> N300
    N331 --> N339
    N331 --> N392
    N331 --> N340
    N332 --> N257
    N332 --> N284
    N332 --> N300
    N332 --> N339
    N332 --> N392
    N332 --> N340
    N332 --> N290
    N332 --> N324
    N333 --> N304
    N333 --> N257
    N333 --> N284
    N333 --> N300
    N333 --> N339
    N333 --> N392
    N333 --> N340
    N334 --> N340
    N334 --> N297
    N334 --> N304
    N335 --> N340
    N336 --> N311
    N336 --> N332
    N336 --> N340
    N337 --> N304
    N337 --> N290
    N337 --> N324
    N337 --> N340
    N338 --> N311
    N338 --> N332
    N338 --> N340
    N339 --> N304
    N339 --> N257
    N339 --> N284
    N339 --> N300
    N339 --> N392
    N339 --> N340
    N340 --> N257
    N340 --> N284
    N340 --> N300
    N340 --> N339
    N340 --> N392
    N341 --> N304
    N341 --> N257
    N341 --> N284
    N341 --> N300
    N341 --> N339
    N341 --> N392
    N341 --> N340
    N342 --> N340
    N342 --> N304
    N344 --> N311
    N344 --> N332
    N344 --> N340
    N346 --> N304
    N346 --> N340
    N347 --> N340
    N347 --> N304
    N348 --> N340
    N349 --> N290
    N349 --> N324
    N349 --> N304
    N349 --> N340
    N350 --> N257
    N350 --> N284
    N350 --> N300
    N350 --> N339
    N350 --> N392
    N350 --> N290
    N350 --> N324
    N350 --> N340
    N351 --> N340
    N352 --> N340
    N353 --> N340
    N354 --> N290
    N354 --> N324
    N354 --> N304
    N354 --> N340
    N354 --> N320
    N355 --> N290
    N355 --> N324
    N355 --> N340
    N356 --> N290
    N356 --> N324
    N356 --> N340
    N356 --> N304
    N356 --> N257
    N356 --> N284
    N356 --> N300
    N356 --> N339
    N356 --> N392
    N357 --> N257
    N357 --> N284
    N357 --> N300
    N357 --> N339
    N357 --> N392
    N357 --> N340
    N359 --> N340
    N361 --> N340
    N361 --> N320
    N362 --> N340
    N363 --> N340
    N363 --> N304
    N363 --> N257
    N363 --> N284
    N363 --> N300
    N363 --> N339
    N363 --> N392
    N364 --> N340
    N365 --> N257
    N365 --> N284
    N365 --> N300
    N365 --> N339
    N365 --> N392
    N365 --> N340
    N366 --> N290
    N366 --> N324
    N366 --> N340
    N367 --> N340
    N368 --> N340
    N369 --> N290
    N369 --> N324
    N369 --> N340
    N370 --> N257
    N370 --> N284
    N370 --> N300
    N370 --> N339
    N370 --> N392
    N370 --> N340
    N371 --> N290
    N371 --> N324
    N371 --> N304
    N371 --> N257
    N371 --> N284
    N371 --> N300
    N371 --> N339
    N371 --> N392
    N371 --> N340
    N372 --> N340
    N373 --> N340
    N374 --> N340
    N375 --> N340
    N376 --> N340
    N377 --> N304
    N377 --> N340
    N378 --> N304
    N378 --> N340
    N379 --> N340
    N380 --> N340
    N381 --> N311
    N381 --> N332
    N381 --> N340
    N382 --> N276
    N383 --> N290
    N383 --> N324
    N383 --> N340
    N384 --> N311
    N384 --> N332
    N384 --> N276
    N384 --> N340
    N385 --> N276
    N385 --> N311
    N385 --> N332
    N385 --> N340
    N386 --> N257
    N386 --> N284
    N386 --> N300
    N386 --> N339
    N386 --> N392
    N386 --> N304
    N386 --> N340
    N387 --> N340
    N388 --> N340
    N389 --> N304
    N390 --> N340
    N391 --> N311
    N391 --> N332
    N391 --> N304
    N391 --> N257
    N391 --> N284
    N391 --> N300
    N391 --> N339
    N391 --> N392
    N391 --> N340
    N392 --> N340
    N393 --> N311
    N393 --> N332
    N393 --> N340
    N394 --> N340
    N395 --> N340
    N395 --> N420
    N397 --> N340
    N400 --> N340
    N401 --> N266
    N401 --> N340
    N403 --> N311
    N403 --> N332
    N403 --> N340
    N405 --> N304
    N405 --> N340
    N406 --> N340
    N407 --> N420
    N407 --> N311
    N407 --> N332
    N407 --> N409
    N407 --> N340
    N408 --> N340
    N409 --> N276
    N409 --> N340
    N410 --> N420
    N410 --> N409
    N410 --> N304
    N410 --> N340
    N411 --> N420
    N411 --> N409
    N411 --> N257
    N411 --> N284
    N411 --> N300
    N411 --> N339
    N411 --> N392
    N411 --> N340
    N412 --> N420
    N412 --> N409
    N412 --> N304
    N412 --> N340
    N413 --> N420
    N413 --> N340
    N415 --> N257
    N415 --> N284
    N415 --> N300
    N415 --> N339
    N415 --> N392
    N415 --> N340
    N418 --> N340
    N419 --> N420
    N419 --> N409
    N419 --> N340
    N421 --> N420
    N421 --> N422
    N422 --> N420
    N424 --> N409
    N424 --> N340
    N426 --> N420
    N426 --> N304
    N427 --> N420
    N428 --> N420
    N429 --> N420
    N430 --> N420
    N430 --> N276
    N430 --> N409
    N430 --> N340
    N431 --> N420
    N431 --> N276
    N431 --> N409
    N431 --> N340
    N432 --> N420
    N432 --> N259
    N432 --> N393
    N433 --> N420
    N433 --> N276
    N433 --> N409
    N433 --> N340
    N433 --> N259
    N433 --> N393
    N434 --> N420
    N434 --> N409
    N434 --> N276
    N434 --> N340
    N434 --> N259
    N434 --> N393
    N435 --> N420
    N435 --> N409
    N435 --> N340
    N436 --> N409
    N436 --> N257
    N436 --> N284
    N436 --> N300
    N436 --> N339
    N436 --> N392
    N437 --> N409
    N437 --> N340
    N438 --> N409
    N440 --> N340
    N442 --> N195
    N443 --> N200
    N443 --> N445
    N444 --> N443
    N445 --> N207
    N445 --> N446
    N445 --> N447
    N445 --> N210
    N445 --> N451
    N445 --> N208
    N445 --> N448
    N445 --> N209
    N445 --> N449
    N445 --> N204
    N445 --> N450
```

## Detailed File Index
- **build_standalone.py**
  - Imports: `glob`
  - Imports: `json`
  - Imports: `meridian_mobile`
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
  - Imports: `_thread`
  - Imports: `ast`
  - Imports: `asyncio`
  - Imports: `base64`
  - Imports: `contextlib`
  - Imports: `database`
  - Imports: `fastapi`
  - Imports: `hashlib`
  - Imports: `hmac`
  - Imports: `httpx`
  - Imports: `json`
  - Imports: `logging`
  - Imports: `ollama`
  - Imports: `os`
  - Imports: `platform`
  - Imports: `psutil`
  - Imports: `pydantic`
  - Imports: `random`
  - Imports: `re`
  - Imports: `secrets`
  - Imports: `shutil`
  - Imports: `slowapi`
  - Imports: `socket`
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
- **meridian_backend/src/core/action_journal.py**
  - Imports: `database`
  - Imports: `json`
  - Imports: `logging`
  - Imports: `src`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/core/ar_bridge.py**
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
  - Imports: `hmac`
  - Imports: `os`
  - Imports: `secrets`
  - Imports: `src`
  - Imports: `typing`
- **meridian_backend/src/core/behavior_monitor.py**
  - Imports: `logging`
  - Imports: `os`
  - Imports: `psutil`
  - Imports: `typing`
- **meridian_backend/src/core/breach_sentinel.py**
  - Imports: `hashlib`
  - Imports: `logging`
  - Imports: `typing`
  - Imports: `urllib`
- **meridian_backend/src/core/bus.py**
  - Imports: `asyncio`
  - Imports: `typing`
- **meridian_backend/src/core/camera_sentinel.py**
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
- **meridian_backend/src/core/config.py**
  - Imports: `os`
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
- **meridian_backend/src/core/logging_config.py**
  - Imports: `json`
  - Imports: `logging`
  - Imports: `os`
  - Imports: `src`
  - Imports: `sys`
- **meridian_backend/src/core/loop.py**
  - Imports: `anthropic`
  - Imports: `ast`
  - Imports: `asyncio`
  - Imports: `database`
  - Imports: `datetime`
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
  - Imports: `typing`
- **meridian_backend/src/core/mcp_executor.py**
  - Imports: `asyncio`
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
- **meridian_backend/src/core/memory_editor.py**
  - Imports: `database`
  - Imports: `json`
  - Imports: `src`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/core/mobile_bridge.py**
  - Imports: `asyncio`
  - Imports: `fastapi`
  - Imports: `json`
  - Imports: `logging`
  - Imports: `os`
  - Imports: `psutil`
  - Imports: `socket`
  - Imports: `sys`
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
- **meridian_backend/src/core/predictive_engine.py**
  - Imports: `logging`
  - Imports: `src`
  - Imports: `subprocess`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/core/presence_briefing.py**
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
- **meridian_backend/src/core/watcher.py**
  - Imports: `logging`
  - Imports: `os`
  - Imports: `re`
  - Imports: `src`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/core/workflow_engine.py**
  - Imports: `json`
  - Imports: `os`
  - Imports: `re`
  - Imports: `src`
  - Imports: `time`
  - Imports: `typing`
  - Imports: `uuid`
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
- **meridian_backend/src/tools/browser_agent.py**
  - Imports: `json`
  - Imports: `os`
  - Imports: `playwright`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/tools/cam_guard.py**
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
  - Imports: `json`
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
- **meridian_backend/src/tools/mcp_marketplace.py**
  - Imports: `json`
  - Imports: `os`
  - Imports: `time`
  - Imports: `typing`
- **meridian_backend/src/tools/media_player.py**
  - Imports: `database`
  - Imports: `playwright`
  - Imports: `pyautogui`
  - Imports: `src`
  - Imports: `time`
  - Imports: `typing`
  - Imports: `urllib`
- **meridian_backend/src/tools/network_guardian.py**
  - Imports: `socket`
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
  - Imports: `typing`
- **meridian_backend/src/tools/registry.py**
  - Imports: `asyncio`
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
  - Imports: `json`
  - Imports: `os`
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
  - Imports: `time`
  - Imports: `typing`
  - Imports: `urllib`
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
- **meridian_backend/tests/test_auto_bug_fixer.py**
  - Imports: `api`
  - Imports: `asyncio`
  - Imports: `fastapi`
  - Imports: `os`
  - Imports: `pytest`
  - Imports: `src`
  - Imports: `sys`
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
- **meridian_backend/tests/test_butler_media.py**
  - Imports: `database`
  - Imports: `os`
  - Imports: `src`
  - Imports: `sys`
  - Imports: `unittest`
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
- **meridian_backend/tests/test_document_tools.py**
  - Imports: `os`
  - Imports: `pytest`
  - Imports: `src`
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
- **meridian_backend/tests/test_sprint2_features.py**
  - Imports: `api`
  - Imports: `fastapi`
  - Imports: `os`
  - Imports: `pytest`
  - Imports: `src`
  - Imports: `unittest`
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
  - Imports: `yaml`
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
  - Imports: `numpy`
  - Imports: `os`
  - Imports: `pytest`
  - Imports: `sys`
  - Imports: `voice`
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
- **meridian_frontend/src/AppContext.tsx**
  - Imports: `config`
  - Imports: `core`
  - Imports: `event`
  - Imports: `react`
  - Imports: `types`
- **meridian_frontend/src/Mascot.tsx**
  - Imports: `Mascot3DCharacter`
  - Imports: `config`
  - Imports: `core`
  - Imports: `event`
  - Imports: `react`
  - Imports: `window`
- **meridian_frontend/src/Mascot3DCharacter.tsx**
  - Imports: `animejs`
  - Imports: `react`
  - Imports: `three`
- **meridian_frontend/src/MobileApp.tsx**
  - Imports: `DropdownNav`
  - Imports: `LiveThoughtCarousel`
  - Imports: `QRScannerModal`
  - Imports: `VoiceOrbHUD`
  - Imports: `lucide-react`
  - Imports: `react`
- **meridian_frontend/src/components/CommandPalette.tsx**
  - Imports: `lucide-react`
  - Imports: `react`
- **meridian_frontend/src/components/NavRail.tsx**
  - Imports: `AppContext`
  - Imports: `Mascot`
  - Imports: `core`
  - Imports: `react`
  - Imports: `window`
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
  - Imports: `Jobs`
  - Imports: `MemoryEditor`
  - Imports: `NavRail`
  - Imports: `Productivity`
  - Imports: `RightDrawer`
  - Imports: `Settings`
  - Imports: `StatusBar`
  - Imports: `SwarmDebate`
  - Imports: `Timeline`
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
- **meridian_frontend/src/components/mobile/QRScannerModal.tsx**
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
  - Imports: `GlowCard`
  - Imports: `HoloButton`
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
  - Imports: `types`
- **meridian_frontend/src/views/WorkflowBuilder.tsx**
  - Imports: `config`
  - Imports: `react`
- **meridian_frontend/vite.config.ts**
  - Imports: `path`
  - Imports: `plugin-react`
  - Imports: `vite`
- **meridian_mobile/build_apk.py**
  - Imports: `os`
  - Imports: `shutil`
  - Imports: `subprocess`
  - Imports: `sys`
- **meridian_mobile/src/App.tsx**
  - Imports: `MobileApp`
  - Imports: `react`
- **meridian_mobile/src/MobileApp.tsx**
  - Imports: `DropdownNav`
  - Imports: `LiveThoughtCarousel`
  - Imports: `QRScannerModal`
  - Imports: `ServerConnectionModal`
  - Imports: `VoiceOrbHUD`
  - Imports: `react`
- **meridian_mobile/src/components/DropdownNav.tsx**
  - Imports: `lucide-react`
  - Imports: `react`
- **meridian_mobile/src/components/mobile/DropdownNav.tsx**
  - Imports: `lucide-react`
  - Imports: `react`
- **meridian_mobile/src/components/mobile/LiveThoughtCarousel.tsx**
  - Imports: `lucide-react`
  - Imports: `react`
- **meridian_mobile/src/components/mobile/QRScannerModal.tsx**
  - Imports: `lucide-react`
  - Imports: `react`
- **meridian_mobile/src/components/mobile/ServerConnectionModal.tsx**
  - Imports: `lucide-react`
  - Imports: `react`
- **meridian_mobile/src/components/mobile/VoiceOrbHUD.tsx**
  - Imports: `lucide-react`
  - Imports: `react`
- **meridian_mobile/src/main.tsx**
  - Imports: `App`
  - Imports: `client`
  - Imports: `index.css`
  - Imports: `react`
- **meridian_mobile/vite.config.ts**
  - Imports: `path`
  - Imports: `plugin-react`
  - Imports: `vite`
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