for f in *.jpg; do
    convert $f -resize '500x>' preview/$f
done
