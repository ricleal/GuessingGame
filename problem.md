# Guessing Game Take-Home Problem

This is a take-home project for candidates. It should be doable in 1-3 hours of work.

Problem

Implement a distributed number guessing game. The guessing game is played by a human, talking to a game server. There should be two components: a client and a server. The client and server communicate with one another over HTTP. The client has the following operations:

- Start a new game
- Ask a question
- Guess an answer

When the client sends &quot;start a new game&quot;, the server picks a &quot;solution&quot; for the new game. For example, a solution might be &quot;42&quot;. The client can then send questions to the server using the &quot;ask a question&quot; operation and the server responds with &quot;true&quot; or &quot;false&quot;. For example, if the client asks &quot;is it less than 7&quot;, the server should respond with &quot;false&quot; (for the solution 42). After asking a series of questions, the client can use the &quot;guess an answer&quot; operation to attempt to win the game. The server responds with &quot;you won!&quot; or &quot;you lost!&quot; and ends the game.

Assumptions and Constraints

The client will be used by a human. It can either be a command line utility, an interactive prompt, or anything else that lets the user submit questions and guesses . You can have a static and shared set of allowable questions. Examples of good questions to support are:

- \&lt; X?
- \&gt; X?
- Even?
- Odd?

Feel free to add others, but the supported questions and their format should be documented.

Supporting multiple concurrent games would be logical but isn&#39;t strictly required.

Deliverables

Send us a tarball containing your code and a README with directions on how to build and run your guessing game. If you include tests, we will give those a try too. Add a Dockerfile if that would make it easier to build and run your game.
