'use client';

import { useState, useEffect } from 'react';
import { useRouter } from 'next/navigation';
import ChatLayout from '@/components/chat/ChatLayout';
import { apiClient } from '@/lib/apiClient';
import { Upload, FileText, Loader2, CheckCircle } from 'lucide-react';

export default function DocsPage() {
  const router = useRouter();
  const [documents, setDocuments] = useState([]);
  const [uploading, setUploading] = useState(false);
  const [success, setSuccess] = useState('');

  useEffect(() => {
    const token = localStorage.getItem('token');
    if (!token) {
      router.push('/login');
      return;
    }
    loadDocuments();
  }, [router]);

  const loadDocuments = async () => {
    try {
      const response = await apiClient.listDocuments();
      setDocuments(response.documents);
    } catch (error) {
      console.error('Error loading documents:', error);
    }
  };

  const handleFileUpload = async (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (!file) return;

    setUploading(true);
    setSuccess('');

    try {
      await apiClient.uploadDocument(file);
      setSuccess(`✅ Documento "${file.name}" procesado exitosamente`);
      loadDocuments();
    } catch (error: any) {
      alert('Error al subir documento: ' + (error.response?.data?.detail || error.message));
    } finally {
      setUploading(false);
    }
  };

  return (
    <ChatLayout>
      <div className="h-full overflow-auto p-8">
        <div className="max-w-4xl mx-auto">
          <h2 className="text-3xl font-bold text-gray-800 mb-2">Gestión de Documentos</h2>
          <p className="text-gray-600 mb-8">Sube y administra los documentos del chatbot</p>

          {/* Upload Section */}
          <div className="bg-white rounded-xl border-2 border-dashed border-gray-300 p-8 mb-8 hover:border-primary-500 transition-colors">
            <div className="text-center">
              <Upload className="mx-auto mb-4 text-gray-400" size={48} />
              <h3 className="text-lg font-semibold text-gray-700 mb-2">Subir Documento PDF</h3>
              <p className="text-sm text-gray-500 mb-4">Arrastra un archivo o haz clic para seleccionar</p>

              <label className="inline-flex items-center gap-2 px-6 py-3 bg-primary-500 text-white rounded-lg font-medium cursor-pointer hover:bg-primary-600 transition-colors">
                {uploading ? (
                  <>
                    <Loader2 size={20} className="animate-spin" />
                    Procesando...
                  </>
                ) : (
                  <>
                    <Upload size={20} />
                    Seleccionar PDF
                  </>
                )}
                <input
                  type="file"
                  accept=".pdf"
                  onChange={handleFileUpload}
                  disabled={uploading}
                  className="hidden"
                />
              </label>
            </div>
          </div>

          {success && (
            <div className="bg-green-50 border border-green-200 text-green-700 px-4 py-3 rounded-lg mb-8 flex items-center gap-2">
              <CheckCircle size={20} />
              {success}
            </div>
          )}

          {/* Documents List */}
          <div className="bg-white rounded-xl shadow-sm border border-gray-200 overflow-hidden">
            <div className="px-6 py-4 border-b border-gray-200 bg-gray-50">
              <h3 className="text-lg font-semibold text-gray-800">Documentos Cargados ({documents.length})</h3>
            </div>

            <div className="divide-y divide-gray-200">
              {documents.length === 0 ? (
                <div className="px-6 py-12 text-center text-gray-500">
                  <FileText className="mx-auto mb-3 text-gray-300" size={48} />
                  <p>No hay documentos cargados aún</p>
                </div>
              ) : (
                documents.map((doc: any, index: number) => (
                  <div key={index} className="px-6 py-4 flex items-center justify-between hover:bg-gray-50 transition-colors">
                    <div className="flex items-center gap-3">
                      <div className="w-10 h-10 bg-blue-100 rounded-lg flex items-center justify-center">
                        <FileText className="text-blue-600" size={20} />
                      </div>
                      <div>
                        <p className="font-medium text-gray-800">{doc.filename}</p>
                        <p className="text-sm text-gray-500">{doc.chunks} fragmentos indexados</p>
                      </div>
                    </div>
                    <span className="px-3 py-1 bg-green-100 text-green-700 text-xs font-medium rounded-full">
                      Activo
                    </span>
                  </div>
                ))
              )}
            </div>
          </div>
        </div>
      </div>
    </ChatLayout>
  );
}
