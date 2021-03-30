# python-3.8.8:
#   pyenv.installed:
#     - default: True

python-pip:
  pkg.installed

virtualenvwrapper:
  pip.installed:
    - require:
      - pkg: python-pip

pipreqs:
  pip.installed:
    - requirements: /srv/data/requirements.txt
    - require:
      - pkg: python-pip
