{
  "targets": [
    {
      "target_name": "tree_sitter_beancount_binding",
      "dependencies": [
        "<!(node -p \"require('node-addon-api').targets\"):node_addon_api_except",
      ],
      "include_dirs": [
        "<!(node -e \"require('nan')\")",
        "<!(node -e \"require('node-addon-api').include\")",
        "src",
      ],
      "sources": [
        "bindings/node/binding.cc",
        "src/parser.c",
        # NOTE: if your language has an external scanner, add it here.
      ],
      "conditions": [
        ["OS!='win'", {
          "cflags_c": [
            "-std=c11",
          ],
          "cflags_cc": [
            "-std=c++11",
          ],
        }, { # OS == "win"
          "cflags_c": [
            "/std:c11",
            "/utf-8",
          ],
          "cflags_cc": [
            "/std:c++11",
          ],
        }],
      ],
      "cflags_cc": ["-std=c++11"],
      "xcode_settings": {
        "CLANG_CXX_LANGUAGE_STANDARD": "c++11",
        "CLANG_CXX_LIBRARY": "libc++"
      },
      "msvs_settings": {
        "VCCLCompilerTool": {
          "AdditionalOptions": ["/std:c++11"]
        }
      }
    }
  ]
}
