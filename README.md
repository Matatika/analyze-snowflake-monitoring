# analyze-snowflake-monitoring

Meltano project [file bundle](https://meltano.com/docs/command-line-interface.html#file-bundle) of datasets for monitoring snowflake.

Files:
- [`analyze/datasets`](./bundle/analyze/datasets) (directory)

### Adding this file bundle to your own Meltano project

Add plugin to `discovery.yml`:
```yaml
files:
- name: analyze-snowflake-monitoring
  namespace: snowflake_monitoring
  repo: https://github.com/Matatika/analyze-example.git
  pip_url: git+https://github.com/Matatika/analyze-example.git
```

Add plugin to your Meltano project:
```bash
# Add only the file bundle
meltano add files analyze-snowflake-monitoring
```

### Adding this file bundle to your Matatika workspace

Go to the `Lab` then `Plugins` page, click on the `CUSTOM` tab, click `add` and then copy and paste in:

```yaml
files:
  - name: analyze-snowflake-monitoring
    namespace: snowflake_monitoring
    update:
      '*.yml': true
    pip_url: git+https://github.com/Matatika/analyze-example.git
```