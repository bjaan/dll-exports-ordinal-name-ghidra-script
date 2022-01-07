# DLL exports ordinal and function name report script for Ghidra

This Python script for Ghidra will write a table of function names and corresponding ordinals that a .dll-file exports, when Dependency Walker or other tools fails to show both the function name and the ordinal.

This script will write them anyway by using Ghidra, but requires the .pdb file as well for this process.  In case the .pdb-file isn't loaded and auto-analyzed, it will just report what it can (usually just a handful of functions).

Based on idea implemented here: https://github.com/NationalSecurityAgency/ghidra/blob/master/Ghidra/Features/Base/src/main/java/ghidra/app/util/opinion/LibrarySymbolTable.java#L106 

It tries to look for all Ordinal\_* functions, and for each of those if will look for the next symbol, when that one isn't starting with Ordinal\_ then we have the real name of exportable symbol, i.e. a function exported by the DLL.

Example: Ghidra listing: *Ordinal_6845* is a symbol that has below it a symbol with the real name, we find *?WriteString@CInternetFile@@UEAAXPEBG@Z* or *public virtual void __thiscall CInternetFile::WriteString(unsigned short const * __ptr64) __ptr64*
```
                             **************************************************************
                             *                          FUNCTION                          *
                             **************************************************************
                             undefined __fastcall Ordinal_6845(longlong * param_1, LP
             undefined         AL:1           <RETURN>
             longlong *        RCX:8          param_1
             LPCWSTR           RDX:8          param_2
             undefined8        Stack[-0x20]:8 local_20                                XREF[1]:     7ff77d9d56d(W)  
             undefined8        Stack[-0x28]:8 local_28                                XREF[3]:     7ff77d9d58d(W), 
                                                                                                   7ff77d9d5b8(W), 
                                                                                                   7ff77d9d5c4(*)  
                             0x9d560  6845  
                             ?WriteString@CInternetFile@@UEAAXPEBG@Z         XREF[5]:     Entry Point(*), 7ff77de4640(*), 
                             Ordinal_6845                                                 7ff77de4ef0(*), 7ff77e151f4(*), 
                                                                                          7ff77e3c018(*)  
     7ff77d9d560 53              PUSH       RBX
     7ff77d9d561 56              PUSH       RSI
     7ff77d9d562 57              PUSH       RDI
     7ff77d9d563 48 83 ec 30     SUB        RSP,0x30
     7ff77d9d567 48 8b f2        MOV        RSI,param_2
     7ff77d9d56a 48 8b f9        MOV        RDI,param_1
     7ff77d9d56d 48 c7 44        MOV        qword ptr [RSP + local_20],-0x2
                 24 28 fe 
                 ff ff ff
```

To generate in Ghidra, in your existing project:

1. _File_ > _Import File_: select the .dll-file
2. Double-click the .dll-file to open
4. Answer _No_ to question to start _Analyze_ process
5. _File_ > _Load PBP File..._, load it from disk here
6. Run _Auto-Analyze_ by _Analyze_ > _Auto-Analyze_, make sure the _PDB_ step is checked
7. Run the below code as a new Python Script in Script Manager
8. Find _exports.txt_ in the root installation folder

It exports a text file _output.txt_ in the root installation folder of Ghidra that is tab-separated.

Columns:
* Ordinal
* Function name, for VC++ functions this is often a Decorated Name, see https://docs.microsoft.com/en-us/cpp/build/reference/decorated-names
* Undecorated name: when a Decorated Name

Example output for MFC42U.DLL:
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

