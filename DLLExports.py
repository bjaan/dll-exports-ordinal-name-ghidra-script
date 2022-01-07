#Write a text file with the Ordinal and Function Names inside a .DLL file. NB: load .PDB first so that both the mangled (decorated) and ordinal are available (see https://docs.microsoft.com/en-us/cpp/build/reference/decorated-names)
#@author bjaan
#@category Symbol
#@keybinding 
#@menupath 
#@toolbar 

parser = ghidra.app.util.demangler.microsoft.MicrosoftDemangler()
symTab = currentProgram.getSymbolTable()
iter = symTab.getSymbolIterator(Ordinal_, True)

f = open(exports.txt, 'w')
for sym in iter
	ordinal = sym.getName()[len(Ordinal_)]
	symAddr = sym.getAddress()
	primary = symTab.getPrimarySymbol(symAddr)
	realName = primary.getName()
	symbolsAt = symTab.getSymbols(symAddr);
	for i in range(0, len(symbolsAt)-1)
		if sym.getName() == symbolsAt[i].getName()
			if i + 1  len(symbolsAt)
				realName = symbolsAt[i + 1].getName()
				break;
	if realName.startswith(Ordinal_)
		continue
	demangledObject = parser.demangle(realName, True)
	if demangledObject is None
		demangled = 
	else
		demangled = demangledObject.toString()
	f.write(ordinal + t + realName)
	if len(demangled)  0 
		f.write(t + demangled)
	f.write('n')
