using System;

namespace Matikkapeli
{
    class Program
    {
        static void Main(string[] args)
        {
            {
                var rnd = new Random();
                var quit = false;
                var userScore = 0;
                var totalProblems = 0;
                var percentCorrect = 0d;

                while (!quit)
                {
                    Console.Clear();

                    //Arvotaan numero ja operaattori kysymykseen
                    var number1 = rnd.Next(1, 31);
                    var number2 = rnd.Next(1, 31);
                    var operation = rnd.Next(1, 5);
                    string operatorString;
                    int answer;
                    totalProblems++;

                    Console.WriteLine("\tOngelma");
                    
                   
                    switch (operation)
                    {
                        case 1:
                            answer = number1 + number2;
                            operatorString = "+";
                            break;
                        case 2:
                            answer = number1 - number2;
                            operatorString = "-";
                            break;
                        case 3:
                            answer = number1 * number2;
                            operatorString = "*";
                            break;
                        case 4:
                            answer = number1 / number2;
                            operatorString = "/";
                            break;
                        default:
                            answer = 0;
                            operatorString = "?";
                            break;
                    }

                    //Kirjoittaa ongelman
                    Console.WriteLine("\t{0} {1} {2}", number1, operatorString, number2);

                    //Kayttajan antaa vastauksen 
                    Console.Write("\nVastauksesi. Pyöristä alaspäin jos tarve ");
                    var input = Console.ReadLine();
                    int inputAsInt;

                    //Jos vastaus ei ole numero, antaa errorin
                    while (!int.TryParse(input, out inputAsInt))
                    {
                        Console.Write("Vastaus on pakko olla numero. Yritä uudelleen.");
                        input = Console.ReadLine();
                    }

                    // Tarkistaa onko vastaus oikein, jos oikein lisää pisteen käyttäjälle
                    if (inputAsInt == answer)
                    {
                        Console.WriteLine("Correct!");
                        userScore++;
                    }

                    //Jos väärä vastaus näyttää oikean vastauksen
                    else
                    {
                        Console.WriteLine("Väärin, oikea vastaus on {0}", answer);
                    }

                    //Laskee kayttajalle pisteet prosentteina
                    percentCorrect = Math.Round((double)userScore / totalProblems * 100, 2);

                    //Naytetaan monta vastausta pelaaja on saanut oikein
                    Console.WriteLine("\nOlet vastannut {0} of {1} ongelmaan oikein, " +
                        "yhteensä {2}%.", userScore, totalProblems, percentCorrect);

                    //Kysyy ja tarkistaa lopettaako pelaaja pelin
                    Console.Write("\nPaina 'Q' jos haluat lopettaa pelin tai paina entteriä jatkaaksesi. ");
                    if (Console.ReadKey().Key == ConsoleKey.Q) quit = true;
                }
                //Kun pelaaja lopettaa lasketaan arvosana
                var letterGrade = 
                    percentCorrect < 60 ? "4"
                    : percentCorrect < 65 ? "5"
                    : percentCorrect < 70 ? "6"
                    : percentCorrect < 75 ? "7"
                    : percentCorrect < 80 ? "8"
                    : percentCorrect < 85 ? "9"
                    : "10";

                //Kun kayttaja lopettaa pelin, naytetaan arvosana.
                Console.WriteLine("\n\nKiitos pelaamisesta sait " +"arvosanaksi {0}", letterGrade + " / 10");
                Console.Write("\nPaina mita tahansa nappainta poistuaksesi");
                Console.ReadKey();
            }
        }
    }
}

