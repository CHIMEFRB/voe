# Changelog

## [0.5.0](https://github.com/CHIMEFRB/voe/compare/v0.4.0...v0.5.0) (2024-10-29)


### Features

* **backend/voe.py:** adding create voe endpoint ([488c000](https://github.com/CHIMEFRB/voe/commit/488c00062a41e910c5b3001aa064a310c62fb297))
* **backends/subscriber.py:** added subscriber backend and CLI ([8d818c2](https://github.com/CHIMEFRB/voe/commit/8d818c27acf46f24ca002a1367861cd5e52d0b1c))
* **backends/subscriber:** added subscriber backend and CLI ([dc124c3](https://github.com/CHIMEFRB/voe/commit/dc124c3aaef97e828c90010e37bbcc335dff5a2c))
* **cd:** added a release action ([59b091c](https://github.com/CHIMEFRB/voe/commit/59b091c2896bce4332f1b03657004ede971de2e7))
* **cli:** added click cli support ([bc6f784](https://github.com/CHIMEFRB/voe/commit/bc6f784c19bd62ef266ca7426cf9f8adf95f2246))
* **CLI:** Added subscriber CLI ([4e987a6](https://github.com/CHIMEFRB/voe/commit/4e987a6881f42d9b9d8b7252a45d5ebad3ce7f1a))
* **devops:** basic system setup ([1724127](https://github.com/CHIMEFRB/voe/commit/172412752c97ccbaf679c5ff4225bf28f3b40e57))
* **docker-compose:** Added a poetry install command to docker ([e8e4d3c](https://github.com/CHIMEFRB/voe/commit/e8e4d3cda059c96d38ad106e051745a135cd11a2))
* **docker:** added dockerfile and a docker compose config ([dda30fb](https://github.com/CHIMEFRB/voe/commit/dda30fb13b31978906f9f258d41d392f0a60bb67))
* **docker:** fixes to Dockerfile ([b4cd247](https://github.com/CHIMEFRB/voe/commit/b4cd247e5a8d259cdcbe3a3e3e52cf7ba620b435))
* **Documentation:** Added "Configuring Your Observatory" to the README ([1517694](https://github.com/CHIMEFRB/voe/commit/15176947259f295910464d336a78796b46099c93))
* **Documentation:** Added "Configuring Your Observatory" to the README ([44a617d](https://github.com/CHIMEFRB/voe/commit/44a617df3c3c1a70fbb7c16bdcd692272df07dd8))
* **email:** Added functionality to send a voe email ([d55725b](https://github.com/CHIMEFRB/voe/commit/d55725b899e055e7f0b744fa418157a84a582025))
* **examples:** Added a sample script to send HTTP requests to the frb-voe server ([dbc169e](https://github.com/CHIMEFRB/voe/commit/dbc169e36b93482ac8c677e623f540e678b79615))
* **frbvoe/models/subscriber.py:** Created functionality to add a subscriber to the DB ([8b63fe7](https://github.com/CHIMEFRB/voe/commit/8b63fe7f398da0677fa25f65c2819d1f00e7ad52))
* **linting:** linting changes ([c253a7b](https://github.com/CHIMEFRB/voe/commit/c253a7bf584410b5e8a99b2e101c81b95ec5da4c))
* **server:** started on server side logic ([620ce77](https://github.com/CHIMEFRB/voe/commit/620ce7720ee66f11c2c1fd79dba645e57270e16c))
* **structure:** added core project structure ([c38f6e2](https://github.com/CHIMEFRB/voe/commit/c38f6e26894671b731343656654145415841cfdd))
* **testing-+-CI:** added working tests and added a default ci workflow ([47a23a8](https://github.com/CHIMEFRB/voe/commit/47a23a887ae96e572c265f48291d68a288a2f7c5))
* **TNSReport.py,-VOEvent.py:** Added VOEvent and TNSReport classes (using Pydantic) ([bb6cd5f](https://github.com/CHIMEFRB/voe/commit/bb6cd5f44b22a54217f869cd5e1450fa3cce167d))


### Bug Fixes

* **CLI:** Added some CLI commands + docs ([9ed6779](https://github.com/CHIMEFRB/voe/commit/9ed677984041b4e4816aaeb6729fc6a4331427a4))
* **Dockerfile:** fixed Dockerfile ([f29fd50](https://github.com/CHIMEFRB/voe/commit/f29fd50f5a0e577de836f18c65ccaf93a0dc7713))
* **Everything:** Tidied-up ([81d3d26](https://github.com/CHIMEFRB/voe/commit/81d3d2653139f7c741d1ae115e92c10d4011ef65))
* **Fixed-linting:** Fixed linting for utilities/email.py ([1806807](https://github.com/CHIMEFRB/voe/commit/18068078808316b166c6f61415f0ef5a96ca0ea6))
* **frbvoe/server.py:** Fixed Fallback error ([3bdeafe](https://github.com/CHIMEFRB/voe/commit/3bdeafeaf7fe17ce9d7c4d0af9163fbec38a6421))
* **frbvoe:** WIP ([f085e07](https://github.com/CHIMEFRB/voe/commit/f085e07f671adaf1c554da36d9c4f049b2b4b649))
* **linting:** Fixed pre-commit linting ([3777b5c](https://github.com/CHIMEFRB/voe/commit/3777b5cea260858f923b3697a6bceeca543ec144))
* **models:** Added tokenized attributes ([100c867](https://github.com/CHIMEFRB/voe/commit/100c867735a3461a24269ab6f32532b5a3d91a77))
* **README-+-Tests:** Added schematic to readme and testing for CLI ([b5ad815](https://github.com/CHIMEFRB/voe/commit/b5ad81500a54e74807ac695ff7efec4c2306f020))
* **readme:** added coverage badge ([364afb2](https://github.com/CHIMEFRB/voe/commit/364afb238805fd8080986d2c4781a27d6b34bfca))
* **README:** added figure ([a659b43](https://github.com/CHIMEFRB/voe/commit/a659b43f2917e4ae2ffe1c11a08d2d4f64a8c1f6))
* **tests:** added coverage for CLI and backends ([07fd67b](https://github.com/CHIMEFRB/voe/commit/07fd67bf55ab92c709e22a9010e6ac036677b336))
* **tests:** added some tests ([8098802](https://github.com/CHIMEFRB/voe/commit/8098802b48737cc448275032c64c933987cd5e47))
* **tests:** Added tests ([00daee7](https://github.com/CHIMEFRB/voe/commit/00daee7fd9dc7393c3849d637c8fa2d86b0e3b2e))
* **Tests:** Fixed some broken tests - removed part of the TNS test ([bab3d9e](https://github.com/CHIMEFRB/voe/commit/bab3d9e5c2aff3e0938a6e4b827640d4bd372a62))
* **voe:** Fixed formatting according to black formatting style ([d6069fe](https://github.com/CHIMEFRB/voe/commit/d6069fe6ee96f1a52bd5b32f2a19448a2cdd325e))
* **WIP:** WIP ([e898ccf](https://github.com/CHIMEFRB/voe/commit/e898ccf1913da1ee010c250bce41ab6e00c3ac4a))
* **WIP:** WIP ([ed44c7b](https://github.com/CHIMEFRB/voe/commit/ed44c7b07f7c7e4c1b1f0e00512223453d881eda))

## [0.4.0](https://github.com/CHIMEFRB/voe/compare/v0.3.0...v0.4.0) (2024-07-19)


### Features

* **backend/voe.py:** adding create voe endpoint ([488c000](https://github.com/CHIMEFRB/voe/commit/488c00062a41e910c5b3001aa064a310c62fb297))
* **backends/subscriber.py:** added subscriber backend and CLI ([8d818c2](https://github.com/CHIMEFRB/voe/commit/8d818c27acf46f24ca002a1367861cd5e52d0b1c))
* **backends/subscriber:** added subscriber backend and CLI ([dc124c3](https://github.com/CHIMEFRB/voe/commit/dc124c3aaef97e828c90010e37bbcc335dff5a2c))
* **cli:** added click cli support ([bc6f784](https://github.com/CHIMEFRB/voe/commit/bc6f784c19bd62ef266ca7426cf9f8adf95f2246))
* **CLI:** Added subscriber CLI ([4e987a6](https://github.com/CHIMEFRB/voe/commit/4e987a6881f42d9b9d8b7252a45d5ebad3ce7f1a))
* **docker-compose:** Added a poetry install command to docker ([e8e4d3c](https://github.com/CHIMEFRB/voe/commit/e8e4d3cda059c96d38ad106e051745a135cd11a2))
* **email:** Added functionality to send a voe email ([d55725b](https://github.com/CHIMEFRB/voe/commit/d55725b899e055e7f0b744fa418157a84a582025))
* **frbvoe/models/subscriber.py:** Created functionality to add a subscriber to the DB ([8b63fe7](https://github.com/CHIMEFRB/voe/commit/8b63fe7f398da0677fa25f65c2819d1f00e7ad52))
* **linting:** linting changes ([c253a7b](https://github.com/CHIMEFRB/voe/commit/c253a7bf584410b5e8a99b2e101c81b95ec5da4c))
* **server:** started on server side logic ([620ce77](https://github.com/CHIMEFRB/voe/commit/620ce7720ee66f11c2c1fd79dba645e57270e16c))


### Bug Fixes

* **Dockerfile:** fixed Dockerfile ([f29fd50](https://github.com/CHIMEFRB/voe/commit/f29fd50f5a0e577de836f18c65ccaf93a0dc7713))
* **Everything:** Tidied-up ([81d3d26](https://github.com/CHIMEFRB/voe/commit/81d3d2653139f7c741d1ae115e92c10d4011ef65))
* **Fixed-linting:** Fixed linting for utilities/email.py ([1806807](https://github.com/CHIMEFRB/voe/commit/18068078808316b166c6f61415f0ef5a96ca0ea6))
* **frbvoe/server.py:** Fixed Fallback error ([3bdeafe](https://github.com/CHIMEFRB/voe/commit/3bdeafeaf7fe17ce9d7c4d0af9163fbec38a6421))
* **frbvoe:** WIP ([f085e07](https://github.com/CHIMEFRB/voe/commit/f085e07f671adaf1c554da36d9c4f049b2b4b649))
* **linting:** Fixed pre-commit linting ([3777b5c](https://github.com/CHIMEFRB/voe/commit/3777b5cea260858f923b3697a6bceeca543ec144))
* **README-+-Tests:** Added schematic to readme and testing for CLI ([b5ad815](https://github.com/CHIMEFRB/voe/commit/b5ad81500a54e74807ac695ff7efec4c2306f020))
* **README:** added figure ([a659b43](https://github.com/CHIMEFRB/voe/commit/a659b43f2917e4ae2ffe1c11a08d2d4f64a8c1f6))
* **tests:** added coverage for CLI and backends ([07fd67b](https://github.com/CHIMEFRB/voe/commit/07fd67bf55ab92c709e22a9010e6ac036677b336))
* **tests:** added some tests ([8098802](https://github.com/CHIMEFRB/voe/commit/8098802b48737cc448275032c64c933987cd5e47))

## [0.3.0](https://github.com/CHIMEFRB/voe/compare/v0.2.0...v0.3.0) (2024-05-01)


### Features

* **docker:** fixes to Dockerfile ([b4cd247](https://github.com/CHIMEFRB/voe/commit/b4cd247e5a8d259cdcbe3a3e3e52cf7ba620b435))

## [0.2.0](https://github.com/CHIMEFRB/voe/compare/v0.1.0...v0.2.0) (2024-05-01)


### Features

* **docker:** added dockerfile and a docker compose config ([dda30fb](https://github.com/CHIMEFRB/voe/commit/dda30fb13b31978906f9f258d41d392f0a60bb67))

## 0.1.0 (2024-04-30)


### Features

* **cd:** added a release action ([59b091c](https://github.com/CHIMEFRB/voe/commit/59b091c2896bce4332f1b03657004ede971de2e7))
* **devops:** basic system setup ([1724127](https://github.com/CHIMEFRB/voe/commit/172412752c97ccbaf679c5ff4225bf28f3b40e57))
* **structure:** added core project structure ([c38f6e2](https://github.com/CHIMEFRB/voe/commit/c38f6e26894671b731343656654145415841cfdd))
* **testing-+-CI:** added working tests and added a default ci workflow ([47a23a8](https://github.com/CHIMEFRB/voe/commit/47a23a887ae96e572c265f48291d68a288a2f7c5))
* **TNSReport.py,-VOEvent.py:** Added VOEvent and TNSReport classes (using Pydantic) ([bb6cd5f](https://github.com/CHIMEFRB/voe/commit/bb6cd5f44b22a54217f869cd5e1450fa3cce167d))


### Bug Fixes

* **models:** Added tokenized attributes ([100c867](https://github.com/CHIMEFRB/voe/commit/100c867735a3461a24269ab6f32532b5a3d91a77))
* **readme:** added coverage badge ([364afb2](https://github.com/CHIMEFRB/voe/commit/364afb238805fd8080986d2c4781a27d6b34bfca))
* **tests:** Added tests ([00daee7](https://github.com/CHIMEFRB/voe/commit/00daee7fd9dc7393c3849d637c8fa2d86b0e3b2e))
* **voe:** Fixed formatting according to black formatting style ([d6069fe](https://github.com/CHIMEFRB/voe/commit/d6069fe6ee96f1a52bd5b32f2a19448a2cdd325e))
* **WIP:** WIP ([e898ccf](https://github.com/CHIMEFRB/voe/commit/e898ccf1913da1ee010c250bce41ab6e00c3ac4a))
* **WIP:** WIP ([ed44c7b](https://github.com/CHIMEFRB/voe/commit/ed44c7b07f7c7e4c1b1f0e00512223453d881eda))
