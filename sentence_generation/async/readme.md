### Async Assignment

For the async assignment, I made a Markov text generator which outputs rap verses in the style of MF DOOM.<br>
<br>
The corpus of words is taken from multiple verses by MF DOOM from multiple albums.<br>
The data was acquired from [here](https://github.com/nabilhassein/generative-DOOM/tree/master/data)<br>
<br>
In addition to using the Markov method of text generation, I also wanted to have cuplets which would include rhyming words. To do this, I created a function that would iterate through two lines of text at a time and extract the last two words from each of the two sentences, storing them in a dictionary, the words from the first line being the key and the words form the last two lines being the value. This did require cleaning the data a bit to assure all key value pairs would result in accurate rhyming words.<br>
Once I had a dictionary of rhyming words, I restructured the text generating function to generate one line at a time. I would have the function generate 6 words of a line using the markov method, then I would add the rhyming words at the end of the line. In most cases, this would be chosen randomly, but the function would check to see if the next word in the markov chain would be a word from the rhyme dictionary in which case those words would be used.<br>
I then created a cuplet generator which would take a generated line, look at the last words of the line which would have come from the rhyme dictionary as a key and then generate a second sentence which would end with the corresponding rhyming words that were the value pair to the words from the first sentence.<br>
Finally, I made a verse generator which takes an argument for how many lines you want your verse to be (the standard being 16 lines).<br>
<br>
**Example Output**
```
Transaction drama... awww come with his folklore legend
Borderline schizo, sort of trying to more, bredren
Come clean, a flask He went fountain glass
Instead of hash to remember when, been last
Please, at the "Is you It's a standstill
East river Larger than the hook man killed
Versus Doom wit' the eye closed no doubt
Supervillian He just to the mic I'm out
Ms. Mary Mack Wait 'til he or... dude
Status: RaeDawn Chong Let alone Let too screwed
Crunk He be better off New by design
Kraus I'll tell her cat out come rewind
Hands so you Maybe even this totin toast
Schooled the Tec-9 holder of them Lodine dose
Enough about my fate Tired of the worsest
Mr. Fantastik at a brush with boundless universes
```
