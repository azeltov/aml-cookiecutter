import os
import shutil


def remove(filepath):
    if os.path.isfile(filepath):
        os.remove(filepath)
    elif os.path.isdir(filepath):
        shutil.rmtree(filepath)


remove_dataset = "{{ cookiecutter.include_dataset_yaml }}" == "None"
dataset_yaml = "{{ cookiecutter.include_dataset_yaml }}"

if remove_dataset:
    remove(os.path.join(os.getcwd(), 'aml/datasets'))
elif dataset_yaml == "Files":
    pth = os.path.join(os.getcwd(), 'aml/datasets/{{ cookiecutter.training_dataset }}_table.json')
    remove(pth)
elif dataset_yaml == "Tabular":
    pth = os.path.join(os.getcwd(), 'aml/datasets/{{ cookiecutter.training_dataset }}_files.json')
    remove(pth)
