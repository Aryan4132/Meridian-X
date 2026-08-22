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
    N65["clipboard.py [meridian_backend/src/tools]"]
    N66["communication.py [meridian_backend/src/tools]"]
    N67["db_query.py [meridian_backend/src/tools]"]
    N68["desktop.py [meridian_backend/src/tools]"]
    N69["developer.py [meridian_backend/src/tools]"]
    N70["documents.py [meridian_backend/src/tools]"]
    N71["dynamic_manager.py [meridian_backend/src/tools]"]
    N72["exporter.py [meridian_backend/src/tools]"]
    N73["external_connectors.py [meridian_backend/src/tools]"]
    N74["filesystem.py [meridian_backend/src/tools]"]
    N75["geo_location.py [meridian_backend/src/tools]"]
    N76["knowledge.py [meridian_backend/src/tools]"]
    N77["mcp_marketplace.py [meridian_backend/src/tools]"]
    N78["ollama_manager.py [meridian_backend/src/tools]"]
    N79["papercoder.py [meridian_backend/src/tools]"]
    N80["recording.py [meridian_backend/src/tools]"]
    N81["registry.py [meridian_backend/src/tools]"]
    N82["review.py [meridian_backend/src/tools]"]
    N83["scheduler.py [meridian_backend/src/tools]"]
    N84["security_auditor.py [meridian_backend/src/tools]"]
    N85["shell.py [meridian_backend/src/tools]"]
    N86["system.py [meridian_backend/src/tools]"]
    N87["task_scheduler.py [meridian_backend/src/tools]"]
    N88["vault.py [meridian_backend/src/tools]"]
    N89["voice.py [meridian_backend/src/tools]"]
    N90["watcher.py [meridian_backend/src/tools]"]
    N91["web.py [meridian_backend/src/tools]"]
    N92["web_browser.py [meridian_backend/src/tools]"]
    N93["whatsapp_manager.py [meridian_backend/src/tools]"]
    N94["duplex.py [meridian_backend/src/voice]"]
    N95["polyglot.py [meridian_backend/src/voice]"]
    N96["stt.py [meridian_backend/src/voice]"]
    N97["tts.py [meridian_backend/src/voice]"]
    N98["voice_biometrics.py [meridian_backend/src/voice]"]
    N99["wakeword.py [meridian_backend/src/voice]"]
    N100["conftest.py [meridian_backend/tests]"]
    N101["run_tests.py [meridian_backend/tests]"]
    N102["test_auto_bug_fixer.py [meridian_backend/tests]"]
    N103["test_backlog_features.py [meridian_backend/tests]"]
    N104["test_backlog_sprint.py [meridian_backend/tests]"]
    N105["test_bridges.py [meridian_backend/tests]"]
    N106["test_config.py [meridian_backend/tests]"]
    N107["test_context_budget.py [meridian_backend/tests]"]
    N108["test_database.py [meridian_backend/tests]"]
    N109["test_day3_features.py [meridian_backend/tests]"]
    N110["test_day4_features.py [meridian_backend/tests]"]
    N111["test_day5_features.py [meridian_backend/tests]"]
    N112["test_day6_features.py [meridian_backend/tests]"]
    N113["test_document_tools.py [meridian_backend/tests]"]
    N114["test_geo_location.py [meridian_backend/tests]"]
    N115["test_jarvis_perception.py [meridian_backend/tests]"]
    N116["test_llm_provider.py [meridian_backend/tests]"]
    N117["test_logging.py [meridian_backend/tests]"]
    N118["test_loop_parser.py [meridian_backend/tests]"]
    N119["test_loop_submodules.py [meridian_backend/tests]"]
    N120["test_model_source.py [meridian_backend/tests]"]
    N121["test_multi_os.py [meridian_backend/tests]"]
    N122["test_oauth.py [meridian_backend/tests]"]
    N123["test_p2p.py [meridian_backend/tests]"]
    N124["test_proactive.py [meridian_backend/tests]"]
    N125["test_proactive_notifications.py [meridian_backend/tests]"]
    N126["test_security_features.py [meridian_backend/tests]"]
    N127["test_sprint2_features.py [meridian_backend/tests]"]
    N128["test_stream_resiliency.py [meridian_backend/tests]"]
    N129["test_swarm.py [meridian_backend/tests]"]
    N130["test_tools.py [meridian_backend/tests]"]
    N131["test_vault.py [meridian_backend/tests]"]
    N132["test_voice_speed.py [meridian_backend/tests]"]
    N133["test_wakeword_continuous.py [meridian_backend/tests]"]
    N134["test_wakeword_onnx.py [meridian_backend/tests]"]
    N135["test_workflow.py [meridian_backend/tests]"]
    N136["vite.config.ts [meridian_frontend]"]
    N137["AppContext.tsx [meridian_frontend/src]"]
    N138["main.tsx [meridian_frontend/src]"]
    N139["Mascot.tsx [meridian_frontend/src]"]
    N140["Mascot3DCharacter.tsx [meridian_frontend/src]"]
    N141["CommandPalette.tsx [meridian_frontend/src/components]"]
    N142["NavRail.tsx [meridian_frontend/src/components]"]
    N143["RightDrawer.tsx [meridian_frontend/src/components]"]
    N144["ServerConnectionModal.tsx [meridian_frontend/src/components]"]
    N145["Shell.tsx [meridian_frontend/src/components]"]
    N146["StatusBar.tsx [meridian_frontend/src/components]"]
    N147["AmbientParticles.tsx [meridian_frontend/src/components/ui]"]
    N148["DataBadge.tsx [meridian_frontend/src/components/ui]"]
    N149["GlowCard.tsx [meridian_frontend/src/components/ui]"]
    N150["HoloButton.tsx [meridian_frontend/src/components/ui]"]
    N151["ProgressArc.tsx [meridian_frontend/src/components/ui]"]
    N152["TerminalLine.tsx [meridian_frontend/src/components/ui]"]
    N153["useMemoryOptimizer.ts [meridian_frontend/src/hooks]"]
    N154["oauthService.ts [meridian_frontend/src/services]"]
    N155["BackendSetup.tsx [meridian_frontend/src/startup]"]
    N156["BootSequence.tsx [meridian_frontend/src/startup]"]
    N157["OnboardingWizard.tsx [meridian_frontend/src/startup]"]
    N158["SetupWizard.tsx [meridian_frontend/src/startup]"]
    N159["Clipboard.tsx [meridian_frontend/src/views]"]
    N160["Jobs.tsx [meridian_frontend/src/views]"]
    N161["Productivity.tsx [meridian_frontend/src/views]"]
    N162["Settings.tsx [meridian_frontend/src/views]"]
    N163["SwarmDebate.tsx [meridian_frontend/src/views]"]
    N164["Timeline.tsx [meridian_frontend/src/views]"]
    N165["WorkflowBuilder.tsx [meridian_frontend/src/views]"]
    N166["applications.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N167["background.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N168["cli.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N169["concurrency.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N170["datastructures.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N171["encoders.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N172["exceptions.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N173["exception_handlers.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N174["logger.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N175["params.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N176["param_functions.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N177["requests.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N178["responses.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N179["routing.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N180["sse.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N181["staticfiles.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N182["templating.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N183["testclient.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N184["types.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N185["utils.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N186["websockets.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N187["__init__.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N188["__main__.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N189["models.py [meridian_frontend/src-tauri/api/_internal/fastapi/dependencies]"]
    N190["utils.py [meridian_frontend/src-tauri/api/_internal/fastapi/dependencies]"]
    N191["asyncexitstack.py [meridian_frontend/src-tauri/api/_internal/fastapi/middleware]"]
    N192["cors.py [meridian_frontend/src-tauri/api/_internal/fastapi/middleware]"]
    N193["gzip.py [meridian_frontend/src-tauri/api/_internal/fastapi/middleware]"]
    N194["httpsredirect.py [meridian_frontend/src-tauri/api/_internal/fastapi/middleware]"]
    N195["trustedhost.py [meridian_frontend/src-tauri/api/_internal/fastapi/middleware]"]
    N196["wsgi.py [meridian_frontend/src-tauri/api/_internal/fastapi/middleware]"]
    N197["__init__.py [meridian_frontend/src-tauri/api/_internal/fastapi/middleware]"]
    N198["docs.py [meridian_frontend/src-tauri/api/_internal/fastapi/openapi]"]
    N199["models.py [meridian_frontend/src-tauri/api/_internal/fastapi/openapi]"]
    N200["utils.py [meridian_frontend/src-tauri/api/_internal/fastapi/openapi]"]
    N201["api_key.py [meridian_frontend/src-tauri/api/_internal/fastapi/security]"]
    N202["base.py [meridian_frontend/src-tauri/api/_internal/fastapi/security]"]
    N203["http.py [meridian_frontend/src-tauri/api/_internal/fastapi/security]"]
    N204["oauth2.py [meridian_frontend/src-tauri/api/_internal/fastapi/security]"]
    N205["open_id_connect_url.py [meridian_frontend/src-tauri/api/_internal/fastapi/security]"]
    N206["shared.py [meridian_frontend/src-tauri/api/_internal/fastapi/_compat]"]
    N207["v2.py [meridian_frontend/src-tauri/api/_internal/fastapi/_compat]"]
    N208["coreBundle.js [meridian_frontend/src-tauri/api/_internal/playwright/driver/package/lib]"]
    N209["utilsBundle.js [meridian_frontend/src-tauri/api/_internal/playwright/driver/package/lib]"]
    N210["structs.d.ts [meridian_frontend/src-tauri/api/_internal/playwright/driver/package/types]"]
    N211["types.d.ts [meridian_frontend/src-tauri/api/_internal/playwright/driver/package/types]"]
    N212["aliases.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N213["alias_generators.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N214["annotated_handlers.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N215["color.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N216["config.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N217["dataclasses.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N218["errors.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N219["fields.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N220["functional_serializers.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N221["functional_validators.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N222["json_schema.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N223["main.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N224["mypy.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N225["networks.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N226["root_model.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N227["types.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N228["type_adapter.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N229["validate_call_decorator.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N230["version.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N231["warnings.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N232["_migration.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N233["__init__.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N234["class_validators.py [meridian_frontend/src-tauri/api/_internal/pydantic/deprecated]"]
    N235["config.py [meridian_frontend/src-tauri/api/_internal/pydantic/deprecated]"]
    N236["copy_internals.py [meridian_frontend/src-tauri/api/_internal/pydantic/deprecated]"]
    N237["decorator.py [meridian_frontend/src-tauri/api/_internal/pydantic/deprecated]"]
    N238["json.py [meridian_frontend/src-tauri/api/_internal/pydantic/deprecated]"]
    N239["parse.py [meridian_frontend/src-tauri/api/_internal/pydantic/deprecated]"]
    N240["tools.py [meridian_frontend/src-tauri/api/_internal/pydantic/deprecated]"]
    N241["arguments_schema.py [meridian_frontend/src-tauri/api/_internal/pydantic/experimental]"]
    N242["missing_sentinel.py [meridian_frontend/src-tauri/api/_internal/pydantic/experimental]"]
    N243["pipeline.py [meridian_frontend/src-tauri/api/_internal/pydantic/experimental]"]
    N244["_loader.py [meridian_frontend/src-tauri/api/_internal/pydantic/plugin]"]
    N245["_schema_validator.py [meridian_frontend/src-tauri/api/_internal/pydantic/plugin]"]
    N246["__init__.py [meridian_frontend/src-tauri/api/_internal/pydantic/plugin]"]
    N247["annotated_types.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N248["class_validators.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N249["color.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N250["config.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N251["dataclasses.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N252["datetime_parse.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N253["decorator.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N254["env_settings.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N255["errors.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N256["error_wrappers.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N257["fields.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N258["generics.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N259["json.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N260["main.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N261["mypy.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N262["networks.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N263["parse.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N264["schema.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N265["tools.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N266["types.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N267["typing.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N268["utils.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N269["validators.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N270["version.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N271["_hypothesis_plugin.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N272["__init__.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N273["_config.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N274["_core_metadata.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N275["_core_utils.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N276["_dataclasses.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N277["_decorators.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N278["_decorators_v1.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N279["_discriminated_union.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N280["_docs_extraction.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N281["_fields.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N282["_forward_ref.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N283["_generate_schema.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N284["_generics.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N285["_git.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N286["_import_utils.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N287["_internal_dataclass.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N288["_known_annotated_metadata.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N289["_mock_val_ser.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N290["_model_construction.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N291["_namespace_utils.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N292["_repr.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N293["_schema_gather.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N294["_schema_generation_shared.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N295["_serializers.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N296["_signature.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N297["_typing_extra.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N298["_utils.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N299["_validate_call.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N300["_validators.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N301["applications.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N302["authentication.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N303["background.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N304["concurrency.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N305["config.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N306["convertors.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N307["datastructures.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N308["endpoints.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N309["exceptions.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N310["formparsers.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N311["requests.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N312["responses.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N313["routing.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N314["schemas.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N315["staticfiles.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N316["status.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N317["templating.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N318["testclient.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N319["types.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N320["websockets.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N321["_exception_handler.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N322["_utils.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N323["authentication.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N324["base.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N325["cors.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N326["errors.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N327["exceptions.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N328["gzip.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N329["httpsredirect.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N330["sessions.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N331["trustedhost.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N332["wsgi.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N333["__init__.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N334["config.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N335["importer.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N336["logging.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N337["main.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N338["server.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N339["workers.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N340["_compat.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N341["_subprocess.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N342["_types.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N343["__init__.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N344["__main__.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N345["off.py [meridian_frontend/src-tauri/api/_internal/uvicorn/lifespan]"]
    N346["on.py [meridian_frontend/src-tauri/api/_internal/uvicorn/lifespan]"]
    N347["asyncio.py [meridian_frontend/src-tauri/api/_internal/uvicorn/loops]"]
    N348["auto.py [meridian_frontend/src-tauri/api/_internal/uvicorn/loops]"]
    N349["uvloop.py [meridian_frontend/src-tauri/api/_internal/uvicorn/loops]"]
    N350["asgi2.py [meridian_frontend/src-tauri/api/_internal/uvicorn/middleware]"]
    N351["message_logger.py [meridian_frontend/src-tauri/api/_internal/uvicorn/middleware]"]
    N352["proxy_headers.py [meridian_frontend/src-tauri/api/_internal/uvicorn/middleware]"]
    N353["wsgi.py [meridian_frontend/src-tauri/api/_internal/uvicorn/middleware]"]
    N354["utils.py [meridian_frontend/src-tauri/api/_internal/uvicorn/protocols]"]
    N355["auto.py [meridian_frontend/src-tauri/api/_internal/uvicorn/protocols/http]"]
    N356["flow_control.py [meridian_frontend/src-tauri/api/_internal/uvicorn/protocols/http]"]
    N357["h11_impl.py [meridian_frontend/src-tauri/api/_internal/uvicorn/protocols/http]"]
    N358["httptools_impl.py [meridian_frontend/src-tauri/api/_internal/uvicorn/protocols/http]"]
    N359["auto.py [meridian_frontend/src-tauri/api/_internal/uvicorn/protocols/websockets]"]
    N360["websockets_impl.py [meridian_frontend/src-tauri/api/_internal/uvicorn/protocols/websockets]"]
    N361["websockets_sansio_impl.py [meridian_frontend/src-tauri/api/_internal/uvicorn/protocols/websockets]"]
    N362["wsproto_impl.py [meridian_frontend/src-tauri/api/_internal/uvicorn/protocols/websockets]"]
    N363["basereload.py [meridian_frontend/src-tauri/api/_internal/uvicorn/supervisors]"]
    N364["multiprocess.py [meridian_frontend/src-tauri/api/_internal/uvicorn/supervisors]"]
    N365["statreload.py [meridian_frontend/src-tauri/api/_internal/uvicorn/supervisors]"]
    N366["watchfilesreload.py [meridian_frontend/src-tauri/api/_internal/uvicorn/supervisors]"]
    N367["__init__.py [meridian_frontend/src-tauri/api/_internal/uvicorn/supervisors]"]
    N368["get_system_platform_info.py [plugins]"]

    N2 --> N238
    N2 --> N259
    N5 --> N347
    N5 --> N238
    N5 --> N259
    N5 --> N13
    N9 --> N217
    N9 --> N251
    N12 --> N9
    N12 --> N20
    N12 --> N216
    N12 --> N235
    N12 --> N250
    N12 --> N305
    N12 --> N334
    N12 --> N11
    N12 --> N10
    N13 --> N347
    N13 --> N336
    N13 --> N238
    N13 --> N259
    N13 --> N267
    N13 --> N14
    N14 --> N238
    N14 --> N259
    N14 --> N267
    N15 --> N238
    N15 --> N259
    N15 --> N336
    N16 --> N267
    N17 --> N347
    N17 --> N267
    N18 --> N267
    N18 --> N14
    N19 --> N267
    N21 --> N347
    N21 --> N14
    N23 --> N238
    N23 --> N259
    N23 --> N14
    N24 --> N267
    N24 --> N14
    N25 --> N267
    N26 --> N238
    N26 --> N259
    N26 --> N267
    N27 --> N238
    N27 --> N259
    N27 --> N267
    N28 --> N336
    N28 --> N267
    N30 --> N238
    N30 --> N259
    N30 --> N336
    N30 --> N347
    N30 --> N267
    N30 --> N14
    N31 --> N336
    N31 --> N238
    N31 --> N259
    N32 --> N238
    N32 --> N259
    N32 --> N347
    N32 --> N267
    N32 --> N14
    N33 --> N347
    N33 --> N267
    N34 --> N238
    N34 --> N259
    N34 --> N347
    N34 --> N267
    N34 --> N14
    N35 --> N238
    N35 --> N259
    N35 --> N347
    N35 --> N267
    N35 --> N14
    N36 --> N238
    N36 --> N259
    N36 --> N347
    N36 --> N267
    N37 --> N238
    N37 --> N259
    N37 --> N347
    N37 --> N336
    N37 --> N267
    N38 --> N347
    N38 --> N238
    N38 --> N259
    N38 --> N336
    N38 --> N267
    N39 --> N267
    N39 --> N238
    N39 --> N259
    N39 --> N14
    N40 --> N267
    N41 --> N238
    N41 --> N259
    N41 --> N267
    N42 --> N336
    N42 --> N347
    N42 --> N267
    N42 --> N238
    N42 --> N259
    N43 --> N238
    N43 --> N259
    N43 --> N267
    N43 --> N14
    N44 --> N336
    N44 --> N267
    N45 --> N267
    N46 --> N347
    N46 --> N267
    N46 --> N14
    N46 --> N13
    N47 --> N336
    N47 --> N267
    N48 --> N238
    N48 --> N259
    N48 --> N267
    N49 --> N267
    N50 --> N336
    N50 --> N267
    N51 --> N347
    N51 --> N14
    N51 --> N238
    N51 --> N259
    N52 --> N336
    N52 --> N267
    N53 --> N238
    N53 --> N259
    N53 --> N347
    N53 --> N267
    N53 --> N14
    N54 --> N347
    N54 --> N238
    N54 --> N259
    N54 --> N267
    N54 --> N14
    N55 --> N336
    N55 --> N267
    N56 --> N267
    N56 --> N347
    N56 --> N14
    N57 --> N267
    N58 --> N267
    N59 --> N238
    N59 --> N259
    N59 --> N267
    N60 --> N336
    N60 --> N14
    N61 --> N336
    N61 --> N267
    N62 --> N238
    N62 --> N259
    N62 --> N267
    N63 --> N267
    N64 --> N238
    N64 --> N259
    N64 --> N267
    N65 --> N267
    N65 --> N14
    N66 --> N336
    N66 --> N267
    N66 --> N14
    N67 --> N267
    N67 --> N14
    N68 --> N267
    N68 --> N14
    N69 --> N347
    N69 --> N267
    N70 --> N267
    N71 --> N336
    N71 --> N267
    N72 --> N238
    N72 --> N259
    N72 --> N267
    N72 --> N14
    N73 --> N238
    N73 --> N259
    N73 --> N177
    N73 --> N311
    N73 --> N267
    N74 --> N267
    N75 --> N267
    N76 --> N267
    N76 --> N14
    N77 --> N238
    N77 --> N259
    N77 --> N267
    N78 --> N14
    N79 --> N238
    N79 --> N259
    N79 --> N267
    N79 --> N217
    N79 --> N251
    N79 --> N9
    N79 --> N20
    N79 --> N216
    N79 --> N235
    N79 --> N250
    N79 --> N305
    N79 --> N334
    N79 --> N11
    N79 --> N10
    N80 --> N238
    N80 --> N259
    N80 --> N267
    N80 --> N14
    N81 --> N347
    N81 --> N267
    N81 --> N14
    N81 --> N238
    N81 --> N259
    N82 --> N267
    N82 --> N14
    N84 --> N267
    N85 --> N267
    N85 --> N14
    N88 --> N267
    N88 --> N238
    N88 --> N259
    N90 --> N267
    N91 --> N267
    N91 --> N14
    N92 --> N238
    N92 --> N259
    N92 --> N267
    N92 --> N14
    N93 --> N238
    N93 --> N259
    N93 --> N336
    N93 --> N267
    N93 --> N14
    N94 --> N347
    N94 --> N267
    N95 --> N336
    N95 --> N267
    N96 --> N267
    N96 --> N14
    N97 --> N336
    N97 --> N267
    N97 --> N14
    N98 --> N267
    N99 --> N14
    N102 --> N347
    N102 --> N13
    N103 --> N14
    N104 --> N13
    N107 --> N14
    N108 --> N14
    N109 --> N14
    N110 --> N14
    N111 --> N13
    N116 --> N347
    N117 --> N336
    N117 --> N238
    N117 --> N259
    N118 --> N238
    N118 --> N259
    N119 --> N347
    N120 --> N14
    N123 --> N14
    N124 --> N347
    N125 --> N347
    N125 --> N13
    N126 --> N13
    N126 --> N347
    N127 --> N13
    N128 --> N347
    N129 --> N347
    N130 --> N238
    N130 --> N259
    N132 --> N89
    N133 --> N13
    N134 --> N13
    N137 --> N184
    N137 --> N211
    N137 --> N227
    N137 --> N266
    N137 --> N319
    N137 --> N9
    N137 --> N20
    N137 --> N216
    N137 --> N235
    N137 --> N250
    N137 --> N305
    N137 --> N334
    N138 --> N139
    N138 --> N156
    N138 --> N158
    N138 --> N145
    N138 --> N137
    N138 --> N9
    N138 --> N20
    N138 --> N216
    N138 --> N235
    N138 --> N250
    N138 --> N305
    N138 --> N334
    N138 --> N157
    N138 --> N155
    N139 --> N140
    N139 --> N9
    N139 --> N20
    N139 --> N216
    N139 --> N235
    N139 --> N250
    N139 --> N305
    N139 --> N334
    N142 --> N137
    N142 --> N139
    N143 --> N137
    N143 --> N151
    N143 --> N148
    N144 --> N9
    N144 --> N20
    N144 --> N216
    N144 --> N235
    N144 --> N250
    N144 --> N305
    N144 --> N334
    N145 --> N137
    N145 --> N142
    N145 --> N146
    N145 --> N143
    N145 --> N164
    N145 --> N160
    N145 --> N159
    N145 --> N161
    N145 --> N163
    N145 --> N165
    N145 --> N162
    N145 --> N147
    N146 --> N137
    N146 --> N148
    N147 --> N153
    N154 --> N9
    N154 --> N20
    N154 --> N216
    N154 --> N235
    N154 --> N250
    N154 --> N305
    N154 --> N334
    N155 --> N9
    N155 --> N20
    N155 --> N216
    N155 --> N235
    N155 --> N250
    N155 --> N305
    N155 --> N334
    N156 --> N9
    N156 --> N20
    N156 --> N216
    N156 --> N235
    N156 --> N250
    N156 --> N305
    N156 --> N334
    N156 --> N139
    N157 --> N9
    N157 --> N20
    N157 --> N216
    N157 --> N235
    N157 --> N250
    N157 --> N305
    N157 --> N334
    N158 --> N150
    N158 --> N9
    N158 --> N20
    N158 --> N216
    N158 --> N235
    N158 --> N250
    N158 --> N305
    N158 --> N334
    N159 --> N184
    N159 --> N211
    N159 --> N227
    N159 --> N266
    N159 --> N319
    N159 --> N137
    N159 --> N150
    N159 --> N9
    N159 --> N20
    N159 --> N216
    N159 --> N235
    N159 --> N250
    N159 --> N305
    N159 --> N334
    N160 --> N184
    N160 --> N211
    N160 --> N227
    N160 --> N266
    N160 --> N319
    N160 --> N150
    N160 --> N149
    N160 --> N9
    N160 --> N20
    N160 --> N216
    N160 --> N235
    N160 --> N250
    N160 --> N305
    N160 --> N334
    N161 --> N184
    N161 --> N211
    N161 --> N227
    N161 --> N266
    N161 --> N319
    N161 --> N151
    N161 --> N150
    N161 --> N149
    N161 --> N9
    N161 --> N20
    N161 --> N216
    N161 --> N235
    N161 --> N250
    N161 --> N305
    N161 --> N334
    N162 --> N9
    N162 --> N20
    N162 --> N216
    N162 --> N235
    N162 --> N250
    N162 --> N305
    N162 --> N334
    N162 --> N184
    N162 --> N211
    N162 --> N227
    N162 --> N266
    N162 --> N319
    N162 --> N137
    N162 --> N153
    N162 --> N151
    N162 --> N150
    N162 --> N149
    N163 --> N152
    N163 --> N150
    N163 --> N9
    N163 --> N20
    N163 --> N216
    N163 --> N235
    N163 --> N250
    N163 --> N305
    N163 --> N334
    N164 --> N184
    N164 --> N211
    N164 --> N227
    N164 --> N266
    N164 --> N319
    N164 --> N150
    N164 --> N149
    N164 --> N9
    N164 --> N20
    N164 --> N216
    N164 --> N235
    N164 --> N250
    N164 --> N305
    N164 --> N334
    N165 --> N9
    N165 --> N20
    N165 --> N216
    N165 --> N235
    N165 --> N250
    N165 --> N305
    N165 --> N334
    N166 --> N267
    N167 --> N267
    N169 --> N267
    N170 --> N267
    N171 --> N217
    N171 --> N251
    N171 --> N184
    N171 --> N211
    N171 --> N227
    N171 --> N266
    N171 --> N319
    N171 --> N267
    N172 --> N267
    N174 --> N336
    N175 --> N231
    N175 --> N217
    N175 --> N251
    N175 --> N267
    N176 --> N267
    N178 --> N267
    N179 --> N238
    N179 --> N259
    N179 --> N184
    N179 --> N211
    N179 --> N227
    N179 --> N266
    N179 --> N319
    N179 --> N217
    N179 --> N251
    N179 --> N267
    N180 --> N267
    N184 --> N211
    N184 --> N227
    N184 --> N266
    N184 --> N319
    N184 --> N267
    N185 --> N231
    N185 --> N267
    N189 --> N217
    N189 --> N251
    N189 --> N267
    N189 --> N347
    N190 --> N217
    N190 --> N251
    N190 --> N267
    N198 --> N238
    N198 --> N259
    N198 --> N267
    N199 --> N267
    N200 --> N203
    N200 --> N231
    N200 --> N267
    N201 --> N267
    N203 --> N267
    N204 --> N267
    N205 --> N267
    N206 --> N184
    N206 --> N211
    N206 --> N227
    N206 --> N266
    N206 --> N319
    N206 --> N267
    N206 --> N231
    N206 --> N217
    N206 --> N251
    N207 --> N231
    N207 --> N217
    N207 --> N251
    N207 --> N267
    N210 --> N184
    N210 --> N211
    N210 --> N227
    N210 --> N266
    N210 --> N319
    N211 --> N210
    N212 --> N217
    N212 --> N251
    N212 --> N267
    N214 --> N267
    N215 --> N267
    N216 --> N231
    N216 --> N267
    N217 --> N251
    N217 --> N184
    N217 --> N211
    N217 --> N227
    N217 --> N266
    N217 --> N319
    N217 --> N267
    N217 --> N231
    N218 --> N267
    N219 --> N217
    N219 --> N251
    N219 --> N267
    N219 --> N231
    N219 --> N247
    N220 --> N217
    N220 --> N251
    N220 --> N267
    N221 --> N217
    N221 --> N251
    N221 --> N231
    N221 --> N267
    N222 --> N217
    N222 --> N251
    N222 --> N231
    N222 --> N267
    N223 --> N184
    N223 --> N211
    N223 --> N227
    N223 --> N266
    N223 --> N319
    N223 --> N231
    N223 --> N267
    N223 --> N238
    N223 --> N259
    N224 --> N267
    N224 --> N261
    N224 --> N231
    N225 --> N217
    N225 --> N251
    N225 --> N267
    N226 --> N267
    N227 --> N217
    N227 --> N251
    N227 --> N184
    N227 --> N211
    N227 --> N266
    N227 --> N319
    N227 --> N267
    N227 --> N247
    N227 --> N238
    N227 --> N259
    N228 --> N184
    N228 --> N211
    N228 --> N227
    N228 --> N266
    N228 --> N319
    N228 --> N217
    N228 --> N251
    N228 --> N267
    N229 --> N184
    N229 --> N211
    N229 --> N227
    N229 --> N266
    N229 --> N319
    N229 --> N267
    N232 --> N267
    N232 --> N231
    N233 --> N267
    N233 --> N231
    N234 --> N184
    N234 --> N211
    N234 --> N227
    N234 --> N266
    N234 --> N319
    N234 --> N267
    N234 --> N231
    N235 --> N231
    N235 --> N267
    N236 --> N267
    N237 --> N231
    N237 --> N267
    N238 --> N231
    N238 --> N184
    N238 --> N211
    N238 --> N227
    N238 --> N266
    N238 --> N319
    N238 --> N267
    N238 --> N217
    N238 --> N251
    N239 --> N238
    N239 --> N259
    N239 --> N231
    N239 --> N267
    N240 --> N238
    N240 --> N259
    N240 --> N231
    N240 --> N267
    N241 --> N267
    N243 --> N217
    N243 --> N251
    N243 --> N267
    N243 --> N247
    N243 --> N184
    N243 --> N211
    N243 --> N227
    N243 --> N266
    N243 --> N319
    N244 --> N231
    N244 --> N267
    N245 --> N267
    N246 --> N267
    N247 --> N267
    N248 --> N231
    N248 --> N184
    N248 --> N211
    N248 --> N227
    N248 --> N266
    N248 --> N319
    N248 --> N267
    N249 --> N267
    N250 --> N238
    N250 --> N259
    N250 --> N267
    N251 --> N217
    N251 --> N267
    N252 --> N267
    N253 --> N267
    N254 --> N231
    N254 --> N267
    N255 --> N267
    N256 --> N238
    N256 --> N259
    N256 --> N267
    N257 --> N267
    N258 --> N184
    N258 --> N211
    N258 --> N227
    N258 --> N266
    N258 --> N319
    N258 --> N267
    N259 --> N184
    N259 --> N211
    N259 --> N227
    N259 --> N266
    N259 --> N319
    N259 --> N267
    N259 --> N217
    N259 --> N251
    N260 --> N231
    N260 --> N184
    N260 --> N211
    N260 --> N227
    N260 --> N266
    N260 --> N319
    N260 --> N267
    N261 --> N267
    N261 --> N224
    N261 --> N231
    N262 --> N267
    N263 --> N238
    N263 --> N259
    N263 --> N267
    N264 --> N231
    N264 --> N217
    N264 --> N251
    N264 --> N267
    N265 --> N238
    N265 --> N259
    N265 --> N267
    N266 --> N231
    N266 --> N184
    N266 --> N211
    N266 --> N227
    N266 --> N319
    N266 --> N267
    N267 --> N184
    N267 --> N211
    N267 --> N227
    N267 --> N266
    N267 --> N319
    N268 --> N231
    N268 --> N184
    N268 --> N211
    N268 --> N227
    N268 --> N266
    N268 --> N319
    N268 --> N267
    N269 --> N267
    N269 --> N231
    N271 --> N238
    N271 --> N259
    N271 --> N267
    N273 --> N231
    N273 --> N267
    N274 --> N267
    N274 --> N231
    N275 --> N267
    N276 --> N217
    N276 --> N251
    N276 --> N231
    N276 --> N267
    N277 --> N184
    N277 --> N211
    N277 --> N227
    N277 --> N266
    N277 --> N319
    N277 --> N217
    N277 --> N251
    N277 --> N267
    N278 --> N267
    N279 --> N267
    N280 --> N267
    N281 --> N217
    N281 --> N251
    N281 --> N231
    N281 --> N267
    N281 --> N247
    N282 --> N217
    N282 --> N251
    N282 --> N267
    N283 --> N217
    N283 --> N251
    N283 --> N267
    N283 --> N231
    N283 --> N184
    N283 --> N211
    N283 --> N227
    N283 --> N266
    N283 --> N319
    N284 --> N184
    N284 --> N211
    N284 --> N227
    N284 --> N266
    N284 --> N319
    N284 --> N267
    N286 --> N267
    N288 --> N267
    N288 --> N247
    N289 --> N267
    N290 --> N267
    N290 --> N231
    N290 --> N184
    N290 --> N211
    N290 --> N227
    N290 --> N266
    N290 --> N319
    N291 --> N267
    N292 --> N184
    N292 --> N211
    N292 --> N227
    N292 --> N266
    N292 --> N319
    N292 --> N267
    N293 --> N217
    N293 --> N251
    N293 --> N267
    N294 --> N267
    N295 --> N267
    N296 --> N217
    N296 --> N251
    N296 --> N267
    N297 --> N184
    N297 --> N211
    N297 --> N227
    N297 --> N266
    N297 --> N319
    N297 --> N267
    N298 --> N217
    N298 --> N251
    N298 --> N231
    N298 --> N184
    N298 --> N211
    N298 --> N227
    N298 --> N266
    N298 --> N319
    N298 --> N267
    N299 --> N267
    N300 --> N267
    N301 --> N267
    N302 --> N267
    N303 --> N267
    N304 --> N231
    N304 --> N267
    N305 --> N231
    N305 --> N267
    N306 --> N267
    N307 --> N267
    N308 --> N238
    N308 --> N259
    N308 --> N267
    N309 --> N203
    N310 --> N217
    N310 --> N251
    N310 --> N267
    N311 --> N238
    N311 --> N259
    N311 --> N203
    N311 --> N267
    N312 --> N203
    N312 --> N238
    N312 --> N259
    N312 --> N267
    N313 --> N184
    N313 --> N211
    N313 --> N227
    N313 --> N266
    N313 --> N319
    N313 --> N231
    N313 --> N267
    N314 --> N267
    N315 --> N267
    N316 --> N231
    N317 --> N267
    N318 --> N238
    N318 --> N259
    N318 --> N231
    N318 --> N184
    N318 --> N211
    N318 --> N227
    N318 --> N266
    N318 --> N319
    N318 --> N267
    N319 --> N267
    N320 --> N238
    N320 --> N259
    N320 --> N267
    N321 --> N267
    N322 --> N267
    N322 --> N347
    N324 --> N267
    N327 --> N267
    N328 --> N193
    N328 --> N267
    N330 --> N238
    N330 --> N259
    N330 --> N267
    N332 --> N231
    N332 --> N267
    N333 --> N267
    N334 --> N347
    N334 --> N238
    N334 --> N259
    N334 --> N336
    N334 --> N267
    N335 --> N267
    N336 --> N203
    N336 --> N267
    N337 --> N347
    N337 --> N336
    N337 --> N231
    N337 --> N267
    N338 --> N347
    N338 --> N336
    N338 --> N184
    N338 --> N211
    N338 --> N227
    N338 --> N266
    N338 --> N319
    N338 --> N267
    N339 --> N347
    N339 --> N336
    N339 --> N231
    N339 --> N267
    N340 --> N347
    N340 --> N267
    N342 --> N184
    N342 --> N211
    N342 --> N227
    N342 --> N266
    N342 --> N319
    N342 --> N267
    N345 --> N267
    N346 --> N347
    N346 --> N336
    N346 --> N267
    N348 --> N347
    N348 --> N349
    N349 --> N347
    N351 --> N336
    N351 --> N267
    N353 --> N347
    N353 --> N231
    N354 --> N347
    N355 --> N347
    N356 --> N347
    N357 --> N347
    N357 --> N203
    N357 --> N336
    N357 --> N267
    N358 --> N347
    N358 --> N203
    N358 --> N336
    N358 --> N267
    N359 --> N347
    N359 --> N186
    N359 --> N320
    N360 --> N347
    N360 --> N203
    N360 --> N336
    N360 --> N267
    N360 --> N186
    N360 --> N320
    N361 --> N347
    N361 --> N336
    N361 --> N203
    N361 --> N267
    N361 --> N186
    N361 --> N320
    N362 --> N347
    N362 --> N336
    N362 --> N267
    N363 --> N336
    N363 --> N184
    N363 --> N211
    N363 --> N227
    N363 --> N266
    N363 --> N319
    N364 --> N336
    N364 --> N267
    N365 --> N336
    N367 --> N267
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
  - Imports: `hashlib`
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
  - Imports: `database`
  - Imports: `hashlib`
  - Imports: `json`
  - Imports: `numpy`
  - Imports: `os`
  - Imports: `sqlite3`
  - Imports: `time`
  - Imports: `turbovec`
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