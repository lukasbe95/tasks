all:
	@g++ -o out src/bitcoin.cpp src/bitcoin_lib.h src/bitcoin_lib.cpp -std=c++11
	@./out
clean:
	@rm out
