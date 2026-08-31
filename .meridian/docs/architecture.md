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
    N15["audit_logger.py [meridian_backend/src/core]"]
    N16["auth.py [meridian_backend/src/core]"]
    N17["bus.py [meridian_backend/src/core]"]
    N18["clipboard.py [meridian_backend/src/core]"]
    N19["code_graph.py [meridian_backend/src/core]"]
    N20["config.py [meridian_backend/src/core]"]
    N21["discord_bridge.py [meridian_backend/src/core]"]
    N22["doc_generator.py [meridian_backend/src/core]"]
    N23["doc_indexer.py [meridian_backend/src/core]"]
    N24["exporter.py [meridian_backend/src/core]"]
    N25["governor.py [meridian_backend/src/core]"]
    N26["graph_rag.py [meridian_backend/src/core]"]
    N27["graph_sync.py [meridian_backend/src/core]"]
    N28["hardware_detector.py [meridian_backend/src/core]"]
    N29["history_manager.py [meridian_backend/src/core]"]
    N30["llm_provider.py [meridian_backend/src/core]"]
    N31["logging_config.py [meridian_backend/src/core]"]
    N32["loop.py [meridian_backend/src/core]"]
    N33["loop_dispatcher.py [meridian_backend/src/core]"]
    N34["loop_parser.py [meridian_backend/src/core]"]
    N35["loop_stream.py [meridian_backend/src/core]"]
    N36["lsp_client.py [meridian_backend/src/core]"]
    N37["mcp_client.py [meridian_backend/src/core]"]
    N38["mcp_executor.py [meridian_backend/src/core]"]
    N39["mode.py [meridian_backend/src/core]"]
    N40["neural_rag.py [meridian_backend/src/core]"]
    N41["oauth_manager.py [meridian_backend/src/core]"]
    N42["ollama_manager.py [meridian_backend/src/core]"]
    N43["p2p.py [meridian_backend/src/core]"]
    N44["perception.py [meridian_backend/src/core]"]
    N45["plugins.py [meridian_backend/src/core]"]
    N46["proactive.py [meridian_backend/src/core]"]
    N47["prompt_injection.py [meridian_backend/src/core]"]
    N48["prompt_templates.py [meridian_backend/src/core]"]
    N49["rag_optimizer.py [meridian_backend/src/core]"]
    N50["sandbox_runner.py [meridian_backend/src/core]"]
    N51["scheduler.py [meridian_backend/src/core]"]
    N52["security_middleware.py [meridian_backend/src/core]"]
    N53["speculative.py [meridian_backend/src/core]"]
    N54["swarm.py [meridian_backend/src/core]"]
    N55["system_defense.py [meridian_backend/src/core]"]
    N56["telegram_bridge.py [meridian_backend/src/core]"]
    N57["temporal_memory.py [meridian_backend/src/core]"]
    N58["triggers.py [meridian_backend/src/core]"]
    N59["vault.py [meridian_backend/src/core]"]
    N60["vision.py [meridian_backend/src/core]"]
    N61["watcher.py [meridian_backend/src/core]"]
    N62["workflow_engine.py [meridian_backend/src/core]"]
    N63["auto_reviewer.py [meridian_backend/src/tools]"]
    N64["browser_agent.py [meridian_backend/src/tools]"]
    N65["chrome_manager.py [meridian_backend/src/tools]"]
    N66["clipboard.py [meridian_backend/src/tools]"]
    N67["communication.py [meridian_backend/src/tools]"]
    N68["db_query.py [meridian_backend/src/tools]"]
    N69["desktop.py [meridian_backend/src/tools]"]
    N70["developer.py [meridian_backend/src/tools]"]
    N71["documents.py [meridian_backend/src/tools]"]
    N72["dynamic_manager.py [meridian_backend/src/tools]"]
    N73["exporter.py [meridian_backend/src/tools]"]
    N74["external_connectors.py [meridian_backend/src/tools]"]
    N75["filesystem.py [meridian_backend/src/tools]"]
    N76["geo_location.py [meridian_backend/src/tools]"]
    N77["knowledge.py [meridian_backend/src/tools]"]
    N78["mcp_marketplace.py [meridian_backend/src/tools]"]
    N79["media_player.py [meridian_backend/src/tools]"]
    N80["ollama_manager.py [meridian_backend/src/tools]"]
    N81["papercoder.py [meridian_backend/src/tools]"]
    N82["recording.py [meridian_backend/src/tools]"]
    N83["registry.py [meridian_backend/src/tools]"]
    N84["review.py [meridian_backend/src/tools]"]
    N85["scheduler.py [meridian_backend/src/tools]"]
    N86["security_auditor.py [meridian_backend/src/tools]"]
    N87["shell.py [meridian_backend/src/tools]"]
    N88["system.py [meridian_backend/src/tools]"]
    N89["task_scheduler.py [meridian_backend/src/tools]"]
    N90["vault.py [meridian_backend/src/tools]"]
    N91["voice.py [meridian_backend/src/tools]"]
    N92["watcher.py [meridian_backend/src/tools]"]
    N93["web.py [meridian_backend/src/tools]"]
    N94["web_browser.py [meridian_backend/src/tools]"]
    N95["whatsapp_manager.py [meridian_backend/src/tools]"]
    N96["duplex.py [meridian_backend/src/voice]"]
    N97["polyglot.py [meridian_backend/src/voice]"]
    N98["stt.py [meridian_backend/src/voice]"]
    N99["tts.py [meridian_backend/src/voice]"]
    N100["voice_biometrics.py [meridian_backend/src/voice]"]
    N101["wakeword.py [meridian_backend/src/voice]"]
    N102["conftest.py [meridian_backend/tests]"]
    N103["run_tests.py [meridian_backend/tests]"]
    N104["test_auto_bug_fixer.py [meridian_backend/tests]"]
    N105["test_backlog_features.py [meridian_backend/tests]"]
    N106["test_backlog_sprint.py [meridian_backend/tests]"]
    N107["test_bridges.py [meridian_backend/tests]"]
    N108["test_butler_media.py [meridian_backend/tests]"]
    N109["test_config.py [meridian_backend/tests]"]
    N110["test_context_budget.py [meridian_backend/tests]"]
    N111["test_database.py [meridian_backend/tests]"]
    N112["test_day3_features.py [meridian_backend/tests]"]
    N113["test_day4_features.py [meridian_backend/tests]"]
    N114["test_day5_features.py [meridian_backend/tests]"]
    N115["test_day6_features.py [meridian_backend/tests]"]
    N116["test_day7_features.py [meridian_backend/tests]"]
    N117["test_document_tools.py [meridian_backend/tests]"]
    N118["test_geo_location.py [meridian_backend/tests]"]
    N119["test_jarvis_perception.py [meridian_backend/tests]"]
    N120["test_llm_provider.py [meridian_backend/tests]"]
    N121["test_logging.py [meridian_backend/tests]"]
    N122["test_loop_parser.py [meridian_backend/tests]"]
    N123["test_loop_submodules.py [meridian_backend/tests]"]
    N124["test_model_source.py [meridian_backend/tests]"]
    N125["test_multi_os.py [meridian_backend/tests]"]
    N126["test_oauth.py [meridian_backend/tests]"]
    N127["test_p2p.py [meridian_backend/tests]"]
    N128["test_proactive.py [meridian_backend/tests]"]
    N129["test_proactive_notifications.py [meridian_backend/tests]"]
    N130["test_security_features.py [meridian_backend/tests]"]
    N131["test_sprint2_features.py [meridian_backend/tests]"]
    N132["test_stream_resiliency.py [meridian_backend/tests]"]
    N133["test_swarm.py [meridian_backend/tests]"]
    N134["test_tools.py [meridian_backend/tests]"]
    N135["test_vault.py [meridian_backend/tests]"]
    N136["test_voice_speed.py [meridian_backend/tests]"]
    N137["test_wakeword_continuous.py [meridian_backend/tests]"]
    N138["test_wakeword_onnx.py [meridian_backend/tests]"]
    N139["test_workflow.py [meridian_backend/tests]"]
    N140["vite.config.ts [meridian_frontend]"]
    N141["AppContext.tsx [meridian_frontend/src]"]
    N142["main.tsx [meridian_frontend/src]"]
    N143["Mascot.tsx [meridian_frontend/src]"]
    N144["Mascot3DCharacter.tsx [meridian_frontend/src]"]
    N145["CommandPalette.tsx [meridian_frontend/src/components]"]
    N146["NavRail.tsx [meridian_frontend/src/components]"]
    N147["RightDrawer.tsx [meridian_frontend/src/components]"]
    N148["ServerConnectionModal.tsx [meridian_frontend/src/components]"]
    N149["Shell.tsx [meridian_frontend/src/components]"]
    N150["StatusBar.tsx [meridian_frontend/src/components]"]
    N151["AmbientParticles.tsx [meridian_frontend/src/components/ui]"]
    N152["DataBadge.tsx [meridian_frontend/src/components/ui]"]
    N153["GlowCard.tsx [meridian_frontend/src/components/ui]"]
    N154["HoloButton.tsx [meridian_frontend/src/components/ui]"]
    N155["ProgressArc.tsx [meridian_frontend/src/components/ui]"]
    N156["TerminalLine.tsx [meridian_frontend/src/components/ui]"]
    N157["useMemoryOptimizer.ts [meridian_frontend/src/hooks]"]
    N158["oauthService.ts [meridian_frontend/src/services]"]
    N159["BackendSetup.tsx [meridian_frontend/src/startup]"]
    N160["BootSequence.tsx [meridian_frontend/src/startup]"]
    N161["OnboardingWizard.tsx [meridian_frontend/src/startup]"]
    N162["SetupWizard.tsx [meridian_frontend/src/startup]"]
    N163["Clipboard.tsx [meridian_frontend/src/views]"]
    N164["Jobs.tsx [meridian_frontend/src/views]"]
    N165["Productivity.tsx [meridian_frontend/src/views]"]
    N166["Settings.tsx [meridian_frontend/src/views]"]
    N167["SwarmDebate.tsx [meridian_frontend/src/views]"]
    N168["Timeline.tsx [meridian_frontend/src/views]"]
    N169["WorkflowBuilder.tsx [meridian_frontend/src/views]"]
    N170["config.py [meridian_frontend/src-tauri/api/_internal/cv2]"]
    N171["load_config_py3.py [meridian_frontend/src-tauri/api/_internal/cv2]"]
    N172["__init__.py [meridian_frontend/src-tauri/api/_internal/cv2]"]
    N173["__init__.py [meridian_frontend/src-tauri/api/_internal/cv2/data]"]
    N174["__init__.py [meridian_frontend/src-tauri/api/_internal/cv2/mat_wrapper]"]
    N175["version.py [meridian_frontend/src-tauri/api/_internal/cv2/misc]"]
    N176["__init__.py [meridian_frontend/src-tauri/api/_internal/cv2/typing]"]
    N177["__init__.py [meridian_frontend/src-tauri/api/_internal/cv2/utils]"]
    N178["applications.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N179["background.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N180["cli.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N181["concurrency.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N182["datastructures.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N183["encoders.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N184["exceptions.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N185["exception_handlers.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N186["logger.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N187["params.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N188["param_functions.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N189["requests.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N190["responses.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N191["routing.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N192["sse.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N193["staticfiles.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N194["templating.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N195["testclient.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N196["types.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N197["utils.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N198["websockets.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N199["__init__.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N200["__main__.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N201["models.py [meridian_frontend/src-tauri/api/_internal/fastapi/dependencies]"]
    N202["utils.py [meridian_frontend/src-tauri/api/_internal/fastapi/dependencies]"]
    N203["asyncexitstack.py [meridian_frontend/src-tauri/api/_internal/fastapi/middleware]"]
    N204["cors.py [meridian_frontend/src-tauri/api/_internal/fastapi/middleware]"]
    N205["gzip.py [meridian_frontend/src-tauri/api/_internal/fastapi/middleware]"]
    N206["httpsredirect.py [meridian_frontend/src-tauri/api/_internal/fastapi/middleware]"]
    N207["trustedhost.py [meridian_frontend/src-tauri/api/_internal/fastapi/middleware]"]
    N208["wsgi.py [meridian_frontend/src-tauri/api/_internal/fastapi/middleware]"]
    N209["__init__.py [meridian_frontend/src-tauri/api/_internal/fastapi/middleware]"]
    N210["docs.py [meridian_frontend/src-tauri/api/_internal/fastapi/openapi]"]
    N211["models.py [meridian_frontend/src-tauri/api/_internal/fastapi/openapi]"]
    N212["utils.py [meridian_frontend/src-tauri/api/_internal/fastapi/openapi]"]
    N213["api_key.py [meridian_frontend/src-tauri/api/_internal/fastapi/security]"]
    N214["base.py [meridian_frontend/src-tauri/api/_internal/fastapi/security]"]
    N215["http.py [meridian_frontend/src-tauri/api/_internal/fastapi/security]"]
    N216["oauth2.py [meridian_frontend/src-tauri/api/_internal/fastapi/security]"]
    N217["open_id_connect_url.py [meridian_frontend/src-tauri/api/_internal/fastapi/security]"]
    N218["shared.py [meridian_frontend/src-tauri/api/_internal/fastapi/_compat]"]
    N219["v2.py [meridian_frontend/src-tauri/api/_internal/fastapi/_compat]"]
    N220["coreBundle.js [meridian_frontend/src-tauri/api/_internal/playwright/driver/package/lib]"]
    N221["utilsBundle.js [meridian_frontend/src-tauri/api/_internal/playwright/driver/package/lib]"]
    N222["structs.d.ts [meridian_frontend/src-tauri/api/_internal/playwright/driver/package/types]"]
    N223["types.d.ts [meridian_frontend/src-tauri/api/_internal/playwright/driver/package/types]"]
    N224["aliases.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N225["alias_generators.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N226["annotated_handlers.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N227["color.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N228["config.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N229["dataclasses.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N230["errors.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N231["fields.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N232["functional_serializers.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N233["functional_validators.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N234["json_schema.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N235["main.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N236["mypy.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N237["networks.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N238["root_model.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N239["types.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N240["type_adapter.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N241["validate_call_decorator.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N242["version.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N243["warnings.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N244["_migration.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N245["__init__.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N246["class_validators.py [meridian_frontend/src-tauri/api/_internal/pydantic/deprecated]"]
    N247["config.py [meridian_frontend/src-tauri/api/_internal/pydantic/deprecated]"]
    N248["copy_internals.py [meridian_frontend/src-tauri/api/_internal/pydantic/deprecated]"]
    N249["decorator.py [meridian_frontend/src-tauri/api/_internal/pydantic/deprecated]"]
    N250["json.py [meridian_frontend/src-tauri/api/_internal/pydantic/deprecated]"]
    N251["parse.py [meridian_frontend/src-tauri/api/_internal/pydantic/deprecated]"]
    N252["tools.py [meridian_frontend/src-tauri/api/_internal/pydantic/deprecated]"]
    N253["arguments_schema.py [meridian_frontend/src-tauri/api/_internal/pydantic/experimental]"]
    N254["missing_sentinel.py [meridian_frontend/src-tauri/api/_internal/pydantic/experimental]"]
    N255["pipeline.py [meridian_frontend/src-tauri/api/_internal/pydantic/experimental]"]
    N256["_loader.py [meridian_frontend/src-tauri/api/_internal/pydantic/plugin]"]
    N257["_schema_validator.py [meridian_frontend/src-tauri/api/_internal/pydantic/plugin]"]
    N258["__init__.py [meridian_frontend/src-tauri/api/_internal/pydantic/plugin]"]
    N259["annotated_types.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N260["class_validators.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N261["color.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N262["config.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N263["dataclasses.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N264["datetime_parse.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N265["decorator.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N266["env_settings.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N267["errors.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N268["error_wrappers.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N269["fields.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N270["generics.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N271["json.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N272["main.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N273["mypy.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N274["networks.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N275["parse.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N276["schema.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N277["tools.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N278["types.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N279["typing.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N280["utils.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N281["validators.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N282["version.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N283["_hypothesis_plugin.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N284["__init__.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N285["_config.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N286["_core_metadata.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N287["_core_utils.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N288["_dataclasses.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N289["_decorators.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N290["_decorators_v1.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N291["_discriminated_union.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N292["_docs_extraction.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N293["_fields.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N294["_forward_ref.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N295["_generate_schema.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N296["_generics.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N297["_git.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N298["_import_utils.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N299["_internal_dataclass.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N300["_known_annotated_metadata.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N301["_mock_val_ser.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N302["_model_construction.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N303["_namespace_utils.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N304["_repr.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N305["_schema_gather.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N306["_schema_generation_shared.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N307["_serializers.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N308["_signature.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N309["_typing_extra.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N310["_utils.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N311["_validate_call.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N312["_validators.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N313["applications.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N314["authentication.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N315["background.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N316["concurrency.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N317["config.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N318["convertors.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N319["datastructures.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N320["endpoints.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N321["exceptions.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N322["formparsers.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N323["requests.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N324["responses.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N325["routing.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N326["schemas.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N327["staticfiles.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N328["status.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N329["templating.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N330["testclient.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N331["types.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N332["websockets.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N333["_exception_handler.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N334["_utils.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N335["authentication.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N336["base.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N337["cors.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N338["errors.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N339["exceptions.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N340["gzip.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N341["httpsredirect.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N342["sessions.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N343["trustedhost.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N344["wsgi.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N345["__init__.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N346["config.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N347["importer.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N348["logging.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N349["main.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N350["server.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N351["workers.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N352["_compat.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N353["_subprocess.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N354["_types.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N355["__init__.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N356["__main__.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N357["off.py [meridian_frontend/src-tauri/api/_internal/uvicorn/lifespan]"]
    N358["on.py [meridian_frontend/src-tauri/api/_internal/uvicorn/lifespan]"]
    N359["asyncio.py [meridian_frontend/src-tauri/api/_internal/uvicorn/loops]"]
    N360["auto.py [meridian_frontend/src-tauri/api/_internal/uvicorn/loops]"]
    N361["uvloop.py [meridian_frontend/src-tauri/api/_internal/uvicorn/loops]"]
    N362["asgi2.py [meridian_frontend/src-tauri/api/_internal/uvicorn/middleware]"]
    N363["message_logger.py [meridian_frontend/src-tauri/api/_internal/uvicorn/middleware]"]
    N364["proxy_headers.py [meridian_frontend/src-tauri/api/_internal/uvicorn/middleware]"]
    N365["wsgi.py [meridian_frontend/src-tauri/api/_internal/uvicorn/middleware]"]
    N366["utils.py [meridian_frontend/src-tauri/api/_internal/uvicorn/protocols]"]
    N367["auto.py [meridian_frontend/src-tauri/api/_internal/uvicorn/protocols/http]"]
    N368["flow_control.py [meridian_frontend/src-tauri/api/_internal/uvicorn/protocols/http]"]
    N369["h11_impl.py [meridian_frontend/src-tauri/api/_internal/uvicorn/protocols/http]"]
    N370["httptools_impl.py [meridian_frontend/src-tauri/api/_internal/uvicorn/protocols/http]"]
    N371["auto.py [meridian_frontend/src-tauri/api/_internal/uvicorn/protocols/websockets]"]
    N372["websockets_impl.py [meridian_frontend/src-tauri/api/_internal/uvicorn/protocols/websockets]"]
    N373["websockets_sansio_impl.py [meridian_frontend/src-tauri/api/_internal/uvicorn/protocols/websockets]"]
    N374["wsproto_impl.py [meridian_frontend/src-tauri/api/_internal/uvicorn/protocols/websockets]"]
    N375["basereload.py [meridian_frontend/src-tauri/api/_internal/uvicorn/supervisors]"]
    N376["multiprocess.py [meridian_frontend/src-tauri/api/_internal/uvicorn/supervisors]"]
    N377["statreload.py [meridian_frontend/src-tauri/api/_internal/uvicorn/supervisors]"]
    N378["watchfilesreload.py [meridian_frontend/src-tauri/api/_internal/uvicorn/supervisors]"]
    N379["__init__.py [meridian_frontend/src-tauri/api/_internal/uvicorn/supervisors]"]
    N380["get_system_platform_info.py [plugins]"]

    N2 --> N250
    N2 --> N271
    N5 --> N359
    N5 --> N250
    N5 --> N271
    N5 --> N13
    N9 --> N229
    N9 --> N263
    N12 --> N9
    N12 --> N20
    N12 --> N170
    N12 --> N228
    N12 --> N247
    N12 --> N262
    N12 --> N317
    N12 --> N346
    N12 --> N11
    N12 --> N10
    N13 --> N359
    N13 --> N348
    N13 --> N250
    N13 --> N271
    N13 --> N279
    N13 --> N14
    N14 --> N250
    N14 --> N271
    N14 --> N279
    N15 --> N250
    N15 --> N271
    N15 --> N348
    N16 --> N279
    N17 --> N359
    N17 --> N279
    N18 --> N279
    N18 --> N14
    N19 --> N279
    N21 --> N359
    N21 --> N14
    N23 --> N250
    N23 --> N271
    N23 --> N279
    N23 --> N14
    N24 --> N279
    N24 --> N14
    N25 --> N279
    N26 --> N250
    N26 --> N271
    N26 --> N279
    N27 --> N250
    N27 --> N271
    N27 --> N279
    N28 --> N348
    N28 --> N279
    N30 --> N250
    N30 --> N271
    N30 --> N348
    N30 --> N359
    N30 --> N279
    N30 --> N14
    N31 --> N348
    N31 --> N250
    N31 --> N271
    N32 --> N250
    N32 --> N271
    N32 --> N359
    N32 --> N279
    N32 --> N14
    N33 --> N359
    N33 --> N279
    N34 --> N250
    N34 --> N271
    N34 --> N359
    N34 --> N279
    N34 --> N14
    N35 --> N250
    N35 --> N271
    N35 --> N359
    N35 --> N279
    N35 --> N14
    N36 --> N250
    N36 --> N271
    N36 --> N359
    N36 --> N279
    N37 --> N250
    N37 --> N271
    N37 --> N359
    N37 --> N348
    N37 --> N279
    N38 --> N359
    N38 --> N250
    N38 --> N271
    N38 --> N348
    N38 --> N279
    N39 --> N279
    N39 --> N250
    N39 --> N271
    N39 --> N14
    N40 --> N279
    N41 --> N250
    N41 --> N271
    N41 --> N279
    N42 --> N348
    N42 --> N359
    N42 --> N279
    N42 --> N250
    N42 --> N271
    N43 --> N250
    N43 --> N271
    N43 --> N279
    N43 --> N14
    N44 --> N348
    N44 --> N279
    N45 --> N279
    N46 --> N359
    N46 --> N279
    N46 --> N14
    N46 --> N13
    N47 --> N348
    N47 --> N279
    N48 --> N250
    N48 --> N271
    N48 --> N279
    N49 --> N279
    N50 --> N348
    N50 --> N279
    N51 --> N359
    N51 --> N14
    N51 --> N250
    N51 --> N271
    N52 --> N348
    N52 --> N279
    N53 --> N250
    N53 --> N271
    N53 --> N359
    N53 --> N279
    N53 --> N14
    N54 --> N359
    N54 --> N250
    N54 --> N271
    N54 --> N279
    N54 --> N14
    N55 --> N348
    N55 --> N279
    N56 --> N279
    N56 --> N359
    N56 --> N14
    N57 --> N279
    N58 --> N279
    N59 --> N250
    N59 --> N271
    N59 --> N279
    N60 --> N348
    N60 --> N279
    N60 --> N14
    N61 --> N348
    N61 --> N279
    N62 --> N250
    N62 --> N271
    N62 --> N279
    N63 --> N279
    N64 --> N250
    N64 --> N271
    N64 --> N279
    N65 --> N279
    N65 --> N14
    N66 --> N279
    N66 --> N14
    N67 --> N348
    N67 --> N279
    N67 --> N14
    N68 --> N279
    N68 --> N14
    N69 --> N279
    N69 --> N14
    N70 --> N359
    N70 --> N279
    N71 --> N279
    N72 --> N348
    N72 --> N279
    N73 --> N250
    N73 --> N271
    N73 --> N279
    N73 --> N14
    N74 --> N250
    N74 --> N271
    N74 --> N189
    N74 --> N323
    N74 --> N279
    N75 --> N279
    N76 --> N279
    N77 --> N279
    N77 --> N14
    N78 --> N250
    N78 --> N271
    N78 --> N279
    N79 --> N279
    N79 --> N14
    N80 --> N14
    N81 --> N250
    N81 --> N271
    N81 --> N279
    N81 --> N229
    N81 --> N263
    N81 --> N9
    N81 --> N20
    N81 --> N170
    N81 --> N228
    N81 --> N247
    N81 --> N262
    N81 --> N317
    N81 --> N346
    N81 --> N11
    N81 --> N10
    N82 --> N250
    N82 --> N271
    N82 --> N279
    N82 --> N14
    N83 --> N359
    N83 --> N279
    N83 --> N14
    N83 --> N250
    N83 --> N271
    N84 --> N279
    N84 --> N14
    N86 --> N279
    N87 --> N279
    N87 --> N14
    N90 --> N279
    N90 --> N250
    N90 --> N271
    N92 --> N279
    N93 --> N279
    N93 --> N14
    N94 --> N250
    N94 --> N271
    N94 --> N279
    N94 --> N14
    N95 --> N250
    N95 --> N271
    N95 --> N348
    N95 --> N279
    N95 --> N14
    N96 --> N359
    N96 --> N279
    N97 --> N348
    N97 --> N279
    N98 --> N279
    N98 --> N14
    N99 --> N348
    N99 --> N279
    N99 --> N14
    N100 --> N279
    N101 --> N14
    N104 --> N359
    N104 --> N13
    N105 --> N14
    N106 --> N13
    N108 --> N14
    N110 --> N14
    N111 --> N14
    N112 --> N14
    N113 --> N14
    N114 --> N13
    N116 --> N250
    N116 --> N271
    N116 --> N14
    N120 --> N359
    N121 --> N348
    N121 --> N250
    N121 --> N271
    N122 --> N250
    N122 --> N271
    N123 --> N359
    N124 --> N14
    N127 --> N14
    N128 --> N359
    N129 --> N359
    N129 --> N13
    N130 --> N13
    N130 --> N359
    N131 --> N13
    N132 --> N359
    N133 --> N359
    N134 --> N250
    N134 --> N271
    N136 --> N91
    N137 --> N13
    N138 --> N13
    N141 --> N196
    N141 --> N223
    N141 --> N239
    N141 --> N278
    N141 --> N331
    N141 --> N9
    N141 --> N20
    N141 --> N170
    N141 --> N228
    N141 --> N247
    N141 --> N262
    N141 --> N317
    N141 --> N346
    N142 --> N143
    N142 --> N160
    N142 --> N162
    N142 --> N149
    N142 --> N141
    N142 --> N9
    N142 --> N20
    N142 --> N170
    N142 --> N228
    N142 --> N247
    N142 --> N262
    N142 --> N317
    N142 --> N346
    N142 --> N161
    N142 --> N159
    N143 --> N144
    N143 --> N9
    N143 --> N20
    N143 --> N170
    N143 --> N228
    N143 --> N247
    N143 --> N262
    N143 --> N317
    N143 --> N346
    N146 --> N141
    N146 --> N143
    N147 --> N141
    N147 --> N155
    N147 --> N152
    N148 --> N9
    N148 --> N20
    N148 --> N170
    N148 --> N228
    N148 --> N247
    N148 --> N262
    N148 --> N317
    N148 --> N346
    N149 --> N141
    N149 --> N146
    N149 --> N150
    N149 --> N147
    N149 --> N168
    N149 --> N164
    N149 --> N163
    N149 --> N165
    N149 --> N167
    N149 --> N169
    N149 --> N166
    N149 --> N151
    N150 --> N141
    N150 --> N152
    N151 --> N157
    N158 --> N9
    N158 --> N20
    N158 --> N170
    N158 --> N228
    N158 --> N247
    N158 --> N262
    N158 --> N317
    N158 --> N346
    N159 --> N9
    N159 --> N20
    N159 --> N170
    N159 --> N228
    N159 --> N247
    N159 --> N262
    N159 --> N317
    N159 --> N346
    N160 --> N9
    N160 --> N20
    N160 --> N170
    N160 --> N228
    N160 --> N247
    N160 --> N262
    N160 --> N317
    N160 --> N346
    N160 --> N143
    N161 --> N9
    N161 --> N20
    N161 --> N170
    N161 --> N228
    N161 --> N247
    N161 --> N262
    N161 --> N317
    N161 --> N346
    N162 --> N154
    N162 --> N9
    N162 --> N20
    N162 --> N170
    N162 --> N228
    N162 --> N247
    N162 --> N262
    N162 --> N317
    N162 --> N346
    N163 --> N196
    N163 --> N223
    N163 --> N239
    N163 --> N278
    N163 --> N331
    N163 --> N141
    N163 --> N154
    N163 --> N9
    N163 --> N20
    N163 --> N170
    N163 --> N228
    N163 --> N247
    N163 --> N262
    N163 --> N317
    N163 --> N346
    N164 --> N196
    N164 --> N223
    N164 --> N239
    N164 --> N278
    N164 --> N331
    N164 --> N154
    N164 --> N153
    N164 --> N9
    N164 --> N20
    N164 --> N170
    N164 --> N228
    N164 --> N247
    N164 --> N262
    N164 --> N317
    N164 --> N346
    N165 --> N196
    N165 --> N223
    N165 --> N239
    N165 --> N278
    N165 --> N331
    N165 --> N155
    N165 --> N154
    N165 --> N153
    N165 --> N9
    N165 --> N20
    N165 --> N170
    N165 --> N228
    N165 --> N247
    N165 --> N262
    N165 --> N317
    N165 --> N346
    N166 --> N9
    N166 --> N20
    N166 --> N170
    N166 --> N228
    N166 --> N247
    N166 --> N262
    N166 --> N317
    N166 --> N346
    N166 --> N196
    N166 --> N223
    N166 --> N239
    N166 --> N278
    N166 --> N331
    N166 --> N141
    N166 --> N157
    N166 --> N155
    N166 --> N154
    N166 --> N153
    N167 --> N156
    N167 --> N154
    N167 --> N9
    N167 --> N20
    N167 --> N170
    N167 --> N228
    N167 --> N247
    N167 --> N262
    N167 --> N317
    N167 --> N346
    N168 --> N196
    N168 --> N223
    N168 --> N239
    N168 --> N278
    N168 --> N331
    N168 --> N154
    N168 --> N153
    N168 --> N9
    N168 --> N20
    N168 --> N170
    N168 --> N228
    N168 --> N247
    N168 --> N262
    N168 --> N317
    N168 --> N346
    N169 --> N9
    N169 --> N20
    N169 --> N170
    N169 --> N228
    N169 --> N247
    N169 --> N262
    N169 --> N317
    N169 --> N346
    N174 --> N279
    N176 --> N279
    N178 --> N279
    N179 --> N279
    N181 --> N279
    N182 --> N279
    N183 --> N229
    N183 --> N263
    N183 --> N196
    N183 --> N223
    N183 --> N239
    N183 --> N278
    N183 --> N331
    N183 --> N279
    N184 --> N279
    N186 --> N348
    N187 --> N243
    N187 --> N229
    N187 --> N263
    N187 --> N279
    N188 --> N279
    N190 --> N279
    N191 --> N250
    N191 --> N271
    N191 --> N196
    N191 --> N223
    N191 --> N239
    N191 --> N278
    N191 --> N331
    N191 --> N229
    N191 --> N263
    N191 --> N279
    N192 --> N279
    N196 --> N223
    N196 --> N239
    N196 --> N278
    N196 --> N331
    N196 --> N279
    N197 --> N243
    N197 --> N279
    N201 --> N229
    N201 --> N263
    N201 --> N279
    N201 --> N359
    N202 --> N229
    N202 --> N263
    N202 --> N279
    N210 --> N250
    N210 --> N271
    N210 --> N279
    N211 --> N279
    N212 --> N215
    N212 --> N243
    N212 --> N279
    N213 --> N279
    N215 --> N279
    N216 --> N279
    N217 --> N279
    N218 --> N196
    N218 --> N223
    N218 --> N239
    N218 --> N278
    N218 --> N331
    N218 --> N279
    N218 --> N243
    N218 --> N229
    N218 --> N263
    N219 --> N243
    N219 --> N229
    N219 --> N263
    N219 --> N279
    N222 --> N196
    N222 --> N223
    N222 --> N239
    N222 --> N278
    N222 --> N331
    N223 --> N222
    N224 --> N229
    N224 --> N263
    N224 --> N279
    N226 --> N279
    N227 --> N279
    N228 --> N243
    N228 --> N279
    N229 --> N263
    N229 --> N196
    N229 --> N223
    N229 --> N239
    N229 --> N278
    N229 --> N331
    N229 --> N279
    N229 --> N243
    N230 --> N279
    N231 --> N229
    N231 --> N263
    N231 --> N279
    N231 --> N243
    N231 --> N259
    N232 --> N229
    N232 --> N263
    N232 --> N279
    N233 --> N229
    N233 --> N263
    N233 --> N243
    N233 --> N279
    N234 --> N229
    N234 --> N263
    N234 --> N243
    N234 --> N279
    N235 --> N196
    N235 --> N223
    N235 --> N239
    N235 --> N278
    N235 --> N331
    N235 --> N243
    N235 --> N279
    N235 --> N250
    N235 --> N271
    N236 --> N279
    N236 --> N273
    N236 --> N243
    N237 --> N229
    N237 --> N263
    N237 --> N279
    N238 --> N279
    N239 --> N229
    N239 --> N263
    N239 --> N196
    N239 --> N223
    N239 --> N278
    N239 --> N331
    N239 --> N279
    N239 --> N259
    N239 --> N250
    N239 --> N271
    N240 --> N196
    N240 --> N223
    N240 --> N239
    N240 --> N278
    N240 --> N331
    N240 --> N229
    N240 --> N263
    N240 --> N279
    N241 --> N196
    N241 --> N223
    N241 --> N239
    N241 --> N278
    N241 --> N331
    N241 --> N279
    N244 --> N279
    N244 --> N243
    N245 --> N279
    N245 --> N243
    N246 --> N196
    N246 --> N223
    N246 --> N239
    N246 --> N278
    N246 --> N331
    N246 --> N279
    N246 --> N243
    N247 --> N243
    N247 --> N279
    N248 --> N279
    N249 --> N243
    N249 --> N279
    N250 --> N243
    N250 --> N196
    N250 --> N223
    N250 --> N239
    N250 --> N278
    N250 --> N331
    N250 --> N279
    N250 --> N229
    N250 --> N263
    N251 --> N250
    N251 --> N271
    N251 --> N243
    N251 --> N279
    N252 --> N250
    N252 --> N271
    N252 --> N243
    N252 --> N279
    N253 --> N279
    N255 --> N229
    N255 --> N263
    N255 --> N279
    N255 --> N259
    N255 --> N196
    N255 --> N223
    N255 --> N239
    N255 --> N278
    N255 --> N331
    N256 --> N243
    N256 --> N279
    N257 --> N279
    N258 --> N279
    N259 --> N279
    N260 --> N243
    N260 --> N196
    N260 --> N223
    N260 --> N239
    N260 --> N278
    N260 --> N331
    N260 --> N279
    N261 --> N279
    N262 --> N250
    N262 --> N271
    N262 --> N279
    N263 --> N229
    N263 --> N279
    N264 --> N279
    N265 --> N279
    N266 --> N243
    N266 --> N279
    N267 --> N279
    N268 --> N250
    N268 --> N271
    N268 --> N279
    N269 --> N279
    N270 --> N196
    N270 --> N223
    N270 --> N239
    N270 --> N278
    N270 --> N331
    N270 --> N279
    N271 --> N196
    N271 --> N223
    N271 --> N239
    N271 --> N278
    N271 --> N331
    N271 --> N279
    N271 --> N229
    N271 --> N263
    N272 --> N243
    N272 --> N196
    N272 --> N223
    N272 --> N239
    N272 --> N278
    N272 --> N331
    N272 --> N279
    N273 --> N279
    N273 --> N236
    N273 --> N243
    N274 --> N279
    N275 --> N250
    N275 --> N271
    N275 --> N279
    N276 --> N243
    N276 --> N229
    N276 --> N263
    N276 --> N279
    N277 --> N250
    N277 --> N271
    N277 --> N279
    N278 --> N243
    N278 --> N196
    N278 --> N223
    N278 --> N239
    N278 --> N331
    N278 --> N279
    N279 --> N196
    N279 --> N223
    N279 --> N239
    N279 --> N278
    N279 --> N331
    N280 --> N243
    N280 --> N196
    N280 --> N223
    N280 --> N239
    N280 --> N278
    N280 --> N331
    N280 --> N279
    N281 --> N279
    N281 --> N243
    N283 --> N250
    N283 --> N271
    N283 --> N279
    N285 --> N243
    N285 --> N279
    N286 --> N279
    N286 --> N243
    N287 --> N279
    N288 --> N229
    N288 --> N263
    N288 --> N243
    N288 --> N279
    N289 --> N196
    N289 --> N223
    N289 --> N239
    N289 --> N278
    N289 --> N331
    N289 --> N229
    N289 --> N263
    N289 --> N279
    N290 --> N279
    N291 --> N279
    N292 --> N279
    N293 --> N229
    N293 --> N263
    N293 --> N243
    N293 --> N279
    N293 --> N259
    N294 --> N229
    N294 --> N263
    N294 --> N279
    N295 --> N229
    N295 --> N263
    N295 --> N279
    N295 --> N243
    N295 --> N196
    N295 --> N223
    N295 --> N239
    N295 --> N278
    N295 --> N331
    N296 --> N196
    N296 --> N223
    N296 --> N239
    N296 --> N278
    N296 --> N331
    N296 --> N279
    N298 --> N279
    N300 --> N279
    N300 --> N259
    N301 --> N279
    N302 --> N279
    N302 --> N243
    N302 --> N196
    N302 --> N223
    N302 --> N239
    N302 --> N278
    N302 --> N331
    N303 --> N279
    N304 --> N196
    N304 --> N223
    N304 --> N239
    N304 --> N278
    N304 --> N331
    N304 --> N279
    N305 --> N229
    N305 --> N263
    N305 --> N279
    N306 --> N279
    N307 --> N279
    N308 --> N229
    N308 --> N263
    N308 --> N279
    N309 --> N196
    N309 --> N223
    N309 --> N239
    N309 --> N278
    N309 --> N331
    N309 --> N279
    N310 --> N229
    N310 --> N263
    N310 --> N243
    N310 --> N196
    N310 --> N223
    N310 --> N239
    N310 --> N278
    N310 --> N331
    N310 --> N279
    N311 --> N279
    N312 --> N279
    N313 --> N279
    N314 --> N279
    N315 --> N279
    N316 --> N243
    N316 --> N279
    N317 --> N243
    N317 --> N279
    N318 --> N279
    N319 --> N279
    N320 --> N250
    N320 --> N271
    N320 --> N279
    N321 --> N215
    N322 --> N229
    N322 --> N263
    N322 --> N279
    N323 --> N250
    N323 --> N271
    N323 --> N215
    N323 --> N279
    N324 --> N215
    N324 --> N250
    N324 --> N271
    N324 --> N279
    N325 --> N196
    N325 --> N223
    N325 --> N239
    N325 --> N278
    N325 --> N331
    N325 --> N243
    N325 --> N279
    N326 --> N279
    N327 --> N279
    N328 --> N243
    N329 --> N279
    N330 --> N250
    N330 --> N271
    N330 --> N243
    N330 --> N196
    N330 --> N223
    N330 --> N239
    N330 --> N278
    N330 --> N331
    N330 --> N279
    N331 --> N279
    N332 --> N250
    N332 --> N271
    N332 --> N279
    N333 --> N279
    N334 --> N279
    N334 --> N359
    N336 --> N279
    N339 --> N279
    N340 --> N205
    N340 --> N279
    N342 --> N250
    N342 --> N271
    N342 --> N279
    N344 --> N243
    N344 --> N279
    N345 --> N279
    N346 --> N359
    N346 --> N250
    N346 --> N271
    N346 --> N348
    N346 --> N279
    N347 --> N279
    N348 --> N215
    N348 --> N279
    N349 --> N359
    N349 --> N348
    N349 --> N243
    N349 --> N279
    N350 --> N359
    N350 --> N348
    N350 --> N196
    N350 --> N223
    N350 --> N239
    N350 --> N278
    N350 --> N331
    N350 --> N279
    N351 --> N359
    N351 --> N348
    N351 --> N243
    N351 --> N279
    N352 --> N359
    N352 --> N279
    N354 --> N196
    N354 --> N223
    N354 --> N239
    N354 --> N278
    N354 --> N331
    N354 --> N279
    N357 --> N279
    N358 --> N359
    N358 --> N348
    N358 --> N279
    N360 --> N359
    N360 --> N361
    N361 --> N359
    N363 --> N348
    N363 --> N279
    N365 --> N359
    N365 --> N243
    N366 --> N359
    N367 --> N359
    N368 --> N359
    N369 --> N359
    N369 --> N215
    N369 --> N348
    N369 --> N279
    N370 --> N359
    N370 --> N215
    N370 --> N348
    N370 --> N279
    N371 --> N359
    N371 --> N198
    N371 --> N332
    N372 --> N359
    N372 --> N215
    N372 --> N348
    N372 --> N279
    N372 --> N198
    N372 --> N332
    N373 --> N359
    N373 --> N348
    N373 --> N215
    N373 --> N279
    N373 --> N198
    N373 --> N332
    N374 --> N359
    N374 --> N348
    N374 --> N279
    N375 --> N348
    N375 --> N196
    N375 --> N223
    N375 --> N239
    N375 --> N278
    N375 --> N331
    N376 --> N348
    N376 --> N279
    N377 --> N348
    N379 --> N279
```

## Detailed File Index
- **build_standalone.py**
  - Imports: `glob`
  - Imports: `os`
  - Imports: `platform`
  - Imports: `shutil`
  - Imports: `subprocess`
  - Imports: `sys`
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
- **meridian_backend/src/core/bus.py**
  - Imports: `asyncio`
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
  - Imports: `threading`
  - Imports: `time`
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
- **meridian_backend/src/core/exporter.py**
  - Imports: `database`
  - Imports: `os`
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
- **meridian_backend/src/core/mode.py**
  - Imports: `database`
  - Imports: `datetime`
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
- **meridian_backend/src/core/security_middleware.py**
  - Imports: `fastapi`
  - Imports: `logging`
  - Imports: `starlette`
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
- **meridian_backend/src/tools/browser_agent.py**
  - Imports: `json`
  - Imports: `os`
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
- **meridian_backend/src/tools/documents.py**
  - Imports: `docx`
  - Imports: `openpyxl`
  - Imports: `os`
  - Imports: `pptx`
  - Imports: `pypdf`
  - Imports: `re`
  - Imports: `reportlab`
  - Imports: `src`
  - Imports: `typing`
  - Imports: `xlrd`
- **meridian_backend/src/tools/dynamic_manager.py**
  - Imports: `ast`
  - Imports: `logging`
  - Imports: `os`
  - Imports: `src`
  - Imports: `sys`
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
- **meridian_backend/src/tools/filesystem.py**
  - Imports: `glob`
  - Imports: `os`
  - Imports: `shutil`
  - Imports: `src`
  - Imports: `typing`
- **meridian_backend/src/tools/geo_location.py**
  - Imports: `httpx`
  - Imports: `os`
  - Imports: `time`
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
- **meridian_backend/src/tools/recording.py**
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
- **meridian_backend/src/tools/vault.py**
  - Imports: `base64`
  - Imports: `cryptography`
  - Imports: `json`
  - Imports: `os`
  - Imports: `src`
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
  - Imports: `pytest`
  - Imports: `src`
  - Imports: `time`
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
- **meridian_backend/tests/test_day3_features.py**
  - Imports: `database`
  - Imports: `pytest`
  - Imports: `src`
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