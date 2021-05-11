
MINIZINC=$HOME/Dropbox/development/minizinc/build/Release/minizinc
DTRACE=$HOME/Dropbox/development/minizinc/tests/dtrace/cse.d

for i in *.dzn; do
  $DTRACE -c "${MINIZINC} --solver org.minizinc.mzn-fzn -c $1 $i" > ${i}_orig.txt
done
