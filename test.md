
HAproxy�����ļ������������ݣ�

------ ����ģʽ --------
    1   ��ѯ��¼
    2   ���Ӽ�¼
    3   ɾ����¼
    4   ���¼�¼
-----------------------

>>1
�������ѯ���ݣ�www.oldboy.org

        server 100.1.7.9 100.1.7.9 weight 20 maxconn 3000

------ ����ģʽ --------
    1   ��ѯ��¼
    2   ���Ӽ�¼
    3   ɾ����¼
    4   ���¼�¼
-----------------------

>>2
�������������ݣ�{'backend' : 'www.baidu.com', 'record' : {'server': '100.1.7.9', 'weight' : 20, 'maxconn' : 30}}
	��ã���������Ӳ�����

------ ����ģʽ --------
    1   ��ѯ��¼
    2   ���Ӽ�¼
    3   ɾ����¼
    4   ���¼�¼
-----------------------

>>3
������ɾ�����ݣ�{'backend' : 'www.baidu.com', 'record' : {'server': '100.1.7.9', 'weight' : 20, 'maxconn' : 30}}
	��ã������ɾ��������

------ ����ģʽ --------
    1   ��ѯ��¼
    2   ���Ӽ�¼
    3   ɾ����¼
    4   ���¼�¼
-----------------------

>>2
�������������ݣ�{'backend' : 'www.baidu.com', 'record' : {'server': '100.1.7.9', 'weight' : 20, 'maxconn' : 30}}
	��ã���������Ӳ�����

------ ����ģʽ --------
    1   ��ѯ��¼
    2   ���Ӽ�¼
    3   ɾ����¼
    4   ���¼�¼
-----------------------

>>4
������������ݣ�{'backend' : 'www.baidu.com', 'record' : {'server': '100.1.7.10', 'weight' : 20, 'maxconn' : 30}}
	��ã�����ɸ��²�����

------ ����ģʽ --------
    1   ��ѯ��¼
    2   ���Ӽ�¼
    3   ɾ����¼
    4   ���¼�¼
-----------------------

>>q

Process finished with exit code 0