<?xml version='1.0' encoding='UTF-8'?>
<Project Type="Project" LVVersion="17008000">
	<Property Name="SMProvider.SMVersion" Type="Int">201310</Property>
	<Item Name="My Computer" Type="My Computer">
		<Property Name="IOScan.Faults" Type="Str"></Property>
		<Property Name="IOScan.NetVarPeriod" Type="UInt">100</Property>
		<Property Name="IOScan.NetWatchdogEnabled" Type="Bool">false</Property>
		<Property Name="IOScan.Period" Type="UInt">10000</Property>
		<Property Name="IOScan.PowerupMode" Type="UInt">0</Property>
		<Property Name="IOScan.Priority" Type="UInt">9</Property>
		<Property Name="IOScan.ReportModeConflict" Type="Bool">true</Property>
		<Property Name="IOScan.StartEngineOnDeploy" Type="Bool">false</Property>
		<Property Name="NI.SortType" Type="Int">3</Property>
		<Property Name="server.app.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="server.control.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="server.tcp.enabled" Type="Bool">false</Property>
		<Property Name="server.tcp.port" Type="Int">0</Property>
		<Property Name="server.tcp.serviceName" Type="Str">My Computer/VI Server</Property>
		<Property Name="server.tcp.serviceName.default" Type="Str">My Computer/VI Server</Property>
		<Property Name="server.vi.callsEnabled" Type="Bool">true</Property>
		<Property Name="server.vi.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="specify.custom.address" Type="Bool">false</Property>
		<Item Name="software_resource" Type="Folder">
			<Item Name="offline_sample" Type="Folder">
				<Item Name="bottom-OK-1.png" Type="Document" URL="../software_resource/offline_sample/bottom-OK-1.png"/>
			</Item>
			<Item Name="output" Type="Folder"/>
		</Item>
		<Item Name="AOI_Main.vi" Type="VI" URL="../AOI_Main.vi"/>
		<Item Name="IO_TEST.vi" Type="VI" URL="../IO_TEST.vi"/>
		<Item Name="TimeFlow_for_泰克.vi" Type="VI" URL="../TimeFlow_for_泰克.vi"/>
		<Item Name="parameter.txt" Type="Document" URL="../parameter.txt"/>
		<Item Name="pwd.vi" Type="VI" URL="../pwd.vi"/>
		<Item Name="Dependencies" Type="Dependencies">
			<Item Name="user.lib" Type="Folder">
				<Item Name="2Darray1DDigitalWfm.vi" Type="VI" URL="/&lt;userlib&gt;/DAQNavi Polymorphic VI/component/2Darray1DDigitalWfm.vi"/>
				<Item Name="2Darray1DWfm.vi" Type="VI" URL="/&lt;userlib&gt;/DAQNavi Polymorphic VI/component/2Darray1DWfm.vi"/>
				<Item Name="2DarrayTo1DarrayDouble.vi" Type="VI" URL="/&lt;userlib&gt;/DAQNavi Polymorphic VI/component/2DarrayTo1DarrayDouble.vi"/>
				<Item Name="2DarrayTo1DarrayUint8.vi" Type="VI" URL="/&lt;userlib&gt;/DAQNavi Polymorphic VI/component/2DarrayTo1DarrayUint8.vi"/>
				<Item Name="2DarrayTo1DarrayUint16.vi" Type="VI" URL="/&lt;userlib&gt;/DAQNavi Polymorphic VI/component/2DarrayTo1DarrayUint16.vi"/>
				<Item Name="2DarrayTo1DarrayUint32.vi" Type="VI" URL="/&lt;userlib&gt;/DAQNavi Polymorphic VI/component/2DarrayTo1DarrayUint32.vi"/>
				<Item Name="1730u Initial.vi" Type="VI" URL="/&lt;userlib&gt;/DAQNavi Polymorphic VI/1730U/1730u Initial.vi"/>
				<Item Name="1730u Read.vi" Type="VI" URL="/&lt;userlib&gt;/DAQNavi Polymorphic VI/1730U/1730u Read.vi"/>
				<Item Name="1730u Write.vi" Type="VI" URL="/&lt;userlib&gt;/DAQNavi Polymorphic VI/1730U/1730u Write.vi"/>
				<Item Name="BioIsFailed_Polymorphic.vi" Type="VI" URL="/&lt;userlib&gt;/DAQNavi Polymorphic VI/component/BioIsFailed_Polymorphic.vi"/>
				<Item Name="Check DI State 1730u.vi" Type="VI" URL="/&lt;userlib&gt;/DAQNavi Polymorphic VI/1730U/Check DI State 1730u.vi"/>
				<Item Name="CheckChannelCount.vi" Type="VI" URL="/&lt;userlib&gt;/DAQNavi Polymorphic VI/component/CheckChannelCount.vi"/>
				<Item Name="CheckEveryChannel&apos;sSamplesCount.vi" Type="VI" URL="/&lt;userlib&gt;/DAQNavi Polymorphic VI/component/CheckEveryChannel&apos;sSamplesCount.vi"/>
				<Item Name="CheckSamplesCount.vi" Type="VI" URL="/&lt;userlib&gt;/DAQNavi Polymorphic VI/component/CheckSamplesCount.vi"/>
				<Item Name="CheckSamplesCountAndChannelsCount.vi" Type="VI" URL="/&lt;userlib&gt;/DAQNavi Polymorphic VI/component/CheckSamplesCountAndChannelsCount.vi"/>
				<Item Name="DAQNavi Create Channel(AI-Current).vi" Type="VI" URL="/&lt;userlib&gt;/DAQNavi Polymorphic VI/create/DAQNavi Create Channel(AI-Current).vi"/>
				<Item Name="DAQNavi Create Channel(AI-Temperature).vi" Type="VI" URL="/&lt;userlib&gt;/DAQNavi Polymorphic VI/create/DAQNavi Create Channel(AI-Temperature).vi"/>
				<Item Name="DAQNavi Create Channel(AI-Voltage).vi" Type="VI" URL="/&lt;userlib&gt;/DAQNavi Polymorphic VI/create/DAQNavi Create Channel(AI-Voltage).vi"/>
				<Item Name="DAQNavi Create Channel(AO-Current).vi" Type="VI" URL="/&lt;userlib&gt;/DAQNavi Polymorphic VI/create/DAQNavi Create Channel(AO-Current).vi"/>
				<Item Name="DAQNavi Create Channel(AO-Voltage).vi" Type="VI" URL="/&lt;userlib&gt;/DAQNavi Polymorphic VI/create/DAQNavi Create Channel(AO-Voltage).vi"/>
				<Item Name="DAQNavi Create Channel(CI-Count Value).vi" Type="VI" URL="/&lt;userlib&gt;/DAQNavi Polymorphic VI/create/DAQNavi Create Channel(CI-Count Value).vi"/>
				<Item Name="DAQNavi Create Channel(CI-Frequency).vi" Type="VI" URL="/&lt;userlib&gt;/DAQNavi Polymorphic VI/create/DAQNavi Create Channel(CI-Frequency).vi"/>
				<Item Name="DAQNavi Create Channel(CI-PulseWidth).vi" Type="VI" URL="/&lt;userlib&gt;/DAQNavi Polymorphic VI/create/DAQNavi Create Channel(CI-PulseWidth).vi"/>
				<Item Name="DAQNavi Create Channel(CI-UpDown Count Value).vi" Type="VI" URL="/&lt;userlib&gt;/DAQNavi Polymorphic VI/create/DAQNavi Create Channel(CI-UpDown Count Value).vi"/>
				<Item Name="DAQNavi Create Channel(CO-Delayed Pulse).vi" Type="VI" URL="/&lt;userlib&gt;/DAQNavi Polymorphic VI/create/DAQNavi Create Channel(CO-Delayed Pulse).vi"/>
				<Item Name="DAQNavi Create Channel(CO-Frequency).vi" Type="VI" URL="/&lt;userlib&gt;/DAQNavi Polymorphic VI/create/DAQNavi Create Channel(CO-Frequency).vi"/>
				<Item Name="DAQNavi Create Channel(CO-Pulse Width).vi" Type="VI" URL="/&lt;userlib&gt;/DAQNavi Polymorphic VI/create/DAQNavi Create Channel(CO-Pulse Width).vi"/>
				<Item Name="DAQNavi Create Channel(DI-Digital Input).vi" Type="VI" URL="/&lt;userlib&gt;/DAQNavi Polymorphic VI/create/DAQNavi Create Channel(DI-Digital Input).vi"/>
				<Item Name="DAQNavi Create Channel(DO-Digital Output).vi" Type="VI" URL="/&lt;userlib&gt;/DAQNavi Polymorphic VI/create/DAQNavi Create Channel(DO-Digital Output).vi"/>
				<Item Name="DAQNavi Create Channel.vi" Type="VI" URL="/&lt;userlib&gt;/DAQNavi Polymorphic VI/create/DAQNavi Create Channel.vi"/>
				<Item Name="DAQNavi Read (Analog 1D DBL 1Chan NSamp).vi" Type="VI" URL="/&lt;userlib&gt;/DAQNavi Polymorphic VI/read/DAQNavi Read (Analog 1D DBL 1Chan NSamp).vi"/>
				<Item Name="DAQNavi Read (Analog 1D DBL NChan 1Samp).vi" Type="VI" URL="/&lt;userlib&gt;/DAQNavi Polymorphic VI/read/DAQNavi Read (Analog 1D DBL NChan 1Samp).vi"/>
				<Item Name="DAQNavi Read (Analog 1D U16 NChan NSamp).vi" Type="VI" URL="/&lt;userlib&gt;/DAQNavi Polymorphic VI/read/DAQNavi Read (Analog 1D U16 NChan NSamp).vi"/>
				<Item Name="DAQNavi Read (Analog 1D U32 NChan NSamp).vi" Type="VI" URL="/&lt;userlib&gt;/DAQNavi Polymorphic VI/read/DAQNavi Read (Analog 1D U32 NChan NSamp).vi"/>
				<Item Name="DAQNavi Read (Analog 1D Wfm NChan 1Samp).vi" Type="VI" URL="/&lt;userlib&gt;/DAQNavi Polymorphic VI/read/DAQNavi Read (Analog 1D Wfm NChan 1Samp).vi"/>
				<Item Name="DAQNavi Read (Analog 1D Wfm NChan NSamp).vi" Type="VI" URL="/&lt;userlib&gt;/DAQNavi Polymorphic VI/read/DAQNavi Read (Analog 1D Wfm NChan NSamp).vi"/>
				<Item Name="DAQNavi Read (Analog 2D DBL NChan NSamp).vi" Type="VI" URL="/&lt;userlib&gt;/DAQNavi Polymorphic VI/read/DAQNavi Read (Analog 2D DBL NChan NSamp).vi"/>
				<Item Name="DAQNavi Read (Analog 2D U16 NChan NSamp).vi" Type="VI" URL="/&lt;userlib&gt;/DAQNavi Polymorphic VI/read/DAQNavi Read (Analog 2D U16 NChan NSamp).vi"/>
				<Item Name="DAQNavi Read (Analog 2D U32 NChan NSamp).vi" Type="VI" URL="/&lt;userlib&gt;/DAQNavi Polymorphic VI/read/DAQNavi Read (Analog 2D U32 NChan NSamp).vi"/>
				<Item Name="DAQNavi Read (Analog DBL 1Chan 1Samp).vi" Type="VI" URL="/&lt;userlib&gt;/DAQNavi Polymorphic VI/read/DAQNavi Read (Analog DBL 1Chan 1Samp).vi"/>
				<Item Name="DAQNavi Read (Analog Wfm 1Chan 1Samp).vi" Type="VI" URL="/&lt;userlib&gt;/DAQNavi Polymorphic VI/read/DAQNavi Read (Analog Wfm 1Chan 1Samp).vi"/>
				<Item Name="DAQNavi Read (Analog Wfm 1Chan NSamp).vi" Type="VI" URL="/&lt;userlib&gt;/DAQNavi Polymorphic VI/read/DAQNavi Read (Analog Wfm 1Chan NSamp).vi"/>
				<Item Name="DAQNavi Read (Counter 1D Count Value 1Chan NSamp).vi" Type="VI" URL="/&lt;userlib&gt;/DAQNavi Polymorphic VI/read/DAQNavi Read (Counter 1D Count Value 1Chan NSamp).vi"/>
				<Item Name="DAQNavi Read (Counter 1D Frequency 1Chan NSamp).vi" Type="VI" URL="/&lt;userlib&gt;/DAQNavi Polymorphic VI/read/DAQNavi Read (Counter 1D Frequency 1Chan NSamp).vi"/>
				<Item Name="DAQNavi Read (Counter 1D Pulse Width 1Chan NSamp).vi" Type="VI" URL="/&lt;userlib&gt;/DAQNavi Polymorphic VI/read/DAQNavi Read (Counter 1D Pulse Width 1Chan NSamp).vi"/>
				<Item Name="DAQNavi Read (Counter Count Value 1Chan 1Samp).vi" Type="VI" URL="/&lt;userlib&gt;/DAQNavi Polymorphic VI/read/DAQNavi Read (Counter Count Value 1Chan 1Samp).vi"/>
				<Item Name="DAQNavi Read (Counter Frequency 1Chan 1Samp).vi" Type="VI" URL="/&lt;userlib&gt;/DAQNavi Polymorphic VI/read/DAQNavi Read (Counter Frequency 1Chan 1Samp).vi"/>
				<Item Name="DAQNavi Read (Counter Pulse Width 1Chan 1Samp).vi" Type="VI" URL="/&lt;userlib&gt;/DAQNavi Polymorphic VI/read/DAQNavi Read (Counter Pulse Width 1Chan 1Samp).vi"/>
				<Item Name="DAQNavi Read (Digital 1D U8 1Chan NSamp).vi" Type="VI" URL="/&lt;userlib&gt;/DAQNavi Polymorphic VI/read/DAQNavi Read (Digital 1D U8 1Chan NSamp).vi"/>
				<Item Name="DAQNavi Read (Digital 1D U8 NChan 1Samp).vi" Type="VI" URL="/&lt;userlib&gt;/DAQNavi Polymorphic VI/read/DAQNavi Read (Digital 1D U8 NChan 1Samp).vi"/>
				<Item Name="DAQNavi Read (Digital 1D Wfm NChan 1Samp).vi" Type="VI" URL="/&lt;userlib&gt;/DAQNavi Polymorphic VI/read/DAQNavi Read (Digital 1D Wfm NChan 1Samp).vi"/>
				<Item Name="DAQNavi Read (Digital 1D Wfm NChan NSamp).vi" Type="VI" URL="/&lt;userlib&gt;/DAQNavi Polymorphic VI/read/DAQNavi Read (Digital 1D Wfm NChan NSamp).vi"/>
				<Item Name="DAQNavi Read (Digital 2D U8 NChan NSamp).vi" Type="VI" URL="/&lt;userlib&gt;/DAQNavi Polymorphic VI/read/DAQNavi Read (Digital 2D U8 NChan NSamp).vi"/>
				<Item Name="DAQNavi Read (Digital U8 1Chan 1Samp).vi" Type="VI" URL="/&lt;userlib&gt;/DAQNavi Polymorphic VI/read/DAQNavi Read (Digital U8 1Chan 1Samp).vi"/>
				<Item Name="DAQNavi Read (Digital Wfm 1Chan 1Samp).vi" Type="VI" URL="/&lt;userlib&gt;/DAQNavi Polymorphic VI/read/DAQNavi Read (Digital Wfm 1Chan 1Samp).vi"/>
				<Item Name="DAQNavi Read (Digital Wfm 1Chan NSamp).vi" Type="VI" URL="/&lt;userlib&gt;/DAQNavi Polymorphic VI/read/DAQNavi Read (Digital Wfm 1Chan NSamp).vi"/>
				<Item Name="DAQNavi Read.vi" Type="VI" URL="/&lt;userlib&gt;/DAQNavi Polymorphic VI/read/DAQNavi Read.vi"/>
				<Item Name="DAQNavi String To Enum.vi" Type="VI" URL="/&lt;userlib&gt;/DAQNavi Polymorphic VI/component/DAQNavi String To Enum.vi"/>
				<Item Name="DAQNavi Write (Analog 1D DBL 1Chan NSamp).vi" Type="VI" URL="/&lt;userlib&gt;/DAQNavi Polymorphic VI/write/DAQNavi Write (Analog 1D DBL 1Chan NSamp).vi"/>
				<Item Name="DAQNavi Write (Analog 1D DBL NChan 1Samp).vi" Type="VI" URL="/&lt;userlib&gt;/DAQNavi Polymorphic VI/write/DAQNavi Write (Analog 1D DBL NChan 1Samp).vi"/>
				<Item Name="DAQNavi Write (Analog 1D Wfm NChan 1Samp).vi" Type="VI" URL="/&lt;userlib&gt;/DAQNavi Polymorphic VI/write/DAQNavi Write (Analog 1D Wfm NChan 1Samp).vi"/>
				<Item Name="DAQNavi Write (Analog 1D Wfm NChan NSamp).vi" Type="VI" URL="/&lt;userlib&gt;/DAQNavi Polymorphic VI/write/DAQNavi Write (Analog 1D Wfm NChan NSamp).vi"/>
				<Item Name="DAQNavi Write (Analog 2D DBL NChan NSamp).vi" Type="VI" URL="/&lt;userlib&gt;/DAQNavi Polymorphic VI/write/DAQNavi Write (Analog 2D DBL NChan NSamp).vi"/>
				<Item Name="DAQNavi Write (Analog 2D U16 NChan NSamp).vi" Type="VI" URL="/&lt;userlib&gt;/DAQNavi Polymorphic VI/write/DAQNavi Write (Analog 2D U16 NChan NSamp).vi"/>
				<Item Name="DAQNavi Write (Analog 2D U32 NChan NSamp).vi" Type="VI" URL="/&lt;userlib&gt;/DAQNavi Polymorphic VI/write/DAQNavi Write (Analog 2D U32 NChan NSamp).vi"/>
				<Item Name="DAQNavi Write (Analog DBL 1Chan 1Samp).vi" Type="VI" URL="/&lt;userlib&gt;/DAQNavi Polymorphic VI/write/DAQNavi Write (Analog DBL 1Chan 1Samp).vi"/>
				<Item Name="DAQNavi Write (Analog Wfm 1Chan 1Samp).vi" Type="VI" URL="/&lt;userlib&gt;/DAQNavi Polymorphic VI/write/DAQNavi Write (Analog Wfm 1Chan 1Samp).vi"/>
				<Item Name="DAQNavi Write (Analog Wfm 1Chan NSamp).vi" Type="VI" URL="/&lt;userlib&gt;/DAQNavi Polymorphic VI/write/DAQNavi Write (Analog Wfm 1Chan NSamp).vi"/>
				<Item Name="DAQNavi Write (Digital 1D U8 1Chan NSamp).vi" Type="VI" URL="/&lt;userlib&gt;/DAQNavi Polymorphic VI/write/DAQNavi Write (Digital 1D U8 1Chan NSamp).vi"/>
				<Item Name="DAQNavi Write (Digital 1D Wfm NChan 1Samp).vi" Type="VI" URL="/&lt;userlib&gt;/DAQNavi Polymorphic VI/write/DAQNavi Write (Digital 1D Wfm NChan 1Samp).vi"/>
				<Item Name="DAQNavi Write (Digital 1D Wfm NChan NSamp).vi" Type="VI" URL="/&lt;userlib&gt;/DAQNavi Polymorphic VI/write/DAQNavi Write (Digital 1D Wfm NChan NSamp).vi"/>
				<Item Name="DAQNavi Write (Digital 2D U8 NChan NSamp).vi" Type="VI" URL="/&lt;userlib&gt;/DAQNavi Polymorphic VI/write/DAQNavi Write (Digital 2D U8 NChan NSamp).vi"/>
				<Item Name="DAQNavi Write (Digital U8 1Chan 1Samp).vi" Type="VI" URL="/&lt;userlib&gt;/DAQNavi Polymorphic VI/write/DAQNavi Write (Digital U8 1Chan 1Samp).vi"/>
				<Item Name="DAQNavi Write (Digital Wfm 1Chan 1Samp).vi" Type="VI" URL="/&lt;userlib&gt;/DAQNavi Polymorphic VI/write/DAQNavi Write (Digital Wfm 1Chan 1Samp).vi"/>
				<Item Name="DAQNavi Write (Digital Wfm 1Chan NSamp).vi" Type="VI" URL="/&lt;userlib&gt;/DAQNavi Polymorphic VI/write/DAQNavi Write (Digital Wfm 1Chan NSamp).vi"/>
				<Item Name="DAQNavi Write (Digtial 1D U8 NChan 1Samp).vi" Type="VI" URL="/&lt;userlib&gt;/DAQNavi Polymorphic VI/write/DAQNavi Write (Digtial 1D U8 NChan 1Samp).vi"/>
				<Item Name="DAQNavi Write.vi" Type="VI" URL="/&lt;userlib&gt;/DAQNavi Polymorphic VI/write/DAQNavi Write.vi"/>
				<Item Name="DAQNaviGet_AI_ChannelCount.vi" Type="VI" URL="/&lt;userlib&gt;/DAQNavi Polymorphic VI/configure/DAQNavi Get Property/AI/DAQNaviGet_AI_ChannelCount.vi"/>
				<Item Name="DAQNaviGet_AI_ConvertClock_Rate.vi" Type="VI" URL="/&lt;userlib&gt;/DAQNavi Polymorphic VI/configure/DAQNavi Get Property/AI/DAQNaviGet_AI_ConvertClock_Rate.vi"/>
				<Item Name="DAQNaviGet_AO_ChannelCount.vi" Type="VI" URL="/&lt;userlib&gt;/DAQNavi Polymorphic VI/configure/DAQNavi Get Property/AO/DAQNaviGet_AO_ChannelCount.vi"/>
				<Item Name="DAQNaviGet_DI_PortCount.vi" Type="VI" URL="/&lt;userlib&gt;/DAQNavi Polymorphic VI/configure/DAQNavi Get Property/DI/DAQNaviGet_DI_PortCount.vi"/>
				<Item Name="DAQNaviGet_DIO_PortCount.vi" Type="VI" URL="/&lt;userlib&gt;/DAQNavi Polymorphic VI/component/DAQNaviGet_DIO_PortCount.vi"/>
				<Item Name="DAQNaviGet_DO_PortCount.vi" Type="VI" URL="/&lt;userlib&gt;/DAQNavi Polymorphic VI/configure/DAQNavi Get Property/DO/DAQNaviGet_DO_PortCount.vi"/>
				<Item Name="DAQNaviSet_CI_CollectionPeriod.vi" Type="VI" URL="/&lt;userlib&gt;/DAQNavi Polymorphic VI/configure/DAQNavi Set Property/DAQNaviSet_CI_CollectionPeriod.vi"/>
				<Item Name="DAQNaviSet_CI_FreqMeasureMethod.vi" Type="VI" URL="/&lt;userlib&gt;/DAQNavi Polymorphic VI/configure/DAQNavi Set Property/DAQNaviSet_CI_FreqMeasureMethod.vi"/>
				<Item Name="DAQNaviSet_CI_UpDownCounterInitialValue.vi" Type="VI" URL="/&lt;userlib&gt;/DAQNavi Polymorphic VI/configure/DAQNavi Set Property/DAQNaviSet_CI_UpDownCounterInitialValue.vi"/>
				<Item Name="DAQNaviSet_CI_UpDownCounterResetTimesByIndex.vi" Type="VI" URL="/&lt;userlib&gt;/DAQNavi Polymorphic VI/configure/DAQNavi Set Property/DAQNaviSet_CI_UpDownCounterResetTimesByIndex.vi"/>
				<Item Name="DAQNaviSet_CI_UpDownCounterSignalCountingType.vi" Type="VI" URL="/&lt;userlib&gt;/DAQNavi Polymorphic VI/configure/DAQNavi Set Property/DAQNaviSet_CI_UpDownCounterSignalCountingType.vi"/>
				<Item Name="DAQNaviSet_CO_DelayCount.vi" Type="VI" URL="/&lt;userlib&gt;/DAQNavi Polymorphic VI/configure/DAQNavi Set Property/DAQNaviSet_CO_DelayCount.vi"/>
				<Item Name="DAQNaviSet_CO_FreqValue.vi" Type="VI" URL="/&lt;userlib&gt;/DAQNavi Polymorphic VI/configure/DAQNavi Set Property/DAQNaviSet_CO_FreqValue.vi"/>
				<Item Name="DAQNaviSet_CO_PulseWidth.vi" Type="VI" URL="/&lt;userlib&gt;/DAQNavi Polymorphic VI/configure/DAQNavi Set Property/DAQNaviSet_CO_PulseWidth.vi"/>
				<Item Name="GetErrorInformation.vi" Type="VI" URL="/&lt;userlib&gt;/DAQNavi Polymorphic VI/component/GetErrorInformation.vi"/>
				<Item Name="GetErrorPosition.vi" Type="VI" URL="/&lt;userlib&gt;/DAQNavi Polymorphic VI/component/GetErrorPosition.vi"/>
				<Item Name="Set value.vi" Type="VI" URL="/&lt;userlib&gt;/CST/Set value.vi"/>
				<Item Name="ToErrorCluster_Polymorphic.vi" Type="VI" URL="/&lt;userlib&gt;/DAQNavi Polymorphic VI/component/ToErrorCluster_Polymorphic.vi"/>
				<Item Name="ini.vi" Type="VI" URL="/&lt;userlib&gt;/CST/ini.vi"/>
			</Item>
			<Item Name="vi.lib" Type="Folder">
				<Item Name="Boolean Array to Digital.vi" Type="VI" URL="/&lt;vilib&gt;/Waveform/DWDT.llb/Boolean Array to Digital.vi"/>
				<Item Name="Check if File or Folder Exists.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/libraryn.llb/Check if File or Folder Exists.vi"/>
				<Item Name="Close File+.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Close File+.vi"/>
				<Item Name="compatReadText.vi" Type="VI" URL="/&lt;vilib&gt;/_oldvers/_oldvers.llb/compatReadText.vi"/>
				<Item Name="Digital Size.vi" Type="VI" URL="/&lt;vilib&gt;/Waveform/DWDT.llb/Digital Size.vi"/>
				<Item Name="Digital to Binary.vi" Type="VI" URL="/&lt;vilib&gt;/Waveform/DWDT.llb/Digital to Binary.vi"/>
				<Item Name="DTbl Boolean Array to Digital.vi" Type="VI" URL="/&lt;vilib&gt;/Waveform/DTblOps.llb/DTbl Boolean Array to Digital.vi"/>
				<Item Name="DTbl Compress Digital.vi" Type="VI" URL="/&lt;vilib&gt;/Waveform/DTblOps.llb/DTbl Compress Digital.vi"/>
				<Item Name="DTbl Digital Size.vi" Type="VI" URL="/&lt;vilib&gt;/Waveform/DTblOps.llb/DTbl Digital Size.vi"/>
				<Item Name="DTbl Digital to Binary U8.vi" Type="VI" URL="/&lt;vilib&gt;/Waveform/DTblOps.llb/DTbl Digital to Binary U8.vi"/>
				<Item Name="DTbl Digital to Binary U16.vi" Type="VI" URL="/&lt;vilib&gt;/Waveform/DTblOps.llb/DTbl Digital to Binary U16.vi"/>
				<Item Name="DTbl Digital to Binary U32.vi" Type="VI" URL="/&lt;vilib&gt;/Waveform/DTblOps.llb/DTbl Digital to Binary U32.vi"/>
				<Item Name="DWDT Boolean Array to Digital.vi" Type="VI" URL="/&lt;vilib&gt;/Waveform/DWDTOps.llb/DWDT Boolean Array to Digital.vi"/>
				<Item Name="DWDT Digital Size.vi" Type="VI" URL="/&lt;vilib&gt;/Waveform/DWDTOps.llb/DWDT Digital Size.vi"/>
				<Item Name="DWDT Digital to Binary U8.vi" Type="VI" URL="/&lt;vilib&gt;/Waveform/DWDTOps.llb/DWDT Digital to Binary U8.vi"/>
				<Item Name="DWDT Digital to Binary U16.vi" Type="VI" URL="/&lt;vilib&gt;/Waveform/DWDTOps.llb/DWDT Digital to Binary U16.vi"/>
				<Item Name="DWDT Digital to Binary U32.vi" Type="VI" URL="/&lt;vilib&gt;/Waveform/DWDTOps.llb/DWDT Digital to Binary U32.vi"/>
				<Item Name="Error Cluster From Error Code.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Error Cluster From Error Code.vi"/>
				<Item Name="Find First Error.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Find First Error.vi"/>
				<Item Name="Image Type" Type="VI" URL="/&lt;vilib&gt;/vision/Image Controls.llb/Image Type"/>
				<Item Name="IMAQ Create" Type="VI" URL="/&lt;vilib&gt;/vision/Basics.llb/IMAQ Create"/>
				<Item Name="IMAQ Image.ctl" Type="VI" URL="/&lt;vilib&gt;/vision/Image Controls.llb/IMAQ Image.ctl"/>
				<Item Name="IMAQdx.ctl" Type="VI" URL="/&lt;vilib&gt;/userdefined/High Color/IMAQdx.ctl"/>
				<Item Name="NI_FileType.lvlib" Type="Library" URL="/&lt;vilib&gt;/Utility/lvfile.llb/NI_FileType.lvlib"/>
				<Item Name="NI_PackedLibraryUtility.lvlib" Type="Library" URL="/&lt;vilib&gt;/Utility/LVLibp/NI_PackedLibraryUtility.lvlib"/>
				<Item Name="NI_Vision_Acquisition_Software.lvlib" Type="Library" URL="/&lt;vilib&gt;/vision/driver/NI_Vision_Acquisition_Software.lvlib"/>
				<Item Name="NI_Vision_Development_Module.lvlib" Type="Library" URL="/&lt;vilib&gt;/vision/NI_Vision_Development_Module.lvlib"/>
				<Item Name="Open File+.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Open File+.vi"/>
				<Item Name="Read Delimited Spreadsheet (DBL).vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Read Delimited Spreadsheet (DBL).vi"/>
				<Item Name="Read Delimited Spreadsheet (I64).vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Read Delimited Spreadsheet (I64).vi"/>
				<Item Name="Read Delimited Spreadsheet (string).vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Read Delimited Spreadsheet (string).vi"/>
				<Item Name="Read Delimited Spreadsheet.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Read Delimited Spreadsheet.vi"/>
				<Item Name="Read File+ (string).vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Read File+ (string).vi"/>
				<Item Name="Read Lines From File (with error IO).vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Read Lines From File (with error IO).vi"/>
				<Item Name="Write Delimited Spreadsheet (DBL).vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Write Delimited Spreadsheet (DBL).vi"/>
				<Item Name="Write Delimited Spreadsheet (I64).vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Write Delimited Spreadsheet (I64).vi"/>
				<Item Name="Write Delimited Spreadsheet (string).vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Write Delimited Spreadsheet (string).vi"/>
				<Item Name="Write Delimited Spreadsheet.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Write Delimited Spreadsheet.vi"/>
				<Item Name="Write Spreadsheet String.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Write Spreadsheet String.vi"/>
				<Item Name="VISA Configure Serial Port" Type="VI" URL="/&lt;vilib&gt;/Instr/_visa.llb/VISA Configure Serial Port"/>
				<Item Name="VISA Configure Serial Port (Instr).vi" Type="VI" URL="/&lt;vilib&gt;/Instr/_visa.llb/VISA Configure Serial Port (Instr).vi"/>
				<Item Name="VISA Configure Serial Port (Serial Instr).vi" Type="VI" URL="/&lt;vilib&gt;/Instr/_visa.llb/VISA Configure Serial Port (Serial Instr).vi"/>
				<Item Name="Color to RGB.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/colorconv.llb/Color to RGB.vi"/>
				<Item Name="IMAQ Connect Range Setting.ctl" Type="VI" URL="/&lt;vilib&gt;/vision/Contour.llb/IMAQ Connect Range Setting.ctl"/>
				<Item Name="IMAQ Contour Curve Extraction.ctl" Type="VI" URL="/&lt;vilib&gt;/vision/Contour.llb/IMAQ Contour Curve Extraction.ctl"/>
				<Item Name="IMAQ Convert Curve Extraction To Internal" Type="VI" URL="/&lt;vilib&gt;/vision/Contour.llb/IMAQ Convert Curve Extraction To Internal"/>
				<Item Name="IMAQ Copy" Type="VI" URL="/&lt;vilib&gt;/vision/Management.llb/IMAQ Copy"/>
				<Item Name="IMAQ Merge Overlay" Type="VI" URL="/&lt;vilib&gt;/vision/Overlay.llb/IMAQ Merge Overlay"/>
				<Item Name="IMAQ Overlay Line" Type="VI" URL="/&lt;vilib&gt;/vision/Overlay.llb/IMAQ Overlay Line"/>
				<Item Name="IMAQ Overlay Oval" Type="VI" URL="/&lt;vilib&gt;/vision/Overlay.llb/IMAQ Overlay Oval"/>
				<Item Name="IMAQ Overlay Points" Type="VI" URL="/&lt;vilib&gt;/vision/Overlay.llb/IMAQ Overlay Points"/>
				<Item Name="IMAQ Overlay Text" Type="VI" URL="/&lt;vilib&gt;/vision/Overlay.llb/IMAQ Overlay Text"/>
				<Item Name="IMAQ Write BMP File 2" Type="VI" URL="/&lt;vilib&gt;/vision/Files.llb/IMAQ Write BMP File 2"/>
				<Item Name="IMAQ Write File 2" Type="VI" URL="/&lt;vilib&gt;/vision/Files.llb/IMAQ Write File 2"/>
				<Item Name="IMAQ Write Image And Vision Info File 2" Type="VI" URL="/&lt;vilib&gt;/vision/Files.llb/IMAQ Write Image And Vision Info File 2"/>
				<Item Name="IMAQ Write JPEG File 2" Type="VI" URL="/&lt;vilib&gt;/vision/Files.llb/IMAQ Write JPEG File 2"/>
				<Item Name="IMAQ Write JPEG2000 File 2" Type="VI" URL="/&lt;vilib&gt;/vision/Files.llb/IMAQ Write JPEG2000 File 2"/>
				<Item Name="IMAQ Write PNG File 2" Type="VI" URL="/&lt;vilib&gt;/vision/Files.llb/IMAQ Write PNG File 2"/>
				<Item Name="IMAQ Write TIFF File 2" Type="VI" URL="/&lt;vilib&gt;/vision/Files.llb/IMAQ Write TIFF File 2"/>
				<Item Name="NI_AALPro.lvlib" Type="Library" URL="/&lt;vilib&gt;/Analysis/NI_AALPro.lvlib"/>
				<Item Name="IMAQ ReadFile" Type="VI" URL="/&lt;vilib&gt;/vision/Files.llb/IMAQ ReadFile"/>
				<Item Name="Image Unit" Type="VI" URL="/&lt;vilib&gt;/vision/Image Controls.llb/Image Unit"/>
				<Item Name="IMAQ GetImageInfo" Type="VI" URL="/&lt;vilib&gt;/vision/Basics.llb/IMAQ GetImageInfo"/>
				<Item Name="subFile Dialog.vi" Type="VI" URL="/&lt;vilib&gt;/express/express input/FileDialogBlock.llb/subFile Dialog.vi"/>
				<Item Name="ex_CorrectErrorChain.vi" Type="VI" URL="/&lt;vilib&gt;/express/express shared/ex_CorrectErrorChain.vi"/>
				<Item Name="IMAQ Convert Overlay Settings To Internal" Type="VI" URL="/&lt;vilib&gt;/vision/Contour.llb/IMAQ Convert Overlay Settings To Internal"/>
			</Item>
			<Item Name="create_NG_folder.vi" Type="VI" URL="../function/create_NG_folder.vi"/>
			<Item Name="DAQNavi_LV.dll" Type="Document" URL="/C/Windows/System32/DAQNavi_LV.dll"/>
			<Item Name="niimaqdx.dll" Type="Document" URL="niimaqdx.dll">
				<Property Name="NI.PreserveRelativePath" Type="Bool">true</Property>
			</Item>
			<Item Name="nivision.dll" Type="Document" URL="nivision.dll">
				<Property Name="NI.PreserveRelativePath" Type="Bool">true</Property>
			</Item>
			<Item Name="nivissvc.dll" Type="Document" URL="nivissvc.dll">
				<Property Name="NI.PreserveRelativePath" Type="Bool">true</Property>
			</Item>
			<Item Name="np_astype_str.vi" Type="VI" URL="../function/np_astype_str.vi"/>
			<Item Name="re_create_folder.vi" Type="VI" URL="../function/re_create_folder.vi"/>
			<Item Name="files_in_folder.vi" Type="VI" URL="../function/files_in_folder.vi"/>
			<Item Name="load_single_image.vi" Type="VI" URL="../function/load_single_image.vi"/>
			<Item Name="array_for_overlay.vi" Type="VI" URL="../function/array_for_overlay.vi"/>
			<Item Name="plot_line_array2cluster.vi" Type="VI" URL="../function/plot_line_array2cluster.vi"/>
			<Item Name="plot_side_cutting_offset.vi" Type="VI" URL="../function/plot_side_cutting_offset.vi"/>
			<Item Name="float2str.vi" Type="VI" URL="../function/float2str.vi"/>
			<Item Name="pllot_text_side_cutting_offset.vi" Type="VI" URL="../function/pllot_text_side_cutting_offset.vi"/>
			<Item Name="D_point2line.vi" Type="VI" URL="../function/D_point2line.vi"/>
			<Item Name="find_close_point_on_line.vi" Type="VI" URL="../function/find_close_point_on_line.vi"/>
			<Item Name="find_close_point_on_side.vi" Type="VI" URL="../function/find_close_point_on_side.vi"/>
			<Item Name="plot_text_glitch_damaged.vi" Type="VI" URL="../function/plot_text_glitch_damaged.vi"/>
			<Item Name="plot_rec2circle.vi" Type="VI" URL="../function/plot_rec2circle.vi"/>
			<Item Name="cluster2array_side_circle_overlay.vi" Type="VI" URL="../function/cluster2array_side_circle_overlay.vi"/>
			<Item Name="cluster2array_for_overlay.vi" Type="VI" URL="../function/cluster2array_for_overlay.vi"/>
			<Item Name="find_corner.vi" Type="VI" URL="../function/find_corner.vi"/>
			<Item Name="corner_for_rectangle.vi" Type="VI" URL="../function/corner_for_rectangle.vi"/>
			<Item Name="find_sub_contour.vi" Type="VI" URL="../function/find_sub_contour.vi"/>
			<Item Name="create_morph_kernel.vi" Type="VI" URL="../function/create_morph_kernel.vi"/>
			<Item Name="giltch_damaged_detector.vi" Type="VI" URL="../function/giltch_damaged_detector.vi"/>
			<Item Name="side_giltch_damaged_detector.vi" Type="VI" URL="../function/side_giltch_damaged_detector.vi"/>
			<Item Name="slope2angle.vi" Type="VI" URL="../function/slope2angle.vi"/>
			<Item Name="np_extraction_by_index_1d.vi" Type="VI" URL="../function/np_extraction_by_index_1d.vi"/>
			<Item Name="np_argwhere.vi" Type="VI" URL="../function/np_argwhere.vi"/>
			<Item Name="binary_array.vi" Type="VI" URL="../function/binary_array.vi"/>
			<Item Name="velocity_filter.vi" Type="VI" URL="../function/velocity_filter.vi"/>
			<Item Name="fitting_1d_pixel.vi" Type="VI" URL="../function/fitting_1d_pixel.vi"/>
			<Item Name="fitting_side.vi" Type="VI" URL="../function/fitting_side.vi"/>
			<Item Name="sort_XY.vi" Type="VI" URL="../function/sort_XY.vi"/>
			<Item Name="np_extraction_by_index_2d.vi" Type="VI" URL="../function/np_extraction_by_index_2d.vi"/>
			<Item Name="find_side_points.vi" Type="VI" URL="../function/find_side_points.vi"/>
			<Item Name="ratio_pixel2mil.vi" Type="VI" URL="../function/ratio_pixel2mil.vi"/>
			<Item Name="find_main_contour.vi" Type="VI" URL="../function/find_main_contour.vi"/>
			<Item Name="find_contours.vi" Type="VI" URL="../function/find_contours.vi"/>
			<Item Name="threshold2gray.vi" Type="VI" URL="../function/threshold2gray.vi"/>
			<Item Name="image_copy.vi" Type="VI" URL="../function/image_copy.vi"/>
			<Item Name="image_processing.vi" Type="VI" URL="../image_processing.vi"/>
			<Item Name="lvanlys.dll" Type="Document" URL="/&lt;resource&gt;/lvanlys.dll"/>
			<Item Name="fitting_padding_array.vi" Type="VI" URL="../function/fitting_padding_array.vi"/>
			<Item Name="SHA-1.vi" Type="VI" URL="../SHA-1 LV8/SHA-1.vi"/>
			<Item Name="SHA-1 Pad.vi" Type="VI" URL="../SHA-1 LV8/SHA-1 Pad.vi"/>
			<Item Name="SHA-1 Core.vi" Type="VI" URL="../SHA-1 LV8/SHA-1 Core.vi"/>
			<Item Name="SHA-1 Digest.vi" Type="VI" URL="../SHA-1 LV8/SHA-1 Digest.vi"/>
			<Item Name="boolean_inverse.vi" Type="VI" URL="../function/boolean_inverse.vi"/>
			<Item Name="check_point_inside_rect.vi" Type="VI" URL="../function/check_point_inside_rect.vi"/>
			<Item Name="time_name.vi" Type="VI" URL="../function/time_name.vi"/>
		</Item>
		<Item Name="Build Specifications" Type="Build">
			<Item Name="G163" Type="EXE">
				<Property Name="App_copyErrors" Type="Bool">true</Property>
				<Property Name="App_INI_aliasGUID" Type="Str">{989B22EF-4EE4-4A2F-BE4F-B98AC27879AE}</Property>
				<Property Name="App_INI_GUID" Type="Str">{12754471-CCBB-43E3-ACA6-B4FF01B392BC}</Property>
				<Property Name="App_serverConfig.httpPort" Type="Int">8002</Property>
				<Property Name="Bld_autoIncrement" Type="Bool">true</Property>
				<Property Name="Bld_buildCacheID" Type="Str">{E486EB4E-BB72-423D-B5F2-74FAA799DD15}</Property>
				<Property Name="Bld_buildSpecName" Type="Str">G163</Property>
				<Property Name="Bld_excludeInlineSubVIs" Type="Bool">true</Property>
				<Property Name="Bld_excludeLibraryItems" Type="Bool">true</Property>
				<Property Name="Bld_excludePolymorphicVIs" Type="Bool">true</Property>
				<Property Name="Bld_localDestDir" Type="Path">../G163</Property>
				<Property Name="Bld_localDestDirType" Type="Str">relativeToCommon</Property>
				<Property Name="Bld_modifyLibraryFile" Type="Bool">true</Property>
				<Property Name="Bld_previewCacheID" Type="Str">{7676EF79-86CF-46B7-B49C-08030C59C8C6}</Property>
				<Property Name="Bld_version.build" Type="Int">6</Property>
				<Property Name="Bld_version.major" Type="Int">1</Property>
				<Property Name="Destination[0].destName" Type="Str">G163.exe</Property>
				<Property Name="Destination[0].path" Type="Path">../G163/G163.exe</Property>
				<Property Name="Destination[0].preserveHierarchy" Type="Bool">true</Property>
				<Property Name="Destination[0].type" Type="Str">App</Property>
				<Property Name="Destination[1].destName" Type="Str">Support Directory</Property>
				<Property Name="Destination[1].path" Type="Path">../G163</Property>
				<Property Name="DestinationCount" Type="Int">2</Property>
				<Property Name="Source[0].itemID" Type="Str">{079AB484-2B86-4905-B069-F294961CEFCF}</Property>
				<Property Name="Source[0].type" Type="Str">Container</Property>
				<Property Name="Source[1].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[1].itemID" Type="Ref">/My Computer/AOI_Main.vi</Property>
				<Property Name="Source[1].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[1].type" Type="Str">VI</Property>
				<Property Name="Source[2].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[2].itemID" Type="Ref">/My Computer/parameter.txt</Property>
				<Property Name="Source[2].sourceInclusion" Type="Str">Include</Property>
				<Property Name="SourceCount" Type="Int">3</Property>
				<Property Name="TgtF_companyName" Type="Str">光?科技股份有限公司</Property>
				<Property Name="TgtF_fileDescription" Type="Str">G163</Property>
				<Property Name="TgtF_internalName" Type="Str">G163</Property>
				<Property Name="TgtF_legalCopyright" Type="Str">Copyright ?2021 光?科技股份有限公司</Property>
				<Property Name="TgtF_productName" Type="Str">G163</Property>
				<Property Name="TgtF_targetfileGUID" Type="Str">{F5CDAB35-1AD1-4B4D-AC43-81896619C3D1}</Property>
				<Property Name="TgtF_targetfileName" Type="Str">G163.exe</Property>
				<Property Name="TgtF_versionIndependent" Type="Bool">true</Property>
			</Item>
			<Item Name="IO_TEST" Type="EXE">
				<Property Name="App_copyErrors" Type="Bool">true</Property>
				<Property Name="App_INI_aliasGUID" Type="Str">{AD18DE8E-D55C-4186-8429-CE45A8A3D820}</Property>
				<Property Name="App_INI_GUID" Type="Str">{E9E49AA0-2FF0-4B9B-86ED-3325DDECFBB7}</Property>
				<Property Name="App_serverConfig.httpPort" Type="Int">8002</Property>
				<Property Name="Bld_autoIncrement" Type="Bool">true</Property>
				<Property Name="Bld_buildCacheID" Type="Str">{2EAD3FEB-95BB-49A9-8F5F-073A35A8B749}</Property>
				<Property Name="Bld_buildSpecName" Type="Str">IO_TEST</Property>
				<Property Name="Bld_excludeInlineSubVIs" Type="Bool">true</Property>
				<Property Name="Bld_excludeLibraryItems" Type="Bool">true</Property>
				<Property Name="Bld_excludePolymorphicVIs" Type="Bool">true</Property>
				<Property Name="Bld_localDestDir" Type="Path">../IO_TEST</Property>
				<Property Name="Bld_localDestDirType" Type="Str">relativeToCommon</Property>
				<Property Name="Bld_modifyLibraryFile" Type="Bool">true</Property>
				<Property Name="Bld_previewCacheID" Type="Str">{7E68EEE3-8553-49F7-BD0D-0BDDAA320B47}</Property>
				<Property Name="Bld_version.build" Type="Int">1</Property>
				<Property Name="Bld_version.major" Type="Int">1</Property>
				<Property Name="Destination[0].destName" Type="Str">IO_TEST.exe</Property>
				<Property Name="Destination[0].path" Type="Path">../IO_TEST/IO_TEST.exe</Property>
				<Property Name="Destination[0].preserveHierarchy" Type="Bool">true</Property>
				<Property Name="Destination[0].type" Type="Str">App</Property>
				<Property Name="Destination[1].destName" Type="Str">Support Directory</Property>
				<Property Name="Destination[1].path" Type="Path">../IO_TEST/data</Property>
				<Property Name="DestinationCount" Type="Int">2</Property>
				<Property Name="Source[0].itemID" Type="Str">{079AB484-2B86-4905-B069-F294961CEFCF}</Property>
				<Property Name="Source[0].type" Type="Str">Container</Property>
				<Property Name="Source[1].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[1].itemID" Type="Ref">/My Computer/IO_TEST.vi</Property>
				<Property Name="Source[1].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[1].type" Type="Str">VI</Property>
				<Property Name="SourceCount" Type="Int">2</Property>
				<Property Name="TgtF_companyName" Type="Str">光?科技股份有限公司</Property>
				<Property Name="TgtF_fileDescription" Type="Str">IO_TEST</Property>
				<Property Name="TgtF_internalName" Type="Str">IO_TEST</Property>
				<Property Name="TgtF_legalCopyright" Type="Str">Copyright ?2021 光?科技股份有限公司</Property>
				<Property Name="TgtF_productName" Type="Str">IO_TEST</Property>
				<Property Name="TgtF_targetfileGUID" Type="Str">{2BD44948-0819-41BC-9BAC-AEA51A3314AC}</Property>
				<Property Name="TgtF_targetfileName" Type="Str">IO_TEST.exe</Property>
				<Property Name="TgtF_versionIndependent" Type="Bool">true</Property>
			</Item>
			<Item Name="TimeFlow_for_泰克" Type="EXE">
				<Property Name="App_copyErrors" Type="Bool">true</Property>
				<Property Name="App_INI_aliasGUID" Type="Str">{8969D804-80E6-4686-AA8A-B1628E6A436C}</Property>
				<Property Name="App_INI_GUID" Type="Str">{440AECE1-4C39-4C96-94AA-435EA3B24C85}</Property>
				<Property Name="App_serverConfig.httpPort" Type="Int">8002</Property>
				<Property Name="Bld_autoIncrement" Type="Bool">true</Property>
				<Property Name="Bld_buildCacheID" Type="Str">{6FFBDE2A-1CE2-4EED-88AA-FB95737BA394}</Property>
				<Property Name="Bld_buildSpecName" Type="Str">TimeFlow_for_泰克</Property>
				<Property Name="Bld_excludeInlineSubVIs" Type="Bool">true</Property>
				<Property Name="Bld_excludeLibraryItems" Type="Bool">true</Property>
				<Property Name="Bld_excludePolymorphicVIs" Type="Bool">true</Property>
				<Property Name="Bld_localDestDir" Type="Path">../TimeFlow_for_泰克</Property>
				<Property Name="Bld_localDestDirType" Type="Str">relativeToCommon</Property>
				<Property Name="Bld_modifyLibraryFile" Type="Bool">true</Property>
				<Property Name="Bld_previewCacheID" Type="Str">{DE7E1D05-2248-4695-A193-8F93A69E8355}</Property>
				<Property Name="Bld_version.major" Type="Int">1</Property>
				<Property Name="Destination[0].destName" Type="Str">TimeFlow_for_泰克.exe</Property>
				<Property Name="Destination[0].path" Type="Path">../TimeFlow_for_泰克/TimeFlow_for_泰克.exe</Property>
				<Property Name="Destination[0].preserveHierarchy" Type="Bool">true</Property>
				<Property Name="Destination[0].type" Type="Str">App</Property>
				<Property Name="Destination[1].destName" Type="Str">Support Directory</Property>
				<Property Name="Destination[1].path" Type="Path">../TimeFlow_for_泰克/data</Property>
				<Property Name="DestinationCount" Type="Int">2</Property>
				<Property Name="Source[0].itemID" Type="Str">{39308C53-CA73-4FDE-B24F-055447865BFC}</Property>
				<Property Name="Source[0].type" Type="Str">Container</Property>
				<Property Name="Source[1].destinationIndex" Type="Int">0</Property>
				<Property Name="Source[1].itemID" Type="Ref">/My Computer/TimeFlow_for_泰克.vi</Property>
				<Property Name="Source[1].sourceInclusion" Type="Str">TopLevel</Property>
				<Property Name="Source[1].type" Type="Str">VI</Property>
				<Property Name="SourceCount" Type="Int">2</Property>
				<Property Name="TgtF_companyName" Type="Str">光?科技股份有限公司</Property>
				<Property Name="TgtF_fileDescription" Type="Str">TimeFlow_for_泰克</Property>
				<Property Name="TgtF_internalName" Type="Str">TimeFlow_for_泰克</Property>
				<Property Name="TgtF_legalCopyright" Type="Str">Copyright ?2021 光?科技股份有限公司</Property>
				<Property Name="TgtF_productName" Type="Str">TimeFlow_for_泰克</Property>
				<Property Name="TgtF_targetfileGUID" Type="Str">{5478F3D0-B045-4EC0-A911-F1B6E4AA1C72}</Property>
				<Property Name="TgtF_targetfileName" Type="Str">TimeFlow_for_泰克.exe</Property>
				<Property Name="TgtF_versionIndependent" Type="Bool">true</Property>
			</Item>
		</Item>
	</Item>
</Project>
