#!/usr/bin/env python
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Converts file from YAML to Plist format."""

import argparse
import ruamel.yaml
import plistlib


def load_yaml(input_path):
  """Loads YAML file at input_path."""
  yaml = ruamel.yaml.YAML()
  with open(input_path, 'rb') as input_file:
    return yaml.load(input_file)


def fix_data(yaml_data):
  """Fixes data so that it can be exported as Plist.

  Converts dictionary keys to strings as this is required by Plist.
  """
  if isinstance(yaml_data, list):
    return [ fix_data(item) for item in yaml_data ]
  if isinstance(yaml_data, dict):
    return { str(key): fix_data(yaml_data[key]) for key in yaml_data }
  return yaml_data


def save_plist(data, output_path):
  """Save data as Plist to output_path."""
  with open(output_path, 'wb') as output_file:
    plistlib.writePlist(data, output_file)


def process(input_path, output_path):
  """Converts YAML data from input_path and save it to output_path."""
  save_plist(fix_data(load_yaml(input_path)), output_path)


def main():
  parser = argparse.ArgumentParser(description=__doc__)
  parser.add_argument('input', help='path to YAML file to convert')
  parser.add_argument('output', help='path to Plist file to write')
  args = parser.parse_args()
  return process(args.input, args.output)


if __name__ == '__main__':
  main()
