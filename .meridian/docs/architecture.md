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
    N170["applications.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N171["background.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N172["cli.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N173["concurrency.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N174["datastructures.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N175["encoders.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N176["exceptions.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N177["exception_handlers.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N178["logger.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N179["params.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N180["param_functions.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N181["requests.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N182["responses.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N183["routing.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N184["sse.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N185["staticfiles.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N186["templating.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N187["testclient.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N188["types.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N189["utils.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N190["websockets.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N191["__init__.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N192["__main__.py [meridian_frontend/src-tauri/api/_internal/fastapi]"]
    N193["models.py [meridian_frontend/src-tauri/api/_internal/fastapi/dependencies]"]
    N194["utils.py [meridian_frontend/src-tauri/api/_internal/fastapi/dependencies]"]
    N195["asyncexitstack.py [meridian_frontend/src-tauri/api/_internal/fastapi/middleware]"]
    N196["cors.py [meridian_frontend/src-tauri/api/_internal/fastapi/middleware]"]
    N197["gzip.py [meridian_frontend/src-tauri/api/_internal/fastapi/middleware]"]
    N198["httpsredirect.py [meridian_frontend/src-tauri/api/_internal/fastapi/middleware]"]
    N199["trustedhost.py [meridian_frontend/src-tauri/api/_internal/fastapi/middleware]"]
    N200["wsgi.py [meridian_frontend/src-tauri/api/_internal/fastapi/middleware]"]
    N201["__init__.py [meridian_frontend/src-tauri/api/_internal/fastapi/middleware]"]
    N202["docs.py [meridian_frontend/src-tauri/api/_internal/fastapi/openapi]"]
    N203["models.py [meridian_frontend/src-tauri/api/_internal/fastapi/openapi]"]
    N204["utils.py [meridian_frontend/src-tauri/api/_internal/fastapi/openapi]"]
    N205["api_key.py [meridian_frontend/src-tauri/api/_internal/fastapi/security]"]
    N206["base.py [meridian_frontend/src-tauri/api/_internal/fastapi/security]"]
    N207["http.py [meridian_frontend/src-tauri/api/_internal/fastapi/security]"]
    N208["oauth2.py [meridian_frontend/src-tauri/api/_internal/fastapi/security]"]
    N209["open_id_connect_url.py [meridian_frontend/src-tauri/api/_internal/fastapi/security]"]
    N210["shared.py [meridian_frontend/src-tauri/api/_internal/fastapi/_compat]"]
    N211["v2.py [meridian_frontend/src-tauri/api/_internal/fastapi/_compat]"]
    N212["coreBundle.js [meridian_frontend/src-tauri/api/_internal/playwright/driver/package/lib]"]
    N213["utilsBundle.js [meridian_frontend/src-tauri/api/_internal/playwright/driver/package/lib]"]
    N214["structs.d.ts [meridian_frontend/src-tauri/api/_internal/playwright/driver/package/types]"]
    N215["types.d.ts [meridian_frontend/src-tauri/api/_internal/playwright/driver/package/types]"]
    N216["aliases.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N217["alias_generators.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N218["annotated_handlers.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N219["color.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N220["config.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N221["dataclasses.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N222["errors.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N223["fields.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N224["functional_serializers.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N225["functional_validators.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N226["json_schema.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N227["main.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N228["mypy.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N229["networks.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N230["root_model.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N231["types.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N232["type_adapter.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N233["validate_call_decorator.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N234["version.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N235["warnings.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N236["_migration.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N237["__init__.py [meridian_frontend/src-tauri/api/_internal/pydantic]"]
    N238["class_validators.py [meridian_frontend/src-tauri/api/_internal/pydantic/deprecated]"]
    N239["config.py [meridian_frontend/src-tauri/api/_internal/pydantic/deprecated]"]
    N240["copy_internals.py [meridian_frontend/src-tauri/api/_internal/pydantic/deprecated]"]
    N241["decorator.py [meridian_frontend/src-tauri/api/_internal/pydantic/deprecated]"]
    N242["json.py [meridian_frontend/src-tauri/api/_internal/pydantic/deprecated]"]
    N243["parse.py [meridian_frontend/src-tauri/api/_internal/pydantic/deprecated]"]
    N244["tools.py [meridian_frontend/src-tauri/api/_internal/pydantic/deprecated]"]
    N245["arguments_schema.py [meridian_frontend/src-tauri/api/_internal/pydantic/experimental]"]
    N246["missing_sentinel.py [meridian_frontend/src-tauri/api/_internal/pydantic/experimental]"]
    N247["pipeline.py [meridian_frontend/src-tauri/api/_internal/pydantic/experimental]"]
    N248["_loader.py [meridian_frontend/src-tauri/api/_internal/pydantic/plugin]"]
    N249["_schema_validator.py [meridian_frontend/src-tauri/api/_internal/pydantic/plugin]"]
    N250["__init__.py [meridian_frontend/src-tauri/api/_internal/pydantic/plugin]"]
    N251["annotated_types.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N252["class_validators.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N253["color.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N254["config.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N255["dataclasses.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N256["datetime_parse.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N257["decorator.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N258["env_settings.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N259["errors.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N260["error_wrappers.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N261["fields.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N262["generics.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N263["json.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N264["main.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N265["mypy.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N266["networks.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N267["parse.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N268["schema.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N269["tools.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N270["types.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N271["typing.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N272["utils.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N273["validators.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N274["version.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N275["_hypothesis_plugin.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N276["__init__.py [meridian_frontend/src-tauri/api/_internal/pydantic/v1]"]
    N277["_config.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N278["_core_metadata.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N279["_core_utils.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N280["_dataclasses.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N281["_decorators.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N282["_decorators_v1.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N283["_discriminated_union.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N284["_docs_extraction.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N285["_fields.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N286["_forward_ref.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N287["_generate_schema.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N288["_generics.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N289["_git.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N290["_import_utils.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N291["_internal_dataclass.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N292["_known_annotated_metadata.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N293["_mock_val_ser.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N294["_model_construction.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N295["_namespace_utils.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N296["_repr.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N297["_schema_gather.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N298["_schema_generation_shared.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N299["_serializers.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N300["_signature.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N301["_typing_extra.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N302["_utils.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N303["_validate_call.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N304["_validators.py [meridian_frontend/src-tauri/api/_internal/pydantic/_internal]"]
    N305["applications.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N306["authentication.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N307["background.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N308["concurrency.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N309["config.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N310["convertors.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N311["datastructures.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N312["endpoints.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N313["exceptions.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N314["formparsers.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N315["requests.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N316["responses.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N317["routing.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N318["schemas.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N319["staticfiles.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N320["status.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N321["templating.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N322["testclient.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N323["types.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N324["websockets.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N325["_exception_handler.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N326["_utils.py [meridian_frontend/src-tauri/api/_internal/starlette]"]
    N327["authentication.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N328["base.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N329["cors.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N330["errors.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N331["exceptions.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N332["gzip.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N333["httpsredirect.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N334["sessions.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N335["trustedhost.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N336["wsgi.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N337["__init__.py [meridian_frontend/src-tauri/api/_internal/starlette/middleware]"]
    N338["config.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N339["importer.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N340["logging.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N341["main.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N342["server.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N343["workers.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N344["_compat.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N345["_subprocess.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N346["_types.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N347["__init__.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N348["__main__.py [meridian_frontend/src-tauri/api/_internal/uvicorn]"]
    N349["off.py [meridian_frontend/src-tauri/api/_internal/uvicorn/lifespan]"]
    N350["on.py [meridian_frontend/src-tauri/api/_internal/uvicorn/lifespan]"]
    N351["asyncio.py [meridian_frontend/src-tauri/api/_internal/uvicorn/loops]"]
    N352["auto.py [meridian_frontend/src-tauri/api/_internal/uvicorn/loops]"]
    N353["uvloop.py [meridian_frontend/src-tauri/api/_internal/uvicorn/loops]"]
    N354["asgi2.py [meridian_frontend/src-tauri/api/_internal/uvicorn/middleware]"]
    N355["message_logger.py [meridian_frontend/src-tauri/api/_internal/uvicorn/middleware]"]
    N356["proxy_headers.py [meridian_frontend/src-tauri/api/_internal/uvicorn/middleware]"]
    N357["wsgi.py [meridian_frontend/src-tauri/api/_internal/uvicorn/middleware]"]
    N358["utils.py [meridian_frontend/src-tauri/api/_internal/uvicorn/protocols]"]
    N359["auto.py [meridian_frontend/src-tauri/api/_internal/uvicorn/protocols/http]"]
    N360["flow_control.py [meridian_frontend/src-tauri/api/_internal/uvicorn/protocols/http]"]
    N361["h11_impl.py [meridian_frontend/src-tauri/api/_internal/uvicorn/protocols/http]"]
    N362["httptools_impl.py [meridian_frontend/src-tauri/api/_internal/uvicorn/protocols/http]"]
    N363["auto.py [meridian_frontend/src-tauri/api/_internal/uvicorn/protocols/websockets]"]
    N364["websockets_impl.py [meridian_frontend/src-tauri/api/_internal/uvicorn/protocols/websockets]"]
    N365["websockets_sansio_impl.py [meridian_frontend/src-tauri/api/_internal/uvicorn/protocols/websockets]"]
    N366["wsproto_impl.py [meridian_frontend/src-tauri/api/_internal/uvicorn/protocols/websockets]"]
    N367["basereload.py [meridian_frontend/src-tauri/api/_internal/uvicorn/supervisors]"]
    N368["multiprocess.py [meridian_frontend/src-tauri/api/_internal/uvicorn/supervisors]"]
    N369["statreload.py [meridian_frontend/src-tauri/api/_internal/uvicorn/supervisors]"]
    N370["watchfilesreload.py [meridian_frontend/src-tauri/api/_internal/uvicorn/supervisors]"]
    N371["__init__.py [meridian_frontend/src-tauri/api/_internal/uvicorn/supervisors]"]
    N372["get_system_platform_info.py [plugins]"]

    N2 --> N242
    N2 --> N263
    N5 --> N351
    N5 --> N242
    N5 --> N263
    N5 --> N13
    N9 --> N221
    N9 --> N255
    N12 --> N9
    N12 --> N20
    N12 --> N220
    N12 --> N239
    N12 --> N254
    N12 --> N309
    N12 --> N338
    N12 --> N11
    N12 --> N10
    N13 --> N351
    N13 --> N340
    N13 --> N242
    N13 --> N263
    N13 --> N271
    N13 --> N14
    N14 --> N242
    N14 --> N263
    N14 --> N271
    N15 --> N242
    N15 --> N263
    N15 --> N340
    N16 --> N271
    N17 --> N351
    N17 --> N271
    N18 --> N271
    N18 --> N14
    N19 --> N271
    N21 --> N351
    N21 --> N14
    N23 --> N242
    N23 --> N263
    N23 --> N271
    N23 --> N14
    N24 --> N271
    N24 --> N14
    N25 --> N271
    N26 --> N242
    N26 --> N263
    N26 --> N271
    N27 --> N242
    N27 --> N263
    N27 --> N271
    N28 --> N340
    N28 --> N271
    N30 --> N242
    N30 --> N263
    N30 --> N340
    N30 --> N351
    N30 --> N271
    N30 --> N14
    N31 --> N340
    N31 --> N242
    N31 --> N263
    N32 --> N242
    N32 --> N263
    N32 --> N351
    N32 --> N271
    N32 --> N14
    N33 --> N351
    N33 --> N271
    N34 --> N242
    N34 --> N263
    N34 --> N351
    N34 --> N271
    N34 --> N14
    N35 --> N242
    N35 --> N263
    N35 --> N351
    N35 --> N271
    N35 --> N14
    N36 --> N242
    N36 --> N263
    N36 --> N351
    N36 --> N271
    N37 --> N242
    N37 --> N263
    N37 --> N351
    N37 --> N340
    N37 --> N271
    N38 --> N351
    N38 --> N242
    N38 --> N263
    N38 --> N340
    N38 --> N271
    N39 --> N271
    N39 --> N242
    N39 --> N263
    N39 --> N14
    N40 --> N271
    N41 --> N242
    N41 --> N263
    N41 --> N271
    N42 --> N340
    N42 --> N351
    N42 --> N271
    N42 --> N242
    N42 --> N263
    N43 --> N242
    N43 --> N263
    N43 --> N271
    N43 --> N14
    N44 --> N340
    N44 --> N271
    N45 --> N271
    N46 --> N351
    N46 --> N271
    N46 --> N14
    N46 --> N13
    N47 --> N340
    N47 --> N271
    N48 --> N242
    N48 --> N263
    N48 --> N271
    N49 --> N271
    N50 --> N340
    N50 --> N271
    N51 --> N351
    N51 --> N14
    N51 --> N242
    N51 --> N263
    N52 --> N340
    N52 --> N271
    N53 --> N242
    N53 --> N263
    N53 --> N351
    N53 --> N271
    N53 --> N14
    N54 --> N351
    N54 --> N242
    N54 --> N263
    N54 --> N271
    N54 --> N14
    N55 --> N340
    N55 --> N271
    N56 --> N271
    N56 --> N351
    N56 --> N14
    N57 --> N271
    N58 --> N271
    N59 --> N242
    N59 --> N263
    N59 --> N271
    N60 --> N340
    N60 --> N14
    N61 --> N340
    N61 --> N271
    N62 --> N242
    N62 --> N263
    N62 --> N271
    N63 --> N271
    N64 --> N242
    N64 --> N263
    N64 --> N271
    N65 --> N271
    N65 --> N14
    N66 --> N271
    N66 --> N14
    N67 --> N340
    N67 --> N271
    N67 --> N14
    N68 --> N271
    N68 --> N14
    N69 --> N271
    N69 --> N14
    N70 --> N351
    N70 --> N271
    N71 --> N271
    N72 --> N340
    N72 --> N271
    N73 --> N242
    N73 --> N263
    N73 --> N271
    N73 --> N14
    N74 --> N242
    N74 --> N263
    N74 --> N181
    N74 --> N315
    N74 --> N271
    N75 --> N271
    N76 --> N271
    N77 --> N271
    N77 --> N14
    N78 --> N242
    N78 --> N263
    N78 --> N271
    N79 --> N271
    N79 --> N14
    N80 --> N14
    N81 --> N242
    N81 --> N263
    N81 --> N271
    N81 --> N221
    N81 --> N255
    N81 --> N9
    N81 --> N20
    N81 --> N220
    N81 --> N239
    N81 --> N254
    N81 --> N309
    N81 --> N338
    N81 --> N11
    N81 --> N10
    N82 --> N242
    N82 --> N263
    N82 --> N271
    N82 --> N14
    N83 --> N351
    N83 --> N271
    N83 --> N14
    N83 --> N242
    N83 --> N263
    N84 --> N271
    N84 --> N14
    N86 --> N271
    N87 --> N271
    N87 --> N14
    N90 --> N271
    N90 --> N242
    N90 --> N263
    N92 --> N271
    N93 --> N271
    N93 --> N14
    N94 --> N242
    N94 --> N263
    N94 --> N271
    N94 --> N14
    N95 --> N242
    N95 --> N263
    N95 --> N340
    N95 --> N271
    N95 --> N14
    N96 --> N351
    N96 --> N271
    N97 --> N340
    N97 --> N271
    N98 --> N271
    N98 --> N14
    N99 --> N340
    N99 --> N271
    N99 --> N14
    N100 --> N271
    N101 --> N14
    N104 --> N351
    N104 --> N13
    N105 --> N14
    N106 --> N13
    N108 --> N14
    N110 --> N14
    N111 --> N14
    N112 --> N14
    N113 --> N14
    N114 --> N13
    N116 --> N242
    N116 --> N263
    N116 --> N14
    N120 --> N351
    N121 --> N340
    N121 --> N242
    N121 --> N263
    N122 --> N242
    N122 --> N263
    N123 --> N351
    N124 --> N14
    N127 --> N14
    N128 --> N351
    N129 --> N351
    N129 --> N13
    N130 --> N13
    N130 --> N351
    N131 --> N13
    N132 --> N351
    N133 --> N351
    N134 --> N242
    N134 --> N263
    N136 --> N91
    N137 --> N13
    N138 --> N13
    N141 --> N188
    N141 --> N215
    N141 --> N231
    N141 --> N270
    N141 --> N323
    N141 --> N9
    N141 --> N20
    N141 --> N220
    N141 --> N239
    N141 --> N254
    N141 --> N309
    N141 --> N338
    N142 --> N143
    N142 --> N160
    N142 --> N162
    N142 --> N149
    N142 --> N141
    N142 --> N9
    N142 --> N20
    N142 --> N220
    N142 --> N239
    N142 --> N254
    N142 --> N309
    N142 --> N338
    N142 --> N161
    N142 --> N159
    N143 --> N144
    N143 --> N9
    N143 --> N20
    N143 --> N220
    N143 --> N239
    N143 --> N254
    N143 --> N309
    N143 --> N338
    N146 --> N141
    N146 --> N143
    N147 --> N141
    N147 --> N155
    N147 --> N152
    N148 --> N9
    N148 --> N20
    N148 --> N220
    N148 --> N239
    N148 --> N254
    N148 --> N309
    N148 --> N338
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
    N158 --> N220
    N158 --> N239
    N158 --> N254
    N158 --> N309
    N158 --> N338
    N159 --> N9
    N159 --> N20
    N159 --> N220
    N159 --> N239
    N159 --> N254
    N159 --> N309
    N159 --> N338
    N160 --> N9
    N160 --> N20
    N160 --> N220
    N160 --> N239
    N160 --> N254
    N160 --> N309
    N160 --> N338
    N160 --> N143
    N161 --> N9
    N161 --> N20
    N161 --> N220
    N161 --> N239
    N161 --> N254
    N161 --> N309
    N161 --> N338
    N162 --> N154
    N162 --> N9
    N162 --> N20
    N162 --> N220
    N162 --> N239
    N162 --> N254
    N162 --> N309
    N162 --> N338
    N163 --> N188
    N163 --> N215
    N163 --> N231
    N163 --> N270
    N163 --> N323
    N163 --> N141
    N163 --> N154
    N163 --> N9
    N163 --> N20
    N163 --> N220
    N163 --> N239
    N163 --> N254
    N163 --> N309
    N163 --> N338
    N164 --> N188
    N164 --> N215
    N164 --> N231
    N164 --> N270
    N164 --> N323
    N164 --> N154
    N164 --> N153
    N164 --> N9
    N164 --> N20
    N164 --> N220
    N164 --> N239
    N164 --> N254
    N164 --> N309
    N164 --> N338
    N165 --> N188
    N165 --> N215
    N165 --> N231
    N165 --> N270
    N165 --> N323
    N165 --> N155
    N165 --> N154
    N165 --> N153
    N165 --> N9
    N165 --> N20
    N165 --> N220
    N165 --> N239
    N165 --> N254
    N165 --> N309
    N165 --> N338
    N166 --> N9
    N166 --> N20
    N166 --> N220
    N166 --> N239
    N166 --> N254
    N166 --> N309
    N166 --> N338
    N166 --> N188
    N166 --> N215
    N166 --> N231
    N166 --> N270
    N166 --> N323
    N166 --> N141
    N166 --> N157
    N166 --> N155
    N166 --> N154
    N166 --> N153
    N167 --> N156
    N167 --> N154
    N167 --> N9
    N167 --> N20
    N167 --> N220
    N167 --> N239
    N167 --> N254
    N167 --> N309
    N167 --> N338
    N168 --> N188
    N168 --> N215
    N168 --> N231
    N168 --> N270
    N168 --> N323
    N168 --> N154
    N168 --> N153
    N168 --> N9
    N168 --> N20
    N168 --> N220
    N168 --> N239
    N168 --> N254
    N168 --> N309
    N168 --> N338
    N169 --> N9
    N169 --> N20
    N169 --> N220
    N169 --> N239
    N169 --> N254
    N169 --> N309
    N169 --> N338
    N170 --> N271
    N171 --> N271
    N173 --> N271
    N174 --> N271
    N175 --> N221
    N175 --> N255
    N175 --> N188
    N175 --> N215
    N175 --> N231
    N175 --> N270
    N175 --> N323
    N175 --> N271
    N176 --> N271
    N178 --> N340
    N179 --> N235
    N179 --> N221
    N179 --> N255
    N179 --> N271
    N180 --> N271
    N182 --> N271
    N183 --> N242
    N183 --> N263
    N183 --> N188
    N183 --> N215
    N183 --> N231
    N183 --> N270
    N183 --> N323
    N183 --> N221
    N183 --> N255
    N183 --> N271
    N184 --> N271
    N188 --> N215
    N188 --> N231
    N188 --> N270
    N188 --> N323
    N188 --> N271
    N189 --> N235
    N189 --> N271
    N193 --> N221
    N193 --> N255
    N193 --> N271
    N193 --> N351
    N194 --> N221
    N194 --> N255
    N194 --> N271
    N202 --> N242
    N202 --> N263
    N202 --> N271
    N203 --> N271
    N204 --> N207
    N204 --> N235
    N204 --> N271
    N205 --> N271
    N207 --> N271
    N208 --> N271
    N209 --> N271
    N210 --> N188
    N210 --> N215
    N210 --> N231
    N210 --> N270
    N210 --> N323
    N210 --> N271
    N210 --> N235
    N210 --> N221
    N210 --> N255
    N211 --> N235
    N211 --> N221
    N211 --> N255
    N211 --> N271
    N214 --> N188
    N214 --> N215
    N214 --> N231
    N214 --> N270
    N214 --> N323
    N215 --> N214
    N216 --> N221
    N216 --> N255
    N216 --> N271
    N218 --> N271
    N219 --> N271
    N220 --> N235
    N220 --> N271
    N221 --> N255
    N221 --> N188
    N221 --> N215
    N221 --> N231
    N221 --> N270
    N221 --> N323
    N221 --> N271
    N221 --> N235
    N222 --> N271
    N223 --> N221
    N223 --> N255
    N223 --> N271
    N223 --> N235
    N223 --> N251
    N224 --> N221
    N224 --> N255
    N224 --> N271
    N225 --> N221
    N225 --> N255
    N225 --> N235
    N225 --> N271
    N226 --> N221
    N226 --> N255
    N226 --> N235
    N226 --> N271
    N227 --> N188
    N227 --> N215
    N227 --> N231
    N227 --> N270
    N227 --> N323
    N227 --> N235
    N227 --> N271
    N227 --> N242
    N227 --> N263
    N228 --> N271
    N228 --> N265
    N228 --> N235
    N229 --> N221
    N229 --> N255
    N229 --> N271
    N230 --> N271
    N231 --> N221
    N231 --> N255
    N231 --> N188
    N231 --> N215
    N231 --> N270
    N231 --> N323
    N231 --> N271
    N231 --> N251
    N231 --> N242
    N231 --> N263
    N232 --> N188
    N232 --> N215
    N232 --> N231
    N232 --> N270
    N232 --> N323
    N232 --> N221
    N232 --> N255
    N232 --> N271
    N233 --> N188
    N233 --> N215
    N233 --> N231
    N233 --> N270
    N233 --> N323
    N233 --> N271
    N236 --> N271
    N236 --> N235
    N237 --> N271
    N237 --> N235
    N238 --> N188
    N238 --> N215
    N238 --> N231
    N238 --> N270
    N238 --> N323
    N238 --> N271
    N238 --> N235
    N239 --> N235
    N239 --> N271
    N240 --> N271
    N241 --> N235
    N241 --> N271
    N242 --> N235
    N242 --> N188
    N242 --> N215
    N242 --> N231
    N242 --> N270
    N242 --> N323
    N242 --> N271
    N242 --> N221
    N242 --> N255
    N243 --> N242
    N243 --> N263
    N243 --> N235
    N243 --> N271
    N244 --> N242
    N244 --> N263
    N244 --> N235
    N244 --> N271
    N245 --> N271
    N247 --> N221
    N247 --> N255
    N247 --> N271
    N247 --> N251
    N247 --> N188
    N247 --> N215
    N247 --> N231
    N247 --> N270
    N247 --> N323
    N248 --> N235
    N248 --> N271
    N249 --> N271
    N250 --> N271
    N251 --> N271
    N252 --> N235
    N252 --> N188
    N252 --> N215
    N252 --> N231
    N252 --> N270
    N252 --> N323
    N252 --> N271
    N253 --> N271
    N254 --> N242
    N254 --> N263
    N254 --> N271
    N255 --> N221
    N255 --> N271
    N256 --> N271
    N257 --> N271
    N258 --> N235
    N258 --> N271
    N259 --> N271
    N260 --> N242
    N260 --> N263
    N260 --> N271
    N261 --> N271
    N262 --> N188
    N262 --> N215
    N262 --> N231
    N262 --> N270
    N262 --> N323
    N262 --> N271
    N263 --> N188
    N263 --> N215
    N263 --> N231
    N263 --> N270
    N263 --> N323
    N263 --> N271
    N263 --> N221
    N263 --> N255
    N264 --> N235
    N264 --> N188
    N264 --> N215
    N264 --> N231
    N264 --> N270
    N264 --> N323
    N264 --> N271
    N265 --> N271
    N265 --> N228
    N265 --> N235
    N266 --> N271
    N267 --> N242
    N267 --> N263
    N267 --> N271
    N268 --> N235
    N268 --> N221
    N268 --> N255
    N268 --> N271
    N269 --> N242
    N269 --> N263
    N269 --> N271
    N270 --> N235
    N270 --> N188
    N270 --> N215
    N270 --> N231
    N270 --> N323
    N270 --> N271
    N271 --> N188
    N271 --> N215
    N271 --> N231
    N271 --> N270
    N271 --> N323
    N272 --> N235
    N272 --> N188
    N272 --> N215
    N272 --> N231
    N272 --> N270
    N272 --> N323
    N272 --> N271
    N273 --> N271
    N273 --> N235
    N275 --> N242
    N275 --> N263
    N275 --> N271
    N277 --> N235
    N277 --> N271
    N278 --> N271
    N278 --> N235
    N279 --> N271
    N280 --> N221
    N280 --> N255
    N280 --> N235
    N280 --> N271
    N281 --> N188
    N281 --> N215
    N281 --> N231
    N281 --> N270
    N281 --> N323
    N281 --> N221
    N281 --> N255
    N281 --> N271
    N282 --> N271
    N283 --> N271
    N284 --> N271
    N285 --> N221
    N285 --> N255
    N285 --> N235
    N285 --> N271
    N285 --> N251
    N286 --> N221
    N286 --> N255
    N286 --> N271
    N287 --> N221
    N287 --> N255
    N287 --> N271
    N287 --> N235
    N287 --> N188
    N287 --> N215
    N287 --> N231
    N287 --> N270
    N287 --> N323
    N288 --> N188
    N288 --> N215
    N288 --> N231
    N288 --> N270
    N288 --> N323
    N288 --> N271
    N290 --> N271
    N292 --> N271
    N292 --> N251
    N293 --> N271
    N294 --> N271
    N294 --> N235
    N294 --> N188
    N294 --> N215
    N294 --> N231
    N294 --> N270
    N294 --> N323
    N295 --> N271
    N296 --> N188
    N296 --> N215
    N296 --> N231
    N296 --> N270
    N296 --> N323
    N296 --> N271
    N297 --> N221
    N297 --> N255
    N297 --> N271
    N298 --> N271
    N299 --> N271
    N300 --> N221
    N300 --> N255
    N300 --> N271
    N301 --> N188
    N301 --> N215
    N301 --> N231
    N301 --> N270
    N301 --> N323
    N301 --> N271
    N302 --> N221
    N302 --> N255
    N302 --> N235
    N302 --> N188
    N302 --> N215
    N302 --> N231
    N302 --> N270
    N302 --> N323
    N302 --> N271
    N303 --> N271
    N304 --> N271
    N305 --> N271
    N306 --> N271
    N307 --> N271
    N308 --> N235
    N308 --> N271
    N309 --> N235
    N309 --> N271
    N310 --> N271
    N311 --> N271
    N312 --> N242
    N312 --> N263
    N312 --> N271
    N313 --> N207
    N314 --> N221
    N314 --> N255
    N314 --> N271
    N315 --> N242
    N315 --> N263
    N315 --> N207
    N315 --> N271
    N316 --> N207
    N316 --> N242
    N316 --> N263
    N316 --> N271
    N317 --> N188
    N317 --> N215
    N317 --> N231
    N317 --> N270
    N317 --> N323
    N317 --> N235
    N317 --> N271
    N318 --> N271
    N319 --> N271
    N320 --> N235
    N321 --> N271
    N322 --> N242
    N322 --> N263
    N322 --> N235
    N322 --> N188
    N322 --> N215
    N322 --> N231
    N322 --> N270
    N322 --> N323
    N322 --> N271
    N323 --> N271
    N324 --> N242
    N324 --> N263
    N324 --> N271
    N325 --> N271
    N326 --> N271
    N326 --> N351
    N328 --> N271
    N331 --> N271
    N332 --> N197
    N332 --> N271
    N334 --> N242
    N334 --> N263
    N334 --> N271
    N336 --> N235
    N336 --> N271
    N337 --> N271
    N338 --> N351
    N338 --> N242
    N338 --> N263
    N338 --> N340
    N338 --> N271
    N339 --> N271
    N340 --> N207
    N340 --> N271
    N341 --> N351
    N341 --> N340
    N341 --> N235
    N341 --> N271
    N342 --> N351
    N342 --> N340
    N342 --> N188
    N342 --> N215
    N342 --> N231
    N342 --> N270
    N342 --> N323
    N342 --> N271
    N343 --> N351
    N343 --> N340
    N343 --> N235
    N343 --> N271
    N344 --> N351
    N344 --> N271
    N346 --> N188
    N346 --> N215
    N346 --> N231
    N346 --> N270
    N346 --> N323
    N346 --> N271
    N349 --> N271
    N350 --> N351
    N350 --> N340
    N350 --> N271
    N352 --> N351
    N352 --> N353
    N353 --> N351
    N355 --> N340
    N355 --> N271
    N357 --> N351
    N357 --> N235
    N358 --> N351
    N359 --> N351
    N360 --> N351
    N361 --> N351
    N361 --> N207
    N361 --> N340
    N361 --> N271
    N362 --> N351
    N362 --> N207
    N362 --> N340
    N362 --> N271
    N363 --> N351
    N363 --> N190
    N363 --> N324
    N364 --> N351
    N364 --> N207
    N364 --> N340
    N364 --> N271
    N364 --> N190
    N364 --> N324
    N365 --> N351
    N365 --> N340
    N365 --> N207
    N365 --> N271
    N365 --> N190
    N365 --> N324
    N366 --> N351
    N366 --> N340
    N366 --> N271
    N367 --> N340
    N367 --> N188
    N367 --> N215
    N367 --> N231
    N367 --> N270
    N367 --> N323
    N368 --> N340
    N368 --> N271
    N369 --> N340
    N371 --> N271
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