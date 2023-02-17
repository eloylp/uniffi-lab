#!/bin/bash

cargo run -p uniffi-bindgen generate ./src/basic.udl --language python
mv ./src/basic.py generated
cargo build --release
mv ../target/release/libbasic.so generated