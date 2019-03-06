prez.pdf : prez.md
	pandoc -t beamer prez.md --slide-level 2 -V theme:Boadilla -V lang=pl-PL -o prez.pdf

clean:
	rm -f prez.pdf
