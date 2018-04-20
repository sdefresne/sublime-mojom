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

vpath
vpath %.yaml src

package   = Mojom.sublime-package

sources   = \
	src/Mojom.tmLanguage.yaml \
	src/Mojom.tmPreferences.yaml \
	src/package-metadata.json

builddir  = out

converter = tools/convert-yaml-to-plist.py
converted = $(patsubst src/%.yaml,$(builddir)/%,$(filter %.yaml,$(sources)))

all: $(package)

$(package): $(converted) $(filter-out %.yaml,$(sources))
	rm -f $@ && zip -jq $@ $+

$(builddir)/% : src/%.yaml $(converter) $(builddir)/.stamp
	python $(converter) $< $@

%/.stamp:
	mkdir -p $(dir $@) && touch $@

clean:
	rm -rf $(builddir)

realclean:
	rm -rf $(builddir) $(package)

.PRECIOUS: %/.stamp
.PHONY: clean realclean all

