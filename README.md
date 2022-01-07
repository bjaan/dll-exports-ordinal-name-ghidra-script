# DLL exports ordinal and function name report script for Ghidra

This Python script for Ghidra will export a table of function names and corresponding ordinals of a DLL, when Dependency Walker fails to show both the function name and the ordinal.

This script will export them anyway by using Ghidra, but you require the .pdb file as well for this process.  In case you do not have the .pdb, it will just export what it can.

To generate in Ghidra, in your existing project:

1. _File_ > _Import File_: select the .dll-file
2. Double-click the the .dll-file to open
4. Cancel _Auto-Analyze_ dialog
5. _File_ > _Load PBP File..._
6. Run _Auto-Analyze_ by _Analyze_ > _Auto-Analyze_, make sure the _PDB_ step is checked
7. 
4. Run the below code as a new Python Script in Script Manager
5. Find _exports.txt_ in the root installation folder

It exports a text file _output.txt_ in the root installation folder of Ghidra that is tab-separated.

Columns:
* Ordinal
* Function name, for VC++ functions this is often a Decorated Name, see https://docs.microsoft.com/en-us/cpp/build/reference/decorated-names
* Undecorated name: when a Decorated Name

Example output:
```
875	??1CEvent@@UEAA@XZ	public virtual __thiscall CEvent::~CEvent(void) __ptr64 
6858	IsPlatformNT
6856	InitMultipleMonitorStubs
6864	xMonitorFromRect
6865	xMonitorFromWindow
6861	xGetMonitorInfo
923	??1CMDIFrameWnd@@UEAA@XZ	public virtual __thiscall CMDIFrameWnd::~CMDIFrameWnd(void) __ptr64 
922	??1CMDIChildWnd@@UEAA@XZ	public virtual __thiscall CMDIChildWnd::~CMDIChildWnd(void) __ptr64 
928	??1CMiniDockFrameWnd@@UEAA@XZ	public virtual __thiscall CMiniDockFrameWnd::~CMiniDockFrameWnd(void) __ptr64 
1009	??1CReBar@@UEAA@XZ	public virtual __thiscall CReBar::~CReBar(void) __ptr64 
829	??1CColorDialog@@UEAA@XZ	public virtual __thiscall CColorDialog::~CColorDialog(void) __ptr64 
881	??1CFindReplaceDialog@@UEAA@XZ	public virtual __thiscall CFindReplaceDialog::~CFindReplaceDialog(void) __ptr64 
```

Based on idea implemented here: https://github.com/NationalSecurityAgency/ghidra/blob/master/Ghidra/Features/Base/src/main/java/ghidra/app/util/opinion/LibrarySymbolTable.java#L106