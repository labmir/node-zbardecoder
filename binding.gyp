{
  "targets": [
    {
      "target_name": "zbardecoder",
      "cflags!": [ "-fno-exceptions" ],
      "cflags_cc!": [ "-fno-exceptions" ],
      "sources": [
        "./src/decoder.cpp",
        "./src/index.cpp"
      ],
      "libraries":    ["-lzbar", "-lopencv_core", "-lopencv_imgcodecs", "-lopencv_highgui", "-lopencv_imgproc"],
      "include_dirs": [
        "<!@(node -p \"require('node-addon-api').include\")", "/usr/include/opencv4"
      ],
      'defines': [ 'NAPI_DISABLE_CPP_EXCEPTIONS' ],
    }
  ]
}
