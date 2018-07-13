all:
	@g++ -o out src/bitcoin.cpp src/bitcoin_lib.h src/bitcoin_lib.cpp
	@./out
clean:
	@rm out
