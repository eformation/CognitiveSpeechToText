   M S B A M L   `   `   `  ����  SpeechToText-WPF-Sample>    8Microsoft.CognitiveServices.SpeechRecognition.MainWindow   5   	   \ XPresentationFramework, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35R NWindowsBase, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35W SPresentationCore, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35D 9http://schemas.microsoft.com/winfx/2006/xaml/presentation    R NSystem.Xaml, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089:x,http://schemas.microsoft.com/winfx/2006/xaml     5   	   @d2http://schemas.microsoft.com/expression/blend/2008     5   	   Jmc;http://schemas.openxmlformats.org/markup-compatibility/2006     6F   -   5          �Name$  _mainWindow��5   	    � Title$! Self Service Analytics Tool��5   	   $��5,5,5,5q�6-   $	��800��6>   .��5      � $��5q�6    � RowDefinitions 5   
   �� 5	      $
��auto �6   �� 5
      $��* �6    � ColumnDefinitions 5   
   �� 5      $
��467* �6   $	��200��6,   �� 5      $
��933* �6   $	��200��6,   .+�5   
   �� $��0��6   $��0��6   $
��Left=�6-   $6��0Project Cognitive Services Speech To Text Sample��6H   $	��272��6�   � 5   
   $��0��6   $��1��6   $��6.333,0,10,0q�6,   .+�5      ��  �� Orientation$ 
Horizontal=�6   $��Right=�62   .+�5      �� $��Stretch=�6   $��Stretch=�66   $��2q�6T   ��6`   �� *SubscriptionKey+ �� ElementName$ _mainWindow�� �� Mode$ TwoWay=��� 5      -   5        $��
5, 0, 0, 0q�5      $��
5, 0, 5, 0q�6-   $��30��6B   $	��Top=�6N   $��Save Key��6|   �� 5      -   5        $��
5, 0, 0, 0q�5      $��
5, 0, 5, 0q�6-   $��
Delete Key��6Z   �� 5      -   5        $��Center=�5   2   $��
5, 0, 0, 0q�6O   $��
5, 0, 5, 0q�6c   $��Get Key��6x   5      5      � 5   
   $��1��6   $��0��6   $��0,0,9.667,-0.333q�6,    5      �� 5      $
��auto �6    �� 5      �� 5      $
��auto �6    $��89.333��6.   .+�5       �� -   5         ��Name$ _radioGroup��5       $��0��6,   $��10,10,10,10.333q�69   $��0, 0, 10, 10q�6R   .��5!      �� $ Vertical=�6   .+�5"      �� $ ��Speech Recognition Source:��6   	� 5#      -   5         	�Name$ _micRadioButton��5#   "   $��10, 10, 0, 0q�6�   $*��$Use Microphone with ShortPhrase mode��6�   	 d� 	IsChecked	 6;   �� *IsMicrophoneClientShortPhrase+$ _mainWindow��6�   	� 5$      -   5        $ _micDictationRadioButton��5$   "   $��10, 10, 0, 0q�6�   $,��&Use Microphone with LongDictation mode��6�   	 6D   �� *IsMicrophoneClientDictation+$ _mainWindow��6�   	� 5%      -   5        $ _micIntentRadioButton��5%   "   $��10, 10, 0, 0q�6�   $)��#Use Microphone and intent detection��6�   	 6A   �� *IsMicrophoneClientWithIntent+$ _mainWindow��6�   �� 5&      $��30,0,0,0q�6   $&�� (* LUIS registration is needed.)��6.   	� 5'      -	   5        $ _dataShortRadioButton��5'   "   $��10, 10, 0, 0q�6�   $'��!Use wav file for ShortPhrase mode��6�   	 6A   �� *IsDataClientShortPhrase+$ _mainWindow��6�   	� 5(      -
   5        $ _dataLongRadioButton��5(   "   $��10, 10, 0, 0q�6�   $)��#Use wav file for LongDictation mode��6�   	 6@   �� *IsDataClientDictation+$ _mainWindow��6�   	� 5)      -   5        $! _dataShortIntentRadioButton��5)   "   $��10, 10, 0, 0q�6�   $'��!Use wav file and intent detection��6�   	 6G   �� *IsDataClientWithIntent+$ _mainWindow��6�   �� 5*      $��30,0,0,0q�6   $&�� (* LUIS registration is needed.)��6.   5+      5,      � 5-      $��2��6   $��10,0.667,0,9.667q�6    $
��Left=�6:   $	��411��6U    5.      �� 5/      $
��auto �6'   �� 50      $
��auto �6'   .+�52      �� -   5        
 ��Name$
 _startButton��52      $��0��6/   $��Start _Recognition��6?   $��0,5,-0.667,42.999q�6v   $��5q�6�   $��2��6�   �� 53      -   5        $
 _selfserveTool��53      $��Start Self Service Tool��61   $��1��6S   $
��Left=�6c   $��97,5,-199.333,0q�6~   $	��Top=�6�   $	��165��6�   $��31��6�   6�   54      �� 55      -   5        $
 _codeAnalysis��55      $+��%Code Analysis (Find Depricated Calls)��6,   $
��Left=�6\   $��10,45.667,0,0q�6w   $��2��6�   $	��Top=�6�   $	��282��6�   $��34��6�   6�   56      �� 57   
   -   5         ��Name$ _logText��57      $��1��6$   $��Stretch=�61   $��Stretch=�6O    �� TextWrapping$
 Wrap=�6k   $�� ��6   " �� VerticalScrollBarVisibility$ Visible=�6�   $��3.333,10,10,9.667q�6�   $��1��6�   $��14(�6�   $
��Bold"�6�   58      59      