# T0

### Ex2

No seguinte exercício pretende-se criar uma comunicação privada assíncrona entre um agente Emitter e um agente Receiver com as seguintes propriedades:

    a. Autenticação do criptograma e dos metadados. Usar uma cifra simétrica num dos modos stream cipher
    b. Derivação da chave a partir de uma password usando um KDF
    c. Autenticação prévia da chave usando um MAC
    
Definiu-se numa fase inicial o agente *Emitter* e o agente *Receiver* que comunicavam entre si assíncronamente. O Receiver liga-se ao host 127.0.0.1 na porta 9999 e fica a "espera" de receber dados enviados pelo Emitter. O Emitter envia a mensagem 'Hello, World!' para o mesmo host e porta onde o Reciever está à espera.

Após termos realizado esta conexão com sucesso é que procedemos a definir as funções de derivação de chave (KDF) e de mac.

A password escolhida ('Some password') é simples e possui pouca complexidade. Como tal, é necessário usar uma Key Derivation Function (KDF) tranformando a password em algo facilmente reconhecivel pela máquina mas dificilmente por humanos, aumentando assim a proteção do sistema.

O Message Authentication Code (MAC) server para autenticar a mensagem passada na ligação dos agentes.

O Emitter cifra a mensagem que deseja enviar, produzindo um ciphertext que corresponde a essa mensagem. Esta cifra foi calculada utilizando a cifra Advanced Encryption Standard(AES), algoritmo criptográfico de chave simétrica, no modo CTR, stream cipher (utiliza um contador).

O Reciever recebe os parâmetros necessários para decifrar a mensagem. Primeiro compara a tag que recebeu com a que consegue calcular através da função de mac. Caso as tags sejam iguais pode continuar o processo de decifragem, senão para o processo e indica que houve um problema na integridade da mensagem.

