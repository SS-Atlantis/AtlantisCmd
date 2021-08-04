# Atlantis Temporary Run Directory Template

This directory is a [cookiecutter](https://cookiecutter.readthedocs.io/en/latest/)
template for the temporary run directory for a run of the CSIRO Atlantis ecosystem model.
It is used by the
[`atlantis run` sub-command](https://atlantiscmd.readthedocs.io/en/latest/subcommands.html#run-sub-command).

The `cookiecutter.json` file contains the template variables, and their default values.
The defaults are (mostly) overridden by values calculated by the `atlantis run` sub-command.
Sadly,
comments are not allowed in JSON files.
So,
you will have to guess the meaning of the template variables from their names and values,
or read the code in the `atlantis_cmd/run.py` module to learn more about them.

The `{{cookiecutter.tmp_run_dir}}/` directory is the template for the temporary run directory.
The rendered temporary run directory will have the name given by the `tmp_run_dir` template variable.

Please see the [cookiecutter docs](https://cookiecutter.readthedocs.io/en/latest/)
for more details of the template structure,
template variables,
and how the template rendering process works.
