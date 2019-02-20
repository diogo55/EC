# T0

### Ex2

No seguinte exercício pretende-se criar uma comunicaçpão privada assíncrona entre um agente Emitter e um agente Receiver com as seguintes propriedades:

    a. Autenticação do criptograma e dos metadados. Usar uma cifra simétrica num dos modos stream cipher
    b. Derivação da chave a partir de uma password usando um KDF
    c. Autenticação prévia da chave usando um MAC
    
Definiu-se numa fase inicial o agente *Emitter* e o agente *Receiver* que comunicavam entre si assíncronamente. O Receiver liga-se ao host 127.0.0.1 na porta 9999 e fica a "espera" de receber dados enviados pelo Emitter. O Emitter envia a mensagem 'Hello, World!' para o mesmo host e porta onde o Reciever está à espera.

Após termos realizado esta conexão com sucesso é que procedemos a definir as funções de derivação de chave (KDF), de mac e de hash.

A password escolhida ('Some password') é simples e possui pouca complexidade. Como tal, é necessário usar uma Key Derivation Function (KDF) tranformando a password em algo facilmente reconhecivel pela máquina mas dificilmente por humanos, aumentando assim a proteção do sistema.

O Message Authentication Code (MAC) server para autenticar a mensagem passada na ligação dos agentes.

Hash serve para guardar os dados de uma forma criptograficamente segura (não permite deduzir a password através do valor do hash)

