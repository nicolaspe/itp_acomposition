# Algorithmic Composition - Mar 07

## [Supercollider](https://supercollider.github.io/)
Creative music coding language. Used to be paid and later open sourced.

It uses a client-server architecture, where there are many many frontend versions. This is GREAT for networked music!

Uses a programming language based on **smalltalk** (like Obj-C, whereas C++, C# are based in **simula**)
It has first class functions: you can assign a function as a variable (like JavaScript), and pass them as arguments for other functions

We also have `ar` for **audio rate** and `kr` for **control rate**



### Syntax
- `{ .. }.play` plays everything between the `{}`, but it can only be one. **HERE** you must write everything that evaluates, needs a scheduler to run.
- `cmd+d` to get help related to the highlighted thing
- `cmd+enter` execute!
- `cmd+.` STOP!
- `( .. )` creates blocks of code to be run simultaneously
- `[a, b]` short hand for multi-channel, `a` in the first, `b` second, and you can go beyond that



**[The Cathedral and the Bazaar](http://www.catb.org/esr/writings/cathedral-bazaar/)**: essay about different models for open source projects


## Extra stuff
- [20 objects](http://www.darwingrosse.com/20Objects/) good MaxMSP tutoriallear
