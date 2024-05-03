This repo can help you to generate interlinked coqdoc documentation in bulk. However, it uses features in unintended ways and uses undocumented globfile shenanigans. Caveat emptor.

`coqdoc` needs glob (globalization) files produced as a byproduct when Coq source is built. Glob files are frequently not installed alongside the built files, so if your Opam switch is already installed, chances are you have lost all your glob files.

But don't fret, we can recover them. We can have opam to rebuild each package with the `-b` flag, which tells opam to save the build directory for our purposes. Something like this should work to rebuild all Coq packages in a switch:

```bash
opam list --columns package | grep coq | xargs opam reinstall -b
``` 

When you are installing packages for the first time you may similarly use the `-b` flag to save build directories.

Now create a `html` folder in this directory (with that name) and run the following in this directory:

```bash
python {your switch root}/{your switch}/.opam-switch/build | xargs coqdoc
```

The script digs around in your build directory for glob files and uses them to generate flags for Coqdoc. Results end up in the `html` directory. 

It can take several minutes for Coqdoc to process a switch.
