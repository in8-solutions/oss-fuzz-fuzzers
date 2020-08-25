all : fuzzer-loadimg fuzzer-load_fli fuzzer-load_jpeg fuzzer-load_jpeg2k fuzzer-load_pcd fuzzer-load_pcx fuzzer-load_png fuzzer-load_sgi fuzzer-load_sun fuzzer-load_tga fuzzer-load_tiff

PYTHON_CONFIG_PATH=$(CPYTHON_INSTALL_PATH)/bin/python3-config
CXXFLAGS += $(shell $(PYTHON_CONFIG_PATH) --cflags)
LDFLAGS += -rdynamic $(shell $(PYTHON_CONFIG_PATH) --ldflags --embed)

fuzzer-loadimg:
	clang++ $(CXXFLAGS) $(LIB_FUZZING_ENGINE) -std=c++17 fuzzer.cpp -DPYTHON_HARNESS_PATH="\"loadimg.py\"" -ldl $(LDFLAGS) -o fuzzer-loadimg

fuzzer-load_fli:
	clang++ $(CXXFLAGS) $(LIB_FUZZING_ENGINE) -std=c++17 fuzzer.cpp -DPYTHON_HARNESS_PATH="\"load_fli.py\"" -ldl $(LDFLAGS) -o fuzzer-load_fli

fuzzer-load_jpeg:
	clang++ $(CXXFLAGS) $(LIB_FUZZING_ENGINE) -std=c++17 fuzzer.cpp -DPYTHON_HARNESS_PATH="\"load_jpeg.py\"" -ldl $(LDFLAGS) -o fuzzer-load_jpeg

fuzzer-load_jpeg2k:
	clang++ $(CXXFLAGS) $(LIB_FUZZING_ENGINE) -std=c++17 fuzzer.cpp -DPYTHON_HARNESS_PATH="\"load_jpeg2k.py\"" -ldl $(LDFLAGS) -o fuzzer-load_jpeg2k

fuzzer-load_pcd:
	clang++ $(CXXFLAGS) $(LIB_FUZZING_ENGINE) -std=c++17 fuzzer.cpp -DPYTHON_HARNESS_PATH="\"load_pcd.py\"" -ldl $(LDFLAGS) -o fuzzer-load_pcd

fuzzer-load_pcx:
	clang++ $(CXXFLAGS) $(LIB_FUZZING_ENGINE) -std=c++17 fuzzer.cpp -DPYTHON_HARNESS_PATH="\"load_pcx.py\"" -ldl $(LDFLAGS) -o fuzzer-load_pcx

fuzzer-load_png:
	clang++ $(CXXFLAGS) $(LIB_FUZZING_ENGINE) -std=c++17 fuzzer.cpp -DPYTHON_HARNESS_PATH="\"load_png.py\"" -ldl $(LDFLAGS) -o fuzzer-load_png

fuzzer-load_sgi:
	clang++ $(CXXFLAGS) $(LIB_FUZZING_ENGINE) -std=c++17 fuzzer.cpp -DPYTHON_HARNESS_PATH="\"load_sgi.py\"" -ldl $(LDFLAGS) -o fuzzer-load_sgi

fuzzer-load_sun:
	clang++ $(CXXFLAGS) $(LIB_FUZZING_ENGINE) -std=c++17 fuzzer.cpp -DPYTHON_HARNESS_PATH="\"load_sun.py\"" -ldl $(LDFLAGS) -o fuzzer-load_sun

fuzzer-load_tga:
	clang++ $(CXXFLAGS) $(LIB_FUZZING_ENGINE) -std=c++17 fuzzer.cpp -DPYTHON_HARNESS_PATH="\"load_tga.py\"" -ldl $(LDFLAGS) -o fuzzer-load_tga

fuzzer-load_tiff:
	clang++ $(CXXFLAGS) $(LIB_FUZZING_ENGINE) -std=c++17 fuzzer.cpp -DPYTHON_HARNESS_PATH="\"load_tiff.py\"" -ldl $(LDFLAGS) -o fuzzer-load_tiff
