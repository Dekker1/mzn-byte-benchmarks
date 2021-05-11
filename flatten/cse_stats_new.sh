MZNCC=$HOME/Dropbox/development/minizinc.byte/build/Release/mzncc
MZNASM=$HOME/Dropbox/development/minizinc.byte/build/Release/mznasm
DTRACE=$HOME/Dropbox/development/minizinc.byte/tests/dtrace/cse.d

$MZNCC -Gstd $1 > _temp.uzn
for i in *.dzn; do
  $DTRACE -c "${MZNASM} --solver org.minizinc.mzn-fzn -c _temp.uzn $i" > ${i}_new.txt
done
rm -f _temp.uzn _temp.fzn
