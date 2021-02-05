date := $(shell date +'%s')
req_file_name = aml-requirements-$(date).txt

# Create datastores and register datasets
register-data:
	{% if cookiecutter.include_dataset_yaml in ['Tabular', 'Both'] -%}
	az ml dataset register -f aml/datasets/{{ cookiecutter.training_dataset }}_table.json --skip-validation
	{%- endif -%}
	{%- if cookiecutter.include_dataset_yaml in ['Files', 'Both'] -%}
	az ml dataset register -f aml/datasets/{{ cookiecutter.training_dataset }}_files.json --skip-validation
	{%- endif %}

create-compute:
	az ml computetarget create amlcompute --max-nodes 5 --idle-seconds-before-scaledown 600 -n cpu-cluster -s standard_ds15_v2

config: register-data create-compute

env: environment

# Build the AML environment
environment:
	az ml environment register -d aml/env
	python aml/utils/build_env.py --name {{ cookiecutter.environment_name }}

# Build or pull the AML environment locally
environment-local:
	az ml environment register -d aml/env
	python aml/utils/build_env.py --name {{ cookiecutter.environment_name }} --local

train:
	az ml run submit-script --path code/train -c cloud_run.yaml

# Update the AML SDK to the latest version
upgrade-aml-sdk:
	pip list -o | grep azureml | awk '{ print $$1"=="$$3}' > $(req_file_name)
	pip install -r $(req_file_name)
	rm $(req_file_name)

lint:
	flake8