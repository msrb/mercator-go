# -*- coding: utf-8 -*-
# vim: set fileencoding=utf-8


java_result = {'digests': {'manifest': '5d6f9b6a9ddca2a28c0216cc44efb2e20d9c23b5'}, 'ecosystem': 'Java-JAR', 'result': {
    'kind': 'JAR',
    'maven_id': {'artifactId': 'json-simple', 'groupId': 'com.googlecode.json-simple', 'version': '1.1.1'},
    'manifest': {'Tool': 'Bnd-1.50.0', 'Built-By': 'fangyidong', 'Build-Jdk': '1.6.0_26',
                 'Export-Package': 'org.json.simple;uses:="org.json.simple.parser";version="1.1.1",org.json.simple.parser;uses:="org.json.simple";version="1.1.1"',
                 'Bundle-Description': 'A simple Java toolkit for JSON',
                 'Bundle-SymbolicName': 'com.googlecode.json-simple', 'Bundle-ManifestVersion': '2',
                 'Bundle-License': 'http://www.apache.org/licenses/LICENSE-2.0.txt', 'Bundle-Name': 'JSON.simple',
                 'Manifest-Version': '1.0', 'Bundle-Version': '1.1.1', 'Bnd-LastModified': '1329633057225',
                 'Created-By': 'Apache Maven Bundle Plugin'},
    'pom.xml': {'artifactId': 'json-simple',
                'dependencies': {'compile': {'junit:junit::': '4.10'}},
                'description': 'A simple Java toolkit for JSON',
                'groupId': 'com.googlecode.json-simple',
                'name': 'JSON.simple',
                'url': 'http://code.google.com/p/json-simple/',
                'version': '1.1.1',
                'licenses': ['The Apache Software License, Version 2.0'],
                'scm_url': 'http://json-simple.googlecode.com/svn/trunk/'}}}
javascript_result = {'digests': {'manifest': '214c91cc37bd9f56c1f79970fe0b34e2af9dac41'}, 'ecosystem': 'NPM',
                     'result': {'files': ['LICENSE', 'HISTORY.md', 'index.js'], 'scripts': {'lint': 'eslint **/*.js',
                                                                                            'test': 'mocha --reporter spec --bail --check-leaks test/',
                                                                                            'test-cov': 'istanbul cover node_modules/mocha/bin/_mocha -- --reporter dot --check-leaks test/',
                                                                                            'test-ci': 'istanbul cover node_modules/mocha/bin/_mocha --report lcovonly -- --reporter spec --check-leaks test/'},
                                'dependencies': {'parseurl': '~1.3.1', 'send': '0.14.1', 'escape-html': '~1.0.3',
                                                 'encodeurl': '~1.0.1'},
                                'devDependencies': {'supertest': '1.1.0', 'eslint-plugin-standard': '1.3.2',
                                                    'istanbul': '0.4.3', 'eslint': '2.11.1',
                                                    'eslint-plugin-promise': '1.3.2', 'eslint-config-standard': '5.3.1',
                                                    'mocha': '2.5.3'}, 'license': 'MIT',
                                'author': 'Douglas Christopher Wilson <doug@somethingdoug.com>',
                                'engines': {'node': '>= 0.8.0'}, 'description': 'Serve static files',
                                'repository': 'expressjs/serve-static', 'version': '1.11.1', 'name': 'serve-static'}}
ruby_result = {'digests': {'manifest': '8df39c2ba4e5da2e8cdc1ca6fea6a274dbccab87'}, 'ecosystem': 'Ruby',
               'result': {'extra_rdoc_files': ['README.md'], 'bindir': 'bin',
                          'cert_chain': [], 'files': [], 'requirements': [],
                          'dependencies': ['activesupport (>= 4.0.0)', 'activemodel (>= 4.0.0)', 'mime-types (>= 1.16)',
                                           'pg (>= 0, development)', 'rails (>= 4.0.0, development)',
                                           'cucumber (~> 2.3.2, development)', 'rspec (~> 3.4.0, development)',
                                           'webmock (>= 0, development)', 'fog (>= 1.28.0, development)',
                                           'mini_magick (>= 3.6.0, development)', 'rmagick (>= 0, development)',
                                           'nokogiri (~> 1.6.3, development)', 'timecop (= 0.7.1, development)',
                                           'generator_spec (>= 0, development)', 'pry (>= 0, development)'],
                          'rdoc_options': ['--main'], 'email': ['jonas.nicklas@gmail.com'], 'specification_version': 4,
                          'test_files': [], 'extensions': [], 'require_paths': ['lib'],
                          'homepage': 'https://github.com/carrierwaveuploader/carrierwave',
                          'required_ruby_version': '>= 2.0.0', 'authors': ['Jonas Nicklas'],
                          'description': 'Upload files in your Ruby applications, map them to a range of ORMs, store them on different backends.',
                          'licenses': ['MIT'], 'executables': [], 'version': '1.0.0.beta', 'platform': 'ruby',
                          'metadata': {}, 'name': 'carrierwave', 'summary': 'Ruby file upload library',
                          'required_rubygems_version': '> 1.3.1'}}
dotnet_result = {'digests': {'manifest': '1e1dcf1f04f12b25cceed23593f2202ae9884e6f'}, 'ecosystem': 'DotNetSolution',
                 'result': {'copyright': 'Copyright \u00a9  2016', 'guid': '3f6a93dd-da21-4333-8610-ceda4d4853da',
                            'product': 'MercatorDotNet', 'version': '1.0.0.0', 'file_version': '1.0.0.0',
                            'name': 'MercatorDotNet'}}
python_result = {'digests': {'manifest': '9503dba97ea4fccebc9f942868fadf4d2c16ea9c'}, 'ecosystem': 'Python',
                 'result': {'url': 'https://www.python.org/sigs/distutils-sig/',
                            'description': 'Python Distribution Utilities',
                            'ext_modules': [],
                            'packages': ['distutils', 'distutils.command'], 'author': 'Greg Ward',
                            'author_email': 'gward@python.net',
                            'version': '1.0', 'name': 'Distutils'}}
rust_result = {'result': {'repository': None, 'readme': None, 'authors': ['Pavel Odvody <podvody@redhat.com>'], 'homepage': None, 'keywords': [], 'description': None, 'documentation': None, 'license': None, 'license_file': None, 'package': {'source': None, 'manifest_path': '/mercator-go/tests/fixtures/rust/Cargo.toml', 'features': {}, 'dependencies': [{'uses_default_features': True, 'req': '^0.3.19', 'source': 'registry+https://github.com/rust-lang/crates.io-index', 'features': [], 'optional': False, 'kind': None, 'target': None, 'name': 'rustc-serialize'}, {'uses_default_features': True, 'req': '^0.13.0', 'source': 'registry+https://github.com/rust-lang/crates.io-index', 'features': [], 'optional': False, 'kind': None, 'target': None, 'name': 'cargo'}], 'targets': [{'src_path': '/mercator-go/tests/fixtures/rust/src/main.rs', 'kind': ['bin'], 'name': 'mercator-rust-handler'}], 'id': 'mercator-rust-handler 0.0.1 (path+file:///mercator-go/tests/fixtures/rust)', 'version': '0.0.1', 'name': 'mercator-rust-handler'}}, 'ecosystem': 'RustCrate', 'digests': {'manifest': 'c943ee4a308e49c29208a75d06bd771d7dc5c7ea'}}

haskell_result = {"digests": {"manifest": "2e8aabfd637644ae498235cf02c2890c319846e3" },"ecosystem": "HaskellCabal","result": {"mdLicense":"MIT","mdHomePage":"","mdDependencies":["base >=4.6.0","Cabal >=1.16.0","aeson >=1.2.1.0","filepath >=1.3.0.1","directory >=1.2.7.1","text >=1.2.2.2"],"mdIssueUrl":"","mdName":"mercator-hs","mdCategory":"Data","mdAuthor":"Pavel Odvody","mdCopyright":"Pavel Odvody 2017","mdDescription":"Haskell package manifest handler for Mercator","mdMaintainer":"podvody@redhat.com","mdRepos":[{"rpType":"git","rpName":"master","rpURL":"git://github.com/shaded-enmity/mercator-hs"}],"mdLockedDeps":[]}}
