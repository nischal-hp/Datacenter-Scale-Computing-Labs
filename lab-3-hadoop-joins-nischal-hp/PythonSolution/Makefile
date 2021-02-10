##
## Makefile

run: input/apat63_99.txt input/cite75_99.txt
	-rm -rf stream-output-new
	./RUN-MAP-REDUCE \
		-files Mapper1.py,Reducer1.py \
		-mapper Mapper1.py \
		-reducer Reducer1.py \
		-input input -output stream-output-new
        
run-2: 
	-rm -rf stream-output-2
	./RUN-MAP-REDUCE \
		-files Mapper2.py,Reducer2.py \
		-mapper Mapper2.py \
		-reducer Reducer2.py \
		-input input-2 -output stream-output-2

run-3: 
	-rm -rf stream-output-3
	./RUN-MAP-REDUCE \
		-files Mapper3.py,Reducer3.py \
		-mapper Mapper3.py \
		-reducer Reducer3.py \
		-input input-3 -output stream-output-3

input:
	mkdir ./input

input/cite75_99.txt: input ../acite75_99.zip
	unzip ../acite75_99.zip
	touch cite75_99.txt # update modification time
	mv cite75_99.txt input

input/apat63_99.txt: input ../apat63_99.zip
	unzip ../apat63_99.zip
	touch apat63_99.txt # update modification time
	mv apat63_99.txt input

prepare:
	echo "Some of the following commands may fail because your"
	echo "files are already setup"
	echo "====="
	-hdfs dfs -mkdir /user
	-hdfs dfs -mkdir /user/$(USER)
	-hdfs dfs -rm -r -f /user/$(USER)/input
	-hdfs dfs -rm -r -f /user/$(USER)/output	


