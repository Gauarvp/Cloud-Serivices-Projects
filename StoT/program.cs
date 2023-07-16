using Microsoft.CognitiveServices.Speech;
using System;
using System. Threading. Tasks;
5
6
7
9
Enamespace Speech_To_Text_App
{
O references class Program
{
O references
static  as Task Main(string[] args)
{
    await RecognizedSpeech();
Console.WriteLine ("Finished");
}
{
private static async Task RecognizeSpeech()
var configuration = SpeechConfig.FromSubscription("bd9d295fc6934211a3339987b894a96d", "centralindia");
using (var recog = new SpeechRecognizer (configuration))
{
Console.WriteLine("Speak something...");
var result = await recog. RecognizeOnceAsync();
if (result.Reason as ResultReason. RecognizedSpeech)
{
Console.WriteLine (result.Text) ;
}
}
}
}
}